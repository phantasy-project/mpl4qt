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

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import NullLocator

import numpy as np
import time
from collections import deque
from functools import partial

from .utils import set_font
from .utils import mfont_to_qfont
from .utils import mplcolor2hex
from .utils import LINE_STY_VALS

MPL_VERSION = mpl.__version__
DTMSEC = 500  # msec
DTSEC = DTMSEC / 1000.0  # sec


class BasePlotWidget(QWidget):
    # combo keyshorts, keystring, timestamp
    keycombo_cached = pyqtSignal(str, float)

    def __init__(self, parent=None, width=5, height=4, dpi=100, **kws):
        super(BasePlotWidget, self).__init__(parent)
        self.figure = Figure(figsize=(width, height), dpi=dpi)
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

        # pan
        self._pan_on = False

        # keypress cache
        self.dq_keycombo = deque([], 2)
        self.keycombo_cached.connect(self.on_update_keycombo_cache)

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
        ## font:
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


class MatplotlibBaseWidget(BasePlotWidget):
    """MatplotlibBaseWidget(BasePlotWidget)
    """
    def __init__(self, parent=None):
         super(MatplotlibBaseWidget, self).__init__(parent)

    def init_figure(self):
        pass


class MatplotlibCMapWidget(BasePlotWidget):
    def __init__(self, parent=None):
        super(MatplotlibCMapWidget, self).__init__(parent, height=0.2)
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
