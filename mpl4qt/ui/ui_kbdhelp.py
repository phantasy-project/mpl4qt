# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_kbdhelp.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(408, 352)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet(
            "QLabel {\n"
            "    padding:0.1em 0.5em;\n"
            "    font-family:Arial,Helvetica,sans-serif;\n"
            "    background-color:#F7F7F7;\n"
            "    color:#333;    \n"
            "    border-radius:3px;\n"
            "    border: 1px solid gray;\n"
            "    margin:0 0.1em;\n"
            "    line-height: 1.4;\n"
            "    font-weight: bold;\n"
            "}")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setStyleSheet("QLabel {\n"
                                    "    font-style: italic;\n"
                                    "}")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 8, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(
            "QLabel {\n"
            "    padding:0.1em 0.5em;\n"
            "    font-family:Arial,Helvetica,sans-serif;\n"
            "    background-color:#F7F7F7;\n"
            "    color:#333;    \n"
            "    border-radius:3px;\n"
            "    border: 1px solid gray;\n"
            "    margin:0 0.1em;\n"
            "    line-height: 1.4;\n"
            "    font-weight: bold;\n"
            "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setStyleSheet("QLabel {\n"
                                    "    font-style: italic;\n"
                                    "}")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setStyleSheet("QLabel {\n"
                                    "    font-style: italic;\n"
                                    "}")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setStyleSheet("QLabel {\n"
                                    "    font-style: italic;\n"
                                    "}")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 7, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet(
            "QLabel {\n"
            "    padding:0.1em 0.5em;\n"
            "    font-family:Arial,Helvetica,sans-serif;\n"
            "    background-color:#F7F7F7;\n"
            "    color:#333;    \n"
            "    border-radius:3px;\n"
            "    border: 1px solid gray;\n"
            "    margin:0 0.1em;\n"
            "    line-height: 1.4;\n"
            "    font-weight: bold;\n"
            "}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet(
            "QLabel {\n"
            "    padding:0.1em 0.5em;\n"
            "    font-family:Arial,Helvetica,sans-serif;\n"
            "    background-color:#F7F7F7;\n"
            "    color:#333;    \n"
            "    border-radius:3px;\n"
            "    border: 1px solid gray;\n"
            "    margin:0 0.1em;\n"
            "    line-height: 1.4;\n"
            "    font-weight: bold;\n"
            "}")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setStyleSheet("QLabel {\n"
                                   "    font-style: italic;\n"
                                   "}")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet(
            "QLabel {\n"
            "    padding:0.1em 0.5em;\n"
            "    font-family:Arial,Helvetica,sans-serif;\n"
            "    background-color:#F7F7F7;\n"
            "    color:#333;    \n"
            "    border-radius:3px;\n"
            "    border: 1px solid gray;\n"
            "    margin:0 0.1em;\n"
            "    line-height: 1.4;\n"
            "    font-weight: bold;\n"
            "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setStyleSheet("QLabel {\n"
                                    "    font-style: italic;\n"
                                    "}")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setStyleSheet("QLabel {\n"
                                   "    font-style: italic;\n"
                                   "}")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(
            "QLabel {\n"
            "    padding:0.1em 0.5em;\n"
            "    font-family:Arial,Helvetica,sans-serif;\n"
            "    background-color:#F7F7F7;\n"
            "    color:#333;    \n"
            "    border-radius:3px;\n"
            "    border: 1px solid gray;\n"
            "    margin:0 0.1em;\n"
            "    line-height: 1.4;\n"
            "    font-weight: bold;\n"
            "}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(
            "QLabel {\n"
            "    padding:0.1em 0.5em;\n"
            "    font-family:Arial,Helvetica,sans-serif;\n"
            "    background-color:#F7F7F7;\n"
            "    color:#333;    \n"
            "    border-radius:3px;\n"
            "    border: 1px solid gray;\n"
            "    margin:0 0.1em;\n"
            "    line-height: 1.4;\n"
            "    font-weight: bold;\n"
            "}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", "?"))
        self.label_14.setText(_translate("Dialog", "Show help message box"))
        self.label_16.setText(_translate("Dialog", "Function"))
        self.label.setText(_translate("Dialog", "g"))
        self.label_11.setText(_translate("Dialog", "Turn on/off legend"))
        self.label_12.setText(_translate("Dialog", "Tight layout on/off"))
        self.label_13.setText(_translate("Dialog", "Force refresh"))
        self.label_5.setText(_translate("Dialog", "t"))
        self.label_6.setText(_translate("Dialog", "r"))
        self.label_8.setText(_translate("Dialog", "Turn on/off grid"))
        self.label_4.setText(_translate("Dialog", "l"))
        self.label_10.setText(_translate("Dialog", "Turn on/off auto scale"))
        self.label_9.setText(_translate("Dialog", "Turn on/off minor ticks"))
        self.label_3.setText(_translate("Dialog", "a"))
        self.label_2.setText(_translate("Dialog", "m"))
        self.label_15.setText(_translate("Dialog", "Key"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
