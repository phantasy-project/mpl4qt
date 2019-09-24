#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Image/Curve fitting.
"""

import numpy as np
from functools import partial
from scipy import interpolate

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

from mpl4qt.ui.ui_fit_image import Ui_Dialog


SMOOTH_METH = {
    'Spline-1': ('linear', 'First Order Spline Interpolation'),
    'Spline-3': ('cubic', 'Third Order Spline Interpolation'),
    'Spline-5': ('quintic', 'Fifth Order Spline Interpolation'),
}


# smooth method, literal to param
SMOOTH_METHOD_DICT = {
    'Nearest': 'nearest',
    'Linear': 'linear',
    'Spline-0': 'zero',
    'Spline-1': 'slinear',
    'Spline-2': 'quadratic',
    'Spline-3': 'cubic',
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

        # reset nx & ny
        self.reset_pts_btn.clicked.connect(self.on_reset_xypoints)

        # 3d view
        self.view_3d_btn.clicked.connect(self.on_view_3d)

        # hm view
        self.view_hm_btn.clicked.connect(self.on_view_hm)

    @pyqtSlot()
    def on_view_3d(self):
        # show data in 3D.
        self._show_surface_view(self.matplotlibimageWidget, 1.2, 0.8)

    @pyqtSlot()
    def on_view_hm(self):
        # show data in heatmap
        self._show_heatmap_view(self.matplotlibimageWidget, 0.8)

    @pyqtSlot()
    def on_reset_xypoints(self):
        self.nx_sbox.setValue(self._nx0)
        self.ny_sbox.setValue(self._ny0)

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
        o.setColorMap(p.getColorMap())

        # post init
        self._reconfig_ui()
        self._update_smooth_func()
        self._update_smooth_data()

        self._initialized = True

    def _reconfig_ui(self):
        # limit spinbox lower limit
        nx, ny = len(self._x), len(self._y)
        self._nx0, self._ny0 = nx, ny
        for n, o in zip((nx, ny), (self.nx_sbox, self.ny_sbox)):
            o.setMinimum(n)
            o.setValue(2.0 * n)

    def _show_surface_view(self, o, f, alpha):
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D

        z = o.get_data()
        x = o.getXData()
        y = o.getYData()
        cm = o.getColorMap()
        xlbl = o.getFigureXlabel()
        ylbl = o.getFigureYlabel()

        fig = plt.figure("View in 3D Surface", figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, cmap=cm, alpha=alpha)
        ax.contour(x, y, z, zdir='z', offset=z.min() * f, cmap=cm)
        ax.contour(x, y, z, zdir='x', offset=x.min() * f, cmap=cm)
        ax.contour(x, y, z, zdir='y', offset=y.max() * f, cmap=cm)
        ax.set_xlim(x.min() * f, x.max() * f)
        ax.set_ylim(y.min() * f, y.max() * f)
        ax.set_zlim(z.min() * f, z.max() * f)
        ax.set_xlabel(xlbl)
        ax.set_ylabel(ylbl)
        plt.show()

    def _show_heatmap_view(self, o, alpha):
        try:
            import seaborn as sns
        except ModuleNotFoundError:
            QMessageBox.warning(self, "Module Not Found",
                    "Python package 'seaborn' is not found.",
                    QMessageBox.Ok)
            return

        import matplotlib.pyplot as plt

        z = o.get_data()
        x = o.getXData()
        y = o.getYData()
        cm = o.getColorMap()
        xlbl = o.getFigureXlabel()
        ylbl = o.getFigureYlabel()

        fig = plt.figure("View in Heatmap", figsize=(10, 8))
        ax = fig.add_subplot(111)
        sns.heatmap(z, ax=ax, cmap=cm, alpha=alpha, linewidth=0.01)
        ax.set_xlabel(xlbl)
        ax.set_ylabel(ylbl)
        plt.show()
