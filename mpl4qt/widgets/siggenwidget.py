#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Signal generator widget.
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import pyqtProperty, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

import numpy as np


class SignalGeneratorWidget(QWidget):

    valueChanged = pyqtSignal([int], ['QString'], [list])

    def __init__(self, parent=None):
        super(SignalGeneratorWidget, self).__init__(parent)

        self._value = 1.0
        signal_chart = SignalChartWidget(self, self.getValue())
        line_edit1 = QLineEdit(str(signal_chart.getValue()))

        vbox = QVBoxLayout()
        vbox.addWidget(signal_chart)
        vbox.addWidget(line_edit1)
        self.setLayout(vbox)
        self.adjustSize()

        # signals/slots
        #self.valueChanged[int].connect(signal_chart.setValue)
        #self.valueChanged['QString'].connect(line_edit1.setText)
        #line_edit1.textChanged.connect(self.setValue_str)

    def getValue(self):
        return self._value

    @pyqtSlot(int, name='setValue')
    def setValue_float(self, x):
        self._value = x
        self.valueChanged[int].emit(x)
        self.valueChanged['QString'].emit(str(x))
        self.update()

    @pyqtSlot('QString')
    def setValue_str(self, x):
        try:
            self._value = int(x)
            self.valueChanged[int].emit(int(x))
            self.valueChanged['QString'].emit(x)
        except:
            pass
        self.update()

    @pyqtSlot(list, name='setValue')
    def setValue_list(self, x):
        self._value = x
        self.valueChanged[list].emit(x)
        self.update()

    value = pyqtProperty(int, getValue, setValue_float)
    value_list = pyqtProperty(list, getValue, setValue_list)


class SignalChartWidget(QWidget):
    def __init__(self, parent=None, value=0.0):
        self._value = value
        super(SignalChartWidget, self).__init__(parent)
        
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 217, 217)))
        painter.drawRect(event.rect())
        tx, ty = self.width() / 2.0, self.height() / 2.0
        painter.drawText(tx - 10, ty, str(self.getValue()))
        painter.end()

    def getValue(self):
        return self._value

    @pyqtSlot(float)
    def setValue(self, x):
        self._value = x


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    #w = SignalGeneratorWidget()
    w = SignalChartWidget()
    w.show()
    sys.exit(app.exec_())
