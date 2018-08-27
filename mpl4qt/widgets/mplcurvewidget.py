#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
mplcurvewidget.py

A PyQt custom widget for Qt Designer: draw curves with matplotlib

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

from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QFont

import numpy as np

from mpl4qt.widgets.mplbasewidget import BasePlotWidget
from mpl4qt.widgets.mplconfig import MatplotlibConfigPanel


class MatplotlibCurveWidget(BasePlotWidget):
    """MatplotlibCurveWidget(BasePlotWidget)

    Provides a custom widget to draw curves with matplotlib, with properties
    and slots that can be used to customize its appearance.
    """
    def __init__(self, parent=None):
        self._fig_width = 4
        self._fig_height = 3
        self._fig_dpi = 120
        self._fig_tight_layout = False
        self._fig_auto_scale = False
        self._fig_mticks_toggle = False
        self._fig_grid_toggle = False
        super(MatplotlibCurveWidget, self).__init__(parent,
                self._fig_width, self._fig_height, self._fig_dpi)
        self._fig_bgcolor = self.sys_bg_color
        self._fig_ticks_color = self.sys_fg_color
        self._fig_grid_color = QColor('gray')
        self._fig_title = ''
        self._fig_xlabel = ''
        self._fig_ylabel = ''
        self._fig_xylabel_font = self.sys_label_font
        self._fig_xyticks_font = self.sys_label_font
        self._fig_title_font = self.sys_title_font

    def init_figure(self):
        # initial xy data and line
        self._x_data = x = np.linspace(-4, 4, 100)
        self._y_data = y = np.sin(10 * x) / x
        self._line, = self.axes.plot(x, y, 'r-')

    def sizeHint(self):
        return QSize(1.1 * self._fig_width * self._fig_dpi,
                     1.1 * self._fig_height * self._fig_dpi)

    def getTightLayoutToggle(self):
        return self._fig_tight_layout

    @pyqtSlot(bool)
    def setTightLayoutToggle(self, f):
        self._fig_tight_layout = f
        if f:
            self.figure.set_tight_layout({'pad': 0.1})
        else:
            self.figure.set_tight_layout({'pad': 1.2})
        self.update_figure()

    figureTightLayout = pyqtProperty(bool, getTightLayoutToggle,
            setTightLayoutToggle)

    def getFigureMTicksToggle(self):
        return self._fig_mticks_toggle

    @pyqtSlot(bool)
    def setFigureMTicksToggle(self, f):
        self._fig_mticks_toggle = f
        self.toggle_mticks(f)
        self.update_figure()

    figureMTicksToggle = pyqtProperty(bool, getFigureMTicksToggle,
            setFigureMTicksToggle)

    def getFigureGridToggle(self):
        return self._fig_grid_toggle

    @pyqtSlot(bool)
    def setFigureGridToggle(self, f, **kws):
        self._fig_grid_toggle = f
        self.toggle_grid(toggle_checked=f, color=self._fig_grid_color.getRgbF(), **{k:v for k,v in kws.items() if k not in ('toggle_checked', 'color')})
        self.update_figure()

    figureGridToggle = pyqtProperty(bool, getFigureGridToggle,
            setFigureGridToggle)

    def getFigureGridColor(self):
        return self._fig_grid_color

    @pyqtSlot(QColor)
    def setFigureGridColor(self, c, **kws):
        self._fig_grid_color = c
        self.toggle_grid(toggle_checked=self._fig_grid_toggle, color=c.getRgbF(), **{k:v for k,v in kws.items() if k not in ('toggle_checked', 'color')})
        self.update_figure()

    figureGridColor = pyqtProperty(QColor, getFigureGridColor,
            setFigureGridColor)

    def getFigureWidth(self):
        return self._fig_width

    @pyqtSlot(int)
    def setFigureWidth(self, w):
        self._fig_width = max(w, 2)
        self.figure.set_size_inches([self._fig_width, self._fig_height])
        self.update_figure()

    figureWidth = pyqtProperty(int, getFigureWidth, setFigureWidth)

    def getFigureHeight(self):
        return self._fig_height

    @pyqtSlot(int)
    def setFigureHeight(self, h):
        self._fig_height = max(h, 2)
        self.figure.set_size_inches([self._fig_width, self._fig_height])
        self.update_figure()

    figureHeight = pyqtProperty(int, getFigureHeight, setFigureHeight)

    def getFigureDpi(self):
        return self._fig_dpi

    @pyqtSlot(int)
    def setFigureDpi(self, d):
        self._fig_dpi = min(1000, max(d, 50))
        self.figure.set_dpi(d)
        self.update_figure()

    figureDPI = pyqtProperty(int, getFigureDpi, setFigureDpi)

    def getFigureXYlabelFont(self):
        return self._fig_xylabel_font

    @pyqtSlot(QFont)
    def setFigureXYlabelFont(self, font):
        self._fig_xylabel_font = font
        self.set_xylabel_font(font)
        self.update_figure()

    figureXYlabelFont = pyqtProperty(QFont, getFigureXYlabelFont,
            setFigureXYlabelFont)

    def getFigureXYticksFont(self):
        return self._fig_xyticks_font

    @pyqtSlot(QFont)
    def setFigureXYticksFont(self, font):
        self._fig_xyticks_font = font
        self.set_xyticks_font(font)
        self.update_figure()

    figureXYticksFont = pyqtProperty(QFont, getFigureXYticksFont,
            setFigureXYticksFont)

    def getFigureTitleFont(self):
        return self._fig_title_font

    @pyqtSlot(QFont)
    def setFigureTitleFont(self, font):
        self._fig_title_font = font
        self.set_title_font(font)
        self.update_figure()

    figureTitleFont = pyqtProperty(QFont, getFigureTitleFont,
            setFigureTitleFont)

    def getFigureBgColor(self):
        return self._fig_bgcolor

    @pyqtSlot(QColor)
    def setFigureBgColor(self, color):
        self._fig_bgcolor = color
        self.set_figure_color(color.getRgbF())
        self.update_figure()

    figureBackgroundColor = pyqtProperty(QColor, getFigureBgColor,
            setFigureBgColor)

    def getFigureXYticksColor(self):
        return self._fig_ticks_color

    @pyqtSlot(QColor)
    def setFigureXYticksColor(self, color):
        self._fig_ticks_color = color
        self.set_ticks_color(color.getRgbF())
        self.update_figure()

    figureXYticksColor = pyqtProperty(QColor, getFigureXYticksColor,
            setFigureXYticksColor)

    def getFigureAutoScale(self):
        return self._fig_auto_scale

    @pyqtSlot(bool)
    def setFigureAutoScale(self, f):
        self._fig_auto_scale = f
        if f:
            self.axes.autoscale()
            self.update_canvas()
            self.update_figure()

    figureAutoScale = pyqtProperty(bool, getFigureAutoScale, setFigureAutoScale)

    def getFigureTitle(self):
        return self._fig_title

    @pyqtSlot('QString')
    def setFigureTitle(self, s):
        self._fig_title = s
        self.axes.set_title(s)
        self.update_figure()

    figureTitle = pyqtProperty('QString', getFigureTitle, setFigureTitle)

    def getFigureXlabel(self):
        return self._fig_xlabel

    @pyqtSlot('QString')
    def setFigureXlabel(self, s):
        self._fig_xlabel = s
        self.axes.set_xlabel(s)
        self.update_figure()

    figureXlabel = pyqtProperty('QString', getFigureXlabel, setFigureXlabel)

    def getFigureYlabel(self):
        return self._fig_ylabel

    @pyqtSlot('QString')
    def setFigureYlabel(self, s):
        self._fig_ylabel = s
        self.axes.set_ylabel(s)
        self.update_figure()

    figureYlabel = pyqtProperty('QString', getFigureYlabel, setFigureYlabel)

    @pyqtSlot(QVariant)
    def setXData(self, x):
        """set x data for figure."""
        self._x_data = x
        self._line.set_xdata(x)
        self.update_figure()

    def getXData(self):
        return self._x_data

    @pyqtSlot(QVariant)
    def setYData(self, x):
        """set y data for figure."""
        self._y_data = x
        self._line.set_ydata(x)
        self.update_figure()

    def getYData(self):
        return self._y_data

    def update_figure(self):
        if self.getFigureAutoScale():
            self.axes.relim()
            self.axes.autoscale()
        self.figure.canvas.draw_idle()
        self.update()

    def contextMenuEvent(self, e):
        menu = QMenu(self)
        config_action = QAction("Config", menu)
        reset_action = QAction("Reset", menu)
        menu.addAction(config_action)
        menu.addSeparator()
        menu.addAction(reset_action)

        config_action.triggered.connect(self.on_config)
        reset_action.triggered.connect(self.on_reset)

        menu.exec_(self.mapToGlobal(e.pos()))

        #menu.move(e.globalPos())
        #menu.show()
        #menu.activateWindow()

    def on_config(self):
        config_panel = MatplotlibConfigPanel(self)
        r = config_panel.exec_()
        #print(r == QDialog.Accepted)
        #print(r == QDialog.Rejected)

    def on_reset(self):
        print("Reset action triggered")


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    window = MatplotlibCurveWidget()
    window.show()
    sys.exit(app.exec_())
