#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
mplbarwidget.py

A PyQt custom widget for Qt Designer: draw bars with matplotlib

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

from mpl4qt.widgets.mplconfig import MatplotlibConfigBarPanel
from mpl4qt.widgets.mplcurvewidget import MatplotlibCurveWidget

from matplotlib.text import Text


class MatplotlibBarWidget(MatplotlibCurveWidget):
    """MatplotlibBarWidget(MatplotlibCurveWidget)
    """

    def __init__(self, parent=None):
        self._init_config()

        self._lines = []
        super(MatplotlibBarWidget, self).__init__(parent)

        # widget type
        self.widget_type = 'bar'

    def _init_config(self):
        self._eb_line_width = 1
        self._eb_line_style = '-'
        self._eb_line_color = QColor('black')
        self._eb_line_alpha = 1.0
        self._eb_line_visible = True
        self._bar_width = 0.2
        self._bar_color = QColor('blue')
        self._bar_alpha = 0.5
        self._label = "_barchart"
        # annotations
        self._all_annotes = None
        self._default_annote_fmt = "${0:.3g}\pm{1:.3g}$"
        self._annote_config_dict = {
            "fmt": self._default_annote_fmt,
            "size": 10, # fontsize
            "rotation": 0.0, # rotation
            "bbox_dict": {
                "boxstyle": "round,pad=0.2",
                "fc": "w", "ec": "0.5", "lw": 1, "alpha": 1.0},
        }
        self._pk_text = None

    def update_annote_config_dict(self, **kws):
        self._annote_config_dict.update(**kws)

    def init_figure(self, x=None, y=None, yerr=None):
        if x is None:
            x = np.linspace(1, 10, 5)
            y = np.sin(10 * x)
            yerr = np.random.random(5)

        self._x_data = x
        self._y_data = y
        self._yerr_data = yerr
        self._bars = self.axes.bar(x, y, self._bar_width,
                                   color=self._bar_color.getRgbF(),
                                   alpha=self._bar_alpha,
                                   label=self._label,
                                   yerr=yerr, error_kw={
                'ecolor': self._eb_line_color.getRgbF(),
                'alpha': self._eb_line_alpha,
                'lw': self._eb_line_width, })

        self._eb_lines = self._bars.errorbar.lines[-1][0]
        self._rects = self._bars.patches

    def on_config(self):
        config_panel = MatplotlibConfigBarPanel(self)
        config_panel.exec_()

    def get_barchart_config(self):
        # eb color, ls, lw, alpha
        eb_color = self._eb_lines.get_color()[0].tolist()  # (r,g,b,a)
        eb_alpha = self._eb_lines.get_alpha()  # float
        eb_lw = self._eb_lines.get_linewidth()[0]  # float
        # bar color, alpha
        rect = self._rects[0]
        bar_color = rect.get_facecolor()  # (r,g,b,a)
        bar_alpha = rect.get_alpha()  # float
        bar_width = rect.get_width()  # float
        # label
        label = self._bars.get_label()
        # annote
        annote_config = self._annote_config_dict

        return {'label': label, 'eb_color': eb_color,
                'eb_alpha': eb_alpha, 'eb_lw': eb_lw,
                'eb_ls': self._eb_line_style,
                'bar_color': bar_color, 'bar_alpha': bar_alpha,
                'bar_width': bar_width,
                'annote_config': annote_config}

    def getLabel(self):
        return self._label

    @pyqtSlot('QString')
    def setLabel(self, s):
        """Set label for current plot.

        Parameters
        ----------
        s : str
            Label string which will be shown as legend.
        """
        self._label = s
        self._bars.set_label(s)
        self.update_legend()
        self.update_figure()

    figureLabel = pyqtProperty('QString', getLabel, setLabel)

    def getEbLineStyle(self):
        return self._eb_line_style

    @pyqtSlot('QString')
    def setEbLineStyle(self, s):
        """Set ebline style for the current curve.

        Parameters
        ----------
        s : str
            String for the line style, see `line style <https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D>`_.
        """
        self._eb_line_style = s
        self._eb_lines.set_linestyle(s)
        self.update_figure()

    figureEbLineStyle = pyqtProperty('QString', getEbLineStyle, setEbLineStyle)

    def getEbLineAlpha(self):
        return self._eb_line_alpha

    def setEbLineAlpha(self, x):
        """Set ebline opacity, range from 0 to 1.0.

        Parameters
        ----------
        x : float
            Alpha value, 0 to 1.0 (defalut).
        """
        self._eb_line_alpha = x
        self._eb_lines.set_alpha(x)
        self.update_figure()

    figureEbLineAlpha = pyqtProperty(float, getEbLineAlpha, setEbLineAlpha)

    def getBarWidth(self):
        return self._bar_width

    @pyqtSlot(float)
    def setBarWidth(self, x):
        self._set_bar_width(x)
        self._bar_width = x
        self.update_figure()

    figureBarWidth = pyqtProperty(float, getBarWidth, setBarWidth)

    def getBarAlpha(self):
        return self._bar_alpha

    def setBarAlpha(self, x):
        """Set bar opacity, range from 0 to 1.0.

        Parameters
        ----------
        x : float
            Alpha value, 0 to 1.0 (defalut).
        """
        self._bar_alpha = x
        [o.set_alpha(x) for o in self._rects]
        self.update_figure()

    figureBarAlpha = pyqtProperty(float, getBarAlpha, setBarAlpha)

    def getBarColor(self):
        return self._bar_color

    @pyqtSlot(QColor)
    def setBarColor(self, c):
        """Set bar color.

        Parameters
        ----------
        c : QColor
            Color to set.
        """
        self._bar_color = c
        [o.set_color(c.getRgbF()) for o in self._rects]
        self.update_figure()

    figureBarColor = pyqtProperty(QColor, getBarColor, setBarColor)

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
        self._eb_lines.set_color(c.getRgbF())
        self.update_figure()

    figureEbLineColor = pyqtProperty(QColor, getEbLineColor, setEbLineColor)

    def getEbLineWidth(self):
        return self._eb_line_width

    @pyqtSlot(float)
    def setEbLineWidth(self, x):
        self._eb_line_width = x
        self._eb_lines.set_linewidth(x)
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
        self._eb_lines.set_linestyle(s)
        self.update_figure()

    figureEbLineStyle = pyqtProperty('QString', getEbLineStyle, setEbLineStyle)

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
        self._eb_lines.set_visible(f)
        self.update_figure()

    figureEbLineVisible = pyqtProperty(bool, getEbLineVisible, setEbLineVisible)

    def _set_bar_width(self, w):
        # set bar with width *w*.
        w0 = self.getBarWidth()
        for rect in self._rects:
            x0, y0 = rect.get_xy()
            rect.set_xy((x0 - (w - w0) / 2.0, y0))
            rect.set_width(w)

    def update_curve(self, x_data=None, y_data=None, yerr_data=None):
        """Update bar, with given data.

        Parameters
        ----------
        x_data : list or array
            Array of x data, which is the average in x.
        y_data : list or array
            Array of y data, which is the average in y.
        yerr_data : list or array
            Error array in y.
        """
        if isinstance(x_data, list):
            x_data = np.asarray(x_data)
        if isinstance(y_data, list):
            y_data = np.asarray(y_data)
        if isinstance(yerr_data, list):
            yerr_data = np.asarray(yerr_data)

        self._x_data = x_data
        self._y_data = y_data
        self._yerr_data = yerr_data
        adjust_bar(self._rects, self._eb_lines, x_data, y_data, yerr_data,
                   self._bar_width)
        self.update_figure()

    def reset_data(self, x, y, yerr):
        """Reset data with *x*, *y* and *yerr*, only requires for barchar.
        """
        self.clear_figure()
        self.init_figure(x, y, yerr)

    @pyqtSlot()
    def on_annote_config_changed(self):
        """Annotations style config is changed.
        """
        self.clear_annote()
        self.annotate_bar(**self._annote_config_dict)
        self.update_figure()

    def annotate_bar(self, **kws):
        """Annotate with height value on top/bottom of bar.

        Keyword Arguments
        -----------------
        fmt : str
            Data (average and error) format, default is "${0:.3g}\pm{1:.3g}$".

        See Also
        --------
        clear_annote : Clear all annotations.
        """
        all_annotes = []
        ax = self.axes
        fmt = kws.pop('fmt')
        bbox_dict = kws.pop('bbox_dict')
        hw = self._bar_width / 2.0
        eta = 0.0
        for ix, iy, iyerr in zip(self._x_data, self._y_data, self._yerr_data):
            if iy >= 0:
                tp_y = iy + iyerr * eta
            else:
                tp_y = iy - iyerr * eta
            tp = (ix - hw, tp_y)
            anote = ax.annotate(s=fmt.format(iy, iyerr), xy=(ix, iy),
                                xytext=tp, bbox=dict(**bbox_dict),
                                **kws)
            anote.set_picker(True)
            all_annotes.append(anote)
        self._all_annotes = all_annotes

    def clear_annote(self):
        if self._all_annotes is not None:
            [o.remove() for o in self._all_annotes if o in self.axes.texts]

    def on_pick(self, evt):
        if isinstance(evt.artist, Text):
            obj = evt.artist
            pos = evt.mouseevent.xdata, evt.mouseevent.ydata
            self._pk_text = (obj, pos)

    def on_release(self, evt):
        if not evt.inaxes or self._pk_text is None:
            return
        n_x, n_y = evt.xdata, evt.ydata
        obj, pos = self._pk_text
        o_x, o_y = obj.get_position()
        x = o_x + n_x - pos[0]
        y = o_y + n_y - pos[1]
        obj.set_position((x, y))
        self.update_figure()
        self._pk_text = None


def adjust_bar(patches, eblines, x, y, yerr, bar_width):
    segs = eblines.get_segments()
    for i, (patch, seg) in enumerate(zip(patches, segs)):
        patch.set_height(y[i])
        patch.set_xy((x[i] - bar_width / 2.0, 0))
        seg[:, 0] = (x[i], x[i])
        seg[:, 1] = (y[i] - yerr[i], y[i] + yerr[i])
    eblines.set_segments(segs)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MatplotlibBarWidget()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
