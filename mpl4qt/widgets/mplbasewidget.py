# -*- coding: utf-8 -*-
"""
mplbasewidget.py

Base class for matplotlib widget for PyQt.

Copyright (C) 2018 Tong Zhang <zhangt@frib.msu.edu>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import time
import numpy as np
from collections import deque
from collections import OrderedDict
from functools import partial

from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QVariant
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QResizeEvent

from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

import matplotlib as mpl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import NullLocator

from mpl4qt.widgets.mpltoolbar import MToolbar
from mpl4qt.widgets.utils import ALL_COLORMAPS
from mpl4qt.widgets.utils import AUTOFORMATTER
from mpl4qt.widgets.utils import AUTOFORMATTER_MATHTEXT
from mpl4qt.widgets.utils import BOOTSTRAP_GREEN
from mpl4qt.widgets.utils import BOOTSTRAP_RED
from mpl4qt.widgets.utils import LINE_STY_VALS
from mpl4qt.widgets.utils import LINE_DS_VALS
from mpl4qt.widgets.utils import MatplotlibCurveWidgetSettings
from mpl4qt.widgets.utils import SCALE_STY_VALS
from mpl4qt.widgets.utils import cycle_list_next
from mpl4qt.widgets.utils import mfont_to_qfont
from mpl4qt.widgets.utils import mplcolor2hex
from mpl4qt.widgets.utils import set_font
from mpl4qt.widgets.utils import generate_formatter
from mpl4qt.widgets.utils import is_cmap_valid

MPL_VERSION = mpl.__version__
DTMSEC = 500  # msec
DTSEC = DTMSEC / 1000.0  # sec


class BasePlotWidget(QWidget):
    # combo keyshorts, keystring, timestamp
    keycombo_cached = pyqtSignal(str, float)

    # indices list of points selected by lasso tool,
    # ind: array, pts: array (selected)
    # for i,idx in enumerate(ind): idx, pts[i]
    selectedIndicesUpdated = pyqtSignal(QVariant, QVariant)

    # zoomed ROI changed
    zoom_roi_changed = pyqtSignal(tuple, tuple)

    # grid
    gridOnUpdated = pyqtSignal(bool)

    # legend
    legendOnUpdated = pyqtSignal(bool)

    # autoscale
    autoScaleOnUpdated = pyqtSignal(bool)

    # bg color
    bgColorChanged = pyqtSignal(QColor)

    # xy pos, x,y (default) or x,y,z
    xyposUpdated = pyqtSignal(list)

    # cross markers updated, is_new_marker?, x, y, mk_name
    markerUpdated = pyqtSignal(bool, float, float, 'QString')

    # selected point/line
    selectedPointChanged = pyqtSignal(float, float)
    selectedLineChanged = pyqtSignal(Line2D)

    # shaded area updated (mpltoolbar)
    shaded_area_updated = pyqtSignal(tuple, tuple)

    # xlimit is changed
    xlimitMinChanged = pyqtSignal(float)
    xlimitMaxChanged = pyqtSignal(float)
    # ylimit is changed
    ylimitMinChanged = pyqtSignal(float)
    ylimitMaxChanged = pyqtSignal(float)

    def __init__(self, parent=None, show_toolbar=True, **kws):
        super(BasePlotWidget, self).__init__(parent)
        self.widget_type = '__BasePlotWidget'
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.axes.set_picker(True)
        self.init_figure()
        self.canvas = FigureCanvas(self.figure)
        self.setParent(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sys_bg_color = self.palette().color(QPalette.Background)
        self.sys_fg_color = self.palette().color(QPalette.Foreground)
        DEFAULT_FONTS = {
            'title': QFontDatabase.systemFont(QFontDatabase.TitleFont),
            'fixed': QFontDatabase.systemFont(QFontDatabase.FixedFont),
            'general': QFontDatabase.systemFont(QFontDatabase.GeneralFont),
        }
        self.sys_label_font = DEFAULT_FONTS['general']
        self.sys_title_font = DEFAULT_FONTS['title']
        self.post_style_figure()
        # set up layout
        self.set_up_layout()

        self.adjustSize()
        self.set_context_menu()

        # track (x,y)
        self.canvas.mpl_connect('motion_notify_event', self.on_motion)

        # key press
        self.canvas.mpl_connect('key_press_event', self.on_key_press)

        # key release
        self.canvas.mpl_connect('key_release_event', self.on_key_release)

        # pick
        self.canvas.mpl_connect('pick_event', self.on_pick)

        # button
        self.canvas.mpl_connect('button_press_event', self.on_press)
        self.canvas.mpl_connect('button_release_event', self.on_release)

        self.canvas.mpl_connect('scroll_event', self.on_scroll)

        self.canvas.setFocusPolicy(Qt.ClickFocus)
        self.canvas.setFocus()

        # patches container: mk_area,
        # see draw_shade_area()
        self._patches = {}

        # dnd
        self.setAcceptDrops(True)

        # window/widget/dialog handlers
        self._handlers = {}

        # cross markers
        self._markers = OrderedDict() # list of {mk_name: [hl,vl,cp,pt,(x,y)]}
        self._to_add_marker = False
        self._added_marker = False # if added or not
        self._marker_id = 1 # initial marker id, always increase, even for deletion
        self._marker_with_xy = False  # anote with (x,y)
        self._visible_hvlines = True  # default visibility
        self.markerUpdated.connect(self.on_cross_markers_update)

        # pan
        self._pan_on = False

        # keypress cache
        self.dq_keycombo = deque([], 2)
        self.keycombo_cached.connect(self.on_update_keycombo_cache)

        # tb_toggle
        self._fig_tb_toggle = show_toolbar
        if self._fig_tb_toggle:
            # show mpltool
            self.__show_mpl_tools()

        #
        self.as_ann = None
        self.autoScaleOnUpdated.connect(self.on_autoscale_toggled)

        # add marker mpltool
        self._mk_add_hint_ann = None

        # [(lbl, (o,lw,mw))]
        self._last_sel_lines = {}

    def on_cross_markers_update(self):
        # cross markers updated.
        if len(self._markers) == 2:
            w = self._handlers.get('w_mpl_tools', None)
            if w is None:
                return  # usually is not None
            w.on_show_mks()
            w.mk_view.close()

    def draw_shade_area(self, p1, p2, **kws):
        # see markers view
        from matplotlib.patches import Rectangle
        def f(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            pts = sorted([[x1, y1], [x2, y2], [x1, y2], [x2, y1]])
            p1, p4 = pts[0], pts[-1]
            return p1, p4[0] - p1[0], p4[1] - p1[1]
        p = Rectangle(*f(p1, p2), **kws)
        self._patches['mk_area'] = p
        self.axes.add_patch(p)
        self.update_figure()

    @pyqtSlot(bool)
    def on_autoscale_toggled(self, auto_scale_enabled):
        # if auto scale is enabled, put text label
        if auto_scale_enabled:
            if self.as_ann is None:
                self.as_ann = self.axes.annotate('AutoScale is Enabled',
                            xy=(1.0, 1.01),
                            ha='right', va='bottom',
                            xycoords=('axes fraction'),
                            color='w',
                            bbox=dict(
                                boxstyle='round,pad=0.3',
                                fc=BOOTSTRAP_GREEN, ec=BOOTSTRAP_GREEN,
                                lw=1.0, alpha=0.8))
            else:
                self.as_ann.set_visible(True)
        else:
            if self.as_ann is not None:
                self.as_ann.set_visible(False)
        self.update_figure()

    @pyqtSlot(bool, 'QString', bool)
    def on_marker_add_checked(self, is_checked, mk_name, update_flag):
        # Add marker tool is checked.
        if update_flag:
            text = "Updating Marker ({}) is Activated, Finish by CTRL+M\nStart New by CTRL+M".format(mk_name)
        else:
            text = "Adding Marker ({}) is Activated, Finish by CTRL+M\nStart New by CTRL+M".format(mk_name)
        if is_checked:
            if self._mk_add_hint_ann is None:
                self._mk_add_hint_ann = self.axes.annotate(
                            text,
                            xy=(0, 1.01),
                            ha='left', va='bottom',
                            xycoords=('axes fraction'),
                            color='w',
                            bbox=dict(
                                boxstyle='round,pad=0.3',
                                fc=BOOTSTRAP_RED, ec=BOOTSTRAP_RED,
                                lw=1.0, alpha=0.8))
            else:
                self._mk_add_hint_ann.set_text(text)
                self._mk_add_hint_ann.set_visible(True)
        else:
            if self._mk_add_hint_ann is not None:
                self._mk_add_hint_ann.set_visible(False)
        self.update_figure()

    def get_crossmk_config(self, name):
        # get cross marker (w/ lines, text) config by name
        hl, _, cp, pt, _, = self._markers[name]
        return {'ls': hl.get_ls(), 'lw': hl.get_lw(),
                'c': hl.get_c(),
                'line_visible': hl.get_visible(),
                'line_alpha': hl.get_alpha(),
                'ms': cp.get_ms(), 'mk': cp.get_marker(),
                'mew': cp.get_mew(), 'mec': cp.get_mec(),
                'mfc': cp.get_mfc(),
                'mk_visible': cp.get_visible(),
                'mk_alpha': cp.get_alpha(),
                'text_visible': pt.get_visible(),
                'text_color': pt.get_color(),
                'text_content': pt.get_text(),
                'text_alpha': pt.get_bbox_patch().get_alpha(),}

    def draw_hvlines(self, x0, y0, name, mc=None):
        if name in self._markers:
            is_new_marker = False
            hl, vl, cp, pt, _ = self._markers[name]
            if mc is None:
                mc = hl.get_color()
        else:
            is_new_marker = True
            hl, vl, cp, pt = None, None, None, None
            assert mc is not None # mc must be given

        if hl is None:
            hl = self.axes.axhline(y0,
                                   alpha=0.8, color=mc, ls='--')
            hl.set_label('_H-Line {}'.format(name))
        else:
            hl.set_ydata([y0, y0])

        if vl is None:
            vl = self.axes.axvline(x0,
                                   alpha=0.8, color=mc, ls='--')
            vl.set_label('_V-Line {}'.format(name))
        else:
            vl.set_xdata([x0, x0])

        if cp is None:
            cp, = self.axes.plot([x0], [y0], 'o',
                                 mec=mc, mfc='w', mew=2.0, alpha=0.9)
            cp.set_label('_Cross-Point {}'.format(name))
            if self._marker_with_xy:
                text = '{0:g},{1:g}'.format(x0, y0)
            else:
                text = name
            pt = self.axes.annotate(text,
                    color='#000000', xy=(x0, y0), xytext=(15, 15),
                    xycoords="data", textcoords="offset pixels",
                    bbox=dict(boxstyle="round", fc='w'))
            pt.get_bbox_patch().set_alpha(0.5)
        else:
            cp.set_data([x0], [y0])
            pt.xy = (x0, y0)
            if self._marker_with_xy:
                pt.set_text('{0:g},{1:g}'.format(x0, y0))
            else:
                pt.set_text(name)
            self._markers[name][-1] = (x0, y0)

        if is_new_marker:
            self._markers[name] = [hl, vl, cp, pt, (x0, y0)]

        self.markerUpdated.emit(is_new_marker, x0, y0, name)
        self.update_figure()

    def set_visible_hvlines(self, flag=True):
        """Set all markers visible (*flag* is True) or invisible (*flag* is False).
        """
        self._visible_hvlines = flag
        for name, (hl, vl, cp, pt, _,) in self._markers.items():
            for o in (hl, vl, cp, pt):
                o.set_visible(flag)
        self.update_figure()

    def __show_mpl_tools(self):
        if 'w_mpl_tools' in self._handlers:
            w = self._handlers['w_mpl_tools']
        else:
            w = MToolbar(self.figure.canvas, self)
            self._handlers['w_mpl_tools'] = w
            w.selectedIndicesUpdated.connect(self.on_selected_indices)
            w.zoom_roi_changed.connect(self.on_zoom_roi_changed)
            w.shaded_area_updated.connect(self.on_shaded_area_updated)
        w.show_toolbar()
        w.floatable_changed.emit(False)

    @pyqtSlot(QVariant, QVariant)
    def on_selected_indices(self, ind, pts):
        self.selectedIndicesUpdated.emit(ind, pts)

    @pyqtSlot(tuple, tuple)
    def on_shaded_area_updated(self, xlim, ylim):
        self.shaded_area_updated.emit(xlim, ylim)

    @pyqtSlot(tuple, tuple)
    def on_zoom_roi_changed(self, xlim, ylim):
        # print("Zoomed Rect ROI: ", xlim, ylim)
        self.zoom_roi_changed.emit(xlim, ylim)

    def set_up_layout(self):
        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.addWidget(self.canvas, 1)
        self.setLayout(self.vbox)

    def post_style_figure(self):
        self.init_prop_settings()
        self.set_figure_color()

    def init_prop_settings(self):
        """Initial settings for properties.
        """
        ## fonts:
        # xy labels
        lbl = self.axes.xaxis.label
        self._fig_xylabel_font = mfont_to_qfont(lbl.get_fontproperties())
        self._fig_xylabel_visible = lbl.get_visible()
        # xy ticklabels
        tklbl = self.axes.get_xticklabels()[0]
        self._fig_xyticks_font = mfont_to_qfont(tklbl.get_fontproperties())
        # title
        title = self.axes.title
        self._fig_title_font = mfont_to_qfont(title.get_fontproperties())
        self._fig_title_visible = title.get_visible()

        ## border, if auto scale is enabled, style could not be changed.
        o = list(self.axes.spines.values())[0]
        # c, lw, ls, vis,
        self._fig_border_color = QColor(mplcolor2hex(o.get_ec()))
        self._fig_border_lw = o.get_linewidth()
        self._fig_border_ls = o.get_linestyle()
        self._fig_border_visible = o.get_visible()

        # aspect
        self._fig_aspect = str(self.axes.get_aspect())

        # tight?
        self._fig_tight_layout = False

        # lbls,title
        self._fig_title = ''
        self._fig_xlabel = ''
        self._fig_ylabel = ''

        # figure, w,h,dpi
        self._fig_width, self._fig_height = self.figure.get_size_inches()
        self._fig_dpi = self.figure.get_dpi()

        # bg color
        self._fig_bgcolor = self.sys_bg_color

        # grid color
        self._fig_grid_color = QColor('gray')
        # grid toggle
        self._fig_grid_toggle = False

        # mticks toggle
        self._fig_mticks_toggle = False

        # legend toggle
        self._legend_toggle = False

        # legend location
        self._legend_location = 0

        # xyticks angle
        self._fig_xticks_angle = 0
        self._fig_yticks_angle = 0

        # xyticks color
        self._fig_ticks_color = self.sys_fg_color

        # tick format
        self._fig_xtick_formatter_type = 'Auto'
        self._fig_xtick_formatter = None  # placeholder only
        self._fig_xtick_cfmt = ''  # c string format for FuncFormatter
        self._fig_ytick_formatter_type = 'Auto'
        self._fig_ytick_formatter = None  # placeholder only
        self._fig_ytick_cfmt = ''  # c string format for FuncFormatter
        self._fig_ticks_enable_mathtext = False  # use math text or not

        # xy axis scale
        self._fig_xscale = 'linear'
        self._fig_yscale = 'linear'

        # xylimits
        self._xlim_min, self._xlim_max = self.axes.get_xlim()
        self._ylim_min, self._ylim_max = self.axes.get_ylim()

        # ticklabels visibility
        xtklbl = self.axes.get_xticklabels()[0]
        ytklbl = self.axes.get_yticklabels()[0]
        self._fig_xticks_visible = xtklbl.get_visible()
        self._fig_yticks_visible = ytklbl.get_visible()

        # auto scale
        self._fig_auto_scale = False  # default disable autoscale

    def on_scroll(self, e):
        if e.inaxes is None:
            return
        if e.step < 0:
            f = 1.05 ** (-e.step)
        else:
            f = 0.95 ** e.step
        self.zoom(e, f)

    def zoom(self, e, factor):
        x0, y0 = e.xdata, e.ydata
        x_left, x_right = self.axes.get_xlim()
        y_bottom, y_up = self.axes.get_ylim()

        self.axes.set_xlim((x0 - (x0 - x_left) * factor,
                            x0 + (x_right - x0) * factor))
        self.axes.set_ylim((y0 - (y0 - y_bottom) * factor,
                            y0 + (y_up - y0) * factor))
        self.update_figure()

    def on_motion(self, evt):
        if evt.inaxes is None:
            return
        x_pos, y_pos = evt.xdata, evt.ydata
        self.xyposUpdated.emit([x_pos, y_pos])

    def on_key_press(self, e):
        k, t = e.key, time.time()
        self.keycombo_cached.emit(k, t)
        QTimer.singleShot(DTMSEC, partial(self._on_delay_pop, k, t))

    def on_key_release(self, e):
        if len(self.dq_keycombo) != 2:
            return
        (k1, t1) = self.dq_keycombo.popleft()
        (k2, t2) = self.dq_keycombo.popleft()
        if t2 - t1 < DTSEC:
            self.process_keyshort_combo(k1, k2)

    def on_pick(self, evt):
        o = evt.artist
        if isinstance(o, Line2D):
            lw0, mw0 = o.get_lw(), o.get_mew()
            x, y = o.get_data()
            ind = evt.ind
            x0, y0 = x[ind][0], y[ind][0]
            o.set_lw(lw0 * 2)
            o.set_mew(mw0 * 2)
            self._last_sel_lines.setdefault(
                    o.get_label(),
                    (o, lw0, mw0))
            self.selectedPointChanged.emit(x0, y0)
            self.selectedLineChanged.emit(o)
            self.update_figure()
        elif isinstance(evt.artist, Axes):
            if self._last_sel_lines:
                for lbl, (o, lw0, mw0) in self._last_sel_lines.items():
                    o.set_lw(lw0)
                    o.set_mew(mw0)
                self.update_figure()
                self._last_sel_lines = {}

    def on_press(self, e):
        if e.inaxes is None:
            return
        if e.button == 1 and self._to_add_marker:
            self.draw_hvlines(e.xdata, e.ydata, self._mk_name, self._current_mc)
            self.set_visible_hvlines(self._visible_hvlines)
            self._added_marker = True
            QGuiApplication.restoreOverrideCursor()

    def on_release(self, e):
        pass

    def dragEnterEvent(self, e):
        pass

    def dropEvent(self, e):
        pass

    def init_figure(self):
        raise NotImplementedError

    def update_figure(self):
        if self._fig_auto_scale:
            try:
                self.axes.relim()
            except:
                pass
            else:
                self.axes.autoscale()
        self.canvas.draw_idle()

    def contextMenuEvent(self, evt):
        self._create_ctxtmenu().exec_(self.mapToGlobal(evt.pos()))

    def _create_ctxtmenu(self):
        menu = QMenu(self)
        config_action = QAction(QIcon(QPixmap(":/tools/config.png")),
                                "Config", menu)
        config_action.setShortcut("c,c")
        config_action.setObjectName('config_action')
        export_action = QAction(QIcon(QPixmap(":/tools/export.png")),
                                "Export", menu)
        import_action = QAction(QIcon(QPixmap(":/tools/import.png")),
                                "Import", menu)
        reset_action = QAction(QIcon(QPixmap(":/tools/reset.png")),
                               "Reset", menu)
        tb_action = QAction(QIcon(QPixmap(":/tools/tools.png")),
                            "Tools", menu)
        tb_action.setObjectName('tb_action')
        tb_action.setShortcut("t,t")
        fitting_action = QAction(QIcon(QPixmap(":/tools/fitting.png")),
                                 "Fitting", menu)
        export_data_action = QAction(QIcon(QPixmap(":/tools/export.png")),
                                "Export Data", menu)
        info_action = QAction(QIcon(QPixmap(":/tools/info.png")),
                                "About", menu)
        keyshort_action = QAction(QIcon(QPixmap(":/tools/keyshort.png")),
                                "Shortcuts", menu)

        menu.addAction(config_action)
        menu.addAction(export_action)
        menu.addAction(import_action)
        menu.addAction(reset_action)
        menu.addSeparator()
        menu.addAction(tb_action)
        menu.addAction(fitting_action)
        menu.addAction(export_data_action)
        menu.addSeparator()
        menu.addAction(keyshort_action)
        menu.addAction(info_action)

        menu.setStyleSheet('QMenu {margin: 2px;}')

        config_action.triggered.connect(self.on_config)
        export_action.triggered.connect(self.on_export_config)
        import_action.triggered.connect(self.on_import_config)
        reset_action.triggered.connect(self.on_reset_config)
        tb_action.triggered.connect(self.toggle_mpl_tools)
        fitting_action.triggered.connect(self.on_fitting_data)
        export_data_action.triggered.connect(self.on_export_data)
        info_action.triggered.connect(self.on_info)
        keyshort_action.triggered.connect(self.kbd_help)

        return menu

    @pyqtSlot()
    def on_fitting_data(self):
        """Fitting data.
        """
        raise NotImplementedError("Fitting data is to be implemented.")

    @pyqtSlot()
    def on_export_data(self):
        raise NotImplementedError("Export data is to be implemented.")

    @pyqtSlot()
    def on_info(self):
        from ._info import get_pkg_info
        QMessageBox.about(self, 'About mpl4qt', get_pkg_info())

    @pyqtSlot()
    def toggle_mpl_tools(self):
        self.setToolbarToggle(not self.getToolbarToggle())

    @pyqtSlot()
    def on_reset_config(self):
        # apply default settings
        raise NotImplementedError("Reset config is to be implemented.")

    @pyqtSlot()
    def on_config(self):
        raise NotImplementedError("Config panel is to be implemented.")

    @pyqtSlot()
    def on_export_config(self):
        filepath, _ = QFileDialog.getSaveFileName(self,
                                                  "Save Settings",
                                                  "./mpl_settings.json",
                                                  "JSON Files (*.json)")
        if not filepath:
            return
        try:
            s = self.get_mpl_settings()
            s.write(filepath, sort_keys=False)
        except:
            QMessageBox.warning(self, "Warning",
                                "Cannot export settings to {}".format(filepath),
                                QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Information",
                                    "Successfully export settings to {}".format(filepath),
                                    QMessageBox.Ok)

    @pyqtSlot()
    def on_import_config(self):
        filepath, _ = QFileDialog.getOpenFileName(self,
                                                  "Open Settings",
                                                  "./mpl_settings.json",
                                                  "JSON Files (*.json)")
        if not filepath:
            return
        self._import_mpl_settings(filepath)

    def apply_mpl_settings(self, settings):
        pass

    def _import_mpl_settings(self, filepath):
        try:
            s = MatplotlibCurveWidgetSettings(filepath)
            self.apply_mpl_settings(s)
        except:
            QMessageBox.warning(self, "Warning",
                                "Cannot import&apply settings with {}".format(filepath),
                                QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Information",
                                    "Successfully import&apply settings with {}".format(filepath),
                                    QMessageBox.Ok)

    def get_mpl_settings(self):
        """Return all the settings for the current figure.
        """
        pass

    def resize_figure(self):
        """Must be triggered for set fig size.
        """
        self.canvas.resizeEvent(QResizeEvent(self.canvas.size(), self.canvas.size()))

    def set_figure_color(self, color=None):
        if color is None:
            color = self.sys_bg_color.getRgbF()
        self.figure.set_facecolor(color)
        self.figure.set_edgecolor(color)
        if MPL_VERSION > "1.5.1":
            self.axes.set_facecolor(color)
        else:
            self.axes.set_axis_bgcolor(color)

    def set_ticks_color(self, color=None):
        if color is None:
            color = self.sys_bg_color.getRgbF()
        all_lbls = self.axes.get_xticklabels() + self.axes.get_yticklabels()
        [lbl.set_color(color) for lbl in all_lbls]

    def set_ticks_visible(self, visible, xoy="x"):
        if getattr(self, "_fig_{}ticks_visible".format(xoy)):
            tklbls = getattr(self.axes, 'get_{}ticklabels'.format(xoy))()
            # !hiding cannot be reversed!
            [i.set_visible(visible) for i in tklbls]
        else:
            getattr(self.axes, '{}axis'.format(xoy)).reset_ticks()
            self.rotate_ticks(self._fig_xticks_angle, 'x')
            self.rotate_ticks(self._fig_yticks_angle, 'y')

    def set_xticks(self, tks):
        self.axes.set_xticks(tks)
        [set_font(lbl, self._fig_xyticks_font) for lbl in self.axes.get_xticklabels()]
        self.update_figure()

    def set_yticks(self, tks):
        self.axes.set_yticks(tks)
        [set_font(lbl, self._fig_xyticks_font) for lbl in self.axes.get_yticklabels()]
        self.update_figure()

    def set_xticklabels(self, tklbls):
        self.axes.set_xticklabels(tklbls)
        self.update_figure()

    def set_yticklabels(self, tklbls):
        self.axes.set_yticklabels(tklbls)
        self.update_figure()

    def toggle_mticks(self, f):
        if f:
            self.axes.xaxis.set_minor_locator(AutoMinorLocator())
            self.axes.yaxis.set_minor_locator(AutoMinorLocator())
        else:
            self.axes.xaxis.set_minor_locator(NullLocator())
            self.axes.yaxis.set_minor_locator(NullLocator())

    def toggle_grid(self,
                    toggle_checked=False,
                    which='major',
                    b=None,
                    color=None,
                    **kws):
        if toggle_checked:
            which = 'both' if kws.get('mticks', True) else 'major'
            self.axes.grid(which=which, color=color, linestyle='--')
        else:
            self.axes.grid(b=False, which='minor')
            self.axes.grid(b=False)

    def set_xylabel_font(self, font=None):
        if font is None:
            font = self.sys_label_font
        set_font(self.axes.xaxis.label, font)
        set_font(self.axes.yaxis.label, font)

    def set_xyticks_font(self, font=None):
        if font is None:
            font = self.sys_label_font
        all_lbls = self.axes.get_xticklabels() + self.axes.get_yticklabels()
        [set_font(lbl, font) for lbl in all_lbls]

    def set_title_font(self, font=None):
        if font is None:
            font = self.sys_title_font
        set_font(self.axes.title, font)

    def set_context_menu(self, ):
        self.setContextMenuPolicy(Qt.DefaultContextMenu)

    def clear_figure(self):
        self.axes.clear()
        self.update_figure()

    def clear_data(self):
        """Set with empty canvas.
        """
        pass

    @pyqtSlot('QString', float)
    def on_update_keycombo_cache(self, key, ts):
        self.dq_keycombo.append((key, ts))

    def _on_delay_pop(self, k, t):
        if (k, t) not in self.dq_keycombo:
            return
        self.process_keyshort(k)
        self.dq_keycombo.remove((k, t))

    def set_border_color(self, c):
        for _, o in self.axes.spines.items():
            o.set_color(c.getRgbF())

    def set_border_lw(self, x):
        for _, o in self.axes.spines.items():
            o.set_linewidth(x)

    def set_border_ls(self, s):
        for _, o in self.axes.spines.items():
            o.set_linestyle(s)

    def set_border_visible(self, f):
        for _, o in self.axes.spines.items():
            o.set_visible(f)

    def getFigureAutoScale(self):
        return self._fig_auto_scale

    @pyqtSlot(bool)
    def setFigureAutoScale(self, f):
        """Set xy limits as autoscale or not.

        Parameters
        ----------
        f : bool
            Toggle for the autoscale.
        """
        self._fig_auto_scale = f
        if f:
            self.set_autoscale()
        #
        self.autoScaleOnUpdated.emit(f)

    figureAutoScale = pyqtProperty(bool, getFigureAutoScale,
                                   setFigureAutoScale)

    def getFigureBorderColor(self):
        return self._fig_border_color

    @pyqtSlot(QColor)
    def setFigureBorderColor(self, c, **kws):
        """Set color for the data boundaries.

        Parameters
        ----------
        c : QColor
            Color of the boundaries.
        """
        self._fig_border_color = c
        self.set_border_color(c)
        self.update_figure()

    figureBorderColor = pyqtProperty(QColor, getFigureBorderColor,
                                     setFigureBorderColor)

    def getFigureBorderLineWidth(self):
        return self._fig_border_lw

    @pyqtSlot(float)
    def setFigureBorderLineWidth(self, x):
        """Set line width for the border.

        Parameters
        ----------
        x : float
            Line width.
        """
        self._fig_border_lw = x
        self.set_border_lw(x)
        self.update_figure()

    figureBorderLineWidth = pyqtProperty(float, getFigureBorderLineWidth,
                                         setFigureBorderLineWidth)

    def getFigureBorderLineStyle(self):
        return self._fig_border_ls

    @pyqtSlot('QString')
    def setFigureBorderLineStyle(self, s):
        """Set line style for the border.

        Parameters
        ----------
        s : str
            String for the line style, see `line style <https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D>`_.
        """
        if s not in LINE_STY_VALS:
            return
        self._fig_border_ls = s
        self.set_border_ls(s)
        self.update_figure()

    figureBorderLineStyle = pyqtProperty('QString',
                                         getFigureBorderLineStyle, setFigureBorderLineStyle)

    def getFigureBorderVisible(self):
        return self._fig_border_visible

    @pyqtSlot(bool)
    def setFigureBorderVisible(self, f):
        """Set borders visible or not.

        Parameters
        ----------
        f : bool
            Line visible (True) or not (False).
        """
        self._fig_border_visible = f
        self.set_border_visible(f)
        self.update_figure()

    figureBorderVisible = pyqtProperty(bool, getFigureBorderVisible,
                                       setFigureBorderVisible)

    def getFigureAspectRatio(self):
        return self._fig_aspect

    @pyqtSlot('QString')
    def setFigureAspectRatio(self, s):
        """Set aspect ratio of the axes.

        Parameters
        ----------
        s : str
            Aspect ratio, 'auto', 'equal' and any number.
        """
        try:
            float(s)
        except ValueError:
            if s in ('auto', 'equal'):
                self._fig_aspect = s
            else:
                return
        else:
            if float(s) <= 0:
                return
            self._fig_aspect = s
        finally:
            self.axes.set_aspect(self._fig_aspect)
            self.update_figure()

    figureAspectRatio = pyqtProperty('QString', getFigureAspectRatio,
                                     setFigureAspectRatio)

    def getTightLayoutToggle(self):
        return self._fig_tight_layout

    @pyqtSlot(bool)
    def setTightLayoutToggle(self, f):
        """Toggle for the tight layout.

        Parameters
        ----------
        f : bool
            Tight layout toggle.
        """
        self._fig_tight_layout = f
        if f:
            # self.figure.set_tight_layout({'pad': 0.1})
            self.figure.subplots_adjust(left=0.05, right=0.98, top=0.98, bottom=0.06)
        else:
            # self.figure.set_tight_layout({'pad': 1.2})
            self.figure.subplots_adjust(left=0.125, right=0.9, top=0.9, bottom=0.10)
        self.update_figure()

    figureTightLayout = pyqtProperty(bool, getTightLayoutToggle,
                                     setTightLayoutToggle)

    def getFigureXlabel(self):
        return self._fig_xlabel

    @pyqtSlot('QString')
    def setFigureXlabel(self, s):
        """Set xlabel string.

        Parameters
        ----------
        s : str
            String for xlabel.
        """
        self._fig_xlabel = s
        self.axes.set_xlabel(s)
        set_font(self.axes.xaxis.label, self._fig_xylabel_font)
        self.update_figure()

    figureXlabel = pyqtProperty('QString', getFigureXlabel, setFigureXlabel)

    def getFigureYlabel(self):
        return self._fig_ylabel

    @pyqtSlot('QString')
    def setFigureYlabel(self, s):
        """Set ylabel string.

        Parameters
        ----------
        s : str
            String for ylabel.
        """
        self._fig_ylabel = s
        self.axes.set_ylabel(s)
        set_font(self.axes.yaxis.label, self._fig_xylabel_font)
        self.update_figure()

    figureYlabel = pyqtProperty('QString', getFigureYlabel, setFigureYlabel)


    def getFigureXYlabelVisible(self):
        return self._fig_xylabel_visible

    @pyqtSlot(bool)
    def setFigureXYlabelVisible(self, f):
        """Set figure xylabels visible or not.

        Parameters
        ----------
        f : bool
            Figure xylabels visible or not.
        """
        self._fig_xylabel_visible = f
        self.axes.xaxis.label.set_visible(f)
        self.axes.yaxis.label.set_visible(f)
        self.update_figure()

    figureXYlabelVisible = pyqtProperty(bool, getFigureXYlabelVisible,
                                        setFigureXYlabelVisible)

    def getFigureTitleVisible(self):
        return self._fig_title_visible

    @pyqtSlot(bool)
    def setFigureTitleVisible(self, f):
        """Set figure title visible or not.

        Parameters
        ----------
        f : bool
            Figure title visible or not.
        """
        self._fig_title_visible = f
        self.axes.title.set_visible(f)
        self.update_figure()

    figureTitleVisible = pyqtProperty(bool, getFigureTitleVisible,
                                      setFigureTitleVisible)

    def getFigureTitle(self):
        return self._fig_title

    @pyqtSlot('QString')
    def setFigureTitle(self, s):
        """Set figure title.

        Parameters
        ----------
        s : str
            Title for the figure.
        """
        self._fig_title = s
        self.axes.set_title(s)
        set_font(self.axes.title, self._fig_title_font)
        self.update_figure()

    figureTitle = pyqtProperty('QString', getFigureTitle, setFigureTitle)

    def getFigureXYlabelFont(self):
        return self._fig_xylabel_font

    @pyqtSlot(QFont)
    def setFigureXYlabelFont(self, font):
        """Set font for x and y labels.

        Parameters
        ----------
        font : QFont
            Font to set.
        """
        self._fig_xylabel_font = font
        self.set_xylabel_font(font)
        self.update_figure()

    figureXYlabelFont = pyqtProperty(QFont, getFigureXYlabelFont,
                                     setFigureXYlabelFont)

    def getFigureTitleFont(self):
        return self._fig_title_font

    @pyqtSlot(QFont)
    def setFigureTitleFont(self, font):
        """Set font for figure title.

        Parameters
        ----------
        font : QFont
            Font to set.
        """
        self._fig_title_font = font
        self.set_title_font(font)
        self.update_figure()

    figureTitleFont = pyqtProperty(QFont, getFigureTitleFont,
                                   setFigureTitleFont)

    def getFigureWidth(self):
        return self._fig_width

    @pyqtSlot(float)
    def setFigureWidth(self, w):
        """Set figure width in inch.

        Parameters
        ----------
        w : float
            Figure width in inch (>= 2.0).
        """
        self._fig_width = max(w, 2.0)
        self.figure.set_size_inches([self._fig_width, self._fig_height])
        self.resize_figure()
        self.update_figure()

    figureWidth = pyqtProperty(float, getFigureWidth, setFigureWidth)

    def getFigureHeight(self):
        return self._fig_height

    @pyqtSlot(float)
    def setFigureHeight(self, h):
        """Set figure height in inch.

        Parameters
        ----------
        h : float
            Figure height in inch (>= 2.0).
        """
        self._fig_height = max(h, 2.0)
        self.figure.set_size_inches([self._fig_width, self._fig_height])
        self.resize_figure()
        self.update_figure()

    figureHeight = pyqtProperty(float, getFigureHeight, setFigureHeight)

    def getFigureDpi(self):
        return self._fig_dpi

    @pyqtSlot(float)
    def setFigureDpi(self, d):
        """Set figure dpi.

        Parameters
        ----------
        d : float
            Figure dpi in [50.0, 600.0].
        """
        self._fig_dpi = min(600.0, max(d, 50.0))
        self.figure.set_dpi(d)
        self.resize_figure()
        self.update_figure()

    figureDPI = pyqtProperty(float, getFigureDpi, setFigureDpi)

    def getXLimitMin(self):
        return self._xlim_min

    @pyqtSlot(float)
    def setXLimitMin(self, x=None):
        """Set minimum of xlimit.

        Parameters
        ----------
        x : float
            Minimum of xlimit.
        """
        if x is None:
            x, _ = self._get_default_xlim()
        self._xlim_min = x
        xmin, xmax = self.get_xlim()
        if x < xmax:
            self.axes.set_xlim([x, xmax])
            self.update_figure()
            self.xlimitMinChanged.emit(x)

    figureXLimitMin = pyqtProperty(float, getXLimitMin, setXLimitMin)

    def getXLimitMax(self):
        return self._xlim_max

    @pyqtSlot(float)
    def setXLimitMax(self, x=None):
        """Set maximum of xlimit.

        Parameters
        ----------
        x : float
            Maximum of xlimit.
        """
        if x is None:
            _, x = self._get_default_xlim()
        self._xlim_max = x
        xmin, xmax = self.get_xlim()
        if x > xmin:
            self.axes.set_xlim([xmin, x])
            self.update_figure()
            self.xlimitMaxChanged.emit(x)

    figureXLimitMax = pyqtProperty(float, getXLimitMax, setXLimitMax)

    def getYLimitMin(self):
        return self._ylim_min

    @pyqtSlot(float)
    def setYLimitMin(self, y=None):
        """Set minimum of ylimit.

        Parameters
        ----------
        y : float
            Minimum of ylimit.
        """
        if y is None:
            y, _ = self._get_default_ylim()
        self._ylim_min = y
        ymin, ymax = self.get_ylim()
        if y < ymax:
            self.axes.set_ylim([y, ymax])
            self.update_figure()
            self.ylimitMinChanged.emit(y)

    figureYLimitMin = pyqtProperty(float, getYLimitMin, setYLimitMin)

    def getYLimitMax(self):
        return self._ylim_max

    @pyqtSlot(float)
    def setYLimitMax(self, y=None):
        """Set maximum of ylimit.

        Parameters
        ----------
        y : float
            Maximum of ylimit.
        """
        if y is None:
            _, y = self._get_default_ylim()
        self._ylim_max = y
        ymin, ymax = self.get_ylim()
        if y > ymin:
            self.axes.set_ylim([ymin, y])
            self.update_figure()
            self.ylimitMaxChanged.emit(y)

    figureYLimitMax = pyqtProperty(float, getYLimitMax, setYLimitMax)

    def getFigureXTicksVisible(self):
        return self._fig_xticks_visible

    @pyqtSlot(bool)
    def setFigureXTicksVisible(self, f):
        """Set xticklabels visible or not.

        Parameters
        ----------
        f : bool
            Object visible (True) or not (False).
        """
        self.set_ticks_visible(f, "x")
        self.update_figure()
        self._fig_xticks_visible = f

    figureXTicksVisible = pyqtProperty(bool, getFigureXTicksVisible,
                                       setFigureXTicksVisible)

    def getFigureYTicksVisible(self):
        return self._fig_yticks_visible

    @pyqtSlot(bool)
    def setFigureYTicksVisible(self, f):
        """Set yticklabels visible or not.

        Parameters
        ----------
        f : bool
            Object visible (True) or not (False).
        """
        self.set_ticks_visible(f, "y")
        self.update_figure()
        self._fig_yticks_visible = f

    figureYTicksVisible = pyqtProperty(bool, getFigureYTicksVisible,
                                       setFigureYTicksVisible)

    def getFigureBgColor(self):
        return self._fig_bgcolor

    @pyqtSlot(QColor)
    def setFigureBgColor(self, color):
        """Set figure background color.

        Parameters
        ----------
        color : QColor
            Color to set.
        """
        self._fig_bgcolor = color
        self.set_figure_color(color.getRgbF())
        self.update_figure()
        self.bgColorChanged.emit(color)

    figureBackgroundColor = pyqtProperty(QColor, getFigureBgColor,
                                         setFigureBgColor)

    def getFigureGridColor(self):
        return self._fig_grid_color

    @pyqtSlot(QColor)
    def setFigureGridColor(self, c, **kws):
        """Set color for the grid line.

        Parameters
        ----------
        c : QColor
            Color of the grid line.
        """
        self._fig_grid_color = c
        self.toggle_grid(
            toggle_checked=self._fig_grid_toggle,
            color=c.getRgbF(),
            **{
                k: v
                for k, v in kws.items() if k not in ('toggle_checked', 'color')
            })
        self.update_figure()

    figureGridColor = pyqtProperty(QColor, getFigureGridColor,
                                   setFigureGridColor)

    def getFigureGridToggle(self):
        return self._fig_grid_toggle

    @pyqtSlot(bool)
    def setFigureGridToggle(self, f, **kws):
        """Toggle for the figure grid.

        Parameters
        ----------
        f : bool
            Figure grid toggle.
        """
        self._fig_grid_toggle = f
        self.toggle_grid(
            toggle_checked=f,
            color=self._fig_grid_color.getRgbF(),
            **{
                k: v
                for k, v in kws.items() if k not in ('toggle_checked', 'color')
            })
        self.update_figure()
        #
        self.gridOnUpdated.emit(f)

    figureGridToggle = pyqtProperty(bool, getFigureGridToggle,
                                    setFigureGridToggle)

    def getFigureMTicksToggle(self):
        return self._fig_mticks_toggle

    @pyqtSlot(bool)
    def setFigureMTicksToggle(self, f):
        """Toggle for the minor ticks.

        Note
        ----
        Before toggle on, be sure the axis scale is linear.

        Parameters
        ----------
        f : bool
            Minor ticks on/off toggle.
        """
        self._fig_mticks_toggle = f

        xscale = self.getFigureXScale()
        yscale = self.getFigureYScale()
        if xscale != 'linear':
            self.setFigureXScale('linear')
        if yscale != 'linear':
            self.setFigureYScale('linear')
        self.toggle_mticks(f)
        if xscale != 'linear':
            self.setFigureXScale(xscale)
        if yscale != 'linear':
            self.setFigureYScale(yscale)

        self.update_figure()

    figureMTicksToggle = pyqtProperty(bool, getFigureMTicksToggle,
                                      setFigureMTicksToggle)

    def getLegendToggle(self):
        return self._legend_toggle

    @pyqtSlot(bool)
    def setLegendToggle(self, f):
        """Toggle for figure legend.

        Parameters
        ----------
        f : bool
            Figure legend on/off toggle.
        """
        self._legend_toggle = f
        if f:
            self._legend_box = self.axes.legend(loc=self._legend_location)
        else:
            try:
                self._legend_box.set_visible(False)
            except AttributeError:
                pass
        self.update_figure()
        #
        self.legendOnUpdated.emit(f)

    figureLegendToggle = pyqtProperty(bool, getLegendToggle, setLegendToggle)

    def getLegendLocation(self):
        return self._legend_location

    @pyqtSlot(int)
    def setLegendLocation(self, i):
        """Set legend location.

        Parameters
        ----------
        i : int
            Index number of legend location,
            see `matplotlib.pyplot.legend <https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html>`_.
        """
        self._legend_location = i
        if self._legend_toggle:
            self._legend_box = self.axes.legend(loc=i)
            self.update_figure()

    figureLegendLocation = pyqtProperty(int, getLegendLocation,
                                        setLegendLocation)

    def getFigureXTicksAngle(self):
        return self._fig_xticks_angle

    @pyqtSlot(float)
    def setFigureXTicksAngle(self, angle):
        """Set rotation angle for the xtick labels.

        Parameters
        ----------
        angle : float
            Angle in degree to rotate.
        """
        self._fig_xticks_angle = angle
        self.rotate_ticks(angle, 'x')
        self.update_figure()

    figureXTicksAngle = pyqtProperty(float, getFigureXTicksAngle,
                                     setFigureXTicksAngle)

    def getFigureYTicksAngle(self):
        return self._fig_yticks_angle

    @pyqtSlot(float)
    def setFigureYTicksAngle(self, angle):
        """Set rotation angle for the ytick labels.

        Parameters
        ----------
        angle : float
            Angle in degree to rotate.
        """
        self._fig_yticks_angle = angle
        self.rotate_ticks(angle, 'y')
        self.update_figure()

    figureYTicksAngle = pyqtProperty(float, getFigureYTicksAngle,
                                     setFigureYTicksAngle)

    def getFigureXYticksFont(self):
        return self._fig_xyticks_font

    @pyqtSlot(QFont)
    def setFigureXYticksFont(self, font):
        """Set font for the tick labels.

        Parameters
        ----------
        font : QFont
            Font to set.
        """
        self._fig_xyticks_font = font
        self.set_xyticks_font(font)
        self.update_figure()

    figureXYticksFont = pyqtProperty(QFont, getFigureXYticksFont,
                                     setFigureXYticksFont)

    def getFigureXYticksColor(self):
        return self._fig_ticks_color

    @pyqtSlot(QColor)
    def setFigureXYticksColor(self, color):
        """Set color for the ticks.

        Parameters
        ----------
        color : QColor
            Color to set.
        """
        self._fig_ticks_color = color
        self.set_ticks_color(color.getRgbF())
        self.update_figure()

    figureXYticksColor = pyqtProperty(QColor, getFigureXYticksColor,
                                      setFigureXYticksColor)

    def getFigureXScale(self):
        return self._fig_xscale

    @pyqtSlot('QString')
    def setFigureXScale(self, s):
        """Set x-axis scale.

        Parameters
        ----------
        s : str
            Scale type, 'linear', 'log', 'symlog', 'logit', etc.
        """
        self._fig_xscale = s
        self.axes.set_xscale(s)
        self.update_figure()

    figureXScale = pyqtProperty('QString', getFigureXScale, setFigureXScale)

    def getFigureYScale(self):
        return self._fig_yscale

    @pyqtSlot('QString')
    def setFigureYScale(self, s):
        """Set y-axis scale.

        Parameters
        ----------
        s : str
            Scale type, 'linear', 'log', 'symlog', 'logit', etc.
        """
        self._fig_yscale = s
        self.axes.set_yscale(s)
        self.update_figure()

    figureYScale = pyqtProperty('QString', getFigureYScale, setFigureYScale)

    def getToolbarToggle(self):
        return self._fig_tb_toggle

    @pyqtSlot(bool)
    def setToolbarToggle(self, f):
        """Toggle for the mpl toolbar.

        Parameters
        ----------
        f : bool
            Turn on/off mpl toolbar.
        """
        self._fig_tb_toggle = f
        w = self._handlers.get('w_mpl_tools', None)
        if w is not None and not f:
            w.floatable_changed.emit(True)
            w.close()
        else:
            self.__show_mpl_tools()
        self.update_figure()

    figureToolbarToggle = pyqtProperty(bool, getToolbarToggle, setToolbarToggle)

    def _get_default_xlim(self):
        """limit range from data
        """
        try:
            xmin, xmax = self._x_data.min(), self._x_data.max()
        except:
            xmin, xmax = self.axes.get_xlim()
        x0, xhw = (xmin + xmax) * 0.5, (xmax - xmin) * 0.5
        return x0 - xhw * 1.1, x0 + xhw * 1.1

    def get_xlim(self):
        return self.axes.get_xlim()

    def _get_default_ylim(self):
        """limit range from data
        """
        try:
            ymin, ymax = self._y_data.min(), self._y_data.max()
        except:
            ymin, ymax = self.axes.get_ylim()
        y0, yhw = (ymin + ymax) * 0.5, (ymax - ymin) * 0.5
        return y0 - yhw * 1.1, y0 + yhw * 1.1

    def get_ylim(self):
        return self.axes.get_ylim()

    @pyqtSlot('QString', 'QString')
    def setXTickFormat(self, ftype, cfmt):
        if ftype == 'Auto':
            self._setXTickAutoFormat(ftype)
        elif ftype == 'Custom':
            self._setXTickCustomFormat(ftype, cfmt)

    def _setXTickAutoFormat(self, ftype):
        """Set x-axis ticks formatter with Auto style.

        Parameters
        ----------
        ftype : str
            Type of formatter, 'Auto'.
        """
        self._fig_xtick_formatter_type = ftype
        if self._fig_ticks_enable_mathtext:
            formatter = AUTOFORMATTER_MATHTEXT
        else:
            formatter = AUTOFORMATTER
        self._fig_xtick_formatter = formatter
        self.axes.xaxis.set_major_formatter(formatter)
        self.update_figure()

    def _setXTickCustomFormat(self, ftype, cfmt):
        """Set x-axis ticks formatter with custom style.

        Parameters
        ----------
        ftype : str
            Type of formatter, 'Custom'.
        cfmt : str
            C style string specifier.
        """
        self._fig_xtick_formatter_type = ftype
        self._fig_xtick_cfmt = cfmt
        formatter = generate_formatter(cfmt, math_text=self._fig_ticks_enable_mathtext)
        self._fig_xtick_formatter = formatter
        self.axes.xaxis.set_major_formatter(formatter)
        self.update_figure()

    @pyqtSlot('QString', 'QString')
    def setYTickFormat(self, ftype, cfmt):
        if ftype == 'Auto':
            self._setYTickAutoFormat(ftype)
        elif ftype == 'Custom':
            self._setYTickCustomFormat(ftype, cfmt)

    def _setYTickAutoFormat(self, ftype):
        """Set y-axis ticks formatter with Auto style.

        Parameters
        ----------
        ftype : str
            Type of formatter, 'Auto'.
        """
        self._fig_ytick_formatter_type = ftype
        if self._fig_ticks_enable_mathtext:
            formatter = AUTOFORMATTER_MATHTEXT
        else:
            formatter = AUTOFORMATTER
        self._fig_ytick_formatter = formatter
        self.axes.yaxis.set_major_formatter(formatter)
        self.update_figure()

    def _setYTickCustomFormat(self, ftype, cfmt):
        """Set y-axis ticks formatter with custom style.

        Parameters
        ----------
        ftype : str
            Type of formatter, 'Custom'.
        cfmt : str
            C style string specifier.
        """
        self._fig_ytick_formatter_type = ftype
        self._fig_ytick_cfmt = cfmt
        formatter = generate_formatter(cfmt, math_text=self._fig_ticks_enable_mathtext)
        self._fig_ytick_formatter = formatter
        self.axes.yaxis.set_major_formatter(formatter)
        self.update_figure()

    def rotate_ticks(self, angle, axis):
        """Rotate *axis* ticks by *angle* in degree.
        """
        lbls = getattr(self.axes, "get_{}ticklabels".format(axis))()
        for o in lbls:
            o.set_rotation(angle)

    def set_autoscale(self, axis='both'):
        self.axes.relim(visible_only=True)
        self.axes.autoscale(axis=axis)
        self.update_figure()

    def process_keyshort_combo(self, k1, k2):
        """Override this method to define combo keyshorts.
        """
        # print("Capture key combo: ", k1, k2)
        if k1 == 'a' and k2 == 'x':
            # auto xscale
            self.set_autoscale('x')
        elif k1 == 'a' and k2 == 'y':
            # auto yscale
            self.set_autoscale('y')
        elif k1 == 'a' and k2 == 'a':
            if self.widget_type == 'image':
                self.setAutoColorLimit(not self.getAutoColorLimit())
            # turn on/off autoscale
            self.setFigureAutoScale(not self.getFigureAutoScale())
        elif k1 == 'a' and k2 == 'c' and self.widget_type == 'image':
            # auto color range
            self.on_auto_clim()
        elif k1 == 'shift' and k2 == '?':
            # help msgbox
            self.kbd_help()
        elif k1 == 'c' and k2 == 'c':
            self._create_ctxtmenu().findChild(QAction, 'config_action').triggered.emit()
        elif k1 == 't' and k2 == 't':
            self._create_ctxtmenu().findChild(QAction, 'tb_action').triggered.emit()
        elif k1 == 'd' and k2 == 's' and self.widget_type in ('curve', 'errorbar'):
            # circulate curve drawstyle
            self.setLineDrawStyle(
                cycle_list_next(list(LINE_DS_VALS), self.getLineDrawStyle()))

    def process_keyshort(self, k):
        """Override this method to define keyshorts.
        """
        # print("Capture key: ", k)
        if k == 'g':
            # turn on/off grid
            self.setFigureGridToggle(not self.getFigureGridToggle())
        elif k == 'a': # and self.widget_type != 'image':
            # autoscale
            self.set_autoscale()
        elif k == 'm':
            # turn on/off mticks
            self.setFigureMTicksToggle(not self.getFigureMTicksToggle())
        elif k == 't':
            # turn on/off tightlayout
            self.setTightLayoutToggle(not self.getTightLayoutToggle())
        elif k == 'l':
            # turn on/off legend
            self.setLegendToggle(not self.getLegendToggle())
        elif k == 'r':
            # force refresh
            self.force_update()
        elif k == 's' and self.widget_type != 'image':
            # circulate y-axis scale type
            self.setFigureYScale(
                cycle_list_next(SCALE_STY_VALS, self.getFigureYScale()))
        elif k == 'c' and self.widget_type == 'image':
            # circulate image colormap
            self.setColorMap(
                cycle_list_next(ALL_COLORMAPS, self.getColorMap()))

    def kbd_help(self):
        """Help message box for keyboard shortcuts.
        """
        from .kbdhelpdialog import KbdHelpDialog
        w = KbdHelpDialog(self)
        w.setWindowTitle("Keyboard Shortcuts Help")
        w.exec_()

    def set_xlimit(self, *args):
        """Set xlimit with new limit, e.g. `set_xlimit(xmin, xmax)`.

        See Also
        --------
        setXLimitMin, setXLimitMax
        """
        self.axes.set_xlim(args)
        self.update_figure()

    def set_ylimit(self, *args):
        """Set ylimit with new limit.

        See Also
        --------
        setYLimitMin, setYLimitMax
        """
        self.axes.set_ylim(args)
        self.update_figure()


class MatplotlibBaseWidget(BasePlotWidget):
    """MatplotlibBaseWidget(BasePlotWidget)
    """

    def __init__(self, parent=None):
        super(MatplotlibBaseWidget, self).__init__(parent)
        self.widget_type = 'base'

    def init_figure(self):
        pass

    @pyqtSlot()
    def on_config(self):
        from .mplconfig import MatplotlibConfigPanel
        config_panel = MatplotlibConfigPanel(self)
        config_panel.exec_()

    def update_figure(self):
        if self._fig_auto_scale:
            try:
                self.axes.relim()
            except:
                pass
            else:
                self.axes.autoscale()
        self.canvas.draw_idle()


class MatplotlibCMapWidget(BasePlotWidget):
    def __init__(self, parent=None):
        super(MatplotlibCMapWidget, self).__init__(parent, False)
        self.figure.set_size_inches((self.getFigureWidth(), 0.2))
        self.figure.set_tight_layout(True)
        self.figure.subplots_adjust(
            top=0.9999, bottom=0.0001, left=0.0001, right=0.9999)
        self.axes.set_axis_off()

        # reverse cmap flag, '' or '_r'
        self._rcmap = ''

    def init_figure(self):
        gradient = np.linspace(0, 1, 256)
        gradient = np.vstack((gradient, gradient))
        self.im = self.axes.imshow(gradient, aspect='auto')

    def set_cmap(self, c):
        if not is_cmap_valid(c):
            return
        self._cmap = c
        self.im.set_cmap(self._cmap + self._rcmap)
        self.update_figure()

    def set_reverse_cmap(self, f):
        self._rcmap = '_r' if f else ''
        self.set_cmap(self._cmap)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])
    window = MatplotlibBaseWidget()
    window.show()

    app.exec_()
