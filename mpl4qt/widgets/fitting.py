#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Image/Curve fitting.
"""

import numpy as np
from functools import partial
from scipy import interpolate

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from mpl4qt.ui.ui_fit_image import Ui_Dialog


SMOOTH_METH = {
    'Spline-1': ('linear', 'First Order Spline Interpolation'),
    'Spline-3': ('cubic', 'Third Order Spline Interpolation'),
    'Spline-5': ('quintic', 'Fifth Order Spline Interpolation'),
}


class FittingImage(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(FittingImage, self).__init__()
        self.parent = parent

        self.setupUi(self)
        self.setWindowTitle("Fitting - Image")

        self.post_init_ui()

    def post_init_ui(self):
        # initialized ready
        self._initialized = False
        # smooth method
        o = self.smooth_method_cbb
        o.currentTextChanged.connect(self.on_update_smethod)
        o.currentTextChanged.emit(o.currentText())

        # nx, ny
        for xoy, o in zip(('x', 'y'), (self.nx_sbox, self.ny_sbox)):
            o.valueChanged.connect(partial(self.on_update_n, xoy))
            o.valueChanged.emit(o.value())

    @pyqtSlot(int)
    def on_update_n(self, xoy, i):
        setattr(self, '_n{}'.format(xoy), i)
        if self._initialized:
            self._update_smooth_data()

    @pyqtSlot('QString')
    def on_update_smethod(self, s):
        meth, info = SMOOTH_METH[s]
        self.method_info_le.setText(info)
        self._smooth_method = meth
        if self._initialized:
            self._update_smooth_func()
            self._update_smooth_data()

    def _update_smooth_func(self):
        print("Update smooth func on '{}'".format(self._smooth_method))
        self._interp_f = interpolate.interp2d(self._x, self._y, self._data,
                                              kind=self._smooth_method)

    def _update_smooth_data(self):
        print("Smooth data with Nx: {}, Ny: {}".format(self._nx, self._ny))
        xs = np.linspace(self._x.min(), self._x.max(), self._nx)
        ys = np.linspace(self._y.min(), self._y.max(), self._ny)
        xx, yy = np.meshgrid(xs, ys)
        zz = self._interp_f(xs, ys)
        o = self.matplotlibimageWidget
        o.setXData(xx)
        o.setYData(yy)
        o.update_image(zz)

    def init_data(self):
        """Initialize data.
        """
        print("Initialize data...")
        data = self.parent.get_data()
        xx = self.parent.getXData()
        yy = self.parent.getYData()
        x, y = xx[0,:], yy[:,0]
        self._x = x
        self._y = y
        self._data = data

        o = self.matplotlibimageWidget
        p = self.parent
        o.setFigureXlabel(p.getFigureXlabel())
        o.setFigureYlabel(p.getFigureYlabel())
        o.setFigureTitle(p.getFigureTitle())

        # post init
        self._reconfig_ui()
        self._update_smooth_func()
        self._update_smooth_data()

        self._initialized = True

    def _reconfig_ui(self):
        # limit spinbox lower limit
        nx, ny = len(self._x), len(self._y)
        for n, o in zip((nx, ny), (self.nx_sbox, self.ny_sbox)):
            o.setMinimum(n)
            o.setValue(2.0 * n)
