#!/usr/bin/env python

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

from PyQt5.QtCore import pyqtProperty, pyqtSlot, QSize
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget

import numpy as np

from mpl4qt.widgets.mplbasewidget import BasePlotWidget


class MatplotlibCurveWidget(BasePlotWidget):
    """MatplotlibCurveWidget(BasePlotWidget)

    Provides a custom widget to draw curves with matplotlib, with properties
    and slots that can be used to customize its appearance.
    """
    def __init__(self, parent=None):
        self._fig_width = 5
        self._fig_height = 4
        self._fig_dpi = 100
        self._fig_tight_layout = False
        self._fig_auto_scale = False
        super(MatplotlibCurveWidget, self).__init__(parent,
                self._fig_width, self._fig_height, self._fig_dpi)
        self._fig_bgcolor = self.sys_bg_color

        # test
        # 1.5.1
        #self.axes.set_axis_bgcolor("blue")
        # 2.1.2
        #self.axes.set_facecolor("blue")

    def init_figure(self):
        x = np.linspace(-4, 4, 400)
        y = np.sin(10 * x) / x
        self.line, = self.axes.plot(x, y, 'r-')

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

    def getFigureWidth(self):
        return self._fig_width

    @pyqtSlot(int)
    def setFigureWidth(self, w):
        self._fig_width = max(w, 2)
        self.figure.set_size_inches([w, self._fig_height])
        self.update_figure()

    figureWidth = pyqtProperty(int, getFigureWidth, setFigureWidth)

    def getFigureHeight(self):
        return self._fig_height

    @pyqtSlot(int)
    def setFigureHeight(self, h):
        self._fig_height = max(h, 2)
        self.figure.set_size_inches([self._fig_width, h])
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

    def getFigureBgColor(self):
        return self._fig_bgcolor

    @pyqtSlot(QColor)
    def setFigureBgColor(self, color):
        self._fig_bgcolor = color
        self.set_figure_color(color.getRgbF())
        self.update_figure()

    figureBackgroundColor = pyqtProperty(QColor, getFigureBgColor,
            setFigureBgColor)

    def getCurveXData(self):
        return self.line.get_xdata().__len__()
    
    @pyqtSlot(int)
    def setCurveXData(self, n):
        xx = np.random.normal(0, 10, n)
        hist, edge = np.histogram(xx, bins=100, density=True)
        self.line.set_xdata((edge[:-1]+edge[1:])/2.0)
        self.line.set_ydata(hist)
        self.update_canvas()
        self.update_figure()

    curveXData = pyqtProperty(int, getCurveXData, setCurveXData)

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

    def update_figure(self):
        if self.getFigureAutoScale():
            self.axes.relim()
            self.axes.autoscale()
        self.figure.canvas.draw_idle()
        self.update()


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    window = MatplotlibCurveWidget()
    window.show()
    sys.exit(app.exec_())
