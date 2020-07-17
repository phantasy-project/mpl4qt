# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fit_image.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(589, 482)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing
                                | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.matplotlibimageWidget = MatplotlibImageWidget(Dialog)
        self.matplotlibimageWidget.setProperty("figureToolbarToggle", False)
        self.matplotlibimageWidget.setProperty("reseverColorMap", False)
        self.matplotlibimageWidget.setAutoColorLimit(True)
        self.matplotlibimageWidget.setObjectName("matplotlibimageWidget")
        self.gridLayout.addWidget(self.matplotlibimageWidget, 3, 0, 1, 5)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.smooth_method_cbb = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.smooth_method_cbb.sizePolicy().hasHeightForWidth())
        self.smooth_method_cbb.setSizePolicy(sizePolicy)
        self.smooth_method_cbb.setObjectName("smooth_method_cbb")
        self.smooth_method_cbb.addItem("")
        self.smooth_method_cbb.addItem("")
        self.smooth_method_cbb.addItem("")
        self.gridLayout.addWidget(self.smooth_method_cbb, 0, 1, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.nx_sbox = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.nx_sbox.sizePolicy().hasHeightForWidth())
        self.nx_sbox.setSizePolicy(sizePolicy)
        self.nx_sbox.setMinimum(1)
        self.nx_sbox.setMaximum(9999)
        self.nx_sbox.setProperty("value", 50)
        self.nx_sbox.setObjectName("nx_sbox")
        self.horizontalLayout.addWidget(self.nx_sbox)
        self.label_4 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.ny_sbox = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ny_sbox.sizePolicy().hasHeightForWidth())
        self.ny_sbox.setSizePolicy(sizePolicy)
        self.ny_sbox.setMinimum(1)
        self.ny_sbox.setMaximum(9999)
        self.ny_sbox.setProperty("value", 50)
        self.ny_sbox.setObjectName("ny_sbox")
        self.horizontalLayout.addWidget(self.ny_sbox)
        self.reset_pts_btn = QtWidgets.QToolButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/reset_btn.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_pts_btn.setIcon(icon)
        self.reset_pts_btn.setIconSize(QtCore.QSize(24, 24))
        self.reset_pts_btn.setAutoRaise(True)
        self.reset_pts_btn.setObjectName("reset_pts_btn")
        self.horizontalLayout.addWidget(self.reset_pts_btn)
        self.view_3d_btn = QtWidgets.QPushButton(Dialog)
        self.view_3d_btn.setObjectName("view_3d_btn")
        self.horizontalLayout.addWidget(self.view_3d_btn)
        self.view_hm_btn = QtWidgets.QPushButton(Dialog)
        self.view_hm_btn.setObjectName("view_hm_btn")
        self.horizontalLayout.addWidget(self.view_hm_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 4)
        self.method_info_le = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.method_info_le.sizePolicy().hasHeightForWidth())
        self.method_info_le.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(False)
        self.method_info_le.setFont(font)
        self.method_info_le.setAlignment(QtCore.Qt.AlignRight
                                         | QtCore.Qt.AlignTrailing
                                         | QtCore.Qt.AlignVCenter)
        self.method_info_le.setReadOnly(True)
        self.method_info_le.setObjectName("method_info_le")
        self.gridLayout.addWidget(self.method_info_le, 0, 3, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Smooth Method"))
        self.matplotlibimageWidget.setFigureAspectRatio(
            _translate("Dialog", "auto"))
        self.label_2.setText(_translate("Dialog", "# of points "))
        self.smooth_method_cbb.setItemText(0, _translate("Dialog", "Spline-1"))
        self.smooth_method_cbb.setItemText(1, _translate("Dialog", "Spline-3"))
        self.smooth_method_cbb.setItemText(2, _translate("Dialog", "Spline-5"))
        self.label_3.setText(_translate("Dialog", "Horizontal"))
        self.label_4.setText(_translate("Dialog", "Vertical"))
        self.reset_pts_btn.setText(_translate("Dialog", "..."))
        self.view_3d_btn.setText(_translate("Dialog", "3D View"))
        self.view_hm_btn.setText(_translate("Dialog", "HM View"))
        self.method_info_le.setText(
            _translate("Dialog", "First Order Spline Interpolation"))


from mpl4qt.widgets.mplimagewidget import MatplotlibImageWidget
from . import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
