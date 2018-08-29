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
        self.matplotlibcurveWidget.setGeometry(QtCore.QRect(210, 100, 528, 396))
        self.matplotlibcurveWidget.setObjectName("matplotlibcurveWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 540, 124, 36))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Random X-Y Curve Plotter"))
        self.pushButton.setText(_translate("Form", "Update"))

from mpl4qt.widgets.mplcurvewidget import MatplotlibCurveWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

