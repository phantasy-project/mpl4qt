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

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtProperty

from mpl4qt.widgets.mplcurvewidget import MatplotlibCurveWidget
from mpl4qt.widgets.mplconfig import MatplotlibConfigImagePanel


class MatplotlibImageWidget(MatplotlibCurveWidget):
    """MatplotlibImageWidget(MatplotlibCurveWidget)

    Provides a custom widget to draw image with matplotlib, with properties
    and slots that can be used to customize its appearance.
    """

    def __init__(self, parent=None):
        # colormap
        #self._cmap = "viridis"
        self._cmap = "jet"

        super(MatplotlibImageWidget, self).__init__(parent)

        # reverse colormap flag
        self._rcmap_toggle = False
        self.setReverseCMapToggle(self._rcmap_toggle)


    def getColorMap(self):
        return self._cmap

    @pyqtSlot('QString')
    def setColorMap(self, c):
        if c == '': return
        print(c)
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

    def get_all_curves(self):
        """Return all additional curves."""
        return self._lines

    def init_figure(self):
        # additional lines
        self._lines = []

        # image
        x, y = np.meshgrid(np.linspace(-3, 3, 100),
                           np.linspace(-3, 3, 100))
        z = fn_peaks(x, y)
        im = self.axes.imshow(z, cmap=self._cmap)#, origin="lower left")

        self.x, self.y, self.z = x, y, z
        self.im = im

        #
        self.figure.colorbar(im)

    @pyqtSlot(float)
    def setXLimitMin(self, x=None):
        pass

    @pyqtSlot(float)
    def setXLimitMax(self, x=None):
        pass

    @pyqtSlot(float)
    def setYLimitMin(self, y=None):
        pass

    @pyqtSlot(float)
    def setYLimitMax(self, y=None):
        pass

    def on_config(self):
        config_panel = MatplotlibConfigImagePanel(self)
        config_panel.exec_()

    def on_motion(self, event):
        if event.inaxes is not None:
            x_pos, y_pos = event.xdata, event.ydata
            x_ind, y_ind = int(x_pos), int(y_pos)
            z_pos = self.z[y_ind][x_ind]
            self.xyposUpdated.emit([x_pos, y_pos, z_pos])


def fn_peaks(x, y):
    return 3.0 * (1.0 - x)**2.0 * np.exp(-(x**2) - (y+1)**2) \
         - 10*(x/5 - x**3 - y**5) * np.exp(-x**2-y**2) \
         - 1.0/3.0*np.exp(-(x+1)**2 - y**2)


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = MatplotlibImageWidget()
    window.show()
    window.setGeometry(100, 100, 800, 600)
    sys.exit(app.exec_())
