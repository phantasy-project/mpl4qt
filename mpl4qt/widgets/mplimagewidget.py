#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
mplimagewidget.py

A PyQt custom widget for Qt Designer: draw image with matplotlib

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

from mpl4qt.widgets.mplconfig import MatplotlibConfigImagePanel
from mpl4qt.widgets.mplcurvewidget import MatplotlibCurveWidget
from mpl4qt.widgets.utils import get_cursor_data
from mpl4qt.widgets.utils import get_array_range
from mpl4qt.widgets.utils import is_cmap_valid
from mpl4qt.widgets.utils import func_peaks


class MatplotlibImageWidget(MatplotlibCurveWidget):
    """MatplotlibImageWidget(MatplotlibCurveWidget)

    Provides a custom widget to draw image with matplotlib, with properties
    and slots that can be used to customize its appearance.
    """

    def __init__(self, parent=None):
        # colormap
        self._cmap = "viridis"
        # colorbar
        self._cb_toggle = False
        self.cb = None
        self._cb_orientation = 'vertical'
        self._auto_clim = False

        # placeholders of xylim (not applicable)
        #self._xlim_min = 0
        #self._xlim_max = 1
        #self._ylim_min = 0
        #self._ylim_max = 1

        super(MatplotlibImageWidget, self).__init__(parent)

        # widget type
        self.widget_type = 'image'

        # reverse colormap flag
        self._rcmap_toggle = False
        self.setReverseCMapToggle(self._rcmap_toggle)

        # auto xyscale
        self.set_autoscale()

    def getColorMap(self):
        return self._cmap

    @pyqtSlot('QString')
    def setColorMap(self, c):
        if not is_cmap_valid(c):
            return
        self._cmap = c
        self.im.set_cmap(self._cmap + self._rcmap)
        self.update_figure()

    colorMap = pyqtProperty('QString', getColorMap, setColorMap)

    def getReverseCMapToggle(self):
        return self._rcmap_toggle

    @pyqtSlot(bool)
    def setReverseCMapToggle(self, f):
        """Input param: bool
        """
        self._rcmap_toggle = f
        self._rcmap = '_r' if f else ''
        self.setColorMap(self._cmap)

    reseverColorMap = pyqtProperty(bool, getReverseCMapToggle,
                                   setReverseCMapToggle)

    def getColorRangeMin(self):
        return self._cr_min

    @pyqtSlot(float)
    def setColorRangeMin(self, x):
        """Min of color range
        """
        self._cr_min = x
        self.im.set_clim(vmin=self._cr_min, vmax=self._cr_max)
        self.update_figure()

    colorRangeMin = pyqtProperty(float, getColorRangeMin, setColorRangeMin)

    def getColorRangeMax(self):
        return self._cr_max

    @pyqtSlot(float)
    def setColorRangeMax(self, x):
        """Max of color range
        """
        self._cr_max = x
        self.im.set_clim(vmin=self._cr_min, vmax=self._cr_max)
        self.update_figure()

    colorRangeMax = pyqtProperty(float, getColorRangeMax, setColorRangeMax)

    def getColorBarToggle(self):
        return self._cb_toggle

    @pyqtSlot(bool)
    def setColorBarToggle(self, f):
        """Turn on/off colorbar.
        """
        self._cb_toggle = f
        if f and self.cb is None:
            self.cb = self.figure.colorbar(self.im,
                                           orientation=self._cb_orientation,
                                           aspect=20, shrink=0.95, pad=0.08,
                                           fraction=0.05)
            self.cb.ax.zorder = -1
        if not f and self.cb is not None:
            self.cb.remove()
            self.cb = None
        self.update_figure()

    colorBarToggle = pyqtProperty(bool, getColorBarToggle, setColorBarToggle)

    def getColorBarOrientation(self):
        return self._cb_orientation

    @pyqtSlot('QString')
    def setColorBarOrientation(self, s):
        self._cb_orientation = s.lower()
        if self.cb is not None:
            self.setColorBarToggle(False)
            self.setColorBarToggle(True)
        self.update_figure()

    colorBarOrientation = pyqtProperty('QString', getColorBarOrientation,
                                       setColorBarOrientation)

    def getAutoColorLimit(self):
        return self._auto_clim

    @pyqtSlot(bool)
    def setAutoColorLimit(self, f):
        """Turn on/off auto clim.
        """
        self._auto_clim = f
        if f:
            self.on_auto_clim()
        else:
            self.update_figure()

    autoColorLimit = pyqtProperty(bool, getAutoColorLimit,
                                  setAutoColorLimit)

    #def set_autoscale(self, axis='both'):
    #    self.axes.autoscale(axis)
    #    self.update_figure()

    def get_all_curves(self):
        """Return all additional curves."""
        return self._lines

    def init_figure(self):
        # additional lines
        self._lines = []

        # image
        x, y = np.meshgrid(np.linspace(-3, 3, 80),
                           np.linspace(-3, 3, 80))
        z = func_peaks(x, y)

        # color range
        self._cr_min, self._cr_max = get_array_range(z)
        et = (x[0, 0], x[-1, -1], y[0, 0], y[-1, -1])
        im = self.axes.imshow(z, cmap=self._cmap,
                              vmin=self._cr_min,
                              vmax=self._cr_max, origin="lower left",
                              extent=et)

        self._x_data, self._y_data, self.z = x, y, z
        self.im = im

