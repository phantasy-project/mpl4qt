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

from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib as mpl

import numpy as np

from mpl4qt.widgets.mpltoolbar import NavigationToolbar

MPL_VERSION = mpl.__version__


class BasePlotWidget(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, **kws):
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.figure.add_subplot(111)
        self.init_figure()
        super(BasePlotWidget, self).__init__(self.figure)
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
        self.adjustSize()
        self.set_context_menu()

    def post_style_figure(self):
        self.set_figure_color()

    def init_figure(self):
        raise NotImplementedError

    def update_figure(self):
        self.figure.canvas.draw_idle()
        self.update()

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

    def toggle_mticks(self, f):
        if f:
            self.axes.minorticks_on()
        else:
            self.axes.minorticks_off()

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
        _set_font(self.axes.xaxis.label, font)
        _set_font(self.axes.yaxis.label, font)

    def set_xyticks_font(self, font=None):
        if font is None:
            font = self.sys_label_font
        all_lbls = self.axes.get_xticklabels() + self.axes.get_yticklabels()
        [_set_font(lbl, font) for lbl in all_lbls]

    def set_title_font(self, font=None):
        if font is None:
            font = self.sys_title_font
        _set_font(self.axes.title, font)

    def update_canvas(self):
        self.draw_idle()

    def set_context_menu(self, ):
        self.setContextMenuPolicy(Qt.DefaultContextMenu)


def _set_font(obj, font):
    obj.set_size(font.pointSizeF())
    obj.set_family(font.family())
    obj.set_weight(int(font.weight() / 87.0 * 1000))
    obj.set_stretch(font.stretch())
    if font.italic():
        obj.set_style('italic')
    else:
        obj.set_style('normal')
