# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mplconfig.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1057, 356)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setStyleSheet(
            " QToolButton#grid_color_btn, #ticks_color_btn, #border_color_btn, #bkgd_color_btn, #bar_color_btn, #ebline_color_btn, #line_color_btn, #mk_facecolor_btn, #mk_edgecolor_btn, #eb_line_color_btn, #eb_mk_facecolor_btn, #eb_mk_edgecolor_btn {\n"
            "    border-color: #F8F7F6;\n"
            "    border-radius: 1px;\n"
            "    background-color: #888A85;\n"
            "    margin: 4px;\n"
            "    qproperty-iconSize: 12px;\n"
            "}\n"
            "QToolButton#grid_color_btn:pressed, QToolButton#ticks_color_btn:pressed,\n"
            "QToolButton#border_color_btn:pressed,\n"
            "QToolButton#bkgd_color_btn:pressed,\n"
            "QToolButton#bar_color_btn:pressed,\n"
            "QToolButton#ebline_color_btn:pressed,\n"
            "QToolButton#line_color_btn:pressed,\n"
            "QToolButton#mk_facecolor_btn:pressed,\n"
            "QToolButton#mk_edgecolor_btn:pressed,\n"
            "QToolButton#eb_mk_edgecolor_btn:pressed,\n"
            "QToolButton#eb_mk_facecolor_btn:pressed,\n"
            "QToolButton#eb_line_color_btn:pressed {\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #DADBDE, stop: 1 #F6F7FA);\n"
            "}\n"
            "\n"
            "QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;}"
        )
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_3.setSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.config_tabWidget = TabWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.config_tabWidget.sizePolicy().hasHeightForWidth())
        self.config_tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(False)
        self.config_tabWidget.setFont(font)
        self.config_tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.config_tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.config_tabWidget.setDocumentMode(True)
        self.config_tabWidget.setTabsClosable(False)
        self.config_tabWidget.setMovable(False)
        self.config_tabWidget.setTabBarAutoHide(False)
        self.config_tabWidget.setObjectName("config_tabWidget")
        self.figure_tab = QtWidgets.QWidget()
        self.figure_tab.setObjectName("figure_tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.figure_tab)
        self.gridLayout_6.setContentsMargins(6, 12, 6, 6)
        self.gridLayout_6.setSpacing(4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_42 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_11.addWidget(self.label_42)
        self.xaxis_scale_cbb = QtWidgets.QComboBox(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xaxis_scale_cbb.sizePolicy().hasHeightForWidth())
        self.xaxis_scale_cbb.setSizePolicy(sizePolicy)
        self.xaxis_scale_cbb.setObjectName("xaxis_scale_cbb")
        self.xaxis_scale_cbb.addItem("")
        self.xaxis_scale_cbb.addItem("")
        self.xaxis_scale_cbb.addItem("")
        self.xaxis_scale_cbb.addItem("")
        self.horizontalLayout_11.addWidget(self.xaxis_scale_cbb)
        self.label_41 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_11.addWidget(self.label_41)
        self.yaxis_scale_cbb = QtWidgets.QComboBox(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.yaxis_scale_cbb.sizePolicy().hasHeightForWidth())
        self.yaxis_scale_cbb.setSizePolicy(sizePolicy)
        self.yaxis_scale_cbb.setObjectName("yaxis_scale_cbb")
        self.yaxis_scale_cbb.addItem("")
        self.yaxis_scale_cbb.addItem("")
        self.yaxis_scale_cbb.addItem("")
        self.yaxis_scale_cbb.addItem("")
        self.horizontalLayout_11.addWidget(self.yaxis_scale_cbb)
        self.gridLayout_6.addLayout(self.horizontalLayout_11, 4, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 1, 0, 1, 1)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_20.setSpacing(4)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_18 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_20.addWidget(self.label_18)
        self.fig_xlabel_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fig_xlabel_lineEdit.sizePolicy().hasHeightForWidth())
        self.fig_xlabel_lineEdit.setSizePolicy(sizePolicy)
        self.fig_xlabel_lineEdit.setText("")
        self.fig_xlabel_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.fig_xlabel_lineEdit.setPlaceholderText("")
        self.fig_xlabel_lineEdit.setObjectName("fig_xlabel_lineEdit")
        self.horizontalLayout_20.addWidget(self.fig_xlabel_lineEdit)
        self.label_11 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_20.addWidget(self.label_11)
        self.fig_ylabel_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fig_ylabel_lineEdit.sizePolicy().hasHeightForWidth())
        self.fig_ylabel_lineEdit.setSizePolicy(sizePolicy)
        self.fig_ylabel_lineEdit.setText("")
        self.fig_ylabel_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.fig_ylabel_lineEdit.setPlaceholderText("")
        self.fig_ylabel_lineEdit.setObjectName("fig_ylabel_lineEdit")
        self.horizontalLayout_20.addWidget(self.fig_ylabel_lineEdit)
        self.hide_xylabel_chkbox = QtWidgets.QCheckBox(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.hide_xylabel_chkbox.sizePolicy().hasHeightForWidth())
        self.hide_xylabel_chkbox.setSizePolicy(sizePolicy)
        self.hide_xylabel_chkbox.setObjectName("hide_xylabel_chkbox")
        self.horizontalLayout_20.addWidget(self.hide_xylabel_chkbox)
        self.xy_label_font_btn = QtWidgets.QToolButton(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xy_label_font_btn.sizePolicy().hasHeightForWidth())
        self.xy_label_font_btn.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/choose-font.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.xy_label_font_btn.setIcon(icon)
        self.xy_label_font_btn.setIconSize(QtCore.QSize(24, 24))
        self.xy_label_font_btn.setAutoRaise(True)
        self.xy_label_font_btn.setObjectName("xy_label_font_btn")
        self.horizontalLayout_20.addWidget(self.xy_label_font_btn)
        self.gridLayout_6.addLayout(self.horizontalLayout_20, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing
                                | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fig_title_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fig_title_lineEdit.sizePolicy().hasHeightForWidth())
        self.fig_title_lineEdit.setSizePolicy(sizePolicy)
        self.fig_title_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.fig_title_lineEdit.setPlaceholderText("")
        self.fig_title_lineEdit.setObjectName("fig_title_lineEdit")
        self.horizontalLayout_2.addWidget(self.fig_title_lineEdit)
        self.hide_title_chkbox = QtWidgets.QCheckBox(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.hide_title_chkbox.sizePolicy().hasHeightForWidth())
        self.hide_title_chkbox.setSizePolicy(sizePolicy)
        self.hide_title_chkbox.setObjectName("hide_title_chkbox")
        self.horizontalLayout_2.addWidget(self.hide_title_chkbox)
        self.title_font_btn = QtWidgets.QToolButton(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.title_font_btn.sizePolicy().hasHeightForWidth())
        self.title_font_btn.setSizePolicy(sizePolicy)
        self.title_font_btn.setIcon(icon)
        self.title_font_btn.setIconSize(QtCore.QSize(24, 24))
        self.title_font_btn.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.title_font_btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.title_font_btn.setAutoRaise(True)
        self.title_font_btn.setArrowType(QtCore.Qt.NoArrow)
        self.title_font_btn.setObjectName("title_font_btn")
        self.horizontalLayout_2.addWidget(self.title_font_btn)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_6.addWidget(self.label_25, 3, 0, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.figure_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout_6.addWidget(self.label_40, 4, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(4)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.legend_on_chkbox = QtWidgets.QCheckBox(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.legend_on_chkbox.sizePolicy().hasHeightForWidth())
        self.legend_on_chkbox.setSizePolicy(sizePolicy)
        self.legend_on_chkbox.setObjectName("legend_on_chkbox")
        self.horizontalLayout_10.addWidget(self.legend_on_chkbox)
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.label_24 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_10.addWidget(self.label_24)
        self.legend_loc_cbb = QtWidgets.QComboBox(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.legend_loc_cbb.sizePolicy().hasHeightForWidth())
        self.legend_loc_cbb.setSizePolicy(sizePolicy)
        self.legend_loc_cbb.setObjectName("legend_loc_cbb")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.horizontalLayout_10.addWidget(self.legend_loc_cbb)
        self.gridLayout_6.addLayout(self.horizontalLayout_10, 3, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.autoScale_chkbox = QtWidgets.QCheckBox(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.autoScale_chkbox.sizePolicy().hasHeightForWidth())
        self.autoScale_chkbox.setSizePolicy(sizePolicy)
        self.autoScale_chkbox.setChecked(True)
        self.autoScale_chkbox.setObjectName("autoScale_chkbox")
        self.horizontalLayout_3.addWidget(self.autoScale_chkbox)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_5.setSpacing(4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.xmin_lbl = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xmin_lbl.sizePolicy().hasHeightForWidth())
        self.xmin_lbl.setSizePolicy(sizePolicy)
        self.xmin_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.xmin_lbl.setObjectName("xmin_lbl")
        self.gridLayout_5.addWidget(self.xmin_lbl, 0, 0, 1, 1)
        self.xmin_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xmin_lineEdit.sizePolicy().hasHeightForWidth())
        self.xmin_lineEdit.setSizePolicy(sizePolicy)
        self.xmin_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.xmin_lineEdit.setObjectName("xmin_lineEdit")
        self.gridLayout_5.addWidget(self.xmin_lineEdit, 0, 1, 1, 1)
        self.xmax_lbl = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xmax_lbl.sizePolicy().hasHeightForWidth())
        self.xmax_lbl.setSizePolicy(sizePolicy)
        self.xmax_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.xmax_lbl.setObjectName("xmax_lbl")
        self.gridLayout_5.addWidget(self.xmax_lbl, 0, 2, 1, 1)
        self.xmax_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xmax_lineEdit.sizePolicy().hasHeightForWidth())
        self.xmax_lineEdit.setSizePolicy(sizePolicy)
        self.xmax_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.xmax_lineEdit.setObjectName("xmax_lineEdit")
        self.gridLayout_5.addWidget(self.xmax_lineEdit, 0, 3, 1, 1)
        self.ymin_lbl = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ymin_lbl.sizePolicy().hasHeightForWidth())
        self.ymin_lbl.setSizePolicy(sizePolicy)
        self.ymin_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ymin_lbl.setObjectName("ymin_lbl")
        self.gridLayout_5.addWidget(self.ymin_lbl, 1, 0, 1, 1)
        self.ymin_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ymin_lineEdit.sizePolicy().hasHeightForWidth())
        self.ymin_lineEdit.setSizePolicy(sizePolicy)
        self.ymin_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ymin_lineEdit.setObjectName("ymin_lineEdit")
        self.gridLayout_5.addWidget(self.ymin_lineEdit, 1, 1, 1, 1)
        self.ymax_lbl = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ymax_lbl.sizePolicy().hasHeightForWidth())
        self.ymax_lbl.setSizePolicy(sizePolicy)
        self.ymax_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ymax_lbl.setObjectName("ymax_lbl")
        self.gridLayout_5.addWidget(self.ymax_lbl, 1, 2, 1, 1)
        self.ymax_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ymax_lineEdit.sizePolicy().hasHeightForWidth())
        self.ymax_lineEdit.setSizePolicy(sizePolicy)
        self.ymax_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ymax_lineEdit.setObjectName("ymax_lineEdit")
        self.gridLayout_5.addWidget(self.ymax_lineEdit, 1, 3, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_5)
        self.gridLayout_6.addLayout(self.horizontalLayout_3, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 5, 2, 1, 1)
        self.label_10.raise_()
        self.label_13.raise_()
        self.label_25.raise_()
        self.label_40.raise_()
        self.label.raise_()
        self.config_tabWidget.addTab(self.figure_tab, "")
        self.style_tab = QtWidgets.QWidget()
        self.style_tab.setObjectName("style_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.style_tab)
        self.gridLayout_7.setContentsMargins(6, 12, 6, 6)
        self.gridLayout_7.setSpacing(4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.style_tab)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.figWidth_lineEdit = QtWidgets.QLineEdit(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.figWidth_lineEdit.sizePolicy().hasHeightForWidth())
        self.figWidth_lineEdit.setSizePolicy(sizePolicy)
        self.figWidth_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.figWidth_lineEdit.setObjectName("figWidth_lineEdit")
        self.horizontalLayout_5.addWidget(self.figWidth_lineEdit)
        self.label_14 = QtWidgets.QLabel(self.style_tab)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.figHeight_lineEdit = QtWidgets.QLineEdit(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.figHeight_lineEdit.sizePolicy().hasHeightForWidth())
        self.figHeight_lineEdit.setSizePolicy(sizePolicy)
        self.figHeight_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.figHeight_lineEdit.setObjectName("figHeight_lineEdit")
        self.horizontalLayout_5.addWidget(self.figHeight_lineEdit)
        self.label_15 = QtWidgets.QLabel(self.style_tab)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.figDpi_lineEdit = QtWidgets.QLineEdit(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.figDpi_lineEdit.sizePolicy().hasHeightForWidth())
        self.figDpi_lineEdit.setSizePolicy(sizePolicy)
        self.figDpi_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.figDpi_lineEdit.setObjectName("figDpi_lineEdit")
        self.horizontalLayout_5.addWidget(self.figDpi_lineEdit)
        self.label_69 = QtWidgets.QLabel(self.style_tab)
        self.label_69.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_69.setObjectName("label_69")
        self.horizontalLayout_5.addWidget(self.label_69)
        self.figAspect_cbb = QtWidgets.QComboBox(self.style_tab)
        self.figAspect_cbb.setEditable(True)
        self.figAspect_cbb.setObjectName("figAspect_cbb")
        self.figAspect_cbb.addItem("")
        self.figAspect_cbb.addItem("")
        self.horizontalLayout_5.addWidget(self.figAspect_cbb)
        self.gridLayout_7.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.style_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_7.addWidget(self.label_17, 1, 0, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_18.setSpacing(4)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_59 = QtWidgets.QLabel(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy)
        self.label_59.setObjectName("label_59")
        self.horizontalLayout_18.addWidget(self.label_59)
        self.line_6 = QtWidgets.QFrame(self.style_tab)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_18.addWidget(self.line_6)
        self.label_60 = QtWidgets.QLabel(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.horizontalLayout_18.addWidget(self.label_60)
        self.xticks_rotation_sbox = QtWidgets.QDoubleSpinBox(self.style_tab)
        self.xticks_rotation_sbox.setToolTip("")
        self.xticks_rotation_sbox.setDecimals(1)
        self.xticks_rotation_sbox.setMinimum(0.0)
        self.xticks_rotation_sbox.setMaximum(360.0)
        self.xticks_rotation_sbox.setSingleStep(0.5)
        self.xticks_rotation_sbox.setObjectName("xticks_rotation_sbox")
        self.horizontalLayout_18.addWidget(self.xticks_rotation_sbox)
        self.label_61 = QtWidgets.QLabel(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.horizontalLayout_18.addWidget(self.label_61)
        self.yticks_rotation_sbox = QtWidgets.QDoubleSpinBox(self.style_tab)
        self.yticks_rotation_sbox.setDecimals(1)
        self.yticks_rotation_sbox.setMaximum(360.0)
        self.yticks_rotation_sbox.setSingleStep(0.5)
        self.yticks_rotation_sbox.setObjectName("yticks_rotation_sbox")
        self.horizontalLayout_18.addWidget(self.yticks_rotation_sbox)
        self.gridLayout_7.addLayout(self.horizontalLayout_18, 3, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.style_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.enable_mathtext_chkbox = QtWidgets.QCheckBox(self.style_tab)
        self.enable_mathtext_chkbox.setObjectName("enable_mathtext_chkbox")
        self.horizontalLayout_9.addWidget(self.enable_mathtext_chkbox)
        self.line = QtWidgets.QFrame(self.style_tab)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout_9.addWidget(self.line)
        self.label_38 = QtWidgets.QLabel(self.style_tab)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_9.addWidget(self.label_38)
        self.xtick_formatter_cbb = QtWidgets.QComboBox(self.style_tab)
        self.xtick_formatter_cbb.setObjectName("xtick_formatter_cbb")
        self.xtick_formatter_cbb.addItem("")
        self.xtick_formatter_cbb.addItem("")
        self.horizontalLayout_9.addWidget(self.xtick_formatter_cbb)
        self.xtick_funcformatter_lineEdit = QtWidgets.QLineEdit(self.style_tab)
        self.xtick_funcformatter_lineEdit.setEnabled(False)
        self.xtick_funcformatter_lineEdit.setPlaceholderText("")
        self.xtick_funcformatter_lineEdit.setObjectName(
            "xtick_funcformatter_lineEdit")
        self.horizontalLayout_9.addWidget(self.xtick_funcformatter_lineEdit)
        self.label_39 = QtWidgets.QLabel(self.style_tab)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_9.addWidget(self.label_39)
        self.ytick_formatter_cbb = QtWidgets.QComboBox(self.style_tab)
        self.ytick_formatter_cbb.setObjectName("ytick_formatter_cbb")
        self.ytick_formatter_cbb.addItem("")
        self.ytick_formatter_cbb.addItem("")
        self.horizontalLayout_9.addWidget(self.ytick_formatter_cbb)
        self.ytick_funcformatter_lineEdit = QtWidgets.QLineEdit(self.style_tab)
        self.ytick_funcformatter_lineEdit.setEnabled(False)
        self.ytick_funcformatter_lineEdit.setPlaceholderText("")
        self.ytick_funcformatter_lineEdit.setObjectName(
            "ytick_funcformatter_lineEdit")
        self.horizontalLayout_9.addWidget(self.ytick_funcformatter_lineEdit)
        self.gridLayout_7.addLayout(self.horizontalLayout_9, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.style_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.style_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 2, 0, 3, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ticks_hide_chkbox = QtWidgets.QCheckBox(self.style_tab)
        self.ticks_hide_chkbox.setObjectName("ticks_hide_chkbox")
        self.horizontalLayout_7.addWidget(self.ticks_hide_chkbox)
        self.mticks_chkbox = QtWidgets.QCheckBox(self.style_tab)
        self.mticks_chkbox.setObjectName("mticks_chkbox")
        self.horizontalLayout_7.addWidget(self.mticks_chkbox)
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
        self.horizontalLayout_7.addWidget(self.xy_ticks_sample_lbl)
        self.xy_ticks_font_btn = QtWidgets.QToolButton(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xy_ticks_font_btn.sizePolicy().hasHeightForWidth())
        self.xy_ticks_font_btn.setSizePolicy(sizePolicy)
        self.xy_ticks_font_btn.setIcon(icon)
        self.xy_ticks_font_btn.setIconSize(QtCore.QSize(24, 24))
        self.xy_ticks_font_btn.setAutoRaise(True)
        self.xy_ticks_font_btn.setObjectName("xy_ticks_font_btn")
        self.horizontalLayout_7.addWidget(self.xy_ticks_font_btn)
        self.gridLayout_7.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tightLayout_chkbox = QtWidgets.QCheckBox(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tightLayout_chkbox.sizePolicy().hasHeightForWidth())
        self.tightLayout_chkbox.setSizePolicy(sizePolicy)
        self.tightLayout_chkbox.setObjectName("tightLayout_chkbox")
        self.horizontalLayout_8.addWidget(self.tightLayout_chkbox)
        self.gridon_chkbox = QtWidgets.QCheckBox(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gridon_chkbox.sizePolicy().hasHeightForWidth())
        self.gridon_chkbox.setSizePolicy(sizePolicy)
        self.gridon_chkbox.setObjectName("gridon_chkbox")
        self.horizontalLayout_8.addWidget(self.gridon_chkbox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.gridLayout_7.addLayout(self.horizontalLayout_8, 5, 1, 1, 1)
        self.border_style_hbox = QtWidgets.QHBoxLayout()
        self.border_style_hbox.setSpacing(4)
        self.border_style_hbox.setObjectName("border_style_hbox")
        self.border_hide_chkbox = QtWidgets.QCheckBox(self.style_tab)
        self.border_hide_chkbox.setObjectName("border_hide_chkbox")
        self.border_style_hbox.addWidget(self.border_hide_chkbox)
        self.line_2 = QtWidgets.QFrame(self.style_tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.border_style_hbox.addWidget(self.line_2)
        self.label_67 = QtWidgets.QLabel(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy)
        self.label_67.setObjectName("label_67")
        self.border_style_hbox.addWidget(self.label_67)
        self.border_color_btn = QtWidgets.QToolButton(self.style_tab)
        self.border_color_btn.setToolTip("")
        self.border_color_btn.setStyleSheet("")
        self.border_color_btn.setText("")
        self.border_color_btn.setIconSize(QtCore.QSize(20, 20))
        self.border_color_btn.setObjectName("border_color_btn")
        self.border_style_hbox.addWidget(self.border_color_btn)
        self.label_65 = QtWidgets.QLabel(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy)
        self.label_65.setObjectName("label_65")
        self.border_style_hbox.addWidget(self.label_65)
        self.border_lw_sbox = QtWidgets.QDoubleSpinBox(self.style_tab)
        self.border_lw_sbox.setDecimals(1)
        self.border_lw_sbox.setMaximum(10.0)
        self.border_lw_sbox.setSingleStep(0.1)
        self.border_lw_sbox.setObjectName("border_lw_sbox")
        self.border_style_hbox.addWidget(self.border_lw_sbox)
        self.label_68 = QtWidgets.QLabel(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy)
        self.label_68.setObjectName("label_68")
        self.border_style_hbox.addWidget(self.label_68)
        self.border_ls_cbb = QtWidgets.QComboBox(self.style_tab)
        self.border_ls_cbb.setSizeAdjustPolicy(
            QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.border_ls_cbb.setObjectName("border_ls_cbb")
        self.border_ls_cbb.addItem("")
        self.border_ls_cbb.addItem("")
        self.border_ls_cbb.addItem("")
        self.border_ls_cbb.addItem("")
        self.border_style_hbox.addWidget(self.border_ls_cbb)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.border_style_hbox.addItem(spacerItem3)
        self.gridLayout_7.addLayout(self.border_style_hbox, 6, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_62 = QtWidgets.QLabel(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy)
        self.label_62.setObjectName("label_62")
        self.horizontalLayout_6.addWidget(self.label_62)
        self.bkgd_color_btn = QtWidgets.QToolButton(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bkgd_color_btn.sizePolicy().hasHeightForWidth())
        self.bkgd_color_btn.setSizePolicy(sizePolicy)
        self.bkgd_color_btn.setText("")
        self.bkgd_color_btn.setAutoRaise(False)
        self.bkgd_color_btn.setObjectName("bkgd_color_btn")
        self.horizontalLayout_6.addWidget(self.bkgd_color_btn)
        self.label_63 = QtWidgets.QLabel(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy)
        self.label_63.setObjectName("label_63")
        self.horizontalLayout_6.addWidget(self.label_63)
        self.ticks_color_btn = QtWidgets.QToolButton(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ticks_color_btn.sizePolicy().hasHeightForWidth())
        self.ticks_color_btn.setSizePolicy(sizePolicy)
        self.ticks_color_btn.setText("")
        self.ticks_color_btn.setIconSize(QtCore.QSize(20, 20))
        self.ticks_color_btn.setObjectName("ticks_color_btn")
        self.horizontalLayout_6.addWidget(self.ticks_color_btn)
        self.label_64 = QtWidgets.QLabel(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy)
        self.label_64.setObjectName("label_64")
        self.horizontalLayout_6.addWidget(self.label_64)
        self.grid_color_btn = QtWidgets.QToolButton(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.grid_color_btn.sizePolicy().hasHeightForWidth())
        self.grid_color_btn.setSizePolicy(sizePolicy)
        self.grid_color_btn.setText("")
        self.grid_color_btn.setIconSize(QtCore.QSize(20, 20))
        self.grid_color_btn.setAutoRaise(False)
        self.grid_color_btn.setObjectName("grid_color_btn")
        self.horizontalLayout_6.addWidget(self.grid_color_btn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.gridLayout_7.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.style_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_66.setFont(font)
        self.label_66.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_66.setObjectName("label_66")
        self.gridLayout_7.addWidget(self.label_66, 6, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem5, 7, 1, 1, 1)
        self.config_tabWidget.addTab(self.style_tab, "")
        self.cross_tab = QtWidgets.QWidget()
        self.cross_tab.setObjectName("cross_tab")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.cross_tab)
        self.gridLayout_27.setContentsMargins(6, 12, 6, 6)
        self.gridLayout_27.setSpacing(4)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.label_173 = QtWidgets.QLabel(self.cross_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_173.setFont(font)
        self.label_173.setAlignment(QtCore.Qt.AlignRight
                                    | QtCore.Qt.AlignTrailing
                                    | QtCore.Qt.AlignVCenter)
        self.label_173.setObjectName("label_173")
        self.gridLayout_27.addWidget(self.label_173, 0, 0, 1, 1)
        self.cross_hide_chkbox = QtWidgets.QCheckBox(self.cross_tab)
        self.cross_hide_chkbox.setTristate(True)
        self.cross_hide_chkbox.setObjectName("cross_hide_chkbox")
        self.gridLayout_27.addWidget(self.cross_hide_chkbox, 0, 5, 1, 1)
        self.label_164 = QtWidgets.QLabel(self.cross_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_164.setFont(font)
        self.label_164.setAlignment(QtCore.Qt.AlignRight
                                    | QtCore.Qt.AlignTrailing
                                    | QtCore.Qt.AlignVCenter)
        self.label_164.setObjectName("label_164")
        self.gridLayout_27.addWidget(self.label_164, 1, 0, 1, 1)
        self.gridLayout_26 = QtWidgets.QGridLayout()
        self.gridLayout_26.setSpacing(4)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.cross_mk_style_cbb = QtWidgets.QComboBox(self.cross_tab)
        self.cross_mk_style_cbb.setObjectName("cross_mk_style_cbb")
        self.gridLayout_26.addWidget(self.cross_mk_style_cbb, 1, 1, 1, 1)
        self.cross_mk_facecolor_btn = QtWidgets.QToolButton(self.cross_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cross_mk_facecolor_btn.sizePolicy().hasHeightForWidth())
        self.cross_mk_facecolor_btn.setSizePolicy(sizePolicy)
        self.cross_mk_facecolor_btn.setToolTip("")
        self.cross_mk_facecolor_btn.setText("")
        self.cross_mk_facecolor_btn.setObjectName("cross_mk_facecolor_btn")
        self.gridLayout_26.addWidget(self.cross_mk_facecolor_btn, 1, 3, 1, 1)
        self.cross_mk_width_lineEdit = QtWidgets.QLineEdit(self.cross_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cross_mk_width_lineEdit.sizePolicy().hasHeightForWidth())
        self.cross_mk_width_lineEdit.setSizePolicy(sizePolicy)
        self.cross_mk_width_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.cross_mk_width_lineEdit.setObjectName("cross_mk_width_lineEdit")
        self.gridLayout_26.addWidget(self.cross_mk_width_lineEdit, 1, 9, 1, 1)
        self.label_169 = QtWidgets.QLabel(self.cross_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_169.sizePolicy().hasHeightForWidth())
        self.label_169.setSizePolicy(sizePolicy)
        self.label_169.setObjectName("label_169")
        self.gridLayout_26.addWidget(self.label_169, 0, 2, 1, 1)
        self.label_170 = QtWidgets.QLabel(self.cross_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_170.sizePolicy().hasHeightForWidth())
        self.label_170.setSizePolicy(sizePolicy)
        self.label_170.setObjectName("label_170")
        self.gridLayout_26.addWidget(self.label_170, 1, 0, 1, 1)
        self.label_166 = QtWidgets.QLabel(self.cross_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_166.sizePolicy().hasHeightForWidth())
        self.label_166.setSizePolicy(sizePolicy)
        self.label_166.setAlignment(QtCore.Qt.AlignRight
                                    | QtCore.Qt.AlignTrailing
                                    | QtCore.Qt.AlignVCenter)
        self.label_166.setObjectName("label_166")
        self.gridLayout_26.addWidget(self.label_166, 1, 6, 1, 1)
        self.cross_line_color_btn = QtWidgets.QToolButton(self.cross_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cross_line_color_btn.sizePolicy().hasHeightForWidth())
        self.cross_line_color_btn.setSizePolicy(sizePolicy)
        self.cross_line_color_btn.setText("")
        self.cross_line_color_btn.setObjectName("cross_line_color_btn")
        self.gridLayout_26.addWidget(self.cross_line_color_btn, 0, 3, 1, 1)
        self.cross_mk_edgecolor_btn = QtWidgets.QToolButton(self.cross_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cross_mk_edgecolor_btn.sizePolicy().hasHeightForWidth())
        self.cross_mk_edgecolor_btn.setSizePolicy(sizePolicy)
        self.cross_mk_edgecolor_btn.setText("")
        self.cross_mk_edgecolor_btn.setObjectName("cross_mk_edgecolor_btn")
        self.gridLayout_26.addWidget(self.cross_mk_edgecolor_btn, 1, 5, 1, 1)
        self.label_165 = QtWidgets.QLabel(self.cross_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_165.sizePolicy().hasHeightForWidth())
        self.label_165.setSizePolicy(sizePolicy)
        self.label_165.setObjectName("label_165")
        self.gridLayout_26.addWidget(self.label_165, 1, 8, 1, 1)
        self.label_167 = QtWidgets.QLabel(self.cross_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_167.sizePolicy().hasHeightForWidth())
        self.label_167.setSizePolicy(sizePolicy)
        self.label_167.setObjectName("label_167")
        self.gridLayout_26.addWidget(self.label_167, 0, 8, 1, 1)
        self.label_171 = QtWidgets.QLabel(self.cross_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_171.sizePolicy().hasHeightForWidth())
        self.label_171.setSizePolicy(sizePolicy)
        self.label_171.setObjectName("label_171")
        self.gridLayout_26.addWidget(self.label_171, 1, 2, 1, 1)
        self.label_172 = QtWidgets.QLabel(self.cross_tab)
        self.label_172.setObjectName("label_172")
        self.gridLayout_26.addWidget(self.label_172, 1, 4, 1, 1)
        self.label_168 = QtWidgets.QLabel(self.cross_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_168.sizePolicy().hasHeightForWidth())
        self.label_168.setSizePolicy(sizePolicy)
        self.label_168.setObjectName("label_168")
        self.gridLayout_26.addWidget(self.label_168, 0, 0, 1, 1)
        self.cross_line_style_cbb = QtWidgets.QComboBox(self.cross_tab)
        self.cross_line_style_cbb.setSizeAdjustPolicy(
            QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.cross_line_style_cbb.setObjectName("cross_line_style_cbb")
        self.cross_line_style_cbb.addItem("")
        self.cross_line_style_cbb.addItem("")
        self.cross_line_style_cbb.addItem("")
        self.cross_line_style_cbb.addItem("")
        self.cross_line_style_cbb.addItem("")
        self.gridLayout_26.addWidget(self.cross_line_style_cbb, 0, 1, 1, 1)
        self.cross_mk_size_lineEdit = QtWidgets.QLineEdit(self.cross_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cross_mk_size_lineEdit.sizePolicy().hasHeightForWidth())
        self.cross_mk_size_lineEdit.setSizePolicy(sizePolicy)
        self.cross_mk_size_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.cross_mk_size_lineEdit.setObjectName("cross_mk_size_lineEdit")
        self.gridLayout_26.addWidget(self.cross_mk_size_lineEdit, 1, 7, 1, 1)
        self.cross_line_width_lineEdit = QtWidgets.QLineEdit(self.cross_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cross_line_width_lineEdit.sizePolicy().hasHeightForWidth())
        self.cross_line_width_lineEdit.setSizePolicy(sizePolicy)
        self.cross_line_width_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.cross_line_width_lineEdit.setObjectName(
            "cross_line_width_lineEdit")
        self.gridLayout_26.addWidget(self.cross_line_width_lineEdit, 0, 9, 1,
                                     1)
        self.cross_line_hide_chkbox = QtWidgets.QCheckBox(self.cross_tab)
        self.cross_line_hide_chkbox.setObjectName("cross_line_hide_chkbox")
        self.gridLayout_26.addWidget(self.cross_line_hide_chkbox, 0, 10, 1, 1)
        self.cross_mk_hide_chkbox = QtWidgets.QCheckBox(self.cross_tab)
        self.cross_mk_hide_chkbox.setObjectName("cross_mk_hide_chkbox")
        self.gridLayout_26.addWidget(self.cross_mk_hide_chkbox, 1, 10, 1, 1)
        self.gridLayout_27.addLayout(self.gridLayout_26, 1, 1, 2, 5)
        self.label_163 = QtWidgets.QLabel(self.cross_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_163.setFont(font)
        self.label_163.setAlignment(QtCore.Qt.AlignRight
                                    | QtCore.Qt.AlignTrailing
                                    | QtCore.Qt.AlignVCenter)
        self.label_163.setObjectName("label_163")
        self.gridLayout_27.addWidget(self.label_163, 2, 0, 1, 1)
        self.label_174 = QtWidgets.QLabel(self.cross_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_174.setFont(font)
        self.label_174.setAlignment(QtCore.Qt.AlignRight
                                    | QtCore.Qt.AlignTrailing
                                    | QtCore.Qt.AlignVCenter)
        self.label_174.setObjectName("label_174")
        self.gridLayout_27.addWidget(self.label_174, 3, 0, 1, 1)
        self.cross_rename_chkbox = QtWidgets.QCheckBox(self.cross_tab)
        self.cross_rename_chkbox.setObjectName("cross_rename_chkbox")
        self.gridLayout_27.addWidget(self.cross_rename_chkbox, 3, 1, 1, 1)
        self.cross_literal_name_lineEdit = QtWidgets.QLineEdit(self.cross_tab)
        self.cross_literal_name_lineEdit.setEnabled(False)
        self.cross_literal_name_lineEdit.setObjectName(
            "cross_literal_name_lineEdit")
        self.gridLayout_27.addWidget(self.cross_literal_name_lineEdit, 3, 2, 1,
                                     1)
        self.label_176 = QtWidgets.QLabel(self.cross_tab)
        self.label_176.setObjectName("label_176")
        self.gridLayout_27.addWidget(self.label_176, 3, 3, 1, 1)
        self.cross_text_color_btn = QtWidgets.QToolButton(self.cross_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cross_text_color_btn.sizePolicy().hasHeightForWidth())
        self.cross_text_color_btn.setSizePolicy(sizePolicy)
        self.cross_text_color_btn.setText("")
        self.cross_text_color_btn.setObjectName("cross_text_color_btn")
        self.gridLayout_27.addWidget(self.cross_text_color_btn, 3, 4, 1, 1)
        self.cross_text_hide_chkbox = QtWidgets.QCheckBox(self.cross_tab)
        self.cross_text_hide_chkbox.setObjectName("cross_text_hide_chkbox")
        self.gridLayout_27.addWidget(self.cross_text_hide_chkbox, 3, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_27.addItem(spacerItem6, 4, 1, 1, 1)
        self.cross_cbb = QtWidgets.QComboBox(self.cross_tab)
        self.cross_cbb.setObjectName("cross_cbb")
        self.gridLayout_27.addWidget(self.cross_cbb, 0, 1, 1, 4)
        self.config_tabWidget.addTab(self.cross_tab, "")
        self.curve_tab = QtWidgets.QWidget()
        self.curve_tab.setObjectName("curve_tab")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.curve_tab)
        self.gridLayout_12.setContentsMargins(6, 12, 6, 6)
        self.gridLayout_12.setSpacing(4)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(4)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.line_id_cbb = QtWidgets.QComboBox(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line_id_cbb.sizePolicy().hasHeightForWidth())
        self.line_id_cbb.setSizePolicy(sizePolicy)
        self.line_id_cbb.setObjectName("line_id_cbb")
        self.horizontalLayout_12.addWidget(self.line_id_cbb)
        self.line_hide_chkbox = QtWidgets.QCheckBox(self.curve_tab)
        self.line_hide_chkbox.setObjectName("line_hide_chkbox")
        self.horizontalLayout_12.addWidget(self.line_hide_chkbox)
        self.gridLayout_12.addLayout(self.horizontalLayout_12, 0, 1, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem7, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.curve_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_12.addWidget(self.label_3, 2, 0, 1, 1)
        self.opacity_val_slider = QtWidgets.QSlider(self.curve_tab)
        self.opacity_val_slider.setStyleSheet(
            "QSlider::groove:horizontal {\n"
            "border: 1px solid #bbb;\n"
            "background: white;\n"
            "height: 12px;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::sub-page:horizontal {\n"
            "background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
            "    stop: 0 #F57900, stop: 1 #FCAF3E);\n"
            "background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
            "    stop: 0 #FCAF3E, stop: 1 #F57900);\n"
            "border: 1px solid #777;\n"
            "height: 10px;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::add-page:horizontal {\n"
            "background: #fff;\n"
            "border: 1px solid #777;\n"
            "height: 10px;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal {\n"
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
            "    stop:0 #eee, stop:1 #ccc);\n"
            "border: 1px solid #777;\n"
            "width: 15px;\n"
            "margin-top: -2px;\n"
            "margin-bottom: -2px;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal:hover {\n"
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
            "    stop:0 #fff, stop:1 #ddd);\n"
            "border: 1px solid #444;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::sub-page:horizontal:disabled {\n"
            "background: #bbb;\n"
            "border-color: #999;\n"
            "}\n"
            "\n"
            "QSlider::add-page:horizontal:disabled {\n"
            "background: #eee;\n"
            "border-color: #999;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal:disabled {\n"
            "background: #eee;\n"
            "border: 1px solid #aaa;\n"
            "border-radius: 4px;\n"
            "}")
        self.opacity_val_slider.setMaximum(100)
        self.opacity_val_slider.setProperty("value", 100)
        self.opacity_val_slider.setOrientation(QtCore.Qt.Horizontal)
        self.opacity_val_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.opacity_val_slider.setObjectName("opacity_val_slider")
        self.gridLayout_12.addWidget(self.opacity_val_slider, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.curve_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_12.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.curve_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_12.addWidget(self.label_26, 4, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.curve_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_12.addWidget(self.label_23, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.curve_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight
                                  | QtCore.Qt.AlignTrailing
                                  | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_12.addWidget(self.label_4, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.mk_edgecolor_btn = QtWidgets.QToolButton(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mk_edgecolor_btn.sizePolicy().hasHeightForWidth())
        self.mk_edgecolor_btn.setSizePolicy(sizePolicy)
        self.mk_edgecolor_btn.setText("")
        self.mk_edgecolor_btn.setIconSize(QtCore.QSize(20, 20))
        self.mk_edgecolor_btn.setObjectName("mk_edgecolor_btn")
        self.gridLayout.addWidget(self.mk_edgecolor_btn, 1, 5, 1, 1)
        self.line_color_btn = QtWidgets.QToolButton(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line_color_btn.sizePolicy().hasHeightForWidth())
        self.line_color_btn.setSizePolicy(sizePolicy)
        self.line_color_btn.setText("")
        self.line_color_btn.setIconSize(QtCore.QSize(20, 20))
        self.line_color_btn.setObjectName("line_color_btn")
        self.gridLayout.addWidget(self.line_color_btn, 0, 3, 1, 1)
        self.mk_style_cbb = QtWidgets.QComboBox(self.curve_tab)
        self.mk_style_cbb.setObjectName("mk_style_cbb")
        self.gridLayout.addWidget(self.mk_style_cbb, 1, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 1, 8, 1, 1)
        self.line_width_lineEdit = QtWidgets.QLineEdit(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line_width_lineEdit.sizePolicy().hasHeightForWidth())
        self.line_width_lineEdit.setSizePolicy(sizePolicy)
        self.line_width_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.line_width_lineEdit.setObjectName("line_width_lineEdit")
        self.gridLayout.addWidget(self.line_width_lineEdit, 0, 9, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 1, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 8, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.line_style_cbb = QtWidgets.QComboBox(self.curve_tab)
        self.line_style_cbb.setSizeAdjustPolicy(
            QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.line_style_cbb.setObjectName("line_style_cbb")
        self.line_style_cbb.addItem("")
        self.line_style_cbb.addItem("")
        self.line_style_cbb.addItem("")
        self.line_style_cbb.addItem("")
        self.line_style_cbb.addItem("")
        self.gridLayout.addWidget(self.line_style_cbb, 0, 1, 1, 1)
        self.mk_size_lineEdit = QtWidgets.QLineEdit(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mk_size_lineEdit.sizePolicy().hasHeightForWidth())
        self.mk_size_lineEdit.setSizePolicy(sizePolicy)
        self.mk_size_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.mk_size_lineEdit.setObjectName("mk_size_lineEdit")
        self.gridLayout.addWidget(self.mk_size_lineEdit, 1, 7, 1, 1)
        self.mk_width_lineEdit = QtWidgets.QLineEdit(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mk_width_lineEdit.sizePolicy().hasHeightForWidth())
        self.mk_width_lineEdit.setSizePolicy(sizePolicy)
        self.mk_width_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.mk_width_lineEdit.setObjectName("mk_width_lineEdit")
        self.gridLayout.addWidget(self.mk_width_lineEdit, 1, 9, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 1, 2, 1, 1)
        self.mk_facecolor_btn = QtWidgets.QToolButton(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mk_facecolor_btn.sizePolicy().hasHeightForWidth())
        self.mk_facecolor_btn.setSizePolicy(sizePolicy)
        self.mk_facecolor_btn.setToolTip("")
        self.mk_facecolor_btn.setText("")
        self.mk_facecolor_btn.setIconSize(QtCore.QSize(20, 20))
        self.mk_facecolor_btn.setObjectName("mk_facecolor_btn")
        self.gridLayout.addWidget(self.mk_facecolor_btn, 1, 3, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.curve_tab)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 1, 4, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.curve_tab)
        self.label_70.setObjectName("label_70")
        self.gridLayout.addWidget(self.label_70, 0, 4, 1, 1)
        self.line_ds_cbb = QtWidgets.QComboBox(self.curve_tab)
        self.line_ds_cbb.setObjectName("line_ds_cbb")
        self.line_ds_cbb.addItem("")
        self.line_ds_cbb.addItem("")
        self.line_ds_cbb.addItem("")
        self.line_ds_cbb.addItem("")
        self.gridLayout.addWidget(self.line_ds_cbb, 0, 5, 1, 2)
        self.gridLayout_12.addLayout(self.gridLayout, 2, 1, 2, 2)
        self.opacity_val_lbl = QtWidgets.QLabel(self.curve_tab)
        self.opacity_val_lbl.setAlignment(QtCore.Qt.AlignRight
                                          | QtCore.Qt.AlignTrailing
                                          | QtCore.Qt.AlignVCenter)
        self.opacity_val_lbl.setObjectName("opacity_val_lbl")
        self.gridLayout_12.addWidget(self.opacity_val_lbl, 4, 2, 1, 1)
        self.line_label_lineEdit = QtWidgets.QLineEdit(self.curve_tab)
        self.line_label_lineEdit.setObjectName("line_label_lineEdit")
        self.gridLayout_12.addWidget(self.line_label_lineEdit, 1, 1, 1, 2)
        self.config_tabWidget.addTab(self.curve_tab, "")
        self.eb_tab = QtWidgets.QWidget()
        self.eb_tab.setObjectName("eb_tab")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.eb_tab)
        self.gridLayout_13.setContentsMargins(6, 12, 6, 6)
        self.gridLayout_13.setSpacing(4)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_36 = QtWidgets.QLabel(self.eb_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_13.addWidget(self.label_36, 0, 0, 1, 1)
        self.eb_line_hide_chkbox = QtWidgets.QCheckBox(self.eb_tab)
        self.eb_line_hide_chkbox.setObjectName("eb_line_hide_chkbox")
        self.gridLayout_13.addWidget(self.eb_line_hide_chkbox, 0, 2, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_13.addWidget(self.label_30, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_33 = QtWidgets.QLabel(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 1, 0, 1, 1)
        self.eb_mk_facecolor_btn = QtWidgets.QToolButton(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.eb_mk_facecolor_btn.sizePolicy().hasHeightForWidth())
        self.eb_mk_facecolor_btn.setSizePolicy(sizePolicy)
        self.eb_mk_facecolor_btn.setText("")
        self.eb_mk_facecolor_btn.setIconSize(QtCore.QSize(20, 20))
        self.eb_mk_facecolor_btn.setObjectName("eb_mk_facecolor_btn")
        self.gridLayout_2.addWidget(self.eb_mk_facecolor_btn, 1, 3, 1, 1)
        self.label_79 = QtWidgets.QLabel(self.eb_tab)
        self.label_79.setObjectName("label_79")
        self.gridLayout_2.addWidget(self.label_79, 2, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 0, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setObjectName("label_35")
        self.gridLayout_2.addWidget(self.label_35, 1, 2, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 0, 8, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 1, 6, 1, 1)
        self.eb_line_width_lineEdit = QtWidgets.QLineEdit(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.eb_line_width_lineEdit.sizePolicy().hasHeightForWidth())
        self.eb_line_width_lineEdit.setSizePolicy(sizePolicy)
        self.eb_line_width_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.eb_line_width_lineEdit.setObjectName("eb_line_width_lineEdit")
        self.gridLayout_2.addWidget(self.eb_line_width_lineEdit, 0, 9, 1, 1)
        self.xeb_mk_style_cbb = QtWidgets.QComboBox(self.eb_tab)
        self.xeb_mk_style_cbb.setObjectName("xeb_mk_style_cbb")
        self.gridLayout_2.addWidget(self.xeb_mk_style_cbb, 2, 1, 1, 1)
        self.eb_mk_size_lineEdit = QtWidgets.QLineEdit(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.eb_mk_size_lineEdit.sizePolicy().hasHeightForWidth())
        self.eb_mk_size_lineEdit.setSizePolicy(sizePolicy)
        self.eb_mk_size_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.eb_mk_size_lineEdit.setObjectName("eb_mk_size_lineEdit")
        self.gridLayout_2.addWidget(self.eb_mk_size_lineEdit, 1, 7, 1, 1)
        self.eb_line_style_cbb = QtWidgets.QComboBox(self.eb_tab)
        self.eb_line_style_cbb.setSizeAdjustPolicy(
            QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.eb_line_style_cbb.setObjectName("eb_line_style_cbb")
        self.eb_line_style_cbb.addItem("")
        self.eb_line_style_cbb.addItem("")
        self.eb_line_style_cbb.addItem("")
        self.eb_line_style_cbb.addItem("")
        self.eb_line_style_cbb.addItem("")
        self.gridLayout_2.addWidget(self.eb_line_style_cbb, 0, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 0, 2, 1, 1)
        self.eb_mk_width_lineEdit = QtWidgets.QLineEdit(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.eb_mk_width_lineEdit.sizePolicy().hasHeightForWidth())
        self.eb_mk_width_lineEdit.setSizePolicy(sizePolicy)
        self.eb_mk_width_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.eb_mk_width_lineEdit.setObjectName("eb_mk_width_lineEdit")
        self.gridLayout_2.addWidget(self.eb_mk_width_lineEdit, 1, 9, 1, 1)
        self.yeb_mk_style_cbb = QtWidgets.QComboBox(self.eb_tab)
        self.yeb_mk_style_cbb.setObjectName("yeb_mk_style_cbb")
        self.gridLayout_2.addWidget(self.yeb_mk_style_cbb, 1, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 1, 8, 1, 1)
        self.eb_line_color_btn = QtWidgets.QToolButton(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.eb_line_color_btn.sizePolicy().hasHeightForWidth())
        self.eb_line_color_btn.setSizePolicy(sizePolicy)
        self.eb_line_color_btn.setText("")
        self.eb_line_color_btn.setIconSize(QtCore.QSize(20, 20))
        self.eb_line_color_btn.setObjectName("eb_line_color_btn")
        self.gridLayout_2.addWidget(self.eb_line_color_btn, 0, 3, 1, 1)
        self.eb_mk_edgecolor_btn = QtWidgets.QToolButton(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.eb_mk_edgecolor_btn.sizePolicy().hasHeightForWidth())
        self.eb_mk_edgecolor_btn.setSizePolicy(sizePolicy)
        self.eb_mk_edgecolor_btn.setText("")
        self.eb_mk_edgecolor_btn.setIconSize(QtCore.QSize(20, 20))
        self.eb_mk_edgecolor_btn.setObjectName("eb_mk_edgecolor_btn")
        self.gridLayout_2.addWidget(self.eb_mk_edgecolor_btn, 1, 5, 1, 1)
        self.label_81 = QtWidgets.QLabel(self.eb_tab)
        self.label_81.setObjectName("label_81")
        self.gridLayout_2.addWidget(self.label_81, 1, 4, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_2, 1, 1, 3, 2)
        self.label_28 = QtWidgets.QLabel(self.eb_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_13.addWidget(self.label_28, 2, 0, 1, 1)
        self.label_80 = QtWidgets.QLabel(self.eb_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_80.setObjectName("label_80")
        self.gridLayout_13.addWidget(self.label_80, 3, 0, 1, 1)
        self.eb_line_id_cbb = QtWidgets.QComboBox(self.eb_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.eb_line_id_cbb.sizePolicy().hasHeightForWidth())
        self.eb_line_id_cbb.setSizePolicy(sizePolicy)
        self.eb_line_id_cbb.setObjectName("eb_line_id_cbb")
        self.gridLayout_13.addWidget(self.eb_line_id_cbb, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem8, 4, 1, 1, 1)
        self.config_tabWidget.addTab(self.eb_tab, "")
        self.image_tab = QtWidgets.QWidget()
        self.image_tab.setObjectName("image_tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.image_tab)
        self.gridLayout_8.setContentsMargins(6, 12, 6, 6)
        self.gridLayout_8.setSpacing(4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_47 = QtWidgets.QLabel(self.image_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.gridLayout_8.addWidget(self.label_47, 2, 0, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSpacing(4)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.cmap_class_cbb = QtWidgets.QComboBox(self.image_tab)
        self.cmap_class_cbb.setObjectName("cmap_class_cbb")
        self.horizontalLayout_16.addWidget(self.cmap_class_cbb)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(4)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.cmap_cbb = QtWidgets.QComboBox(self.image_tab)
        self.cmap_cbb.setObjectName("cmap_cbb")
        self.horizontalLayout_15.addWidget(self.cmap_cbb)
        self.add_to_fav_btn = QtWidgets.QToolButton(self.image_tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/add.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.add_to_fav_btn.setIcon(icon1)
        self.add_to_fav_btn.setAutoRaise(False)
        self.add_to_fav_btn.setObjectName("add_to_fav_btn")
        self.horizontalLayout_15.addWidget(self.add_to_fav_btn)
        self.del_from_fav_btn = QtWidgets.QToolButton(self.image_tab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/del.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.del_from_fav_btn.setIcon(icon2)
        self.del_from_fav_btn.setAutoRaise(False)
        self.del_from_fav_btn.setObjectName("del_from_fav_btn")
        self.horizontalLayout_15.addWidget(self.del_from_fav_btn)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_15)
        self.reverse_cmap_chkbox = QtWidgets.QCheckBox(self.image_tab)
        self.reverse_cmap_chkbox.setObjectName("reverse_cmap_chkbox")
        self.horizontalLayout_16.addWidget(self.reverse_cmap_chkbox)
        self.cm_image = MatplotlibCMapWidget(self.image_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cm_image.sizePolicy().hasHeightForWidth())
        self.cm_image.setSizePolicy(sizePolicy)
        self.cm_image.setObjectName("cm_image")
        self.horizontalLayout_16.addWidget(self.cm_image)
        self.gridLayout_8.addLayout(self.horizontalLayout_16, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.auto_clim_chkbox = QtWidgets.QCheckBox(self.image_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.auto_clim_chkbox.sizePolicy().hasHeightForWidth())
        self.auto_clim_chkbox.setSizePolicy(sizePolicy)
        self.auto_clim_chkbox.setObjectName("auto_clim_chkbox")
        self.horizontalLayout_4.addWidget(self.auto_clim_chkbox)
        self.cr_reset_tbtn = QtWidgets.QToolButton(self.image_tab)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/reset_btn.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cr_reset_tbtn.setIcon(icon3)
        self.cr_reset_tbtn.setAutoRaise(False)
        self.cr_reset_tbtn.setObjectName("cr_reset_tbtn")
        self.horizontalLayout_4.addWidget(self.cr_reset_tbtn)
        self.label_45 = QtWidgets.QLabel(self.image_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy)
        self.label_45.setObjectName("label_45")
        self.horizontalLayout_4.addWidget(self.label_45)
        self.cr_min_dSpinBox = QtWidgets.QDoubleSpinBox(self.image_tab)
        self.cr_min_dSpinBox.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.cr_min_dSpinBox.setProperty("showGroupSeparator", False)
        self.cr_min_dSpinBox.setDecimals(3)
        self.cr_min_dSpinBox.setMinimum(-999.0)
        self.cr_min_dSpinBox.setMaximum(999.0)
        self.cr_min_dSpinBox.setObjectName("cr_min_dSpinBox")
        self.horizontalLayout_4.addWidget(self.cr_min_dSpinBox)
        self.label_46 = QtWidgets.QLabel(self.image_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy)
        self.label_46.setObjectName("label_46")
        self.horizontalLayout_4.addWidget(self.label_46)
        self.cr_max_dSpinBox = QtWidgets.QDoubleSpinBox(self.image_tab)
        self.cr_max_dSpinBox.setDecimals(3)
        self.cr_max_dSpinBox.setMinimum(-999.0)
        self.cr_max_dSpinBox.setMaximum(999.0)
        self.cr_max_dSpinBox.setObjectName("cr_max_dSpinBox")
        self.horizontalLayout_4.addWidget(self.cr_max_dSpinBox)
        self.gridLayout_8.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setSpacing(4)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.show_colorbar_chkbox = QtWidgets.QCheckBox(self.image_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.show_colorbar_chkbox.sizePolicy().hasHeightForWidth())
        self.show_colorbar_chkbox.setSizePolicy(sizePolicy)
        self.show_colorbar_chkbox.setObjectName("show_colorbar_chkbox")
        self.horizontalLayout_17.addWidget(self.show_colorbar_chkbox)
        self.cb_orientation_lbl = QtWidgets.QLabel(self.image_tab)
        self.cb_orientation_lbl.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cb_orientation_lbl.sizePolicy().hasHeightForWidth())
        self.cb_orientation_lbl.setSizePolicy(sizePolicy)
        self.cb_orientation_lbl.setObjectName("cb_orientation_lbl")
        self.horizontalLayout_17.addWidget(self.cb_orientation_lbl)
        self.cb_orientation_cbb = QtWidgets.QComboBox(self.image_tab)
        self.cb_orientation_cbb.setEnabled(False)
        self.cb_orientation_cbb.setObjectName("cb_orientation_cbb")
        self.cb_orientation_cbb.addItem("")
        self.cb_orientation_cbb.addItem("")
        self.horizontalLayout_17.addWidget(self.cb_orientation_cbb)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem9)
        self.gridLayout_8.addLayout(self.horizontalLayout_17, 2, 1, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.image_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout_8.addWidget(self.label_43, 0, 0, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.image_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout_8.addWidget(self.label_44, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40,
                                             QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem10, 3, 1, 1, 1)
        self.config_tabWidget.addTab(self.image_tab, "")
        self.barchart_tab = QtWidgets.QWidget()
        self.barchart_tab.setObjectName("barchart_tab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.barchart_tab)
        self.gridLayout_11.setContentsMargins(6, 12, 6, 6)
        self.gridLayout_11.setSpacing(4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_51 = QtWidgets.QLabel(self.barchart_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.gridLayout_11.addWidget(self.label_51, 1, 0, 1, 1)
        self.label_lineEdit = QtWidgets.QLineEdit(self.barchart_tab)
        self.label_lineEdit.setObjectName("label_lineEdit")
        self.gridLayout_11.addWidget(self.label_lineEdit, 3, 1, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.barchart_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_57.setObjectName("label_57")
        self.gridLayout_11.addWidget(self.label_57, 3, 0, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.barchart_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_72.setFont(font)
        self.label_72.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_72.setObjectName("label_72")
        self.gridLayout_11.addWidget(self.label_72, 4, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setSpacing(4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_50 = QtWidgets.QLabel(self.barchart_tab)
        self.label_50.setObjectName("label_50")
        self.gridLayout_9.addWidget(self.label_50, 0, 0, 1, 1)
        self.bar_opacity_slider = QtWidgets.QSlider(self.barchart_tab)
        self.bar_opacity_slider.setStyleSheet(
            "QSlider::groove:horizontal {\n"
            "border: 1px solid #bbb;\n"
            "background: white;\n"
            "height: 12px;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::sub-page:horizontal {\n"
            "background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
            "    stop: 0 #F57900, stop: 1 #FCAF3E);\n"
            "background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
            "    stop: 0 #FCAF3E, stop: 1 #F57900);\n"
            "border: 1px solid #777;\n"
            "height: 10px;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::add-page:horizontal {\n"
            "background: #fff;\n"
            "border: 1px solid #777;\n"
            "height: 10px;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal {\n"
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
            "    stop:0 #eee, stop:1 #ccc);\n"
            "border: 1px solid #777;\n"
            "width: 15px;\n"
            "margin-top: -2px;\n"
            "margin-bottom: -2px;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal:hover {\n"
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
            "    stop:0 #fff, stop:1 #ddd);\n"
            "border: 1px solid #444;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::sub-page:horizontal:disabled {\n"
            "background: #bbb;\n"
            "border-color: #999;\n"
            "}\n"
            "\n"
            "QSlider::add-page:horizontal:disabled {\n"
            "background: #eee;\n"
            "border-color: #999;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal:disabled {\n"
            "background: #eee;\n"
            "border: 1px solid #aaa;\n"
            "border-radius: 4px;\n"
            "}")
        self.bar_opacity_slider.setMaximum(100)
        self.bar_opacity_slider.setProperty("value", 100)
        self.bar_opacity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.bar_opacity_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.bar_opacity_slider.setObjectName("bar_opacity_slider")
        self.gridLayout_9.addWidget(self.bar_opacity_slider, 0, 1, 1, 1)
        self.bar_opacity_lbl = QtWidgets.QLabel(self.barchart_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bar_opacity_lbl.sizePolicy().hasHeightForWidth())
        self.bar_opacity_lbl.setSizePolicy(sizePolicy)
        self.bar_opacity_lbl.setAlignment(QtCore.Qt.AlignRight
                                          | QtCore.Qt.AlignTrailing
                                          | QtCore.Qt.AlignVCenter)
        self.bar_opacity_lbl.setObjectName("bar_opacity_lbl")
        self.gridLayout_9.addWidget(self.bar_opacity_lbl, 0, 2, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.barchart_tab)
        self.label_56.setObjectName("label_56")
        self.gridLayout_9.addWidget(self.label_56, 1, 0, 1, 1)
        self.ebline_opacity_slider = QtWidgets.QSlider(self.barchart_tab)
        self.ebline_opacity_slider.setStyleSheet(
            "QSlider::groove:horizontal {\n"
            "border: 1px solid #bbb;\n"
            "background: white;\n"
            "height: 12px;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::sub-page:horizontal {\n"
            "background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
            "    stop: 0 #F57900, stop: 1 #FCAF3E);\n"
            "background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
            "    stop: 0 #FCAF3E, stop: 1 #F57900);\n"
            "border: 1px solid #777;\n"
            "height: 10px;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::add-page:horizontal {\n"
            "background: #fff;\n"
            "border: 1px solid #777;\n"
            "height: 10px;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal {\n"
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
            "    stop:0 #eee, stop:1 #ccc);\n"
            "border: 1px solid #777;\n"
            "width: 15px;\n"
            "margin-top: -2px;\n"
            "margin-bottom: -2px;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal:hover {\n"
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
            "    stop:0 #fff, stop:1 #ddd);\n"
            "border: 1px solid #444;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::sub-page:horizontal:disabled {\n"
            "background: #bbb;\n"
            "border-color: #999;\n"
            "}\n"
            "\n"
            "QSlider::add-page:horizontal:disabled {\n"
            "background: #eee;\n"
            "border-color: #999;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal:disabled {\n"
            "background: #eee;\n"
            "border: 1px solid #aaa;\n"
            "border-radius: 4px;\n"
            "}")
        self.ebline_opacity_slider.setMaximum(100)
        self.ebline_opacity_slider.setProperty("value", 100)
        self.ebline_opacity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.ebline_opacity_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.ebline_opacity_slider.setObjectName("ebline_opacity_slider")
        self.gridLayout_9.addWidget(self.ebline_opacity_slider, 1, 1, 1, 1)
        self.ebline_opacity_lbl = QtWidgets.QLabel(self.barchart_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ebline_opacity_lbl.sizePolicy().hasHeightForWidth())
        self.ebline_opacity_lbl.setSizePolicy(sizePolicy)
        self.ebline_opacity_lbl.setAlignment(QtCore.Qt.AlignRight
                                             | QtCore.Qt.AlignTrailing
                                             | QtCore.Qt.AlignVCenter)
        self.ebline_opacity_lbl.setObjectName("ebline_opacity_lbl")
        self.gridLayout_9.addWidget(self.ebline_opacity_lbl, 1, 2, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_9, 2, 1, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.barchart_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.gridLayout_11.addWidget(self.label_48, 0, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setSpacing(4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_54 = QtWidgets.QLabel(self.barchart_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy)
        self.label_54.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_54.setObjectName("label_54")
        self.gridLayout_10.addWidget(self.label_54, 1, 2, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.barchart_tab)
        self.label_52.setObjectName("label_52")
        self.gridLayout_10.addWidget(self.label_52, 1, 0, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.barchart_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy)
        self.label_49.setObjectName("label_49")
        self.gridLayout_10.addWidget(self.label_49, 0, 0, 1, 1)
        self.bar_width_lineEdit = QtWidgets.QLineEdit(self.barchart_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bar_width_lineEdit.sizePolicy().hasHeightForWidth())
        self.bar_width_lineEdit.setSizePolicy(sizePolicy)
        self.bar_width_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.bar_width_lineEdit.setObjectName("bar_width_lineEdit")
        self.gridLayout_10.addWidget(self.bar_width_lineEdit, 0, 3, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.barchart_tab)
        self.label_58.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_58.setObjectName("label_58")
        self.gridLayout_10.addWidget(self.label_58, 0, 2, 1, 1)
        self.ebline_width_lineEdit = QtWidgets.QLineEdit(self.barchart_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ebline_width_lineEdit.sizePolicy().hasHeightForWidth())
        self.ebline_width_lineEdit.setSizePolicy(sizePolicy)
        self.ebline_width_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ebline_width_lineEdit.setObjectName("ebline_width_lineEdit")
        self.gridLayout_10.addWidget(self.ebline_width_lineEdit, 1, 3, 1, 1)
        self.ebline_style_cbb = QtWidgets.QComboBox(self.barchart_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ebline_style_cbb.sizePolicy().hasHeightForWidth())
        self.ebline_style_cbb.setSizePolicy(sizePolicy)
        self.ebline_style_cbb.setSizeAdjustPolicy(
            QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.ebline_style_cbb.setObjectName("ebline_style_cbb")
        self.ebline_style_cbb.addItem("")
        self.ebline_style_cbb.addItem("")
        self.ebline_style_cbb.addItem("")
        self.ebline_style_cbb.addItem("")
        self.ebline_style_cbb.addItem("")
        self.gridLayout_10.addWidget(self.ebline_style_cbb, 1, 5, 1, 1)
        self.ebline_color_btn = QtWidgets.QToolButton(self.barchart_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ebline_color_btn.sizePolicy().hasHeightForWidth())
        self.ebline_color_btn.setSizePolicy(sizePolicy)
        self.ebline_color_btn.setText("")
        self.ebline_color_btn.setIconSize(QtCore.QSize(20, 20))
        self.ebline_color_btn.setObjectName("ebline_color_btn")
        self.gridLayout_10.addWidget(self.ebline_color_btn, 1, 1, 1, 1)
        self.bar_color_btn = QtWidgets.QToolButton(self.barchart_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bar_color_btn.sizePolicy().hasHeightForWidth())
        self.bar_color_btn.setSizePolicy(sizePolicy)
        self.bar_color_btn.setText("")
        self.bar_color_btn.setIconSize(QtCore.QSize(20, 20))
        self.bar_color_btn.setObjectName("bar_color_btn")
        self.gridLayout_10.addWidget(self.bar_color_btn, 0, 1, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.barchart_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy)
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.gridLayout_10.addWidget(self.label_53, 1, 4, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem11, 1, 6, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem12, 0, 6, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 1, 2, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSpacing(4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line_4 = QtWidgets.QFrame(self.barchart_tab)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_4.addWidget(self.line_4, 2, 1, 1, 1)
        self.label_78 = QtWidgets.QLabel(self.barchart_tab)
        self.label_78.setObjectName("label_78")
        self.gridLayout_4.addWidget(self.label_78, 3, 0, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.barchart_tab)
        self.label_74.setObjectName("label_74")
        self.gridLayout_4.addWidget(self.label_74, 1, 3, 1, 1)
        self.annote_fontsize_sbox = QtWidgets.QSpinBox(self.barchart_tab)
        self.annote_fontsize_sbox.setMinimum(8)
        self.annote_fontsize_sbox.setMaximum(30)
        self.annote_fontsize_sbox.setProperty("value", 10)
        self.annote_fontsize_sbox.setObjectName("annote_fontsize_sbox")
        self.gridLayout_4.addWidget(self.annote_fontsize_sbox, 1, 4, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.barchart_tab)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_4.addWidget(self.line_5, 3, 1, 1, 1)
        self.annote_angle_dsbox = QtWidgets.QDoubleSpinBox(self.barchart_tab)
        self.annote_angle_dsbox.setDecimals(1)
        self.annote_angle_dsbox.setMaximum(360.0)
        self.annote_angle_dsbox.setSingleStep(1.0)
        self.annote_angle_dsbox.setObjectName("annote_angle_dsbox")
        self.gridLayout_4.addWidget(self.annote_angle_dsbox, 1, 6, 1, 1)
        self.annote_fmt_lineEdit = QtWidgets.QLineEdit(self.barchart_tab)
        self.annote_fmt_lineEdit.setObjectName("annote_fmt_lineEdit")
        self.gridLayout_4.addWidget(self.annote_fmt_lineEdit, 3, 4, 1, 4)
        self.annote_bbox_alpha_dsbox = QtWidgets.QDoubleSpinBox(
            self.barchart_tab)
        self.annote_bbox_alpha_dsbox.setDecimals(1)
        self.annote_bbox_alpha_dsbox.setMaximum(1.0)
        self.annote_bbox_alpha_dsbox.setSingleStep(0.1)
        self.annote_bbox_alpha_dsbox.setProperty("value", 0.8)
        self.annote_bbox_alpha_dsbox.setObjectName("annote_bbox_alpha_dsbox")
        self.gridLayout_4.addWidget(self.annote_bbox_alpha_dsbox, 2, 4, 1, 1)
        self.label_77 = QtWidgets.QLabel(self.barchart_tab)
        self.label_77.setObjectName("label_77")
        self.gridLayout_4.addWidget(self.label_77, 1, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.barchart_tab)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 1, 1, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.barchart_tab)
        self.label_73.setObjectName("label_73")
        self.gridLayout_4.addWidget(self.label_73, 1, 5, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.barchart_tab)
        self.label_75.setObjectName("label_75")
        self.gridLayout_4.addWidget(self.label_75, 2, 3, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(4)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Preferred,
                                             QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem13)
        self.reset_annote_fmt_btn = QtWidgets.QToolButton(self.barchart_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.reset_annote_fmt_btn.sizePolicy().hasHeightForWidth())
        self.reset_annote_fmt_btn.setSizePolicy(sizePolicy)
        self.reset_annote_fmt_btn.setIcon(icon3)
        self.reset_annote_fmt_btn.setObjectName("reset_annote_fmt_btn")
        self.horizontalLayout_14.addWidget(self.reset_annote_fmt_btn)
        self.gridLayout_4.addLayout(self.horizontalLayout_14, 3, 3, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.barchart_tab)
        self.label_76.setObjectName("label_76")
        self.gridLayout_4.addWidget(self.label_76, 2, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem14, 1, 7, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_4, 4, 1, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.barchart_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_55.setObjectName("label_55")
        self.gridLayout_11.addWidget(self.label_55, 2, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40,
                                             QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem15, 5, 1, 1, 1)
        self.config_tabWidget.addTab(self.barchart_tab, "")
        self.gridLayout_3.addWidget(self.config_tabWidget, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.config_tabWidget.setCurrentIndex(0)
        self.cross_rename_chkbox.toggled['bool'].connect(
            self.cross_literal_name_lineEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.fig_title_lineEdit, self.title_font_btn)
        Dialog.setTabOrder(self.title_font_btn, self.fig_xlabel_lineEdit)
        Dialog.setTabOrder(self.fig_xlabel_lineEdit, self.fig_ylabel_lineEdit)
        Dialog.setTabOrder(self.fig_ylabel_lineEdit, self.xy_label_font_btn)
        Dialog.setTabOrder(self.xy_label_font_btn, self.autoScale_chkbox)
        Dialog.setTabOrder(self.autoScale_chkbox, self.xmin_lineEdit)
        Dialog.setTabOrder(self.xmin_lineEdit, self.xmax_lineEdit)
        Dialog.setTabOrder(self.xmax_lineEdit, self.ymin_lineEdit)
        Dialog.setTabOrder(self.ymin_lineEdit, self.ymax_lineEdit)
        Dialog.setTabOrder(self.ymax_lineEdit, self.legend_on_chkbox)
        Dialog.setTabOrder(self.legend_on_chkbox, self.legend_loc_cbb)
        Dialog.setTabOrder(self.legend_loc_cbb, self.xaxis_scale_cbb)
        Dialog.setTabOrder(self.xaxis_scale_cbb, self.yaxis_scale_cbb)
        Dialog.setTabOrder(self.yaxis_scale_cbb, self.figWidth_lineEdit)
        Dialog.setTabOrder(self.figWidth_lineEdit, self.figHeight_lineEdit)
        Dialog.setTabOrder(self.figHeight_lineEdit, self.figDpi_lineEdit)
        Dialog.setTabOrder(self.figDpi_lineEdit, self.figAspect_cbb)
        Dialog.setTabOrder(self.figAspect_cbb, self.bkgd_color_btn)
        Dialog.setTabOrder(self.bkgd_color_btn, self.ticks_color_btn)
        Dialog.setTabOrder(self.ticks_color_btn, self.grid_color_btn)
        Dialog.setTabOrder(self.grid_color_btn, self.ticks_hide_chkbox)
        Dialog.setTabOrder(self.ticks_hide_chkbox, self.mticks_chkbox)
        Dialog.setTabOrder(self.mticks_chkbox, self.xy_ticks_font_btn)
        Dialog.setTabOrder(self.xy_ticks_font_btn, self.xticks_rotation_sbox)
        Dialog.setTabOrder(self.xticks_rotation_sbox,
                           self.yticks_rotation_sbox)
        Dialog.setTabOrder(self.yticks_rotation_sbox,
                           self.enable_mathtext_chkbox)
        Dialog.setTabOrder(self.enable_mathtext_chkbox,
                           self.xtick_formatter_cbb)
        Dialog.setTabOrder(self.xtick_formatter_cbb,
                           self.xtick_funcformatter_lineEdit)
        Dialog.setTabOrder(self.xtick_funcformatter_lineEdit,
                           self.ytick_formatter_cbb)
        Dialog.setTabOrder(self.ytick_formatter_cbb,
                           self.ytick_funcformatter_lineEdit)
        Dialog.setTabOrder(self.ytick_funcformatter_lineEdit,
                           self.tightLayout_chkbox)
        Dialog.setTabOrder(self.tightLayout_chkbox, self.gridon_chkbox)
        Dialog.setTabOrder(self.gridon_chkbox, self.border_hide_chkbox)
        Dialog.setTabOrder(self.border_hide_chkbox, self.border_color_btn)
        Dialog.setTabOrder(self.border_color_btn, self.border_lw_sbox)
        Dialog.setTabOrder(self.border_lw_sbox, self.border_ls_cbb)
        Dialog.setTabOrder(self.border_ls_cbb, self.line_id_cbb)
        Dialog.setTabOrder(self.line_id_cbb, self.line_hide_chkbox)
        Dialog.setTabOrder(self.line_hide_chkbox, self.line_style_cbb)
        Dialog.setTabOrder(self.line_style_cbb, self.line_color_btn)
        Dialog.setTabOrder(self.line_color_btn, self.line_width_lineEdit)
        Dialog.setTabOrder(self.line_width_lineEdit, self.mk_style_cbb)
        Dialog.setTabOrder(self.mk_style_cbb, self.mk_facecolor_btn)
        Dialog.setTabOrder(self.mk_facecolor_btn, self.mk_edgecolor_btn)
        Dialog.setTabOrder(self.mk_edgecolor_btn, self.mk_size_lineEdit)
        Dialog.setTabOrder(self.mk_size_lineEdit, self.mk_width_lineEdit)
        Dialog.setTabOrder(self.mk_width_lineEdit, self.opacity_val_slider)
        Dialog.setTabOrder(self.opacity_val_slider, self.eb_line_id_cbb)
        Dialog.setTabOrder(self.eb_line_id_cbb, self.eb_line_hide_chkbox)
        Dialog.setTabOrder(self.eb_line_hide_chkbox, self.eb_line_style_cbb)
        Dialog.setTabOrder(self.eb_line_style_cbb, self.eb_line_color_btn)
        Dialog.setTabOrder(self.eb_line_color_btn, self.eb_line_width_lineEdit)
        Dialog.setTabOrder(self.eb_line_width_lineEdit, self.yeb_mk_style_cbb)
        Dialog.setTabOrder(self.yeb_mk_style_cbb, self.eb_mk_facecolor_btn)
        Dialog.setTabOrder(self.eb_mk_facecolor_btn, self.eb_mk_edgecolor_btn)
        Dialog.setTabOrder(self.eb_mk_edgecolor_btn, self.eb_mk_size_lineEdit)
        Dialog.setTabOrder(self.eb_mk_size_lineEdit, self.eb_mk_width_lineEdit)
        Dialog.setTabOrder(self.eb_mk_width_lineEdit, self.xeb_mk_style_cbb)
        Dialog.setTabOrder(self.xeb_mk_style_cbb, self.cmap_class_cbb)
        Dialog.setTabOrder(self.cmap_class_cbb, self.cmap_cbb)
        Dialog.setTabOrder(self.cmap_cbb, self.add_to_fav_btn)
        Dialog.setTabOrder(self.add_to_fav_btn, self.del_from_fav_btn)
        Dialog.setTabOrder(self.del_from_fav_btn, self.reverse_cmap_chkbox)
        Dialog.setTabOrder(self.reverse_cmap_chkbox, self.auto_clim_chkbox)
        Dialog.setTabOrder(self.auto_clim_chkbox, self.cr_reset_tbtn)
        Dialog.setTabOrder(self.cr_reset_tbtn, self.cr_min_dSpinBox)
        Dialog.setTabOrder(self.cr_min_dSpinBox, self.cr_max_dSpinBox)
        Dialog.setTabOrder(self.cr_max_dSpinBox, self.show_colorbar_chkbox)
        Dialog.setTabOrder(self.show_colorbar_chkbox, self.cb_orientation_cbb)
        Dialog.setTabOrder(self.cb_orientation_cbb, self.bar_color_btn)
        Dialog.setTabOrder(self.bar_color_btn, self.bar_width_lineEdit)
        Dialog.setTabOrder(self.bar_width_lineEdit, self.ebline_color_btn)
        Dialog.setTabOrder(self.ebline_color_btn, self.ebline_width_lineEdit)
        Dialog.setTabOrder(self.ebline_width_lineEdit, self.ebline_style_cbb)
        Dialog.setTabOrder(self.ebline_style_cbb, self.bar_opacity_slider)
        Dialog.setTabOrder(self.bar_opacity_slider, self.ebline_opacity_slider)
        Dialog.setTabOrder(self.ebline_opacity_slider, self.label_lineEdit)
        Dialog.setTabOrder(self.label_lineEdit, self.annote_fontsize_sbox)
        Dialog.setTabOrder(self.annote_fontsize_sbox, self.annote_angle_dsbox)
        Dialog.setTabOrder(self.annote_angle_dsbox,
                           self.annote_bbox_alpha_dsbox)
        Dialog.setTabOrder(self.annote_bbox_alpha_dsbox,
                           self.reset_annote_fmt_btn)
        Dialog.setTabOrder(self.reset_annote_fmt_btn, self.annote_fmt_lineEdit)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_42.setText(_translate("Dialog", "X"))
        self.xaxis_scale_cbb.setItemText(0, _translate("Dialog",
                                                       "Linear Scale"))
        self.xaxis_scale_cbb.setItemText(1,
                                         _translate("Dialog", "Log Transform"))
        self.xaxis_scale_cbb.setItemText(
            2, _translate("Dialog", "Symmetrical Log Transform"))
        self.xaxis_scale_cbb.setItemText(
            3, _translate("Dialog", "Logistic Transform"))
        self.label_41.setText(_translate("Dialog", "Y"))
        self.yaxis_scale_cbb.setItemText(0, _translate("Dialog",
                                                       "Linear Scale"))
        self.yaxis_scale_cbb.setItemText(1,
                                         _translate("Dialog", "Log Transform"))
        self.yaxis_scale_cbb.setItemText(
            2, _translate("Dialog", "Symmetrical Log Transform"))
        self.yaxis_scale_cbb.setItemText(
            3, _translate("Dialog", "Logistic Transform"))
        self.label_10.setText(_translate("Dialog", "Labels"))
        self.label_18.setText(_translate("Dialog", "X-Label"))
        self.label_11.setText(_translate("Dialog", "Y-Label"))
        self.hide_xylabel_chkbox.setText(_translate("Dialog", "Hide"))
        self.xy_label_font_btn.setToolTip(_translate("Dialog", "Change font."))
        self.xy_label_font_btn.setText(_translate("Dialog", "Font"))
        self.label.setText(_translate("Dialog", "XY Range"))
        self.hide_title_chkbox.setText(_translate("Dialog", "Hide"))
        self.title_font_btn.setToolTip(_translate("Dialog", "Change font."))
        self.title_font_btn.setText(_translate("Dialog", "Font"))
        self.label_25.setText(_translate("Dialog", "Legend"))
        self.label_40.setText(_translate("Dialog", "Axis Scale"))
        self.legend_on_chkbox.setToolTip(
            _translate("Dialog", "Check to show legend"))
        self.legend_on_chkbox.setText(_translate("Dialog", "Show"))
        self.label_24.setText(_translate("Dialog", "Location"))
        self.legend_loc_cbb.setToolTip(
            _translate("Dialog", "Select location for legend"))
        self.legend_loc_cbb.setItemText(0, _translate("Dialog", "Auto"))
        self.legend_loc_cbb.setItemText(1, _translate("Dialog", "Upper Right"))
        self.legend_loc_cbb.setItemText(2, _translate("Dialog", "Upper Left"))
        self.legend_loc_cbb.setItemText(3, _translate("Dialog", "Lower Left"))
        self.legend_loc_cbb.setItemText(4, _translate("Dialog", "Lower Right"))
        self.legend_loc_cbb.setItemText(5, _translate("Dialog", "Right"))
        self.legend_loc_cbb.setItemText(6, _translate("Dialog", "Center Left"))
        self.legend_loc_cbb.setItemText(7, _translate("Dialog",
                                                      "Center Right"))
        self.legend_loc_cbb.setItemText(8, _translate("Dialog",
                                                      "Lower Center"))
        self.legend_loc_cbb.setItemText(9, _translate("Dialog",
                                                      "Upper Center"))
        self.legend_loc_cbb.setItemText(10, _translate("Dialog", "Center"))
        self.label_13.setText(_translate("Dialog", "Title"))
        self.autoScale_chkbox.setText(_translate("Dialog", "Auto Scale"))
        self.xmin_lbl.setText(_translate("Dialog", "X-min"))
        self.xmax_lbl.setText(_translate("Dialog", "X-max"))
        self.ymin_lbl.setText(_translate("Dialog", "Y-min"))
        self.ymax_lbl.setText(_translate("Dialog", "Y-max"))
        self.config_tabWidget.setTabText(
            self.config_tabWidget.indexOf(self.figure_tab),
            _translate("Dialog", "Figure"))
        self.label_12.setText(_translate("Dialog", "Width"))
        self.figWidth_lineEdit.setText(_translate("Dialog", "4"))
        self.figWidth_lineEdit.setPlaceholderText(_translate("Dialog", "4"))
        self.label_14.setText(_translate("Dialog", "Height"))
        self.figHeight_lineEdit.setText(_translate("Dialog", "3"))
        self.figHeight_lineEdit.setPlaceholderText(_translate("Dialog", "3"))
        self.label_15.setText(_translate("Dialog", "DPI"))
        self.figDpi_lineEdit.setToolTip(
            _translate("Dialog", "Set dot per inch property of the figure."))
        self.figDpi_lineEdit.setText(_translate("Dialog", "120"))
        self.figDpi_lineEdit.setPlaceholderText(_translate("Dialog", "120"))
        self.label_69.setText(_translate("Dialog", "Ratio"))
        self.figAspect_cbb.setToolTip(
            _translate("Dialog", "Set figure aspect."))
        self.figAspect_cbb.setItemText(0, _translate("Dialog", "Auto"))
        self.figAspect_cbb.setItemText(1, _translate("Dialog", "Equal"))
        self.label_17.setText(_translate("Dialog", "Colors"))
        self.label_59.setText(_translate("Dialog", "Rotation"))
        self.label_60.setText(_translate("Dialog", "X"))
        self.xticks_rotation_sbox.setSuffix(_translate("Dialog", " degree"))
        self.label_61.setText(_translate("Dialog", "Y"))
        self.yticks_rotation_sbox.setSuffix(_translate("Dialog", " degree"))
        self.label_16.setText(_translate("Dialog", "Figure Size"))
        self.enable_mathtext_chkbox.setToolTip(
            _translate("Dialog", "Show tick labels as math style."))
        self.enable_mathtext_chkbox.setText(_translate("Dialog", "Math Text"))
        self.label_38.setText(_translate("Dialog", "X"))
        self.xtick_formatter_cbb.setItemText(0, _translate("Dialog", "Auto"))
        self.xtick_formatter_cbb.setItemText(1, _translate("Dialog", "Custom"))
        self.xtick_funcformatter_lineEdit.setToolTip(
            _translate(
                "Dialog",
                "Input c string format specifier, e.g. %1d, %.2f, %.2e, 10^%n, etc."
            ))
        self.xtick_funcformatter_lineEdit.setText(_translate("Dialog", "%g"))
        self.label_39.setText(_translate("Dialog", "Y"))
        self.ytick_formatter_cbb.setItemText(0, _translate("Dialog", "Auto"))
        self.ytick_formatter_cbb.setItemText(1, _translate("Dialog", "Custom"))
        self.ytick_funcformatter_lineEdit.setToolTip(
            _translate(
                "Dialog",
                "Input c string format specifier, e.g. %1d, %.2f, %.3e, 10^%n, etc."
            ))
        self.ytick_funcformatter_lineEdit.setText(_translate("Dialog", "%g"))
        self.label_6.setText(_translate("Dialog", "Layout"))
        self.label_7.setText(_translate("Dialog", "Ticks"))
        self.ticks_hide_chkbox.setToolTip(
            _translate("Dialog", "Check to hide ticks."))
        self.ticks_hide_chkbox.setText(_translate("Dialog", "Hide"))
        self.mticks_chkbox.setToolTip(
            _translate("Dialog", "Check to show minor ticks."))
        self.mticks_chkbox.setText(_translate("Dialog", "Minor On"))
        self.xy_ticks_sample_lbl.setText(_translate("Dialog", "Sample"))
        self.xy_ticks_font_btn.setToolTip(
            _translate("Dialog", "Change tick labels font."))
        self.xy_ticks_font_btn.setText(_translate("Dialog", "Choose Font"))
        self.tightLayout_chkbox.setText(_translate("Dialog", "Tight"))
        self.gridon_chkbox.setToolTip(
            _translate("Dialog", "Check to show grid."))
        self.gridon_chkbox.setText(_translate("Dialog", "Grid On"))
        self.border_hide_chkbox.setToolTip(
            _translate("Dialog", "Check to hide figure border."))
        self.border_hide_chkbox.setText(_translate("Dialog", "Hide"))
        self.label_67.setText(_translate("Dialog", "Color"))
        self.label_65.setText(_translate("Dialog", "Width"))
        self.border_lw_sbox.setToolTip(
            _translate("Dialog", "Change border width."))
        self.label_68.setText(_translate("Dialog", "Style"))
        self.border_ls_cbb.setToolTip(
            _translate("Dialog", "Change border line style."))
        self.border_ls_cbb.setItemText(0, _translate("Dialog", "solid"))
        self.border_ls_cbb.setItemText(1, _translate("Dialog", "dashed"))
        self.border_ls_cbb.setItemText(2, _translate("Dialog", "dashdot"))
        self.border_ls_cbb.setItemText(3, _translate("Dialog", "dotted"))
        self.label_62.setText(_translate("Dialog", "Background"))
        self.label_63.setText(_translate("Dialog", "Ticks"))
        self.label_64.setText(_translate("Dialog", "Grid"))
        self.label_66.setText(_translate("Dialog", "Boundaries"))
        self.config_tabWidget.setTabText(
            self.config_tabWidget.indexOf(self.style_tab),
            _translate("Dialog", "Style"))
        self.label_173.setText(_translate("Dialog", "Cross"))
        self.cross_hide_chkbox.setText(_translate("Dialog", "Hide"))
        self.label_164.setText(_translate("Dialog", "Lines"))
        self.label_169.setText(_translate("Dialog", "Color"))
        self.label_170.setText(_translate("Dialog", "Style"))
        self.label_166.setText(_translate("Dialog", "Size"))
        self.label_165.setText(_translate("Dialog", "Width"))
        self.label_167.setText(_translate("Dialog", "Width"))
        self.label_171.setText(_translate("Dialog", "Face Color"))
        self.label_172.setText(_translate("Dialog", "Edge Color"))
        self.label_168.setText(_translate("Dialog", "Style"))
        self.cross_line_style_cbb.setItemText(0, _translate("Dialog", "solid"))
        self.cross_line_style_cbb.setItemText(1,
                                              _translate("Dialog", "dashed"))
        self.cross_line_style_cbb.setItemText(2,
                                              _translate("Dialog", "dashdot"))
        self.cross_line_style_cbb.setItemText(3,
                                              _translate("Dialog", "dotted"))
        self.cross_line_style_cbb.setItemText(4, _translate("Dialog", "None"))
        self.cross_line_hide_chkbox.setText(_translate("Dialog", "Hide"))
        self.cross_mk_hide_chkbox.setText(_translate("Dialog", "Hide"))
        self.label_163.setText(_translate("Dialog", "Marker"))
        self.label_174.setText(_translate("Dialog", "Text"))
        self.cross_rename_chkbox.setText(_translate("Dialog", "Rename"))
        self.label_176.setText(_translate("Dialog", "Color"))
        self.cross_text_hide_chkbox.setText(_translate("Dialog", "Hide"))
        self.config_tabWidget.setTabText(
            self.config_tabWidget.indexOf(self.cross_tab),
            _translate("Dialog", "Cross"))
        self.line_id_cbb.setToolTip(
            _translate("Dialog", "Select line to configure"))
        self.line_hide_chkbox.setText(_translate("Dialog", "Hide"))
        self.label_3.setText(_translate("Dialog", "Line"))
        self.label_2.setText(_translate("Dialog", "Line ID"))
        self.label_26.setText(_translate("Dialog", "Opacity"))
        self.label_23.setText(_translate("Dialog", "Label"))
        self.label_4.setText(_translate("Dialog", "Marker"))
        self.label_22.setText(_translate("Dialog", "Width"))
        self.label_20.setText(_translate("Dialog", "Size"))
        self.label_9.setText(_translate("Dialog", "Width"))
        self.label_8.setText(_translate("Dialog", "Style"))
        self.line_style_cbb.setItemText(0, _translate("Dialog", "solid"))
        self.line_style_cbb.setItemText(1, _translate("Dialog", "dashed"))
        self.line_style_cbb.setItemText(2, _translate("Dialog", "dashdot"))
        self.line_style_cbb.setItemText(3, _translate("Dialog", "dotted"))
        self.line_style_cbb.setItemText(4, _translate("Dialog", "None"))
        self.label_5.setText(_translate("Dialog", "Color"))
        self.label_19.setText(_translate("Dialog", "Style"))
        self.label_21.setText(_translate("Dialog", "Face Color"))
        self.label_37.setText(_translate("Dialog", "Edge Color"))
        self.label_70.setText(_translate("Dialog", "Draw As"))
        self.line_ds_cbb.setItemText(0, _translate("Dialog", "Line"))
        self.line_ds_cbb.setItemText(1, _translate("Dialog", "Steps"))
        self.line_ds_cbb.setItemText(2, _translate("Dialog", "Mid-Steps"))
        self.line_ds_cbb.setItemText(3, _translate("Dialog", "Post-Steps"))
        self.opacity_val_lbl.setText(_translate("Dialog", "100%"))
        self.config_tabWidget.setTabText(
            self.config_tabWidget.indexOf(self.curve_tab),
            _translate("Dialog", "Curve"))
        self.label_36.setText(_translate("Dialog", "Line ID"))
        self.eb_line_hide_chkbox.setText(_translate("Dialog", "Hide"))
        self.label_30.setText(_translate("Dialog", "Line"))
        self.label_33.setText(_translate("Dialog", "Style"))
        self.label_79.setText(_translate("Dialog", "Style"))
        self.label_27.setText(_translate("Dialog", "Style"))
        self.label_35.setText(_translate("Dialog", "Face Color"))
        self.label_34.setText(_translate("Dialog", "Width"))
        self.label_32.setText(_translate("Dialog", "Size"))
        self.xeb_mk_style_cbb.setToolTip(
            _translate(
                "Dialog",
                "<html><head/><body><p>Set marker style for X errbar</p></body></html>"
            ))
        self.eb_line_style_cbb.setItemText(0, _translate("Dialog", "solid"))
        self.eb_line_style_cbb.setItemText(1, _translate("Dialog", "dashed"))
        self.eb_line_style_cbb.setItemText(2, _translate("Dialog", "dashdot"))
        self.eb_line_style_cbb.setItemText(3, _translate("Dialog", "dotted"))
        self.eb_line_style_cbb.setItemText(4, _translate("Dialog", "None"))
        self.label_29.setText(_translate("Dialog", "Color"))
        self.yeb_mk_style_cbb.setToolTip(
            _translate(
                "Dialog",
                "<html><head/><body><p>Set marker style for Y errbar</p></body></html>"
            ))
        self.label_31.setText(_translate("Dialog", "Width"))
        self.label_81.setText(_translate("Dialog", "Edge Color"))
        self.label_28.setText(_translate("Dialog", "Cap-Y"))
        self.label_80.setText(_translate("Dialog", "Cap-X"))
        self.eb_line_id_cbb.setToolTip(
            _translate("Dialog", "Select line to configure"))
        self.config_tabWidget.setTabText(
            self.config_tabWidget.indexOf(self.eb_tab),
            _translate("Dialog", "Errorbar"))
        self.label_47.setText(_translate("Dialog", "Color Bar"))
        self.add_to_fav_btn.setText(_translate("Dialog", "..."))
        self.del_from_fav_btn.setText(_translate("Dialog", "..."))
        self.reverse_cmap_chkbox.setText(_translate("Dialog", "Reverse"))
        self.auto_clim_chkbox.setText(_translate("Dialog", "Auto"))
        self.cr_reset_tbtn.setToolTip(
            _translate(
                "Dialog",
                "<html><head/><body><p>Reset color range</p></body></html>"))
        self.cr_reset_tbtn.setText(_translate("Dialog", "..."))
        self.label_45.setText(_translate("Dialog", "Min"))
        self.label_46.setText(_translate("Dialog", "Max"))
        self.show_colorbar_chkbox.setText(_translate("Dialog", "Show"))
        self.cb_orientation_lbl.setText(_translate("Dialog", "Orientation"))
        self.cb_orientation_cbb.setItemText(0,
                                            _translate("Dialog", "Vertical"))
        self.cb_orientation_cbb.setItemText(1,
                                            _translate("Dialog", "Horizontal"))
        self.label_43.setText(_translate("Dialog", "Color Map"))
        self.label_44.setText(_translate("Dialog", "Color Range"))
        self.config_tabWidget.setTabText(
            self.config_tabWidget.indexOf(self.image_tab),
            _translate("Dialog", "Image"))
        self.label_51.setText(_translate("Dialog", "ErrorBar"))
        self.label_57.setText(_translate("Dialog", "Label"))
        self.label_72.setText(_translate("Dialog", "Annotation"))
        self.label_50.setText(_translate("Dialog", "Bar"))
        self.bar_opacity_lbl.setText(_translate("Dialog", "100%"))
        self.label_56.setText(_translate("Dialog", "Errorbar"))
        self.ebline_opacity_lbl.setText(_translate("Dialog", "100%"))
        self.label_48.setText(_translate("Dialog", "Bar"))
        self.label_54.setText(_translate("Dialog", "Width"))
        self.label_52.setText(_translate("Dialog", "Color"))
        self.label_49.setText(_translate("Dialog", "Color"))
        self.label_58.setText(_translate("Dialog", "Width"))
        self.ebline_style_cbb.setItemText(0, _translate("Dialog", "solid"))
        self.ebline_style_cbb.setItemText(1, _translate("Dialog", "dashed"))
        self.ebline_style_cbb.setItemText(2, _translate("Dialog", "dashdot"))
        self.ebline_style_cbb.setItemText(3, _translate("Dialog", "dotted"))
        self.ebline_style_cbb.setItemText(4, _translate("Dialog", "None"))
        self.label_53.setText(_translate("Dialog", "Style"))
        self.label_78.setText(_translate("Dialog", "Format"))
        self.label_74.setText(_translate("Dialog", "Font Size"))
        self.annote_angle_dsbox.setSuffix(_translate("Dialog", " deg"))
        self.label_77.setText(_translate("Dialog", "Text"))
        self.label_73.setText(_translate("Dialog", "Rotation"))
        self.label_75.setText(_translate("Dialog", "Alpha"))
        self.reset_annote_fmt_btn.setToolTip(
            _translate("Dialog", "Reset to default format."))
        self.reset_annote_fmt_btn.setText(_translate("Dialog", "Reset"))
        self.label_76.setText(_translate("Dialog", "BBox"))
        self.label_55.setText(_translate("Dialog", "Opacity"))
        self.config_tabWidget.setTabText(
            self.config_tabWidget.indexOf(self.barchart_tab),
            _translate("Dialog", "BarChart"))


from mpl4qt.widgets._widgets import TabWidget
from mpl4qt.widgets.mplbasewidget import MatplotlibCMapWidget
from . import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
