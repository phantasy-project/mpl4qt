#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
mplerrorbarwidget.py

A PyQt custom widget for Qt Designer: draw curves w/ errorbar with matplotlib

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

import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtGui import QColor

from mpl4qt.widgets.mplcurvewidget import MatplotlibCurveWidget
from mpl4qt.widgets.mplconfig import MatplotlibConfigErrorbarPanel


class MatplotlibErrorbarWidget(MatplotlibCurveWidget):
    """MatplotlibErrorbarWidget(MatplotlibCurveWidget)
    """
    def __init__(self, parent=None):
        # initial eb config
        self._init_config()

        # regular lines (avg lines)
        self._lines = []
        # eb lines + mks, each item: {'xerr':(mk, line), 'yerr': (mk, line)}
        self._eb_lines = []

        super(MatplotlibErrorbarWidget, self).__init__(parent)

    def _init_config(self):
        self.eb_fmt = ''
        self.eb_markercolor = '#1E90FF'
        self.eb_markersize = 5
        self.eb_mew = 2
        self.eb_lw = 1

        self.avg_ls = '--'
        self.avg_lw = 1
        self.avg_linecolor = 'g'
        self.avg_mfc = 'r'
        self.avg_mec = 'r'
        self.avg_ms = 5
        self.avg_marker = 's'

    def init_figure(self):
        x = np.linspace(-4, 4, 100)
        y = np.sin(10 * x) / x
        xerr = np.std((np.random.random(100) - 0.5)/500 + 1)
        yerr = np.std((np.random.random(100) - 0.5)/5 + 1)

        self._x_data = x
        self._y_data = y
        self._xerr = xerr
        self._yerr = yerr
        self._avgline, self._ebmks, self._eblines = self.axes.errorbar(
                x, y, xerr=xerr, yerr=yerr,
                fmt=self.eb_fmt,
                color=self.avg_linecolor,
                linewidth=self.avg_lw,
                ls=self.avg_ls,
                marker=self.avg_marker,
                ms=self.avg_ms,
                mfc=self.avg_mfc,
                mec=self.avg_mec,
                elinewidth=self.eb_lw,
                ecolor=self.eb_markercolor,
                capsize=self.eb_markersize,
                capthick=self.eb_mew)

        # update lines
        # average line
        self._lines.append(self._avgline)
        # xerr line and yerr line
        self._eb_lines.append({
            'xerr': (self._ebmks[0:2], self._eblines[0]),
            'yerr': (self._ebmks[2:4], self._eblines[1])
        })

