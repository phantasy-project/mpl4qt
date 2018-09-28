#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpl4qt.examples.ui_app2 import Ui_Form

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtCore import QVariant

import numpy as np


class MyWidget(Ui_Form, QWidget):

    curveChanged = pyqtSignal(QVariant, QVariant, QVariant, QVariant)

    def __init__(self,):
        super(self.__class__, self).__init__()

        # UI
        self.setupUi(self)

        # update curve
        self.curveChanged.connect(
                self.matplotliberrorbarWidget.update_curve)
        self.pushButton.clicked.connect(self.update_xydata)

    @pyqtSlot()
    def update_xydata(self):
        """Set xy data for the curve figure.
        """
        x = np.linspace(-4, 4, 50)
        y = np.sin(10 * x) / x * np.random.random()
        yerr = np.random.random(x.shape)
        xerr = np.random.random(x.shape) * 0.1
        self.curveChanged.emit(x, y, xerr, yerr)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
