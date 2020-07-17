# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_markers_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
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
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_3.setSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.selected_pts_lbl_5 = QtWidgets.QLabel(Form)
        self.selected_pts_lbl_5.setText("")
        self.selected_pts_lbl_5.setObjectName("selected_pts_lbl_5")
        self.gridLayout_3.addWidget(self.selected_pts_lbl_5, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        self.selected_pts_lbl_2 = QtWidgets.QLabel(Form)
        self.selected_pts_lbl_2.setText("")
        self.selected_pts_lbl_2.setObjectName("selected_pts_lbl_2")
        self.gridLayout_3.addWidget(self.selected_pts_lbl_2, 3, 1, 1, 1)
        self.distance_lbl = QtWidgets.QLabel(Form)
        self.distance_lbl.setStyleSheet("QLabel {\n"
                                        "    border: 1px solid gray;\n"
                                        "    color: rgb(0, 85, 255);\n"
                                        "}")
        self.distance_lbl.setText("")
        self.distance_lbl.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.distance_lbl.setObjectName("distance_lbl")
        self.gridLayout_3.addWidget(self.distance_lbl, 3, 2, 1, 1)
        self.selected_pts_lbl_3 = QtWidgets.QLabel(Form)
        self.selected_pts_lbl_3.setText("")
        self.selected_pts_lbl_3.setObjectName("selected_pts_lbl_3")
        self.gridLayout_3.addWidget(self.selected_pts_lbl_3, 4, 1, 1, 1)
        self.selected_pts_lbl_1 = QtWidgets.QLabel(Form)
        self.selected_pts_lbl_1.setText("")
        self.selected_pts_lbl_1.setObjectName("selected_pts_lbl_1")
        self.gridLayout_3.addWidget(self.selected_pts_lbl_1, 0, 1, 1, 1)
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
                                         "}")
        self.mid_point_lbl.setText("")
        self.mid_point_lbl.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.mid_point_lbl.setObjectName("mid_point_lbl")
        self.gridLayout_3.addWidget(self.mid_point_lbl, 0, 2, 1, 1)
        self.selected_pts_lbl_4 = QtWidgets.QLabel(Form)
        self.selected_pts_lbl_4.setText("")
        self.selected_pts_lbl_4.setObjectName("selected_pts_lbl_4")
        self.gridLayout_3.addWidget(self.selected_pts_lbl_4, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 4, 0, 1, 1)
        self.dy_lbl = QtWidgets.QLabel(Form)
        self.dy_lbl.setStyleSheet("QLabel {\n"
                                  "    border: 1px solid gray;\n"
                                  "    color: rgb(0, 85, 255);\n"
                                  "}")
        self.dy_lbl.setText("")
        self.dy_lbl.setObjectName("dy_lbl")
        self.gridLayout_3.addWidget(self.dy_lbl, 2, 2, 1, 1)
        self.dx_lbl = QtWidgets.QLabel(Form)
        self.dx_lbl.setStyleSheet("QLabel {\n"
                                  "    border: 1px solid gray;\n"
                                  "    color: rgb(0, 85, 255);\n"
                                  "}")
        self.dx_lbl.setText("")
        self.dx_lbl.setObjectName("dx_lbl")
        self.gridLayout_3.addWidget(self.dx_lbl, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.area_lbl = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.area_lbl.sizePolicy().hasHeightForWidth())
        self.area_lbl.setSizePolicy(sizePolicy)
        self.area_lbl.setStyleSheet("QLabel {\n"
                                    "    border: 1px solid gray;\n"
                                    "    color: rgb(0, 85, 255);\n"
                                    "}")
        self.area_lbl.setText("")
        self.area_lbl.setObjectName("area_lbl")
        self.horizontalLayout.addWidget(self.area_lbl)
        self.shade_area_chkbox = QtWidgets.QCheckBox(Form)
        self.shade_area_chkbox.setObjectName("shade_area_chkbox")
        self.horizontalLayout.addWidget(self.shade_area_chkbox)
        self.gridLayout_3.addLayout(self.horizontalLayout, 4, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(2, 10, 2, 2)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tableWidget.cellPressed['int', 'int'].connect(Form.on_press)
        self.tableWidget.itemSelectionChanged.connect(
            Form.on_selection_changed)
        self.shade_area_chkbox.toggled['bool'].connect(Form.on_shade_area)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Middle Point of"))
        self.label_3.setText(_translate("Form", "Distance between"))
        self.label_4.setText(
            _translate(
                "Form",
                "<html><head/><body><p>Horizontal displacement of</p></body></html>"
            ))
        self.label_7.setText(_translate("Form", "Vertical displacement of"))
        self.label_2.setText(_translate("Form", "Area of Rectangle"))
        self.shade_area_chkbox.setText(_translate("Form", "Shade"))
        self.groupBox.setTitle(_translate("Form", "A List of Markers"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
