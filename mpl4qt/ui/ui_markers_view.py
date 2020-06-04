# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_markers_view.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(2, 10, 2, 2)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_3.setSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mid_point_lbl = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mid_point_lbl.sizePolicy().hasHeightForWidth())
        self.mid_point_lbl.setSizePolicy(sizePolicy)
        self.mid_point_lbl.setStyleSheet("QLabel {\n"
                                         "    border: 1px solid gray;\n"
                                         "    color: rgb(0, 85, 255);\n"
                                         "    padding: 0px 0px 0px 10px;\n"
                                         "}")
        self.mid_point_lbl.setText("")
        self.mid_point_lbl.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.mid_point_lbl.setObjectName("mid_point_lbl")
        self.gridLayout_3.addWidget(self.mid_point_lbl, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.distance_lbl = QtWidgets.QLabel(Form)
        self.distance_lbl.setStyleSheet("QLabel {\n"
                                        "    border: 1px solid gray;\n"
                                        "    color: rgb(0, 85, 255);\n"
                                        "    padding: 0px 0px 0px 10px;\n"
                                        "}")
        self.distance_lbl.setText("")
        self.distance_lbl.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.distance_lbl.setObjectName("distance_lbl")
        self.gridLayout_3.addWidget(self.distance_lbl, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.selected_pts_lbl_1 = QtWidgets.QLabel(Form)
        self.selected_pts_lbl_1.setText("")
        self.selected_pts_lbl_1.setObjectName("selected_pts_lbl_1")
        self.gridLayout_3.addWidget(self.selected_pts_lbl_1, 0, 1, 1, 1)
        self.selected_pts_lbl_2 = QtWidgets.QLabel(Form)
        self.selected_pts_lbl_2.setText("")
        self.selected_pts_lbl_2.setObjectName("selected_pts_lbl_2")
        self.gridLayout_3.addWidget(self.selected_pts_lbl_2, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.tableWidget.cellPressed['int', 'int'].connect(Form.on_press)
        self.tableWidget.itemSelectionChanged.connect(
            Form.on_selection_changed)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "A List of Markers"))
        self.label_3.setText(_translate("Form", "Distance between"))
        self.label.setText(_translate("Form", "Middle Point of"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