#    def add_curve(self):
#        # append avg line and err lines (dict)
#        pass

    def on_config(self):
        config_panel = MatplotlibConfigErrorbarPanel(self)
        r = config_panel.exec_()

    def get_all_curves(self):
        return self._lines

    def get_all_eb_curves(self):
        """Each eb line is composed of:
        xerr_mk_left, xerr_mk_right, xerr_bar (line) or
        yerr_mk_top, yerr_mk_bottom, yerr_bar (line)
        """
        return self._eb_lines

    def getEbLineID(self):
        return self._eb_line_id

    @pyqtSlot(int)
    def setEbLineID(self, i):
        """Set errorbar line id.

        See Also
        --------
        getLineID, setLineID
        """
        lines = self.get_all_eb_curves()
        if i < lines.__len__():
            self._eb_line_id = i
            self._eb_line = lines[i]
            self._xeb_line = self._eb_line.setdefault('xerr', None)
            self._yeb_line = self._eb_line.setdefault('yerr', None)
            # x[y]eb_line: [(mk_t, mk_b), line]

    def get_eb_line_config(self, line=None):
        """Get eb line config for errbars (mk&line) and avg line (mk&line)
        """
        line = self._eb_line if line is None else line
        xerr_line_tuple = line.get('xerr')
        yerr_line_tuple = line.get('yerr')

        if xerr_line_tuple is not None:
            xeb_mk_config = self._get_errbar_mk_config(xerr_line_tuple)
            xeb_line_config = self._get_errbar_line_config(xerr_line_tuple)
        if yerr_line_tuple is not None:
            yeb_mk_config = self._get_errbar_mk_config(yerr_line_tuple)
            yeb_line_config = self._get_errbar_line_config(yerr_line_tuple)

        return {'xerr': (xeb_mk_config, xeb_line_config),
                'yerr': (yeb_mk_config, yeb_line_config)}

    def _get_errbar_mk_config(self, err_line_tuple):
        """Get *err_line_tuple* artist configuration, return errbar mk config.
        """
        err_mks, _ = err_line_tuple
        mk_config = [
            {p: getattr(mk, 'get_' + p)()
                for p in ('c', 'mec', 'mfc', 'ms', 'mew', 'marker',
                          'visible')}
            for mk in err_mks
        ]
        return mk_config

    def _get_errbar_line_config(self, err_line_tuple):
        """Get *err_line_tuple* artist configuration, return errbar line config.
        """
        _, err_line = err_line_tuple
        line_config = {}
        line_config['color'] = err_line.get_color()[0].tolist()
        line_config['lw'] = err_line.get_linewidth()[0]
        line_config['visible'] = err_line.get_visible()
        #
        line_config['ls'] = err_line.get_linestyle()
        # always set eb linestyle as dashed.
        self.setEbLineStyle('solid')
        return line_config

    def getEbLineColor(self):
        return self._eb_line_color

    @pyqtSlot(QColor)
    def setEbLineColor(self, c):
        """Set eb line color for the current curve.

        Parameters
        ----------
        c : QColor
            Color to set.
        """
        self._eb_line_color = c
        # last element if errline
        [l[-1].set_color(c.getRgbF()) for l in (self._xeb_line, self._yeb_line,) if l is not None]
        self.update_figure()

    figureEbLineColor = pyqtProperty(QColor, getEbLineColor, setEbLineColor)

    def getEbLineWidth(self):
        return self._eb_line_width

    @pyqtSlot(float)
    def setEbLineWidth(self, x):
        """Set err line width for the current curve.

        Parameters
        ----------
        x : float
            Line width.
        """
        self._eb_line_width = x
        # last element if errline
        [l[-1].set_linewidth(x) for l in (self._xeb_line, self._yeb_line,) if l is not None]
        self.update_figure()

    figureEbLineWidth = pyqtProperty(float, getEbLineWidth, setEbLineWidth)

    def getEbLineStyle(self):
        return self._eb_line_style

    @pyqtSlot('QString')
    def setEbLineStyle(self, s):
        """Set eb line style for the current curve.

        Parameters
        ----------
        s : str
            String for the line style, see `line style <https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D>`_.
        """
        self._eb_line_style = s
        # last element if errline
        [l[-1].set_linestyle(s) for l in (self._xeb_line, self._yeb_line,) if l is not None]
        self.update_figure()

    figureEbLineStyle = pyqtProperty('QString', getEbLineStyle, setEbLineStyle)

    def getXEbMarkerStyle(self):
        return self._xeb_marker_style

    @pyqtSlot('QString')
    def setXEbMarkerStyle(self, s):
        """Set xerr marker style.

        Parameters
        ----------
        s : str
            String for the marker style, see `marker style <https://matplotlib.org/api/markers_api.html>`_.
        """
        self._xeb_marker_style = s
        if self._xeb_line is not None:
            [l.set_marker(s) for l in self._xeb_line[0]]
        self.update_figure()

    figureXEbMarkerStyle = pyqtProperty('QString', getXEbMarkerStyle, setXEbMarkerStyle)

    def getYEbMarkerStyle(self):
        return self._yeb_marker_style

    @pyqtSlot('QString')
    def setYEbMarkerStyle(self, s):
        """Set yerr marker style.

        Parameters
        ----------
        s : str
            String for the marker style, see `marker style <https://matplotlib.org/api/markers_api.html>`_.
        """
        self._yeb_marker_style = s
        if self._yeb_line is not None:
            [l.set_marker(s) for l in self._yeb_line[0]]
        self.update_figure()

    figureYEbMarkerStyle = pyqtProperty('QString', getYEbMarkerStyle, setYEbMarkerStyle)

    def getEbMkEdgeColor(self):
        return self._eb_mec

    @pyqtSlot(QColor)
    def setEbMkEdgeColor(self, c):
        """Set err marker edgecolor.

        Parameters
        ----------
        c : QColor
            Color to set.
        """
        self._eb_mec = c
        for eb_line in (self._xeb_line, self._yeb_line):
            if eb_line is not None:
                [l.set_mec(c.getRgbF()) for l in eb_line[0]]
        self.update_figure()

    figureEbMakerEdgeColor = pyqtProperty(QColor, getEbMkEdgeColor, setEbMkEdgeColor)

    def getEbMkFaceColor(self):
        return self._eb_mfc

    @pyqtSlot(QColor)
    def setEbMkFaceColor(self, c):
        """Set err marker facecolor.

        Parameters
        ----------
        c : QColor
            Color to set.
        """
        self._eb_mfc = c
        for eb_line in (self._xeb_line, self._yeb_line):
            if eb_line is not None:
                [l.set_mfc(c.getRgbF()) for l in eb_line[0]]
        self.update_figure()

    figureEbMakerFaceColor = pyqtProperty(QColor, getEbMkFaceColor, setEbMkFaceColor)

    def getEbMarkerSize(self):
        return self._eb_marker_size

    @pyqtSlot(float)
    def setEbMarkerSize(self, x):
        """Set err marker size.

        Parameters
        ----------
        x : float
            Marker size.
        """
        self._eb_marker_size = x
        for eb_line in (self._xeb_line, self._yeb_line):
            if eb_line is not None:
                [l.set_ms(x) for l in eb_line[0]]
        self.update_figure()

    figureEbMarkerSize = pyqtProperty(float, getEbMarkerSize, setEbMarkerSize)

    def getEbMarkerThickness(self):
        return self._eb_mew

    @pyqtSlot(float)
    def setEbMarkerThickness(self, x):
        """Set the thickness of err marker.

        Parameters
        ----------
        x : float
            Number for marker thickness.
        """
        self._mew = x
        for eb_line in (self._xeb_line, self._yeb_line):
            if eb_line is not None:
                [l.set_mew(x) for l in eb_line[0]]
        self.update_figure()

    figureEbMarkerThickness = pyqtProperty(float, getEbMarkerThickness,
                                           setEbMarkerThickness)

    def getEbLineVisible(self):
        return self._eb_line_visible

    @pyqtSlot(bool)
    def setEbLineVisible(self, f):
        """Set err line visible or not.

        Parameters
        ----------
        f : bool
            Line visible (True) or not (False).
        """
        self._eb_line_visible = f
        # err mks
        for l in (self._xeb_line, self._yeb_line):
            if l is not None:
                # err line
                l[-1].set_visible(f)
                [m.set_visible(f) for m in l[0]]
        self.update_figure()

    figureEbLineVisible = pyqtProperty(bool, getEbLineVisible, setEbLineVisible)


if __name__ == "__main__":

    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MatplotlibErrorbarWidget()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
