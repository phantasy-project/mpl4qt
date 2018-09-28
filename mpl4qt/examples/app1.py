#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpl4qt.examples.ui_app1 import Ui_Form

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtCore import QVariant

import numpy as np


class RandomCurveWidget(Ui_Form, QWidget):

    yDataChanged = pyqtSignal(QVariant)

    def __init__(self,):
        super(self.__class__, self).__init__()

        # UI
        self.setupUi(self)

        # update_ydata
        self.yDataChanged.connect(self.matplotlibcurveWidget.setYData)
        self.pushButton.clicked.connect(self.update_ydata)

    @pyqtSlot()
    def update_ydata(self):
        """Set xy data for the curve figure.
        """
        x = self.matplotlibcurveWidget.getXData()
        y = np.sin(x) * (1 + np.random.randn() * np.random.random(x.shape))
        self.yDataChanged.emit(y)


def run():
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = RandomCurveWidget()
    w.setWindowTitle("MatplotlibCurveWidget Example App")
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