#    @pyqtSlot(float)
#    def setXLimitMin(self, x=None):
#        pass
#
#    @pyqtSlot(float)
#    def setXLimitMax(self, x=None):
#        pass
#
#    @pyqtSlot(float)
#    def setYLimitMin(self, y=None):
#        pass
#
#    @pyqtSlot(float)
#    def setYLimitMax(self, y=None):
#        pass

    def on_config(self):
        config_panel = MatplotlibConfigImagePanel(self)
        config_panel.exec_()

    def on_motion(self, event):
        if event.inaxes is not None:
            _in, _ = self.im.contains(event)
            x_pos, y_pos = event.xdata, event.ydata
            if _in:
                z_pos = self.im.get_cursor_data(event)
            else:
                z_pos = np.nan
            # ?
            if z_pos is None: z_pos = np.nan
            #
            if np.ma.is_masked(z_pos):
                z_pos = np.nan

            self.xyposUpdated.emit([x_pos, y_pos, z_pos])

    def update_image(self, zdata):
        """Update image.
        """
        self.z = zdata
        self.im.set_array(zdata)

        ydim, xdim = self.z.shape
        if self.z.shape != self._x_data.shape:
            print("update xydata")
            _x = np.linspace(0, xdim - 1, xdim)
            _y = np.linspace(0, ydim - 1, ydim)
            self._x_data, self._y_data = np.meshgrid(_x, _y)
        self.set_extent()

        if self._auto_clim:
            self.on_auto_clim()
        else:
            self.update_figure()
        self.dataChanged.emit((self.im, self._x_data, self._y_data, zdata))

    def setXData(self, xdata):
        self._x_data = xdata
        self.set_extent()
        self.update_figure()

    def getXData(self):
        return self._x_data

    def setYData(self, ydata):
        self._y_data = ydata
        self.set_extent()
        self.update_figure()

    def getYData(self):
        return self._y_data

    def get_points(self):
        """Return (x, y) coords.
        """
        x, y = self._x_data[0, :], self._y_data[:, 0]
        return np.asarray([(i, j) for j in y for i in x])

    def get_extent(self):
        return self.im.get_extent()

    def set_extent(self, et=None):
        if et is None:
            et = (self._x_data[0, 0], self._x_data[-1, -1],
                  self._y_data[0, 0], self._y_data[-1, -1])
        self.im.set_extent(et)

    def on_auto_clim(self):
        """Auto set clim.
        """
        self._cr_min, self._cr_max = get_array_range(self.z)
        self.im.set_clim(vmin=self._cr_min, vmax=self._cr_max)
        self.update_figure()

    def get_cursor_data(self, x, y):
        return get_cursor_data(self.im, x, y)

    def get_all_data(self):
        return self._x_data, self._y_data, self.get_data()

    def get_data(self):
        return self.im.get_array()

    def clear_data(self):
        """Set with empty canvas, clear image.
        """
        self.update_image(np.ones(self.getXData().shape) * np.nan)

    def export_data(self, filepath):
        # temp
        import json
        zdata = self.get_data()
        xdata = self.getXData()
        ydata = self.getYData()
        d = {'array': zdata.tolist(),
             'shape': zdata.shape,
             'x': xdata.tolist(),
             'y': ydata.tolist()}
        with open(filepath, 'w') as fp:
            json.dump(d, fp, indent=2)


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = MatplotlibImageWidget()
    window.show()
    window.setGeometry(100, 100, 800, 600)
    sys.exit(app.exec_())
