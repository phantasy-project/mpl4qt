#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ui_main import Ui_Form

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtCore import QVariant

import numpy as np


class MyWidget(Ui_Form, QWidget):

    curveChanged = pyqtSignal(QVariant, QVariant, QVariant, QVariant, QVariant, QVariant)
    addCurveSignal = pyqtSignal(QVariant, QVariant, QVariant, QVariant)

    def __init__(self,):
        super(self.__class__, self).__init__()

        # UI
        self.setupUi(self)

        # update curve
        self.curveChanged.connect(self.update_curve)
        self.update_btn.clicked.connect(self.update_xydata)

        # add_curve
        self.add_curve_btn.clicked.connect(self.add_curve)
        self.addCurveSignal.connect(self.matplotliberrorbarWidget.add_curve)

        #
        self.update_line_ids()
        # hide the first line
        self.hide_line(0)
        #
        self.add_curve_btn.clicked.emit()

    def hide_line(self, i):
        self.set_current_line_id(0)
        self.matplotliberrorbarWidget.setLineVisible(False)
        self.matplotliberrorbarWidget.setEbLineVisible(False)

    def update_line_ids(self):
        """Update the inventory of line IDs.
        """
        self.line_id_cbb.clear()
        n_curves = len(self.matplotliberrorbarWidget.get_all_curves())
        self.line_id_cbb.addItems([f'Curve {i}' for i in range(1, n_curves)])
        # set the current line to the last added one
        self.set_current_line_id(n_curves - 1)
        self.line_id_cbb.setCurrentText(f'Curve {n_curves - 1}')
        return n_curves - 1

    def update_curve(self, x, y, xerr_l, xerr_r, yerr_d, yerr_t):
        line_id = self.line_id_cbb.currentIndex() + 1
        self.set_current_line_id(line_id)
        self.matplotliberrorbarWidget.update_curve(x, y, xerr_l, yerr_d,
                err_method='user', xerr_data_r=xerr_r, yerr_data_t=yerr_t)

    def set_current_line_id(self, i):
        self.matplotliberrorbarWidget.setLineID(i)
        self.matplotliberrorbarWidget.setEbLineID(i)

    @pyqtSlot()
    def update_xydata(self):
        """Set xy data for the curve figure.
        """
        line_id = self.line_id_cbb.currentIndex() + 1
        x = self.matplotliberrorbarWidget.get_all_curves()[line_id].get_xdata()
        y = np.sin(x) * np.random.rand() * 6
        self.curveChanged.emit(x, y, 0, 0, y, 0)

    @pyqtSlot()
    def add_curve(self):
        n = np.random.randint(5, 25)
        x = np.linspace(-3, 3, n)
        y = np.sin(x) * 6
        self.addCurveSignal.emit(x, y, None, None)
        #
        last_line_id = self.update_line_ids()
        # set styles
        self.matplotliberrorbarWidget.setLineStyle('None')
        self.matplotliberrorbarWidget.setMarkerSize(10)
        self.matplotliberrorbarWidget.setEbMarkerThickness(2)
        self.matplotliberrorbarWidget.setEbLineWidth(3)
        # call update_curve to set down yerror
        self.update_btn.clicked.emit()




if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
