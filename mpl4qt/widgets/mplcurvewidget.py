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

from collections import OrderedDict

import numpy as np
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QVariant
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMessageBox

from mpl4qt.widgets.kbdhelpdialog import KbdHelpDialog
from mpl4qt.widgets.mplbasewidget import BasePlotWidget
from mpl4qt.widgets.mplconfig import MatplotlibConfigPanel
from mpl4qt.widgets.mpltoolbar import MToolbar
from mpl4qt.widgets.utils import ALL_COLORMAPS
from mpl4qt.widgets.utils import AUTOFORMATTER
from mpl4qt.widgets.utils import AUTOFORMATTER_MATHTEXT
from mpl4qt.widgets.utils import DEFAULT_MPL_SETTINGS
from mpl4qt.widgets.utils import LINE_STY_VALS
from mpl4qt.widgets.utils import MK_SYMBOL
from mpl4qt.widgets.utils import MatplotlibCurveWidgetSettings
from mpl4qt.widgets.utils import SCALE_STY_VALS
from mpl4qt.widgets.utils import cycle_list_next
from mpl4qt.widgets.utils import generate_formatter
from mpl4qt.widgets.utils import mplcolor2hex


class MatplotlibCurveWidget(BasePlotWidget):
    """MatplotlibCurveWidget(BasePlotWidget)

    Provides a custom widget to draw curves with matplotlib, with properties
    and slots that can be used to customize its appearance.
    """
    # indices list of points selected by lasso tool,
    # ind: array, pts: array (selected)
    # for i,idx in enumerate(ind): idx, pts[i]
    selectedIndicesUpdated = pyqtSignal(QVariant, QVariant)

    # xy pos, x,y or x,y,z
    xyposUpdated = pyqtSignal(list)

    # grid
    gridOnUpdated = pyqtSignal(bool)

    # legend
    legendOnUpdated = pyqtSignal(bool)

    # autoscale
    autoScaleOnUpdated = pyqtSignal(bool)

    # bg color
    bgColorChanged = pyqtSignal(QColor)

    # zoomed ROI changed
    zoom_roi_changed = pyqtSignal(tuple, tuple)

    def __init__(self, parent=None):
        self._fig_auto_scale = False
        self._fig_xscale = 'linear'
        self._fig_yscale = 'linear'
        self._fig_mticks_toggle = False
        self._fig_grid_toggle = False
        self._legend_toggle = False
        self._legend_location = 0
        super(MatplotlibCurveWidget, self).__init__(parent)
        self._fig_bgcolor = self.sys_bg_color
        self._fig_ticks_color = self.sys_fg_color
        self._fig_grid_color = QColor('gray')
        self._fig_xtick_formatter_type = 'Auto'
        self._fig_xtick_formatter = None  # placeholder only
        self._fig_xtick_cfmt = ''  # c string format for FuncFormatter
        self._fig_ytick_formatter_type = 'Auto'
        self._fig_ytick_formatter = None  # placeholder only
        self._fig_ytick_cfmt = ''  # c string format for FuncFormatter
        self._fig_ticks_enable_mathtext = False  # use math text or not
        self._fig_xticks_angle = 0
        self._fig_yticks_angle = 0
        # x,y limits
        self.setXLimitMin()
        self.setXLimitMax()
        self.setYLimitMin()
        self.setYLimitMax()
        # line_id
        self._line_id = 0
        self._line_visible = True
        self._line_ids = range(self._lines.__len__())
        self._line_color = QColor('red')
        self._line_alpha = 1.0
        self._line_width = 1.5
        self._mec, self._mfc = QColor('red'), QColor('red')
        self._mew = 1.0
        self._line_style = 'solid'
        self._marker_style = ''
        self._marker_size = 6.0
        self._line_label = '_line0'

        # widget type
        self.widget_type = 'curve'

        # tb_toggle
        self._fig_tb_toggle = True
        # show mpltool by default.
        self.__show_mpl_tools()

    def add_curve(self, x_data=None, y_data=None, **kws):
        """Add one curve to figure, accepts all ``pyplot.plot`` keyword
        arguments, see `matplotlib.pyplot.plot <https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html>`_.

        Parameters
        ----------
        x_data : list or array
            Array of x data.
        y_data : list or array
            Array of y data.

        Returns
        -------
        o : Line2D
            The added line object.
        """
        if x_data is None or y_data is None:
            l, = self.axes.plot([], [], **kws)
        else:
            l, = self.axes.plot(x_data, y_data, **kws)
        self._lines.append(l)
        self.update_legend()
        self.update_figure()
        return l

    def update_curve(self, x_data, y_data, **kws):
        """Update curve by feeding two 1D array: *x_data* and *y_data*.
        """
        self._line.set_data(x_data, y_data)
        self._x_data, self._y_data = x_data, y_data
        self.update_figure()

    def get_all_curves(self):
        """Return all curves."""
        return self._lines

    def init_figure(self):
        # initial xy data and line
        self._x_data = x = np.linspace(-4, 4, 100)
        self._y_data = y = np.sin(10 * x) / x
        self._lines = self.axes.plot(x, y, 'r-')

        # set current line
        self.setLineID(0)

    def sizeHint(self):
        return QSize(1.1 * self._fig_width * self._fig_dpi,
                     1.1 * self._fig_height * self._fig_dpi)

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

    def getLineAlpha(self):
        return self._line_alpha

    def setLineAlpha(self, x):
        """Set line opacity, range from 0 to 1.0.

        Parameters
        ----------
        x : float
            Alpha value, 0 to 1.0 (defalut).
        """
        self._line_alpha = x
        self._line.set_alpha(x)
        self.update_figure()

    figureLineAlpha = pyqtProperty(float, getLineAlpha, setLineAlpha)

    def getLineColor(self):
        return self._line_color

    @pyqtSlot(QColor)
    def setLineColor(self, c):
        """Set line color for the current curve.

        Parameters
        ----------
        c : QColor
            Color to set.
        """
        self._line_color = c
        self._line.set_color(c.getRgbF())
        self.update_figure()

    figureLineColor = pyqtProperty(QColor, getLineColor, setLineColor)

    def getMkEdgeColor(self):
        return self._mec

    @pyqtSlot(QColor)
    def setMkEdgeColor(self, c):
        """Set marker edgecolor.

        Parameters
        ----------
        c : QColor
            Color to set.
        """
        self._mec = c
        self._line.set_mec(c.getRgbF())
        self.update_figure()

    figureMakerEdgeColor = pyqtProperty(QColor, getMkEdgeColor, setMkEdgeColor)

    def getMkFaceColor(self):
        return self._mfc

    @pyqtSlot(QColor)
    def setMkFaceColor(self, c):
        """Set marker facecolor.

        Parameters
        ----------
        c : QColor
            Color to set.
        """
        self._mfc = c
        self._line.set_mfc(c.getRgbF())
        self.update_figure()

    figureMakerFaceColor = pyqtProperty(QColor, getMkFaceColor, setMkFaceColor)

    def getLineStyle(self):
        return self._line_style

    @pyqtSlot('QString')
    def setLineStyle(self, s):
        """Set line style for the current curve.

        Parameters
        ----------
        s : str
            String for the line style, see `line style <https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D>`_.
        """
        if s not in LINE_STY_VALS:
            return
        self._line_style = s
        self._line.set_ls(s)
        self.update_figure()

    figureLineStyle = pyqtProperty('QString', getLineStyle, setLineStyle)

    def getMarkerStyle(self):
        return self._marker_style

    @pyqtSlot('QString')
    def setMarkerStyle(self, s):
        """Set marker style.

        Parameters
        ----------
        s : str
            String for the marker style, see `marker style <https://matplotlib.org/api/markers_api.html>`_.
        """
        if s not in MK_SYMBOL:
            return
        self._marker_style = s
        self._line.set_marker(s)
        self.update_figure()

    figureMarkerStyle = pyqtProperty('QString', getMarkerStyle, setMarkerStyle)

    def getMarkerThickness(self):
        return self._mew

    @pyqtSlot(float)
    def setMarkerThickness(self, x):
        """Set the thickness of marker.

        Parameters
        ----------
        x : float
            Number for marker thickness.
        """
        self._mew = x
        self._line.set_mew(x)
        self.update_figure()

    figureMarkerThickness = pyqtProperty(float, getMarkerThickness,
                                         setMarkerThickness)

    def getLineLabel(self):
        return self._line_label

    @pyqtSlot('QString')
    def setLineLabel(self, s):
        """Set label for current curve.

        Parameters
        ----------
        s : str
            Label string which will be shown as legend.
        """
        self._line_label = s
        self._line.set_label(s)
        self.update_legend()
        self.update_figure()

    figureLineLabel = pyqtProperty('QString', getLineLabel, setLineLabel)

    def getLineWidth(self):
        return self._line_width

    @pyqtSlot(float)
    def setLineWidth(self, x):
        """Set line width for the current curve.

        Parameters
        ----------
        x : float
            Line width.
        """
        self._line_width = x
        self._line.set_lw(x)
        self.update_figure()

    figureLineWidth = pyqtProperty(float, getLineWidth, setLineWidth)

    def getMarkerSize(self):
        return self._marker_size

    @pyqtSlot(float)
    def setMarkerSize(self, x):
        """Set marker size.

        Parameters
        ----------
        x : float
            Marker size.
        """
        self._marker_size = x
        self._line.set_ms(x)
        self.update_figure()

    figureMarkerSize = pyqtProperty(float, getMarkerSize, setMarkerSize)

    def getLineVisible(self):
        return self._line_visible

    @pyqtSlot(bool)
    def setLineVisible(self, f):
        """Set line visible or not.

        Parameters
        ----------
        f : bool
            Line visible (True) or not (False).
        """
        self._line_visible = f
        self._line.set_visible(f)
        self.update_figure()

    figureLineVisible = pyqtProperty(bool, getLineVisible, setLineVisible)

    def getLineID(self):
        return self._line_id

    @pyqtSlot(int)
    def setLineID(self, i):
        """Set line id, which is used to discriminate one from another, the
        first drawn line is of index 0, next one is 1, and so on.

        Parameters
        ----------
        i : int
            Line index number.

        See Also
        --------
        add_curve
        """
        lines = self.get_all_curves()
        if i < lines.__len__():
            self._line_id = i
            self._line = lines[i]

    def get_line_config(self, line=None):
        """Get line config for *ls*, *lw*, *c*, *marker*, *ms*, *mew*,
        *mec*, *mfc*, *label*, *visible*, *alpha*.
        """
        line = self._line if line is None else line
        lconf = {
            p: getattr(line, 'get_' + p)()
            for p in ('ls', 'lw', 'c', 'ms', 'mew', 'mec', 'mfc', 'marker',
                      'label', 'visible', 'alpha')
        }
        return lconf

    def get_mpl_settings(self):
        """Return all the settings for the current figure.
        """
        s = MatplotlibCurveWidgetSettings()
        s.update(s.default_settings())

        # figure
        s['figure']['title'].update({
            'value': self.getFigureTitle(),
            'font': self.getFigureTitleFont().toString()
        })
        s['figure']['labels'].update({
            'xlabel': self.getFigureXlabel(),
            'ylabel': self.getFigureYlabel(),
            'font': self.getFigureXYlabelFont().toString()
        })
        s['figure']['xy_range'].update({
            'auto_scale': self.getFigureAutoScale(),
            'xmin': self.getXLimitMin(),
            'xmax': self.getXLimitMax(),
            'ymin': self.getYLimitMin(),
            'ymax': self.getYLimitMax(),
        })
        s['figure']['legend'].update({
            'show': self.getLegendToggle() is True,
            'location': self.getLegendLocation()
        })
        # curve
        curve_settings = []
        for line_id, line in enumerate(self.get_all_curves()):
            config = self.get_line_config(line)
            curve_setting = OrderedDict()
            curve_setting.update({
                'line': {
                    'style': config['ls'],
                    'color': mplcolor2hex(config['c']),
                    'width': config['lw'],
                },
                'marker': {
                    'style': config['marker'],
                    'edgecolor': mplcolor2hex(config['mec']),
                    'facecolor': mplcolor2hex(config['mfc']),
                    'size': config['ms'],
                    'width': config['mew'],
                },
                'label': config['label'],
                'line_id': line_id,
            })
            curve_settings.append(curve_setting)
        s.update({'curve': curve_settings})
        # style
        s['style']['figsize'].update({
            'width': self.getFigureWidth(),
            'height': self.getFigureHeight(),
            'dpi': self.getFigureDpi(),
        })
        s['style']['background'].update({
            'color': self.getFigureBgColor().name(),
        })
        s['style']['ticks'].update({
            'mticks_on': self.getFigureMTicksToggle() is True,
            'font': self.getFigureXYticksFont().toString(),
            'color': self.getFigureXYticksColor().name(),
        })
        s['style']['layout'].update({
            'tight_on': self.getTightLayoutToggle() is True,
            'grid_on': self.getFigureGridToggle() is True,
            'grid_color': self.getFigureGridColor().name(),
        })
        return s

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

    @pyqtSlot(QVariant)
    def setXData(self, x):
        """Set x data for the current curve, signal type should be ``QVariant``.

        Parameters
        ----------
        x : list or array
            Array of x data.
        """
        self._x_data = x
        self._line.set_xdata(x)
        self.update_figure()

    def getXData(self):
        return self._x_data

    @pyqtSlot(QVariant)
    def setYData(self, x):
        """Set y data for the current curve, signal type should be ``QVariant``.

        Parameters
        ----------
        x : list or array
            Array of y data.
        """
        self._y_data = x
        self._line.set_ydata(x)
        self.update_figure()

    def getYData(self):
        return self._y_data

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

    def contextMenuEvent(self, e):
        menu = QMenu(self)
        config_action = QAction(QIcon(QPixmap(":/tools/config.png")),
                                "Config", menu)
        export_action = QAction(QIcon(QPixmap(":/tools/export.png")),
                                "Export", menu)
        import_action = QAction(QIcon(QPixmap(":/tools/import.png")),
                                "Import", menu)
        reset_action = QAction(QIcon(QPixmap(":/tools/reset.png")),
                               "Reset", menu)
        tb_action = QAction(QIcon(QPixmap(":/tools/tools.png")),
                            "Tools", menu)
        fitting_action = QAction(QIcon(QPixmap(":/tools/fitting.png")),
                                 "Fitting", menu)
        menu.addAction(config_action)
        menu.addAction(export_action)
        menu.addAction(import_action)
        menu.addAction(reset_action)
        menu.addSeparator()
        menu.addAction(tb_action)
        menu.addAction(fitting_action)

        menu.setStyleSheet('QMenu {margin: 2px;}')

        config_action.triggered.connect(self.on_config)
        export_action.triggered.connect(self.on_export_config)
        import_action.triggered.connect(self.on_import_config)
        reset_action.triggered.connect(self.on_reset_config)
        tb_action.triggered.connect(self.show_mpl_tools)
        fitting_action.triggered.connect(self.on_fitting_data)

        menu.exec_(self.mapToGlobal(e.pos()))

    def on_fitting_data(self):
        """Fitting data.
        """
        wt = self.widget_type
        if wt == 'curve':
            print("Fitting Curve")
        elif wt == 'image':
            if 'FittingImage' not in dir():
                from mpl4qt.widgets.fitting import FittingImage
            w = self._handlers.setdefault(
                    'fitting_image_widget', FittingImage(self))
            print("Fitting: ", id(w))
            w.show()
            w.init_data()
        else:
            print("To be implemented")

    def show_mpl_tools(self, e):
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

    def on_config(self):
        config_panel = MatplotlibConfigPanel(self)
        config_panel.exec_()

    def on_export_config(self):
        filepath, _ = QFileDialog.getSaveFileName(self,
                                                  "Save Settings",
                                                  "./mpl_settings.json",
                                                  "JSON Files (*.json)")
        if not filepath:
            return
        try:
            s = self.get_mpl_settings()
            s.write(filepath)
        except:
            QMessageBox.warning(self, "Warning",
                                "Cannot export settings to {}".format(filepath),
                                QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Information",
                                    "Successfully export settings to {}".format(filepath),
                                    QMessageBox.Ok)

    def on_import_config(self):
        filepath, _ = QFileDialog.getOpenFileName(self,
                                                  "Open Settings",
                                                  "./mpl_settings.json",
                                                  "JSON Files (*.json)")
        if not filepath:
            return
        self._import_mpl_settings(filepath)

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

    def on_reset_config(self):
        # apply default settings
        if self.widget_type == 'curve':
            self.apply_mpl_settings()
        else:
            QMessageBox.warning(self, "Reset Drawing settings",
                    "Only curve widget is fully implemented.",
                    QMessageBox.Ok)

    def apply_mpl_settings(self, settings=None):
        """Apply mpl settings to the mplcurvewidget, if *settings* is not
        defined, apply the default mpl settings.

        See Also
        --------
        MatplotlibCurveWidgetSettings
        """
        settings = DEFAULT_MPL_SETTINGS if settings is None else settings

        # curve
        scurve = settings['curve']
        for config in scurve:
            self.setLineID(config['line_id'])
            self.setLineLabel(config['label'])
            self.setLineColor(QColor(config['line']['color']))
            self.setLineStyle(config['line']['style'])
            self.setLineWidth(config['line']['width'])
            self.setMarkerStyle(config['marker']['style'])
            self.setMarkerSize(config['marker']['size'])
            self.setMarkerThickness(config['marker']['width'])
            self.setMkEdgeColor(QColor(config['marker']['edgecolor']))
            self.setMkFaceColor(QColor(config['marker']['facecolor']))

        # style
        sstyle = settings['style']
        self.setFigureBgColor(QColor(sstyle['background']['color']))
        self.setFigureWidth(sstyle['figsize']['width'])
        self.setFigureHeight(sstyle['figsize']['height'])
        self.setFigureDpi(sstyle['figsize']['dpi'])
        self.setFigureGridToggle(bool(sstyle['layout']['grid_on']))
        self.setTightLayoutToggle(bool(sstyle['layout']['tight_on']))
        self.setFigureGridColor(QColor(sstyle['layout']['grid_color']))
        self.setFigureXYticksColor(QColor(sstyle['ticks']['color']))
        self.setFigureMTicksToggle(bool(sstyle['ticks']['mticks_on']))
        f = QFont()
        f.fromString(sstyle['ticks']['font'])
        self.setFigureXYticksFont(f)

        # figure
        sfig = settings['figure']
        self.setFigureTitle(sfig['title']['value'])
        f = QFont()
        f.fromString(sfig['title']['font'])
        self.setFigureTitleFont(f)
        self.setFigureXlabel(sfig['labels']['xlabel'])
        self.setFigureYlabel(sfig['labels']['ylabel'])
        f = QFont()
        f.fromString(sfig['labels']['font'])
        self.setFigureXYlabelFont(f)
        self.setLegendToggle(bool(sfig['legend']['show']))
        self.setLegendLocation(sfig['legend']['location'])
        self.setFigureAutoScale(bool(sfig['xy_range']['auto_scale']))
        self.setXLimitMin(sfig['xy_range']['xmin'])
        self.setXLimitMax(sfig['xy_range']['xmax'])
        self.setYLimitMin(sfig['xy_range']['ymin'])
        self.setYLimitMax(sfig['xy_range']['ymax'])

    def force_update(self):
        """Force update widget."""
        self.update_legend()
        self.update_figure()

    def update_legend(self):
        # update legend if on
        self.setLegendToggle(self._legend_toggle)

    def on_motion(self, event):
        if event.inaxes is None:
            return
        x_pos, y_pos = event.xdata, event.ydata
        self.xyposUpdated.emit([x_pos, y_pos])

    def on_press(self, e):
        if e.inaxes is None:
            return
        if e.button == 1 and self._ruler_on:
            self.set_visible_hvlines(True)
            self.draw_hvlines(e.xdata, e.ydata)
        elif e.button == 2:
            self._pan_x0 = e.xdata
            self._pan_y0 = e.ydata
            self._pan_xlim0 = self.axes.get_xlim()
            self._pan_ylim0 = self.axes.get_ylim()
            self._pan_on = True
            self.setCursor(Qt.ClosedHandCursor)

    def on_release(self, e):
        if e.inaxes is None:
            return
        if e.button == 2 and self._pan_on:
            self._pan_on = False
            dx = self._pan_x0 - e.xdata
            dy = self._pan_y0 - e.ydata
            xlim = [i + dx for i in self._pan_xlim0]
            ylim = [i + dy for i in self._pan_ylim0]
            self.axes.set_xlim(xlim)
            self.axes.set_ylim(ylim)
            self.update_figure()
            self.unsetCursor()

    def draw_hvlines(self, x0, y0):
        if self._hline is None:
            self._hline = self.axes.axhline(y0,
                                            alpha=0.8, color='b', ls='--')
            self._hline.set_label('H-Ruler')
            self._lines.append(self._hline)
        else:
            self._hline.set_ydata([y0, y0])

        if self._vline is None:
            self._vline = self.axes.axvline(x0,
                                            alpha=0.8, color='b', ls='--')
            self._vline.set_label('V-Ruler')
            self._lines.append(self._vline)
        else:
            self._vline.set_xdata([x0, x0])

        if self._cpoint is None:
            self._cpoint, = self.axes.plot([x0], [y0], 'o',
                                           mec='b', mfc='b')
            self._cpoint.set_label('Cross-Point')
            self._lines.append(self._cpoint)
            text = '{0:g}, {1:g}'.format(x0, y0)
            self._cpoint_text = self.axes.annotate(
                text, xy=(x0, y0), xytext=(15, 15),
                xycoords="data", textcoords="offset pixels",
                bbox=dict(boxstyle="round", fc='w'))
            self._cpoint_text.get_bbox_patch().set_alpha(0.5)
        else:
            self._cpoint.set_data([x0], [y0])
            self._cpoint_text.xy = (x0, y0)
            text = '{0:g}, {1:g}'.format(x0, y0)
            self._cpoint_text.set_text(text)

        self.update_figure()

    def set_visible_hvlines(self, flag=True):
        """Set hvlines visible (*flag* is True) or invisible (*flag* is False).
        """
        for o in (self._hline, self._vline, self._cpoint, self._cpoint_text):
            if o is not None:
                o.set_visible(flag)
        self.update_figure()

    def process_keyshort_combo(self, k1, k2):
        BasePlotWidget.process_keyshort_combo(self, k1, k2)
        if k1 == 'a' and k2 == 'x':
            # auto xscale
            self.set_autoscale('x')
        elif k1 == 'a' and k2 == 'y':
            # auto yscale
            self.set_autoscale('y')
        elif k1 == 'shift' and k2 == '?':
            # help msgbox
            self.kbd_help()

    def process_keyshort(self, k):
        BasePlotWidget.process_keyshort(self, k)
        if k == 'g':
            # turn on/off grid
            self.setFigureGridToggle(not self.getFigureGridToggle())
        elif k == 'a' and self.widget_type != 'image':
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

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        path = e.mimeData().urls()[0].toLocalFile()
        self._import_mpl_settings(path)

    def kbd_help(self, ):
        """Help message box for keyboard shortcuts.
        """
        w = KbdHelpDialog(self)
        w.setWindowTitle("Keyboard Shortcuts Help")
        w.exec_()

    def rotate_ticks(self, angle, axis):
        """Rotate *axis* ticks by *angle* in degree.
        """
        lbls = getattr(self.axes, "get_{}ticklabels".format(axis))()
        for o in lbls:
            o.set_rotation(angle)

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

    def set_autoscale(self, axis='both'):
        self.axes.relim()
        self.axes.autoscale(axis=axis)
        self.update_figure()

    def update_figure(self):
        if self.getFigureAutoScale():
            self.axes.relim()
            self.axes.autoscale()
        BasePlotWidget.update_figure(self)

    def get_points(self):
        """Return array contains (x, y) coords on curve.
        """
        x = self._x_data
        y = self._y_data
        return np.vstack([x, y]).T

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


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MatplotlibCurveWidget()
    window.show()
    sys.exit(app.exec_())
