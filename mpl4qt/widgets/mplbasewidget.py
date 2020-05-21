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
from collections import deque
from functools import partial

import matplotlib as mpl
import numpy as np
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QVariant
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import NullLocator

from mpl4qt.widgets.mpltoolbar import MToolbar
from mpl4qt.widgets.utils import LINE_STY_VALS
from mpl4qt.widgets.utils import mfont_to_qfont
from mpl4qt.widgets.utils import mplcolor2hex
from mpl4qt.widgets.utils import set_font
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

    # xy pos, x,y or x,y,z
    xyposUpdated = pyqtSignal(list)

    def __init__(self, parent=None, show_toolbar=True, **kws):
        super(BasePlotWidget, self).__init__(parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
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

        # dnd
        self.setAcceptDrops(True)

        # window/widget/dialog handlers
        self._handlers = {}

        # hvlines
        self._hline = None        # h-ruler
        self._vline = None        # v-ruler
        self._cpoint = None       # cross-point of h,v rulers
        self._cpoint_text = None  # coord annote of cross-point
        self._ruler_on = False    # default is not enabled
        self._visible_hvlines = True  # default visibility

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

    def __show_mpl_tools(self):
        if 'w_mpl_tools' in self._handlers:
            w = self._handlers['w_mpl_tools']
        else:
            w = MToolbar(self.figure.canvas, self)
            self._handlers['w_mpl_tools'] = w
            w.selectedIndicesUpdated.connect(self.on_selected_indices)
            w.zoom_roi_changed.connect(self.on_zoom_roi_changed)
        w.show_toolbar()
        w.floatable_changed.emit(False)
        print("MPL Toolbar: ", id(w))

    @pyqtSlot(QVariant, QVariant)
    def on_selected_indices(self, ind, pts):
        self.selectedIndicesUpdated.emit(ind, pts)

    @pyqtSlot(tuple, tuple)
    def on_zoom_roi_changed(self, xlim, ylim):
        print("Zoomed Rect ROI: ", xlim, ylim)
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
        # xy ticklabels
        tklbl = self.axes.get_xticklabels()[0]
        self._fig_xyticks_font = mfont_to_qfont(tklbl.get_fontproperties())
        # title
        title = self.axes.title
        self._fig_title_font = mfont_to_qfont(title.get_fontproperties())

        ## border
        o = list(self.axes.spines.values())[0]
        # c, lw, ls, vis
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

    def on_motion(self, e):
        pass

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

    def on_pick(self, e):
        pass

    def on_press(self, e):
        print(e.button)

    def on_release(self, e):
        pass

    def dragEnterEvent(self, e):
        pass

    def dropEvent(self, e):
        pass

    def init_figure(self):
        raise NotImplementedError

    def update_figure(self):
        self.canvas.draw_idle()

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

    def set_xticks(self, tks):
        self.axes.set_xticks(tks)
        self.update_figure()

    def set_yticks(self, tks):
        self.axes.set_yticks(tks)
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

    def process_keyshort(self, k):
        """Override this method to define keyshorts.
        """
        print("Capture key: ", k)

    def process_keyshort_combo(self, k1, k2):
        """Override this method to define combo keyshorts.
        """
        print("Capture key combo: ", k1, k2)

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
            self.axes.autoscale()
            self.update_figure()
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
        self.update_figure()

    figureYlabel = pyqtProperty('QString', getFigureYlabel, setFigureYlabel)

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
        xmin, xmax = self._x_data.min(), self._x_data.max()
        x0, xhw = (xmin + xmax) * 0.5, (xmax - xmin) * 0.5
        return x0 - xhw * 1.1, x0 + xhw * 1.1

    def get_xlim(self):
        return self.axes.get_xlim()

    def _get_default_ylim(self):
        """limit range from data
        """
        ymin, ymax = self._y_data.min(), self._y_data.max()
        y0, yhw = (ymin + ymax) * 0.5, (ymax - ymin) * 0.5
        return y0 - yhw * 1.1, y0 + yhw * 1.1

    def get_ylim(self):
        return self.axes.get_ylim()



class MatplotlibBaseWidget(BasePlotWidget):
    """MatplotlibBaseWidget(BasePlotWidget)
    """

    def __init__(self, parent=None):
        super(MatplotlibBaseWidget, self).__init__(parent)

    def init_figure(self):
        pass


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
