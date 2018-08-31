# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_app1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(933, 687)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(300, 20, 349, 37))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.matplotlibcurveWidget = MatplotlibCurveWidget(Form)
        self.matplotlibcurveWidget.setGeometry(
            QtCore.QRect(210, 100, 528, 396))
        self.matplotlibcurveWidget.setObjectName("matplotlibcurveWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 540, 124, 36))
        self.pushButton.setObjectName("pushButton")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(490, 600, 81, 36))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(370, 610, 96, 26))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.doubleSpinBox.valueChanged['double'].connect(
            self.matplotlibcurveWidget.setLineWidth)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Random X-Y Curve Plotter"))
        self.pushButton.setText(_translate("Form", "Update"))
        self.label_2.setText(_translate("Form", "Line Width"))


from mpl4qt.widgets.mplcurvewidget import MatplotlibCurveWidget
