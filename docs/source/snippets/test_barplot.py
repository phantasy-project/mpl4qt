#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ui_test4 import Ui_Form

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtCore import QVariant

import numpy as np
from phantasy import MachinePortal


N = 5

class MyWidget(Ui_Form, QWidget):
    curveChanged = pyqtSignal(QVariant, QVariant, QVariant)
    def __init__(self,):
        super(self.__class__, self).__init__()

        # UI
        self.setupUi(self)

        # update curve
        self.curveChanged.connect(self.matplotlibbarWidget.update_curve)
        self.update_btn.clicked.connect(self.update_data)
        #
        self.matplotlibbarWidget.clear_figure()

        self.init_figure()

    def init_figure(self):
        x = [1, 2]
        y = [3, 4]
        yerr = [0, 0]
        self.matplotlibbarWidget.init_figure(x, y, yerr)

    @pyqtSlot()
    def update_data(self):
        """Set bar chart.
        """
        x = np.random.random(N) * 10
        y = np.sin(x) * 6
        yerr = np.random.random(N)

        self.curveChanged.emit(x, y, yerr)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
