# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mplconfig.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(726, 248)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.config_tabWidget = QtWidgets.QTabWidget(Dialog)
        font = QtGui.QFont()
        font.setItalic(False)
        self.config_tabWidget.setFont(font)
        self.config_tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.config_tabWidget.setObjectName("config_tabWidget")
        self.figure_tab = QtWidgets.QWidget()
        self.figure_tab.setObjectName("figure_tab")
        self.formLayout_2 = QtWidgets.QFormLayout(self.figure_tab)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_13 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                    self.label_13)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fig_title_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fig_title_lineEdit.sizePolicy().hasHeightForWidth())
        self.fig_title_lineEdit.setSizePolicy(sizePolicy)
        self.fig_title_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.fig_title_lineEdit.setObjectName("fig_title_lineEdit")
        self.horizontalLayout_5.addWidget(self.fig_title_lineEdit)
        self.title_font_btn = QtWidgets.QPushButton(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.title_font_btn.sizePolicy().hasHeightForWidth())
        self.title_font_btn.setSizePolicy(sizePolicy)
        self.title_font_btn.setAutoDefault(False)
        self.title_font_btn.setObjectName("title_font_btn")
        self.horizontalLayout_5.addWidget(self.title_font_btn)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole,
                                    self.horizontalLayout_5)
        self.label_10 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                    self.label_10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_18 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        self.fig_xlabel_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fig_xlabel_lineEdit.sizePolicy().hasHeightForWidth())
        self.fig_xlabel_lineEdit.setSizePolicy(sizePolicy)
        self.fig_xlabel_lineEdit.setText("")
        self.fig_xlabel_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.fig_xlabel_lineEdit.setObjectName("fig_xlabel_lineEdit")
        self.horizontalLayout_6.addWidget(self.fig_xlabel_lineEdit)
        self.label_11 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.fig_ylabel_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fig_ylabel_lineEdit.sizePolicy().hasHeightForWidth())
        self.fig_ylabel_lineEdit.setSizePolicy(sizePolicy)
        self.fig_ylabel_lineEdit.setText("")
        self.fig_ylabel_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.fig_ylabel_lineEdit.setObjectName("fig_ylabel_lineEdit")
        self.horizontalLayout_6.addWidget(self.fig_ylabel_lineEdit)
        self.xy_label_font_btn = QtWidgets.QPushButton(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xy_label_font_btn.sizePolicy().hasHeightForWidth())
        self.xy_label_font_btn.setSizePolicy(sizePolicy)
        self.xy_label_font_btn.setAutoDefault(False)
        self.xy_label_font_btn.setObjectName("xy_label_font_btn")
        self.horizontalLayout_6.addWidget(self.xy_label_font_btn)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole,
                                    self.horizontalLayout_6)
        self.label = QtWidgets.QLabel(self.figure_tab)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                    self.label)
        self.autoScale_chkbox = QtWidgets.QCheckBox(self.figure_tab)
        self.autoScale_chkbox.setChecked(True)
        self.autoScale_chkbox.setObjectName("autoScale_chkbox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                    self.autoScale_chkbox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.xmin_lbl = QtWidgets.QLabel(self.figure_tab)
        self.xmin_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.xmin_lbl.setObjectName("xmin_lbl")
        self.horizontalLayout_4.addWidget(self.xmin_lbl)
        self.xmin_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xmin_lineEdit.sizePolicy().hasHeightForWidth())
        self.xmin_lineEdit.setSizePolicy(sizePolicy)
        self.xmin_lineEdit.setObjectName("xmin_lineEdit")
        self.horizontalLayout_4.addWidget(self.xmin_lineEdit)
        self.xmax_lbl = QtWidgets.QLabel(self.figure_tab)
        self.xmax_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.xmax_lbl.setObjectName("xmax_lbl")
        self.horizontalLayout_4.addWidget(self.xmax_lbl)
        self.xmax_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xmax_lineEdit.sizePolicy().hasHeightForWidth())
        self.xmax_lineEdit.setSizePolicy(sizePolicy)
        self.xmax_lineEdit.setObjectName("xmax_lineEdit")
        self.horizontalLayout_4.addWidget(self.xmax_lineEdit)
        self.ymin_lbl = QtWidgets.QLabel(self.figure_tab)
        self.ymin_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ymin_lbl.setObjectName("ymin_lbl")
        self.horizontalLayout_4.addWidget(self.ymin_lbl)
        self.ymin_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ymin_lineEdit.sizePolicy().hasHeightForWidth())
        self.ymin_lineEdit.setSizePolicy(sizePolicy)
        self.ymin_lineEdit.setObjectName("ymin_lineEdit")
        self.horizontalLayout_4.addWidget(self.ymin_lineEdit)
        self.ymax_lbl = QtWidgets.QLabel(self.figure_tab)
        self.ymax_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ymax_lbl.setObjectName("ymax_lbl")
        self.horizontalLayout_4.addWidget(self.ymax_lbl)
        self.ymax_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ymax_lineEdit.sizePolicy().hasHeightForWidth())
        self.ymax_lineEdit.setSizePolicy(sizePolicy)
        self.ymax_lineEdit.setObjectName("ymax_lineEdit")
        self.horizontalLayout_4.addWidget(self.ymax_lineEdit)
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole,
                                    self.horizontalLayout_4)
        self.label_10.raise_()
        self.label.raise_()
        self.label_13.raise_()
        self.autoScale_chkbox.raise_()
        self.config_tabWidget.addTab(self.figure_tab, "")
        self.style_tab = QtWidgets.QWidget()
        self.style_tab.setObjectName("style_tab")
        self.formLayout = QtWidgets.QFormLayout(self.style_tab)
        self.formLayout.setObjectName("formLayout")
        self.label_16 = QtWidgets.QLabel(self.style_tab)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                  self.label_16)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_12 = QtWidgets.QLabel(self.style_tab)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.figWidth_lineEdit = QtWidgets.QLineEdit(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.figWidth_lineEdit.sizePolicy().hasHeightForWidth())
        self.figWidth_lineEdit.setSizePolicy(sizePolicy)
        self.figWidth_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.figWidth_lineEdit.setObjectName("figWidth_lineEdit")
        self.horizontalLayout.addWidget(self.figWidth_lineEdit)
        self.label_14 = QtWidgets.QLabel(self.style_tab)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.figHeight_lineEdit = QtWidgets.QLineEdit(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.figHeight_lineEdit.sizePolicy().hasHeightForWidth())
        self.figHeight_lineEdit.setSizePolicy(sizePolicy)
        self.figHeight_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.figHeight_lineEdit.setObjectName("figHeight_lineEdit")
        self.horizontalLayout.addWidget(self.figHeight_lineEdit)
        self.label_15 = QtWidgets.QLabel(self.style_tab)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.figDpi_lineEdit = QtWidgets.QLineEdit(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.figDpi_lineEdit.sizePolicy().hasHeightForWidth())
        self.figDpi_lineEdit.setSizePolicy(sizePolicy)
        self.figDpi_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.figDpi_lineEdit.setObjectName("figDpi_lineEdit")
        self.horizontalLayout.addWidget(self.figDpi_lineEdit)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole,
                                  self.horizontalLayout)
        self.label_17 = QtWidgets.QLabel(self.style_tab)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                  self.label_17)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.bkgd_color_label = QtWidgets.QLabel(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bkgd_color_label.sizePolicy().hasHeightForWidth())
        self.bkgd_color_label.setSizePolicy(sizePolicy)
        self.bkgd_color_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bkgd_color_label.setObjectName("bkgd_color_label")
        self.horizontalLayout_2.addWidget(self.bkgd_color_label)
        self.bkgd_color_btn = QtWidgets.QPushButton(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bkgd_color_btn.sizePolicy().hasHeightForWidth())
        self.bkgd_color_btn.setSizePolicy(sizePolicy)
        self.bkgd_color_btn.setAutoDefault(False)
        self.bkgd_color_btn.setObjectName("bkgd_color_btn")
        self.horizontalLayout_2.addWidget(self.bkgd_color_btn)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole,
                                  self.horizontalLayout_2)
        self.label_7 = QtWidgets.QLabel(self.style_tab)
        self.label_7.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.label_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mticks_chkbox = QtWidgets.QCheckBox(self.style_tab)
        self.mticks_chkbox.setObjectName("mticks_chkbox")
        self.horizontalLayout_3.addWidget(self.mticks_chkbox)
        self.xy_ticks_sample_lbl = QtWidgets.QLabel(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xy_ticks_sample_lbl.sizePolicy().hasHeightForWidth())
        self.xy_ticks_sample_lbl.setSizePolicy(sizePolicy)
        self.xy_ticks_sample_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.xy_ticks_sample_lbl.setObjectName("xy_ticks_sample_lbl")
        self.horizontalLayout_3.addWidget(self.xy_ticks_sample_lbl)
        self.xy_ticks_font_btn = QtWidgets.QPushButton(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xy_ticks_font_btn.sizePolicy().hasHeightForWidth())
        self.xy_ticks_font_btn.setSizePolicy(sizePolicy)
        self.xy_ticks_font_btn.setAutoDefault(False)
        self.xy_ticks_font_btn.setObjectName("xy_ticks_font_btn")
        self.horizontalLayout_3.addWidget(self.xy_ticks_font_btn)
        self.ticks_color_label = QtWidgets.QLabel(self.style_tab)
        self.ticks_color_label.setObjectName("ticks_color_label")
        self.horizontalLayout_3.addWidget(self.ticks_color_label)
        self.ticks_color_btn = QtWidgets.QPushButton(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ticks_color_btn.sizePolicy().hasHeightForWidth())
        self.ticks_color_btn.setSizePolicy(sizePolicy)
        self.ticks_color_btn.setAutoDefault(False)
        self.ticks_color_btn.setObjectName("ticks_color_btn")
        self.horizontalLayout_3.addWidget(self.ticks_color_btn)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole,
                                  self.horizontalLayout_3)
        self.label_6 = QtWidgets.QLabel(self.style_tab)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                  self.label_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tightLayout_chkbox = QtWidgets.QCheckBox(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tightLayout_chkbox.sizePolicy().hasHeightForWidth())
        self.tightLayout_chkbox.setSizePolicy(sizePolicy)
        self.tightLayout_chkbox.setObjectName("tightLayout_chkbox")
        self.horizontalLayout_7.addWidget(self.tightLayout_chkbox)
        self.gridon_chkbox = QtWidgets.QCheckBox(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gridon_chkbox.sizePolicy().hasHeightForWidth())
        self.gridon_chkbox.setSizePolicy(sizePolicy)
        self.gridon_chkbox.setObjectName("gridon_chkbox")
        self.horizontalLayout_7.addWidget(self.gridon_chkbox)
        self.grid_color_btn = QtWidgets.QPushButton(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.grid_color_btn.sizePolicy().hasHeightForWidth())
        self.grid_color_btn.setSizePolicy(sizePolicy)
        self.grid_color_btn.setStyleSheet(" QPushButton {\n"
                                          "    margin: 1px;\n"
                                          "    border-color: rgb(0, 85, 0);\n"
                                          "    border-style: outset;\n"
                                          "    border-radius: 3px;\n"
                                          "    border-width: 1px;\n"
                                          "    color: black;\n"
                                          "    background-color: gray;\n"
                                          "}\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: white;\n"
                                          "}")
        self.grid_color_btn.setText("")
        self.grid_color_btn.setAutoDefault(False)
        self.grid_color_btn.setObjectName("grid_color_btn")
        self.horizontalLayout_7.addWidget(self.grid_color_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole,
                                  self.horizontalLayout_7)
        self.config_tabWidget.addTab(self.style_tab, "")
        self.verticalLayout.addWidget(self.config_tabWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.config_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_13.setText(_translate("Dialog", "Title"))
        self.title_font_btn.setText(_translate("Dialog", "Font"))
        self.label_10.setText(_translate("Dialog", "Labels"))
        self.label_18.setText(_translate("Dialog", "X-Label"))
        self.label_11.setText(_translate("Dialog", "Y-Label"))
        self.xy_label_font_btn.setText(_translate("Dialog", "Font"))
        self.label.setText(_translate("Dialog", "XY Range"))
        self.autoScale_chkbox.setText(_translate("Dialog", "Auto Scale"))
        self.xmin_lbl.setText(_translate("Dialog", "xmin"))
        self.xmax_lbl.setText(_translate("Dialog", "xmax"))
        self.ymin_lbl.setText(_translate("Dialog", "ymin"))
        self.ymax_lbl.setText(_translate("Dialog", "ymax"))
        self.config_tabWidget.setTabText(
            self.config_tabWidget.indexOf(self.figure_tab),
            _translate("Dialog", "Figure"))
        self.label_16.setText(_translate("Dialog", "Figure Size"))
        self.label_12.setText(_translate("Dialog", "Width"))
        self.figWidth_lineEdit.setText(_translate("Dialog", "4"))
        self.figWidth_lineEdit.setPlaceholderText(_translate("Dialog", "4"))
        self.label_14.setText(_translate("Dialog", "Height"))
        self.figHeight_lineEdit.setText(_translate("Dialog", "3"))
        self.figHeight_lineEdit.setPlaceholderText(_translate("Dialog", "3"))
        self.label_15.setText(_translate("Dialog", "DPI"))
        self.figDpi_lineEdit.setText(_translate("Dialog", "120"))
        self.figDpi_lineEdit.setPlaceholderText(_translate("Dialog", "120"))
        self.label_17.setText(_translate("Dialog", "Background Color"))
        self.bkgd_color_label.setText(_translate("Dialog", "#FFFFFF"))
        self.bkgd_color_btn.setText(_translate("Dialog", "Pick Color"))
        self.label_7.setText(_translate("Dialog", "Ticks"))
        self.mticks_chkbox.setText(_translate("Dialog", "Minor On"))
        self.xy_ticks_sample_lbl.setText(_translate("Dialog", "Sample"))
        self.xy_ticks_font_btn.setText(_translate("Dialog", "Choose Font"))
        self.ticks_color_label.setText(_translate("Dialog", "#FFFFFF"))
        self.ticks_color_btn.setText(_translate("Dialog", "Pick Color"))
        self.label_6.setText(_translate("Dialog", "Layout"))
        self.tightLayout_chkbox.setText(_translate("Dialog", "Tight"))
        self.gridon_chkbox.setText(_translate("Dialog", "Grid On"))
        self.config_tabWidget.setTabText(
            self.config_tabWidget.indexOf(self.style_tab),
            _translate("Dialog", "Style"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())