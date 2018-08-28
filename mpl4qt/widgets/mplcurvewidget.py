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
        self._legend_toggle = False
        self._legend_location = 0
        super(MatplotlibCurveWidget, self).__init__(
            parent, self._fig_width, self._fig_height, self._fig_dpi)
        self._fig_bgcolor = self.sys_bg_color
        self._fig_ticks_color = self.sys_fg_color
        self._fig_grid_color = QColor('gray')
        self._fig_title = ''
        self._fig_xlabel = ''
        self._fig_ylabel = ''
        self._fig_xylabel_font = self.sys_label_font
        self._fig_xyticks_font = self.sys_label_font
        self._fig_title_font = self.sys_title_font
        # x,y limits
        self.setXLimitMin()
        self.setXLimitMax()
        self.setYLimitMin()
        self.setYLimitMax()
        # line_id
        self._line_id = 0
        self._lines = self.get_all_curves()  # all lines
        self._line_ids = range(self._lines.__len__())
        self._line = self._lines[0]  # current selected line
        self._line_color = QColor('red')
        self._line_width = 1.5
        self._mec, self._mfc = QColor('red'), QColor('red')
        self._mew = 1.0
        self._line_style = 'solid'
        self._marker_style = ''
        self._marker_size = 6.0
        self._line_label = '_line0'

    def add_curve(self, x_data=None, y_data=None, **kws):
        """Add one curve to figure.
        """
        if x_data is None or y_data is None:
            self.axes.plot([], [], **kws)
        else:
            self.axes.plot(x_data, y_data, **kws)
        self.update_legend()
        self.update_figure()

    def get_all_curves(self):
        """Return all curves."""
        return self.axes.lines

    def init_figure(self):
        # initial xy data and line
        self._x_data = x = np.linspace(-4, 4, 100)
        self._y_data = y = np.sin(10 * x) / x
        self._lines = self.axes.plot(x, y, 'r-')

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
        self.toggle_grid(
            toggle_checked=f,
            color=self._fig_grid_color.getRgbF(),
            **{
                k: v
                for k, v in kws.items() if k not in ('toggle_checked', 'color')
            })
        self.update_figure()

    figureGridToggle = pyqtProperty(bool, getFigureGridToggle,
                                    setFigureGridToggle)

    def getLegendToggle(self):
        return self._legend_toggle

    @pyqtSlot(bool)
    def setLegendToggle(self, f):
        self._legend_toggle = f
        if f:
            self._legend_box = self.axes.legend(loc=self._legend_location)
        else:
            self._legend_box.set_visible(False)
        self.update_figure()

    figureLegendToggle = pyqtProperty(bool, getLegendToggle, setLegendToggle)

    def getLegendLocation(self):
        return self._legend_location

    @pyqtSlot(int)
    def setLegendLocation(self, i):
        self._legend_location = i
        if self._legend_toggle:
            self._legend_box = self.axes.legend(loc=i)
            self.update_figure()

    figureLegendLocation = pyqtProperty(int, getLegendLocation,
                                        setLegendLocation)

    def getFigureGridColor(self):
        return self._fig_grid_color

    @pyqtSlot(QColor)
    def setFigureGridColor(self, c, **kws):
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

    def getLineColor(self):
        return self._line_color

    @pyqtSlot(QColor)
    def setLineColor(self, c):
        self._line_color = c
        self._line.set_color(c.getRgbF())
        self.update_figure()

    figureLineColor = pyqtProperty(QColor, getLineColor, setLineColor)

    def getMkEdgeColor(self):
        return self._mec

    @pyqtSlot(QColor)
    def setMkEdgeColor(self, c):
        self._mec = c
        self._line.set_mec(c.getRgbF())
        self.update_figure()

    figureMakerEdgeColor = pyqtProperty(QColor, getMkEdgeColor, setMkEdgeColor)

    def getMkFaceColor(self):
        return self._mfc

    @pyqtSlot(QColor)
    def setMkFaceColor(self, c):
        self._mfc = c
        self._line.set_mfc(c.getRgbF())
        self.update_figure()

    figureMakerFaceColor = pyqtProperty(QColor, getMkFaceColor, setMkFaceColor)

    def getLineStyle(self):
        return self._line_style

    @pyqtSlot('QString')
    def setLineStyle(self, s):
        self._line_style = s
        self._line.set_ls(s)
        self.update_figure()

    figureLineStyle = pyqtProperty('QString', getLineStyle, setLineStyle)

    def getMarkerStyle(self):
        return self._marker_style

    @pyqtSlot('QString')
    def setMarkerStyle(self, s):
        self._marker_style = s
        self._line.set_marker(s)
        self.update_figure()

    figureMarkerStyle = pyqtProperty('QString', getMarkerStyle, setMarkerStyle)

    def getMarkerThickness(self):
        return self._mew

    @pyqtSlot(float)
    def setMarkerThickness(self, x):
        self._mew = x
        self._line.set_mew(x)
        self.update_figure()

    figureMarkerThickness = pyqtProperty(float, getMarkerThickness,
                                         setMarkerThickness)

    def getLineLabel(self):
        return self._line_label

    @pyqtSlot('QString')
    def setLineLabel(self, s):
        self._line_label = s
        self._line.set_label(s)
        self.update_legend()
        self.update_figure()

    figureLineLabel = pyqtProperty('QString', getLineLabel, setLineLabel)

    def getLineWidth(self):
        return self._line_width

    @pyqtSlot(float)
    def setLineWidth(self, x):
        self._line_width = x
        self._line.set_lw(x)
        self.update_figure()

    figureLineWidth = pyqtProperty(float, getLineWidth, setLineWidth)

    def getMarkerSize(self):
        return self._marker_size

    @pyqtSlot(float)
    def setMarkerSize(self, x):
        self._marker_size = x
        self._line.set_ms(x)
        self.update_figure()

    figureMarkerSize = pyqtProperty(float, getMarkerSize, setMarkerSize)

    def getLineID(self):
        return self._line_id

    @pyqtSlot(int)
    def setLineID(self, i):
        lines = self.get_all_curves()
        if i < lines.__len__():
            self._line_id = i
            self._line = lines[i]

    def get_line_config(self):
        """Get line config: ls, lw, c, marker, ms, mew, mec, mfc, label
        """
        return {
            p: getattr(self._line, 'get_' + p)()
            for p in ('ls', 'lw', 'c', 'ms', 'mew', 'mec', 'mfc', 'marker',
                      'label')
        }

    def getFigureAutoScale(self):
        return self._fig_auto_scale

    @pyqtSlot(bool)
    def setFigureAutoScale(self, f):
        self._fig_auto_scale = f
        if f:
            self.axes.autoscale()
            self.update_canvas()
            self.update_figure()

    figureAutoScale = pyqtProperty(bool, getFigureAutoScale,
                                   setFigureAutoScale)

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

    def getXLimitMin(self):
        return self._xlim_min

    @pyqtSlot(float)
    def setXLimitMin(self, x=None):
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
        if y is None:
            _, y = self._get_default_ylim()
        self._ylim_max = y
        ymin, ymax = self.get_ylim()
        if y > ymin:
            self.axes.set_ylim([ymin, y])
            self.update_figure()

    figureYLimitMax = pyqtProperty(float, getYLimitMax, setYLimitMax)

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

    def on_reset(self):
        print("Reset action triggered")

    def update_legend(self):
        # update legend if on
        self.setLegendToggle(self._legend_toggle)


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    window = MatplotlibCurveWidget()
    window.show()
    sys.exit(app.exec_())
