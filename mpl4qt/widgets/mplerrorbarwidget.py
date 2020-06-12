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
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor

from mpl4qt.widgets.mplconfig import MatplotlibConfigErrorbarPanel
from mpl4qt.widgets.mplcurvewidget import MatplotlibCurveWidget
from mpl4qt.widgets.utils import mplcolor2hex


class MatplotlibErrorbarWidget(MatplotlibCurveWidget):
    """MatplotlibErrorbarWidget(MatplotlibCurveWidget)
    """
    def __init__(self, parent=None):
        # initial eb config
        self._init_config()
        # regular lines (avg lines)
        self._lines = []
        # eb lines + mks, each item:
        # {'xerr':([mk: left, right], line), 'yerr': ([mk: top, bottom], line)}
        self._eb_lines = []

        super(MatplotlibErrorbarWidget, self).__init__(parent)

        # widget type
        self.widget_type = 'errorbar'

        # post_init line attrs
        self._post_init()

    def _post_init(self):
        # sync the settings of colors for avg line, when these objects are
        # created, the parent class does not know, should manually update
        # them. 2019-06-27 16:09:23 PM EDT
        o = self._avgline
        c = mplcolor2hex(o.get_c())
        self._line_color = QColor(c)
        self._mec = QColor(mplcolor2hex(o.get_mec()))
        self._mfc = QColor(mplcolor2hex(o.get_mfc()))

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

        # initial config
        self._eb_line_color = QColor(self.eb_markercolor)
        self._eb_line_width = self.avg_lw
        self._eb_line_style = self.avg_ls
        self._xeb_marker_style = '|'
        self._yeb_marker_style = '-'
        self._eb_mfc = QColor(self.avg_mfc)
        self._eb_mec = QColor(self.avg_mec)
        self._eb_marker_size = self.avg_ms
        self._eb_mew = self.eb_mew
        self._eb_line_visible = True

    def init_figure(self):
        x = np.linspace(-4, 4, 100)
        y = np.sin(10 * x) / x
        xerr = np.std((np.random.random(100) - 0.5)/500 + 1)
        yerr = np.std((np.random.random(100) - 0.5)/1 + 1)

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
        self._avgline.set_picker(True)
        self._avgline.set_pickradius(2)
        # update lines
        # average line
        self._lines.append(self._avgline)
        # xerr line and yerr line
        self._eb_lines.append({
            'xerr': (self._ebmks[0:2], self._eblines[0]),
            'yerr': (self._ebmks[2:4], self._eblines[1])
        })

        # set current avg line and eb line
        self.setLineID(0)
        self.setEbLineID(0)

    def add_curve(self, x_data=None, y_data=None, xerr_data=None, yerr_data=None, **kws):
        """Add one curve with errorbar to figure, accepts all ``pyplot.errorbar``
        keyword arguments.

        Parameters
        ----------
        x_data : list or array
            Array of x data, which is the average in x.
        y_data : list or array
            Array of y data, which is the average in y.
        xerr_data : list or array
            Error array in x.
        yerr_data : list or array
            Error array in y.

        Returns
        -------
        o : Line2D
            The added average line object.
        """
        # Add new line(avg) + errorbar
        # append avg line and err lines (dict)
        x = np.nan if x_data is None else x_data
        y = np.nan if y_data is None else y_data
        xerr = np.nan if xerr_data is None else xerr_data
        yerr = np.nan if yerr_data is None else yerr_data
        avgline, ebmks, eblines = self.axes.errorbar(
                x, y, xerr=xerr, yerr=yerr,
                fmt=self.eb_fmt,
                linewidth=self.avg_lw,
                ls=self.avg_ls,
                marker=self.avg_marker,
                ms=self.avg_ms,
                elinewidth=self.eb_lw,
                capsize=self.eb_markersize,
                capthick=self.eb_mew)
        avgline.set_picker(True)
        avgline.set_pickradius(2)
        self._lines.append(avgline)
        self._eb_lines.append({
            'xerr': (ebmks[0:2], eblines[0]),
            'yerr': (ebmks[2:4], eblines[1])
        })
        self.update_legend()
        self.update_figure()
        return avgline

    def on_config(self):
        config_panel = MatplotlibConfigErrorbarPanel(self)
        config_panel.exec_()

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

    def update_curve(self, x_data=None, y_data=None, xerr_data=None, yerr_data=None):
        """Update curve with errorbar, with given data.

        Parameters
        ----------
        x_data : list or array
            Array of x data, which is the average in x.
        y_data : list or array
            Array of y data, which is the average in y.
        xerr_data : list or array
            Error array in x.
        yerr_data : list or array
            Error array in y.
        """
        if isinstance(x_data, list):
            x_data = np.asarray(x_data)
        if isinstance(y_data, list):
            y_data = np.asarray(y_data)
        if isinstance(xerr_data, list):
            xerr_data = np.asarray(xerr_data)
        if isinstance(yerr_data, list):
            yerr_data = np.asarray(yerr_data)

        self._x_data = x_data
        self._y_data = y_data
        adjust_errorbar(self._line, self._eb_line, x_data, y_data, xerr_data, yerr_data)
        self.update_figure()
        self.dataChanged.emit((self._line, x_data, y_data))

    def clear_data(self):
        """Set with empty canvas, clear curve w/ eb.
        """
        empty_arr = np.asarray([])
        self.update_curve(empty_arr, empty_arr, empty_arr, empty_arr)


def adjust_errorbar(line_obj, ebline_obj, x, y, xerr, yerr):
    """Update curve with errorbars.

    Parameters
    ----------
    line_obj : Line2D object
        Present average line.
    ebline_obj : dict
        Keys: 'xerr' and 'yerr', values: (mk-top, mk-bottom), bar
    x : array
        New x data for `line_obj`.
    y : array:
        New y data for `line_obj`.
    xerr : array
        New error for x data.
    yerr : array
        New error for y data.
    """
    l = line_obj
    (xerr_right, xerr_left), xbar = ebline_obj['xerr']
    (yerr_top, yerr_bottom), ybar = ebline_obj['yerr']

    l.set_data(x, y)

    x_base, y_base = x, y
    xerr_left_val, xerr_right_val = x_base - xerr, x_base + xerr
    yerr_bottom_val, yerr_top_val = y_base - yerr, y_base + yerr

    xerr_left.set_data(xerr_left_val, y_base)
    xerr_right.set_data(xerr_right_val, y_base)

    yerr_bottom.set_data(x_base, yerr_bottom_val)
    yerr_top.set_data(x_base, yerr_top_val)

    new_segments_x = [
        np.array([[xt, y], [xb, y]])
        for xt, xb, y in zip(xerr_right_val, xerr_left_val, y_base)
    ]
    new_segments_y = [
        np.array([[x, yt], [x, yb]])
        for x, yt, yb in zip(x_base, yerr_top_val, yerr_bottom_val)
    ]
    xbar.set_segments(new_segments_x)
    ybar.set_segments(new_segments_y)


if __name__ == "__main__":

    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MatplotlibErrorbarWidget()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
