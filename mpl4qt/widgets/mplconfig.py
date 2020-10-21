#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configuration widget for matplotlib.
"""
import numpy as np
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFontDialog
from PyQt5.QtWidgets import QMessageBox

from mpl4qt.ui.ui_mplconfig import Ui_Dialog
from mpl4qt.widgets.utils import get_array_range
from mpl4qt.widgets.utils import COLORMAPS_DICT
from mpl4qt.widgets.utils import LINE_STY_DICT
from mpl4qt.widgets.utils import LINE_STY_VALS
from mpl4qt.widgets.utils import MK_CODE
from mpl4qt.widgets.utils import MK_SYMBOL
from mpl4qt.widgets.utils import SCALE_STY_KEYS
from mpl4qt.widgets.utils import SCALE_STY_VALS
from mpl4qt.widgets.utils import mplcolor2hex
from mpl4qt.widgets.utils import FIG_WIDTH_MIN
from mpl4qt.widgets.utils import FIG_WIDTH_MAX
from mpl4qt.widgets.utils import FIG_HEIGHT_MIN
from mpl4qt.widgets.utils import FIG_HEIGHT_MAX
from mpl4qt.widgets.utils import FIG_DPI_MIN
from mpl4qt.widgets.utils import FIG_DPI_MAX
from mpl4qt.widgets.utils import LINE_WIDTH_MIN
from mpl4qt.widgets.utils import LINE_WIDTH_MAX
from mpl4qt.widgets.utils import MK_SIZE_MIN
from mpl4qt.widgets.utils import MK_SIZE_MAX
from mpl4qt.widgets.utils import MK_WIDTH_MIN
from mpl4qt.widgets.utils import MK_WIDTH_MAX
from mpl4qt.widgets.utils import LINE_DS_DICT
from mpl4qt.widgets.utils import LINE_DS_DICT_R


class MatplotlibConfigPanel(QDialog, Ui_Dialog):
    # fig size and color
    bgcolorChanged = pyqtSignal(QColor)
    figWidthChanged = pyqtSignal(float)
    figHeightChanged = pyqtSignal(float)
    figDpiChanged = pyqtSignal(float)

    # layout and scale
    figAutoScaleChanged = pyqtSignal(bool)
    figTightLayoutChanged = pyqtSignal(bool)

    # title string
    figTitleFontChanged = pyqtSignal(QFont)

    # label strings and fonts
    figXlabelChanged = pyqtSignal('QString')
    figYlabelChanged = pyqtSignal('QString')
    figXYlabelFontChanged = pyqtSignal(QFont)

    # xy ticks
    figXYticksFontChanged = pyqtSignal(QFont)
    figXYticksColorChanged = pyqtSignal(QColor)
    figMTicksChanged = pyqtSignal(bool)
    # tick format, 'Auto/Custom', formatter
    figXTickFormatChanged = pyqtSignal('QString', 'QString')
    figYTickFormatChanged = pyqtSignal('QString', 'QString')

    # grid
    figGridChanged = pyqtSignal(bool)
    figGridColorChanged = pyqtSignal(QColor)

    # xy limits
    figXminLimitChanged = pyqtSignal(float)
    figXmaxLimitChanged = pyqtSignal(float)
    figYminLimitChanged = pyqtSignal(float)
    figYmaxLimitChanged = pyqtSignal(float)

    # border color
    figBorderColorChanged = pyqtSignal(QColor)
    figBorderLineWidthChanged = pyqtSignal(float)

    def __init__(self, parent=None):
        super(MatplotlibConfigPanel, self).__init__()
        self.parent = parent

        # UI
        self.setupUi(self)
        self.setWindowTitle("Figure Configurations")

        # hide eb_tab and image_tab
        for tab in (self.cross_tab, self.curve_tab, self.eb_tab,
                    self.image_tab, self.barchart_tab):
            self.config_tabWidget.setTabEnabled(
                self.config_tabWidget.indexOf(tab), False)

        # cross mks
        if self.parent._markers:
            self.config_tabWidget.setTabEnabled(
                self.config_tabWidget.indexOf(self.cross_tab), True)
            self.set_up_cross_tab()
        #

        self.figWidth_lineEdit.setValidator(
                QDoubleValidator(FIG_WIDTH_MIN, FIG_WIDTH_MAX, 6, self))
        self.figHeight_lineEdit.setValidator(
                QDoubleValidator(FIG_HEIGHT_MIN, FIG_HEIGHT_MAX, 6, self))
        self.figDpi_lineEdit.setValidator(
                QDoubleValidator(FIG_DPI_MIN, FIG_DPI_MAX, 6, self))
        for o in (self.xmin_lineEdit, self.xmax_lineEdit,
                  self.ymin_lineEdit, self.ymax_lineEdit,):
            o.setValidator(QDoubleValidator(self))

        # events
        self.figWidth_lineEdit.textChanged.connect(self.set_figsize_width)
        self.figHeight_lineEdit.textChanged.connect(self.set_figsize_height)
        self.figDpi_lineEdit.textChanged.connect(self.set_figdpi)
        self.autoScale_chkbox.stateChanged.connect(self.set_fig_autoscale)
        self.show_xyrange_box(not self.autoScale_chkbox.isChecked())
        self.tightLayout_chkbox.stateChanged.connect(self.set_fig_tightlayout)
        self.xy_label_font_btn.clicked.connect(self.set_xy_label_font)
        self.xy_ticks_font_btn.clicked.connect(self.set_xy_ticks_font)
        self.title_font_btn.clicked.connect(self.set_title_font)
        self.xmin_lineEdit.textChanged.connect(self.set_xlimit_min)
        self.xmax_lineEdit.textChanged.connect(self.set_xlimit_max)
        self.ymin_lineEdit.textChanged.connect(self.set_ylimit_min)
        self.ymax_lineEdit.textChanged.connect(self.set_ylimit_max)

        # background color
        self.bgcolorChanged.connect(partial(self.set_btn_color, self.bkgd_color_btn))
        self.bgcolorChanged.connect(self.parent.setFigureBgColor)
        self.bkgd_color_btn.clicked.connect(self.set_bkgdcolor)
        self.set_btn_color(self.bkgd_color_btn, self.parent.getFigureBgColor())

        # borders color
        self.figBorderColorChanged.connect(partial(self.set_btn_color, self.border_color_btn))
        self.figBorderColorChanged.connect(self.parent.setFigureBorderColor)
        self.border_color_btn.clicked.connect(self.set_border_color)
        self.set_btn_color(self.border_color_btn, self.parent.getFigureBorderColor())
        # borders lw
        self.figBorderLineWidthChanged.connect(self.parent.setFigureBorderLineWidth)
        self.border_lw_sbox.valueChanged.connect(self.set_border_lw)
        self.border_lw_sbox.setValue(self.parent.getFigureBorderLineWidth())
        # borders ls
        self.border_ls_cbb.currentTextChanged.connect(self.parent.setFigureBorderLineStyle)
        self.border_ls_cbb.setCurrentText(self.parent.getFigureBorderLineStyle())
        # borders hide?
        self.border_hide_chkbox.toggled.connect(
            lambda f: self.parent.setFigureBorderVisible(not f))
        self.border_hide_chkbox.setChecked(not self.parent.getFigureBorderVisible())

        # aspect ratio
        self.figAspect_cbb.currentTextChanged.connect(
            lambda s: self.parent.setFigureAspectRatio(s.lower()))
        self.figAspect_cbb.setCurrentText(self.parent.getFigureAspectRatio().capitalize())

        self.figWidthChanged[float].connect(self.parent.setFigureWidth)
        self.figHeightChanged[float].connect(self.parent.setFigureHeight)
        self.figDpiChanged[float].connect(self.parent.setFigureDpi)
        self.figAutoScaleChanged[bool].connect(self.parent.setFigureAutoScale)
        self.figTightLayoutChanged[bool].connect(
            self.parent.setTightLayoutToggle)
        self.figXminLimitChanged[float].connect(self.parent.setXLimitMin)
        self.figXmaxLimitChanged[float].connect(self.parent.setXLimitMax)
        self.figYminLimitChanged[float].connect(self.parent.setYLimitMin)
        self.figYmaxLimitChanged[float].connect(self.parent.setYLimitMax)

        ## xy labels
        self.figXYlabelFontChanged[QFont].connect(
            self.parent.setFigureXYlabelFont)
        self.fig_xlabel_lineEdit.textChanged.connect(
            self.parent.setFigureXlabel)
        self.fig_ylabel_lineEdit.textChanged.connect(
            self.parent.setFigureYlabel)
        self.hide_xylabel_chkbox.setChecked(not self.parent.getFigureXYlabelVisible())
        self.hide_xylabel_chkbox.toggled.connect(
                lambda f: self.parent.setFigureXYlabelVisible(not f))

        ## title
        self.fig_title_lineEdit.textChanged.connect(self.parent.setFigureTitle)
        self.figTitleFontChanged.connect(self.parent.setFigureTitleFont)
        self.hide_title_chkbox.setChecked(not self.parent.getFigureTitleVisible())
        self.hide_title_chkbox.toggled.connect(
                lambda f: self.parent.setFigureTitleVisible(not f))

        # xy ticks
        self.figXYticksFontChanged.connect(self.parent.setFigureXYticksFont)
        # color
        self.figXYticksColorChanged.connect(partial(self.set_btn_color, self.ticks_color_btn))
        self.figXYticksColorChanged.connect(self.parent.setFigureXYticksColor)
        self.ticks_color_btn.clicked.connect(self.set_xyticks_color)
        self.set_btn_color(self.ticks_color_btn, self.parent.getFigureXYticksColor())
        # visibility
        self.ticks_hide_chkbox.toggled.connect(
            lambda f: self.parent.setFigureXTicksVisible(not f))
        self.ticks_hide_chkbox.toggled.connect(
            lambda f: self.parent.setFigureYTicksVisible(not f))
        self.ticks_hide_chkbox.setChecked(not self.parent.getFigureXTicksVisible())

        self.mticks_chkbox.stateChanged.connect(self.set_fig_mticks)
        self.figMTicksChanged[bool].connect(self.parent.setFigureMTicksToggle)
        # rot
        self.xticks_rotation_sbox.valueChanged.connect(self.parent.setFigureXTicksAngle)
        self.yticks_rotation_sbox.valueChanged.connect(self.parent.setFigureYTicksAngle)

        # tick formatter
        self.xtick_formatter_cbb.currentTextChanged['QString'].connect(self.on_tickformatter_changed)
        self.ytick_formatter_cbb.currentTextChanged['QString'].connect(self.on_tickformatter_changed)
        self.xtick_funcformatter_lineEdit.returnPressed.connect(
            lambda: self.on_set_funcformatter(self.xtick_funcformatter_lineEdit.text(),
                                              set_xticks=True))
        self.ytick_funcformatter_lineEdit.returnPressed.connect(
            lambda: self.on_set_funcformatter(self.ytick_funcformatter_lineEdit.text(),
                                              set_yticks=True))
        self.figXTickFormatChanged['QString', 'QString'].connect(self.parent.setXTickFormat)
        self.figYTickFormatChanged['QString', 'QString'].connect(self.parent.setYTickFormat)

        # enable math text or not
        self.enable_mathtext_chkbox.toggled.connect(self.on_enable_ticks_mathtext)

        # grid
        self.figGridChanged[bool].connect(
            lambda x: self.parent.setFigureGridToggle(x, mticks=self.mticks_chkbox.isChecked()))
        self.figGridColorChanged.connect(
            lambda x: self.parent.setFigureGridColor(x, mticks=self.mticks_chkbox.isChecked(),
                                                     toggle_checked=self.gridon_chkbox.isChecked()))
        self.figGridColorChanged.connect(partial(self.set_btn_color, self.grid_color_btn))
        self.gridon_chkbox.stateChanged.connect(self.set_fig_grid)
        self.grid_color_btn.clicked.connect(self.set_grid_color)

        # post UI update
        self.post_init_ui()

        # axis scale
        self.xaxis_scale_cbb.currentIndexChanged.connect(
            lambda i: self.parent.setFigureXScale(SCALE_STY_VALS[i]))
        self.yaxis_scale_cbb.currentIndexChanged.connect(
            lambda i: self.parent.setFigureYScale(SCALE_STY_VALS[i]))

        self.adjustSize()

        # quick fix title font, size will be overriden.
        self.parent.setFigureTitleFont(self.parent.getFigureTitleFont())

    def post_init_ui(self):
        self.figWidth_lineEdit.setText(str(self.parent.getFigureWidth()))
        self.figHeight_lineEdit.setText(str(self.parent.getFigureHeight()))
        self.figDpi_lineEdit.setText(str(self.parent.getFigureDpi()))
        self.autoScale_chkbox.setChecked(self.parent.getFigureAutoScale())
        self.tightLayout_chkbox.setChecked(self.parent.getTightLayoutToggle())
        self.fig_title_lineEdit.setText(self.parent.getFigureTitle())
        self.fig_xlabel_lineEdit.setText(self.parent.getFigureXlabel())
        self.fig_ylabel_lineEdit.setText(self.parent.getFigureYlabel())
        self.xy_ticks_sample_lbl.setFont(self.parent.getFigureXYticksFont())
        self.mticks_chkbox.setChecked(self.parent.getFigureMTicksToggle())
        self.xticks_rotation_sbox.setValue(self.parent.getFigureXTicksAngle())
        self.yticks_rotation_sbox.setValue(self.parent.getFigureYTicksAngle())
        self.gridon_chkbox.setChecked(self.parent.getFigureGridToggle())
        self.set_btn_color(self.grid_color_btn, self.parent.getFigureGridColor())
        self.set_xylimits()

        # axis scale
        self.xaxis_scale_cbb.clear()
        self.xaxis_scale_cbb.addItems(SCALE_STY_KEYS)
        self.xaxis_scale_cbb.setCurrentIndex(
            SCALE_STY_VALS.index(self.parent.getFigureXScale()))
        self.yaxis_scale_cbb.clear()
        self.yaxis_scale_cbb.addItems(SCALE_STY_KEYS)
        self.yaxis_scale_cbb.setCurrentIndex(
            SCALE_STY_VALS.index(self.parent.getFigureYScale()))

        self.__set_cfmt()
        # tick formatter
        self.xtick_formatter_cbb.setCurrentText(self.parent._fig_xtick_formatter_type)
        self.ytick_formatter_cbb.setCurrentText(self.parent._fig_ytick_formatter_type)
        # apply math text to ticks indicator
        self.enable_mathtext_chkbox.setChecked(self.parent._fig_ticks_enable_mathtext)

    def __set_cfmt(self):
        # set cfmt for ticks custom formatter
        x_cfmt = self.parent._fig_xtick_cfmt
        y_cfmt = self.parent._fig_ytick_cfmt
        if x_cfmt != '':
            self.xtick_funcformatter_lineEdit.setText(x_cfmt)
        if y_cfmt != '':
            self.ytick_funcformatter_lineEdit.setText(y_cfmt)

    @pyqtSlot()
    def on_set_funcformatter(self, text, set_xticks=False, set_yticks=False):
        """*text* is the current input string in x or y
        tick_funcformatter_lineEdit. If *set_xticks* is True, set xtick
        formatter, the same applies to *set_yticks*.
        """
        if text == '':
            QMessageBox.warning(self, "Customize Tick Format",
                    "Empty input is not valid.", QMessageBox.Ok)
            self.sender().setText("%g")
            return
        if set_xticks:
            self.parent._fig_xtick_cfmt = text
            self.figXTickFormatChanged.emit('Custom', text)
        if set_yticks:
            self.parent._fig_ytick_cfmt = text
            self.figYTickFormatChanged.emit('Custom', text)

    @pyqtSlot(bool)
    def on_enable_ticks_mathtext(self, ischecked):
        self.parent._fig_ticks_enable_mathtext = ischecked
        self.figXTickFormatChanged.emit(
            self.parent._fig_xtick_formatter_type,
            self.parent._fig_xtick_cfmt)
        self.figYTickFormatChanged.emit(
            self.parent._fig_ytick_formatter_type,
            self.parent._fig_ytick_cfmt)

    @pyqtSlot('QString')
    def on_tickformatter_changed(self, s):
        obj = self.sender()
        oname = obj.objectName()
        if s == 'Auto':
            if oname == 'xtick_formatter_cbb':
                self.xtick_funcformatter_lineEdit.setEnabled(False)
                self.figXTickFormatChanged.emit(s, '')
            elif oname == 'ytick_formatter_cbb':
                self.ytick_funcformatter_lineEdit.setEnabled(False)
                self.figYTickFormatChanged.emit(s, '')
        elif s == 'Custom':
            if oname == 'xtick_formatter_cbb':
                self.xtick_funcformatter_lineEdit.setEnabled(True)
                text = self.xtick_funcformatter_lineEdit.text()
                self.figXTickFormatChanged.emit(s, text)
            elif oname == 'ytick_formatter_cbb':
                self.ytick_funcformatter_lineEdit.setEnabled(True)
                text = self.ytick_funcformatter_lineEdit.text()
                self.figYTickFormatChanged.emit(s, text)

    def set_xylimits(self, xlim=None, ylim=None):
        """Set xy limits.
        """
        xmin, xmax = self.parent.get_xlim()
        ymin, ymax = self.parent.get_ylim()
        self.xmin_lineEdit.setText('{0:3g}'.format(xmin))
        self.xmax_lineEdit.setText('{0:3g}'.format(xmax))
        self.ymin_lineEdit.setText('{0:3g}'.format(ymin))
        self.ymax_lineEdit.setText('{0:3g}'.format(ymax))

    @pyqtSlot(float)
    def set_border_lw(self, w):
        self.figBorderLineWidthChanged.emit(w)

    @pyqtSlot('QString')
    def set_xlimit_min(self, s):
        try:
            x = float(s)
            self.figXminLimitChanged.emit(float(s))
        except:
            pass

    @pyqtSlot('QString')
    def set_xlimit_max(self, s):
        try:
            x = float(s)
            self.figXmaxLimitChanged.emit(float(s))
        except:
            pass

    @pyqtSlot('QString')
    def set_ylimit_min(self, s):
        try:
            x = float(s)
        except:
            pass
        else:
            self.figYminLimitChanged.emit(float(s))

    @pyqtSlot('QString')
    def set_ylimit_max(self, s):
        try:
            x = float(s)
        except:
            pass
        else:
            self.figYmaxLimitChanged.emit(float(s))

    @pyqtSlot()
    def set_grid_color(self):
        color = QColorDialog.getColor(self.parent.getFigureGridColor())
        if color.isValid():
            self.figGridColorChanged.emit(color)

    @staticmethod
    def set_btn_color(btn, color):
        """Set the button with giving qcolor.
        """
        btn.setStyleSheet("QToolButton {\n"
                          "  margin: 4px;\n"
                          "  border: 1px solid gray;\n"
                          "  border-radius: 1px;\n"
                          "  background-color: %s;\n" % color.name() + "}\n"
                          "QToolButton:pressed {\n"
                          "  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #DADBDE, stop:1 #F6F7FA);\n"
                          "}\n"
                          "QToolButton:hover {\n"
                          "  border: 2px solid black;\n"
                          "  border-radius: 2px;\n"
                          "  background-color: qradialgradient(cx:0.5, cy:0.5, radius:1, fx:0.5, fy:0.5, stop:0 %s, stop:1 #F6F7FA);\n" % color.name() +
                          "}")
        btn.setToolTip(color.name().upper())

    @pyqtSlot(int)
    def set_fig_grid(self, state):
        self.figGridChanged.emit(state == Qt.Checked)

    @pyqtSlot(int)
    def set_fig_mticks(self, state):
        self.figMTicksChanged.emit(state == Qt.Checked)

    @pyqtSlot()
    def set_fig_xlabel(self):
        t = self.fig_xlabel_lineEdit.text()
        self.figXlabelChanged.emit(t)

    @pyqtSlot()
    def set_fig_ylabel(self):
        t = self.fig_ylabel_lineEdit.text()
        self.figYlabelChanged.emit(t)

    @pyqtSlot()
    def set_bkgdcolor(self):
        color = QColorDialog.getColor(self.parent.getFigureBgColor())
        if color.isValid():
            self.bgcolorChanged.emit(color)

    @pyqtSlot()
    def set_border_color(self):
        color = QColorDialog.getColor(self.parent.getFigureBorderColor())
        if color.isValid():
            self.figBorderColorChanged.emit(color)

    @pyqtSlot()
    def set_xyticks_color(self):
        color = QColorDialog.getColor(self.parent.getFigureXYticksColor())
        if color.isValid():
            self.figXYticksColorChanged.emit(color)

    @pyqtSlot()
    def set_xy_label_font(self):
        cfont = self.parent.getFigureXYlabelFont()
        font, ok = select_font(self, cfont)
        if ok:
            self.figXYlabelFontChanged.emit(font)

    @pyqtSlot()
    def set_xy_ticks_font(self):
        cfont = self.parent.getFigureXYticksFont()
        font, ok = select_font(self, cfont)
        if ok:
            self.xy_ticks_sample_lbl.setFont(font)
            self.figXYticksFontChanged.emit(font)

    @pyqtSlot()
    def set_title_font(self):
        cfont = self.parent.getFigureTitleFont()
        font, ok = select_font(self, cfont)
        if ok:
            self.figTitleFontChanged.emit(font)

    @pyqtSlot('QString')
    def set_figsize_width(self, s):
        if s == '': return
        w = max(float(s), 2.0)
        self.figWidthChanged.emit(w)

    @pyqtSlot('QString')
    def set_figsize_height(self, s):
        if s == '': return
        h = max(float(s), 2.0)
        self.figHeightChanged.emit(h)

    @pyqtSlot('QString')
    def set_figdpi(self, s):
        if s == '': return
        d = max(float(s), 20.0)
        self.figDpiChanged.emit(d)

    @pyqtSlot(int)
    def set_fig_autoscale(self, state):
        self.figAutoScaleChanged.emit(state == Qt.Checked)
        self.show_xyrange_box(state != Qt.Checked)

    def show_xyrange_box(self, b):
        """Show widgets in xyrange box or not.
        """
        widgets = (self.xmin_lbl, self.xmax_lbl, self.ymin_lbl, self.ymax_lbl,
                   self.xmin_lineEdit, self.xmax_lineEdit, self.ymin_lineEdit,
                   self.ymax_lineEdit)
        [w.setEnabled(b) for w in widgets]

    @pyqtSlot(int)
    def set_fig_tightlayout(self, state):
        self.figTightLayoutChanged.emit(state == Qt.Checked)

    def sizeHint(self):
        return QSize(200, 100)

    def set_up_cross_tab(self):
        # set up configurations for cross markers.
        self.cross_line_width_lineEdit.setValidator(
                QDoubleValidator(LINE_WIDTH_MIN, LINE_WIDTH_MAX, 1, self))
        self.cross_mk_size_lineEdit.setValidator(
                QDoubleValidator(MK_SIZE_MIN, MK_SIZE_MAX, 1, self))
        self.cross_mk_width_lineEdit.setValidator(
                QDoubleValidator(MK_WIDTH_MIN, MK_WIDTH_MAX, 1, self))
        self._cross_partial_hide_states = {}
        for o in (self.cross_line_hide_chkbox, self.cross_mk_hide_chkbox,
                  self.cross_text_hide_chkbox):
            o.stateChanged.connect(self.on_update_cross_hide_state)
        self.cross_hide_chkbox.stateChanged.connect(self.on_hide_cross)
        self.cross_mk_style_cbb.addItems(MK_CODE)
        self.cross_cbb.addItems(self.parent._markers.keys())
        self.cross_cbb.currentTextChanged.connect(self.on_current_mkname_changed)
        self.cross_cbb.currentTextChanged.emit(self.cross_cbb.currentText())
        self.cross_line_hide_chkbox.toggled.connect(self.on_hide_cross_line)
        self.cross_mk_hide_chkbox.toggled.connect(self.on_hide_cross_mk)
        self.cross_text_hide_chkbox.toggled.connect(self.on_hide_cross_text)
        self.cross_line_style_cbb.currentTextChanged.connect(self.on_change_cross_ls)
        self.cross_line_width_lineEdit.textChanged.connect(self.on_change_cross_lw)
        self.cross_line_color_btn.clicked.connect(self.on_change_cross_lc)
        self.cross_mk_size_lineEdit.textChanged.connect(self.on_change_cross_mksize)
        self.cross_mk_width_lineEdit.textChanged.connect(self.on_change_cross_mew)
        self.cross_mk_edgecolor_btn.clicked.connect(self.on_change_cross_mec)
        self.cross_mk_facecolor_btn.clicked.connect(self.on_change_cross_mfc)
        self.cross_mk_style_cbb.currentIndexChanged.connect(self.on_change_mkstyle)
        self.cross_text_color_btn.clicked.connect(self.on_change_cross_textc)
        self.cross_literal_name_lineEdit.returnPressed.connect(self.on_change_cross_name)

    def on_update_cross_hide_state(self, state):
        self.cross_hide_chkbox.stateChanged.disconnect(self.on_hide_cross)

        states = (self.cross_line_hide_chkbox.isChecked(),
                  self.cross_mk_hide_chkbox.isChecked(),
                  self.cross_text_hide_chkbox.isChecked(),)
        if all(states):
            self.cross_hide_chkbox.setCheckState(Qt.Checked)
        elif not any(states):
            self.cross_hide_chkbox.setCheckState(Qt.Unchecked)
        else:
            self.cross_hide_chkbox.setCheckState(Qt.PartiallyChecked)
            self._cross_partial_hide_states[self._current_mk_name] = states

        self.cross_hide_chkbox.stateChanged.connect(self.on_hide_cross)

    def on_hide_cross(self, state):
        hide_chkboxes = (self.cross_line_hide_chkbox,
                         self.cross_mk_hide_chkbox,
                         self.cross_text_hide_chkbox,)
        for o in hide_chkboxes:
            o.stateChanged.disconnect(self.on_update_cross_hide_state)

        if state == Qt.PartiallyChecked:
            for o, s in zip(hide_chkboxes,
                            self._cross_partial_hide_states.setdefault(self._current_mk_name, [])):
                o.setChecked(s)
        else:
            for o in hide_chkboxes:
                o.setCheckState(state)

        for o in hide_chkboxes:
            o.stateChanged.connect(self.on_update_cross_hide_state)

    def get_cross_obj_by_name(self, name, otype='line'):
        # get artists from cross markers, otype: line, point, text as a list.
        if otype == 'line':
            hl, vl, _, _, _ = self.parent._markers[name]
            r = [hl, vl]
        elif otype == 'point':
            _, _, cp, _, _ = self.parent._markers[name]
            r = [cp]
        elif otype == 'text':
            _, _, _, pt, _ = self.parent._markers[name]
            r = [pt]
        return r

    @pyqtSlot()
    def on_change_cross_name(self):
        # rename cross marker
        new_name = self.cross_literal_name_lineEdit.text()
        if not new_name.isidentifier():
            QMessageBox.warning(self, "Change the name of cross marker",
                                "Name is not valid!", QMessageBox.Ok)
            return
        if new_name in self.parent._markers:
            QMessageBox.warning(self, "Change the name of cross marker",
                                "Name is using, change another one!", QMessageBox.Ok)
            return

        for o in self.get_cross_obj_by_name(self._current_mk_name, 'text'):
            o.set_text(new_name)
        self.parent.update_figure()
        self.parent._markers.setdefault(new_name,
                self.parent._markers.pop(self.cross_cbb.currentText()))
        #
        if self._cross_partial_hide_states:
            self._cross_partial_hide_states.setdefault(new_name,
                    self._cross_partial_hide_states.pop(self.cross_cbb.currentText()))
        self.cross_cbb.setItemText(self.cross_cbb.currentIndex(), new_name)

    @pyqtSlot()
    def on_change_cross_textc(self):
        # change cross marker text color
        o = self.get_cross_obj_by_name(self._current_mk_name, 'text')[0]
        c = QColorDialog.getColor(QColor(mplcolor2hex(o.get_color())))
        if c.isValid():
            o.set_color(c.getRgbF())
            self.parent.update_figure()
            self.set_btn_color(self.sender(), c)

    @pyqtSlot(int)
    def on_change_mkstyle(self, i):
        for o in self.get_cross_obj_by_name(self._current_mk_name, 'point'):
            o.set_marker(MK_SYMBOL[i])
        self.parent.update_figure()

    @pyqtSlot('QString')
    def on_change_cross_mksize(self, s):
        if s == '': return
        w = max(float(s), 1.0)
        for o in self.get_cross_obj_by_name(self._current_mk_name, 'point'):
            o.set_ms(w)
        self.parent.update_figure()

    @pyqtSlot()
    def on_change_cross_mfc(self):
        o = self.get_cross_obj_by_name(self._current_mk_name, 'point')[0]
        c = QColorDialog.getColor(QColor(mplcolor2hex(o.get_mfc())))
        if c.isValid():
            o.set_mfc(c.getRgbF())
            self.parent.update_figure()
            self.set_btn_color(self.sender(), c)

    @pyqtSlot()
    def on_change_cross_mec(self):
        o = self.get_cross_obj_by_name(self._current_mk_name, 'point')[0]
        c = QColorDialog.getColor(QColor(mplcolor2hex(o.get_mec())))
        if c.isValid():
            o.set_mec(c.getRgbF())
            self.parent.update_figure()
            self.set_btn_color(self.sender(), c)

    @pyqtSlot('QString')
    def on_change_cross_mew(self, s):
        if s == '': return
        w = max(float(s), 0.1)
        for o in self.get_cross_obj_by_name(self._current_mk_name, 'point'):
            o.set_mew(w)
        self.parent.update_figure()

    @pyqtSlot()
    def on_change_cross_lc(self):
        o = self.get_cross_obj_by_name(self._current_mk_name)
        c = QColorDialog.getColor(QColor(mplcolor2hex(o[0].get_color())))
        if c.isValid():
            [i.set_color(c.getRgbF()) for i in o]
            self.parent.update_figure()
            self.set_btn_color(self.sender(), c)

    @pyqtSlot('QString')
    def on_change_cross_lw(self, s):
        if s == '': return
        w = max(float(s), 0.05)
        for o in self.get_cross_obj_by_name(self._current_mk_name):
            o.set_lw(w)
        self.parent.update_figure()

    @pyqtSlot('QString')
    def on_change_cross_ls(self, s):
        if s not in LINE_STY_VALS:
            return
        for o in self.get_cross_obj_by_name(self._current_mk_name):
            o.set_ls(s)
        self.parent.update_figure()

    @pyqtSlot(bool)
    def on_hide_cross_text(self, hide):
        # hide current cross text
        for o in self.get_cross_obj_by_name(self._current_mk_name, 'text'):
            o.set_visible(not hide)
        self.parent.update_figure()

    @pyqtSlot(bool)
    def on_hide_cross_mk(self, hide):
        # hide current cross mk
        for o in self.get_cross_obj_by_name(self._current_mk_name, 'point'):
            o.set_visible(not hide)
        self.parent.update_figure()

    @pyqtSlot(bool)
    def on_hide_cross_line(self, hide):
        # hide current cross line
        for o in self.get_cross_obj_by_name(self._current_mk_name):
            o.set_visible(not hide)
        self.parent.update_figure()

    @pyqtSlot('QString')
    def on_current_mkname_changed(self, mk_name):
        # current mk_name is changed.
        for o in (self.cross_line_hide_chkbox, self.cross_mk_hide_chkbox,
                  self.cross_text_hide_chkbox):
            o.stateChanged.disconnect(self.on_update_cross_hide_state)

        self._current_mk_name = mk_name
        conf = self.parent.get_crossmk_config(mk_name)
        # literal name (text),color,vis
        self.cross_literal_name_lineEdit.setText(mk_name)
        self.set_btn_color(self.cross_text_color_btn, QColor(mplcolor2hex(conf['text_color'])))
        self.cross_text_hide_chkbox.setChecked(not conf['text_visible'])

        # line color
        self.set_btn_color(self.cross_line_color_btn, QColor(mplcolor2hex(conf['c'])))
        # ls
        self.cross_line_style_cbb.setCurrentText(LINE_STY_DICT[conf['ls']])
        # lw
        self.cross_line_width_lineEdit.setText('{}'.format(conf['lw']))
        # line vis
        self.cross_line_hide_chkbox.setChecked(not conf['line_visible'])
        # mk
        self.cross_mk_style_cbb.setCurrentIndex(MK_SYMBOL.index(conf['mk']))
        # ms
        self.cross_mk_size_lineEdit.setText('{}'.format(conf['ms']))
        # mec,mfc
        self.set_btn_color(self.cross_mk_edgecolor_btn, QColor(mplcolor2hex(conf['mec'])))
        self.set_btn_color(self.cross_mk_facecolor_btn, QColor(mplcolor2hex(conf['mfc'])))
        # mew
        self.cross_mk_width_lineEdit.setText('{}'.format(conf['mew']))
        # mk vis
        self.cross_mk_hide_chkbox.setChecked(not conf['mk_visible'])

        for o in (self.cross_line_hide_chkbox, self.cross_mk_hide_chkbox,
                  self.cross_text_hide_chkbox):
            o.stateChanged.connect(self.on_update_cross_hide_state)
        self.on_update_cross_hide_state(None)


class MatplotlibConfigCurvePanel(MatplotlibConfigPanel):

    # line id
    figLineIDChanged = pyqtSignal(int)

    # line
    figLineColorChanged = pyqtSignal(QColor)
    figLineWidthChanged = pyqtSignal(float)
    figLineVisibleChanged = pyqtSignal(bool)

    # color opacity
    figLineAlphaChanged = pyqtSignal(float)

    # legend
    figLegendToggleChanged = pyqtSignal(bool)

    # marker
    figMkeColorChanged = pyqtSignal(QColor)
    figMkfColorChanged = pyqtSignal(QColor)
    figMkStyleChanged = pyqtSignal('QString')
    figMkSizeChanged = pyqtSignal(float)
    figMkWidthChanged = pyqtSignal(float)

    def __init__(self, parent=None):
        super(MatplotlibConfigCurvePanel, self).__init__(parent)

        # show curve_tab
        self.config_tabWidget.setTabEnabled(
            self.config_tabWidget.indexOf(self.curve_tab), True)

        # line, mk
        self.line_width_lineEdit.setValidator(
                QDoubleValidator(LINE_WIDTH_MIN, LINE_WIDTH_MAX, 1, self))
        self.mk_size_lineEdit.setValidator(
                QDoubleValidator(MK_SIZE_MIN, MK_SIZE_MAX, 1, self))
        self.mk_width_lineEdit.setValidator(
                QDoubleValidator(MK_WIDTH_MIN, MK_WIDTH_MAX, 1, self))

        # line visible
        self.line_hide_chkbox.stateChanged.connect(self.set_line_visible)
        # opacity
        self.opacity_val_slider.valueChanged.connect(
            lambda i: self.opacity_val_lbl.setText('{}%'.format(i)))
        self.opacity_val_slider.valueChanged.connect(self.set_line_opacity)

        #
        self.figLineVisibleChanged[bool].connect(self.parent.setLineVisible)
        # line opacity
        self.figLineAlphaChanged[float].connect(self.parent.setLineAlpha)

        # legend
        self.legend_on_chkbox.stateChanged.connect(self.set_legend)
        self.figLegendToggleChanged[bool].connect(self.parent.setLegendToggle)
        self.legend_loc_cbb.currentIndexChanged[int].connect(
            self.parent.setLegendLocation)

        # line id, put after post_init_ui, elliminate cb initialization disturb
        self.figLineIDChanged[int].connect(self.parent.setLineID)
        self.line_id_cbb.currentIndexChanged[int].connect(
            self.on_change_line_id)

        self._post_init_ui()

        # line color
        self.figLineColorChanged.connect(partial(self.set_btn_color, self.line_color_btn))
        self.figLineColorChanged.connect(self.parent.setLineColor)
        self.line_color_btn.clicked.connect(self.set_line_color)
        # line style
        self.line_style_cbb.currentTextChanged['QString'].connect(
            self.parent.setLineStyle)
        # line ds
        self.line_ds_cbb.currentTextChanged['QString'].connect(
            lambda s:self.parent.setLineDrawStyle(LINE_DS_DICT[s]))
        # line width
        self.line_width_lineEdit.textChanged.connect(self.set_line_width)
        self.figLineWidthChanged[float].connect(self.parent.setLineWidth)
        # line label
        self.line_label_lineEdit.textChanged.connect(self.parent.setLineLabel)
        # marker size
        self.mk_size_lineEdit.textChanged.connect(self.set_marker_size)
        self.figMkSizeChanged[float].connect(self.parent.setMarkerSize)
        # marker thickness
        self.mk_width_lineEdit.textChanged.connect(self.set_marker_thickness)
        self.figMkWidthChanged[float].connect(self.parent.setMarkerThickness)
        # marker style
        self.figMkStyleChanged['QString'].connect(self.parent.setMarkerStyle)
        self.mk_style_cbb.currentIndexChanged[int].connect(
            self.set_marker_style)
        # marker: mec
        self.figMkeColorChanged.connect(partial(self.set_btn_color, self.mk_edgecolor_btn))
        self.figMkeColorChanged.connect(self.parent.setMkEdgeColor)
        self.mk_edgecolor_btn.clicked.connect(self.set_mec)
        # marker: mfc
        self.figMkfColorChanged.connect(partial(self.set_btn_color, self.mk_facecolor_btn))
        self.figMkfColorChanged.connect(self.parent.setMkFaceColor)
        self.mk_facecolor_btn.clicked.connect(self.set_mfc)

    def _post_init_ui(self):
        # marker style
        self.mk_style_cbb.clear()
        self.mk_style_cbb.addItems(MK_CODE)

        # line id combo
        if not self.parent.get_all_curves():  # is []
            self.config_tabWidget.setTabEnabled(
                self.config_tabWidget.indexOf(self.curve_tab), False)
        else:
            self.line_id_cbb.clear()
            self.line_id_cbb.addItems(
                [str(i) for i, l in enumerate(self.parent.get_all_curves())])
            try:
                current_line_id = self.parent.get_all_curves().index(self.parent._line)
            except AttributeError:  # no _line attribute
                current_line_id = 0
            self.line_id_cbb.setCurrentIndex(current_line_id)
            self.on_change_line_id(current_line_id)

            # legend on/off
            self.legend_on_chkbox.setChecked(self.parent.getLegendToggle())
            self.legend_loc_cbb.setCurrentIndex(self.parent.getLegendLocation())
            # line visible
            self.line_hide_chkbox.setChecked(not self.parent.getLineVisible())

            # has selected line?
            for lbl, (o, lw0, mw0) in self.parent._last_sel_lines.items():
                lnid = self.parent.get_line_id_by_label(lbl)
                o.set_lw(lw0)
                o.set_mew(mw0)
                self.config_tabWidget.setCurrentIndex(
                        self.config_tabWidget.indexOf(self.curve_tab))
                self.line_id_cbb.setCurrentIndex(lnid)
                self.on_change_line_id(lnid)
            self.parent._last_sel_lines = {}

    @pyqtSlot(int)
    def set_marker_style(self, i):
        self.figMkStyleChanged.emit(MK_SYMBOL[i])

    @pyqtSlot(int)
    def on_change_line_id(self, i):
        self.figLineIDChanged.emit(i)
        self._set_line_config_panel(self.parent.get_line_config())

    def _set_line_config_panel(self, config):
        """Update line config panel when line id is switched."""
        # colors
        self.set_btn_color(self.line_color_btn, QColor(mplcolor2hex(config['c'])))
        self.set_btn_color(self.mk_edgecolor_btn, QColor(mplcolor2hex(config['mec'])))
        self.set_btn_color(self.mk_facecolor_btn, QColor(mplcolor2hex(config['mfc'])))
        # line style
        self.line_style_cbb.setCurrentText(LINE_STY_DICT[config['ls']])
        # line ds
        self.line_ds_cbb.setCurrentText(LINE_DS_DICT_R[config['drawstyle']])
        # marker style
        self.mk_style_cbb.setCurrentIndex(MK_SYMBOL.index(config['marker']))
        # line width
        self.line_width_lineEdit.setText('{}'.format(config['lw']))
        # marker size
        self.mk_size_lineEdit.setText('{}'.format(config['ms']))
        # mew
        self.mk_width_lineEdit.setText('{}'.format(config['mew']))
        # line label
        self.line_label_lineEdit.setText('{}'.format(config['label']))
        # line visible
        self.line_hide_chkbox.setChecked(not config['visible'])
        # opacity: alpha = opacity / 100
        opacity = config['alpha'] * 100
        self.opacity_val_slider.setValue(opacity)

    @pyqtSlot(int)
    def set_line_opacity(self, i):
        self.figLineAlphaChanged.emit(i / 100.0)

    @pyqtSlot('QString')
    def set_line_width(self, s):
        if s == '': return
        w = max(float(s), 0.05)
        self.figLineWidthChanged.emit(w)

    @pyqtSlot('QString')
    def set_marker_size(self, s):
        if s == '': return
        w = max(float(s), 1.0)
        self.figMkSizeChanged.emit(w)

    @pyqtSlot('QString')
    def set_marker_thickness(self, s):
        if s == '': return
        w = max(float(s), 0.1)
        self.figMkWidthChanged.emit(w)

    @pyqtSlot()
    def set_line_color(self):
        color = QColorDialog.getColor(self.parent.getLineColor())
        if color.isValid():
            self.figLineColorChanged.emit(color)

    @pyqtSlot()
    def set_mec(self):
        color = QColorDialog.getColor(self.parent.getMkEdgeColor())
        if color.isValid():
            self.figMkeColorChanged.emit(color)

    @pyqtSlot()
    def set_mfc(self):
        color = QColorDialog.getColor(self.parent.getMkFaceColor())
        if color.isValid():
            self.figMkfColorChanged.emit(color)

    @pyqtSlot(int)
    def set_legend(self, state):
        self.figLegendToggleChanged.emit(state == Qt.Checked)

    @pyqtSlot(int)
    def set_line_visible(self, state):
        self.figLineVisibleChanged.emit(state == Qt.Unchecked)


class MatplotlibConfigErrorbarPanel(MatplotlibConfigCurvePanel):
    # eb line id
    figEbLineIDChanged = pyqtSignal(int)

    # eb line
    figEbLineColorChanged = pyqtSignal(QColor)
    figEbLineWidthChanged = pyqtSignal(float)
    figEbLineVisibleChanged = pyqtSignal(bool)

    # eb marker
    figEbMkeColorChanged = pyqtSignal(QColor)
    figEbMkfColorChanged = pyqtSignal(QColor)
    figXEbMkStyleChanged = pyqtSignal('QString')
    figYEbMkStyleChanged = pyqtSignal('QString')
    figEbMkSizeChanged = pyqtSignal(float)
    figEbMkWidthChanged = pyqtSignal(float)

    def __init__(self, parent=None):
        super(MatplotlibConfigErrorbarPanel, self).__init__(parent)

        # show eb_tab
        self.config_tabWidget.setTabEnabled(
            self.config_tabWidget.indexOf(self.eb_tab), True)

        # eb_tab
        self.eb_line_id_cbb.currentIndexChanged[int].connect(
            self.on_change_eb_line_id)

        # events
        self.figEbLineIDChanged[int].connect(self.parent.setEbLineID)

        # eb line color
        self.figEbLineColorChanged[QColor].connect(self.set_eb_line_color_btn)
        self.figEbLineColorChanged[QColor].connect(self.parent.setEbLineColor)
        self.eb_line_color_btn.clicked.connect(self.set_eb_line_color)

        # line width
        self.eb_line_width_lineEdit.textChanged.connect(self.set_eb_line_width)
        self.figEbLineWidthChanged[float].connect(self.parent.setEbLineWidth)

        # eb line style
        self.eb_line_style_cbb.currentTextChanged['QString'].connect(
            self.parent.setEbLineStyle)

        # post UI
        ## BEGIN eb_line_id_cbb
        self.eb_line_id_cbb.clear()
        self.eb_line_id_cbb.addItems(
            [str(i) for i, l in enumerate(self.parent.get_all_eb_curves())])
        current_eb_line_id = self.parent.get_all_eb_curves().index(self.parent._eb_line)
        self.eb_line_id_cbb.setCurrentIndex(current_eb_line_id)
        ## END eb_line_id_cbb

        # eb_line_style_cbb
        self.eb_line_style_cbb.currentTextChanged['QString'].connect(
            self.parent.setEbLineStyle)

        self.eb_line_width_lineEdit.setValidator(QDoubleValidator(0, 50, 1, self))

        # cap mk style (x)
        self.xeb_mk_style_cbb.clear()
        self.xeb_mk_style_cbb.addItems(MK_CODE)
        self.figXEbMkStyleChanged['QString'].connect(self.parent.setXEbMarkerStyle)
        self.xeb_mk_style_cbb.currentIndexChanged[int].connect(
            self.set_xeb_marker_style)

        # cap mk style (y)
        self.yeb_mk_style_cbb.clear()
        self.yeb_mk_style_cbb.addItems(MK_CODE)
        self.figYEbMkStyleChanged['QString'].connect(self.parent.setYEbMarkerStyle)
        self.yeb_mk_style_cbb.currentIndexChanged[int].connect(
            self.set_yeb_marker_style)

        ## cap marker: mec
        self.figEbMkeColorChanged[QColor].connect(self.set_eb_mec_btn)
        self.figEbMkeColorChanged[QColor].connect(self.parent.setEbMkEdgeColor)
        self.eb_mk_edgecolor_btn.clicked.connect(self.set_eb_mec)
        ## cap marker: mfc
        self.figEbMkfColorChanged[QColor].connect(self.set_eb_mfc_btn)
        self.figEbMkfColorChanged[QColor].connect(self.parent.setEbMkFaceColor)
        self.eb_mk_facecolor_btn.clicked.connect(self.set_eb_mfc)
        # cap marker size
        self.eb_mk_size_lineEdit.setValidator(QDoubleValidator(0, 50, 1, self))
        self.eb_mk_width_lineEdit.setValidator(QDoubleValidator(0, 50, 1, self))
        self.eb_mk_size_lineEdit.textChanged.connect(self.set_eb_marker_size)
        self.figEbMkSizeChanged[float].connect(self.parent.setEbMarkerSize)
        # cap marker thickness
        self.eb_mk_width_lineEdit.textChanged.connect(self.set_eb_marker_thickness)
        self.figEbMkWidthChanged[float].connect(self.parent.setEbMarkerThickness)

        # eb line visibility
        self.eb_line_hide_chkbox.stateChanged.connect(self.set_eb_line_visible)
        self.figEbLineVisibleChanged[bool].connect(self.parent.setEbLineVisible)

        # set current eb line id
        self.on_change_eb_line_id(current_eb_line_id)

    @pyqtSlot(int)
    def set_eb_line_visible(self, state):
        self.figEbLineVisibleChanged.emit(state == Qt.Unchecked)

    @pyqtSlot('QString')
    def set_eb_line_width(self, s):
        if s == '': return
        w = max(float(s), 0.05)
        self.figEbLineWidthChanged.emit(w)

    @pyqtSlot('QString')
    def set_eb_marker_size(self, s):
        if s == '': return
        w = max(float(s), 1.0)
        self.figEbMkSizeChanged.emit(w)

    @pyqtSlot('QString')
    def set_eb_marker_thickness(self, s):
        if s == '': return
        w = max(float(s), 0.1)
        self.figEbMkWidthChanged.emit(w)

    @pyqtSlot()
    def set_eb_mec(self):
        color = QColorDialog.getColor(self.parent.getEbMkEdgeColor())
        if color.isValid():
            self.figEbMkeColorChanged.emit(color)

    @pyqtSlot(QColor)
    def set_eb_mec_btn(self, color):
        self.set_btn_color(self.eb_mk_edgecolor_btn, color)

    @pyqtSlot()
    def set_eb_mfc(self):
        color = QColorDialog.getColor(self.parent.getEbMkFaceColor())
        if color.isValid():
            self.figEbMkfColorChanged.emit(color)

    @pyqtSlot(QColor)
    def set_eb_mfc_btn(self, color):
        self.set_btn_color(self.eb_mk_facecolor_btn, color)

    @pyqtSlot(int)
    def set_xeb_marker_style(self, i):
        self.figXEbMkStyleChanged.emit(MK_SYMBOL[i])

    @pyqtSlot(int)
    def set_yeb_marker_style(self, i):
        self.figYEbMkStyleChanged.emit(MK_SYMBOL[i])

    @pyqtSlot(int)
    def on_change_eb_line_id(self, i):
        self.figEbLineIDChanged.emit(i)
        self._set_eb_line_config_panel(self.parent.get_eb_line_config())

    def _set_eb_line_config_panel(self, config):
        """Update line config for eb.
        """
        (xeb_left, xeb_right), xeb_line = config.get('xerr')
        (yeb_top, yeb_bottom), yeb_line = config.get('yerr')

        # xeb marker style
        self.xeb_mk_style_cbb.setCurrentIndex(MK_SYMBOL.index(xeb_left['marker']))
        # yeb marker style
        self.yeb_mk_style_cbb.setCurrentIndex(MK_SYMBOL.index(yeb_top['marker']))
        # eb marker color
        self.set_eb_mec_btn(QColor(mplcolor2hex(yeb_top['mec'])))
        self.set_eb_mfc_btn(QColor(mplcolor2hex(yeb_top['mfc'])))
        # cap marker size
        self.eb_mk_size_lineEdit.setText('{}'.format(yeb_top['ms']))
        # cap mew
        self.eb_mk_width_lineEdit.setText('{}'.format(yeb_top['mew']))

        # eb line color
        self.set_eb_line_color_btn(QColor(mplcolor2hex(yeb_line['color'])))
        # eb line width
        self.eb_line_width_lineEdit.setText('{}'.format(yeb_line['lw']))
        # eb line style can set, but does not sync to config panel
        # self.eb_line_style_cbb.setCurrentText(
        #        LINE_STY_DICT[str(config['line']['linestyle'])])

        # eb line visibility
        self.eb_line_hide_chkbox.setChecked(not yeb_line['visible'])

    @pyqtSlot()
    def set_eb_line_color(self):
        color = QColorDialog.getColor(self.parent.getEbLineColor())
        if color.isValid():
            self.figEbLineColorChanged.emit(color)

    @pyqtSlot(QColor)
    def set_eb_line_color_btn(self, color):
        self.set_btn_color(self.eb_line_color_btn, color)


class MatplotlibConfigImagePanel(MatplotlibConfigCurvePanel):
    def __init__(self, parent=None):
        super(MatplotlibConfigImagePanel, self).__init__(parent)

        self._post_setup()

    def _post_setup(self):
        """enable/disable controls
        """
        # show image_tab
        self.config_tabWidget.setTabEnabled(
            self.config_tabWidget.indexOf(self.image_tab), True)

        # disable axis scale
        self.xaxis_scale_cbb.currentIndexChanged.disconnect()
        self.yaxis_scale_cbb.currentIndexChanged.disconnect()
        self.xaxis_scale_cbb.setEnabled(False)
        self.yaxis_scale_cbb.setEnabled(False)

        # colormap cbb
        self.cmap_cbb.currentTextChanged.connect(
            self.on_cmap_changed)
        self.cmap_class_cbb.currentTextChanged.connect(
            self.on_cmap_class_changed)
        self.cmap_class_cbb.clear()
        self.cmap_class_cbb.addItems(COLORMAPS_DICT.keys())
        # reverse cmap chkbox
        self.reverse_cmap_chkbox.toggled.connect(self.on_reverse_cmap)
        self.reverse_cmap_chkbox.toggled.connect(self.parent.setReverseCMapToggle)

        # autoclim
        self.auto_clim_chkbox.toggled.connect(self.on_toggle_auto_clim)

        # colorbar toggle
        self.show_colorbar_chkbox.toggled.connect(self.parent.setColorBarToggle)
        self.show_colorbar_chkbox.toggled.connect(self.cb_orientation_cbb.setEnabled)
        self.show_colorbar_chkbox.toggled.connect(self.cb_orientation_lbl.setEnabled)
        self.cb_orientation_cbb.currentTextChanged.connect(self.parent.setColorBarOrientation)

        # sync current image config
        self.set_image_config()

        # connect signals/slots
        # connect: cmap_cbb -> parent.setColorMap
        self.cmap_cbb.currentTextChanged.connect(self.parent.setColorMap)
        # color range spinboxes
        self.cr_min_dSpinBox.valueChanged.connect(self.on_update_crmin)
        self.cr_max_dSpinBox.valueChanged.connect(self.on_update_crmax)
        self.cr_reset_tbtn.clicked.connect(self.reset_color_range)

    @pyqtSlot(bool)
    def on_toggle_auto_clim(self, auto_clim_enabled):
        self.parent.setAutoColorLimit(auto_clim_enabled)
        if not auto_clim_enabled:
            # apply current input [cmin, cmax]
            self.cr_min_dSpinBox.valueChanged.emit(self.cr_min_dSpinBox.value())

    @pyqtSlot(float)
    def on_update_crmin(self, x):
        crmax = self.cr_max_dSpinBox.value()
        try:
            assert x <= crmax
        except AssertionError:
            QMessageBox.warning(self, "Input Color Range",
                    "Color range input is invalid: {0:.3f} !<= {1:.3f}, reset it to {2:.3f}.".format(x, crmax, crmax),
                    QMessageBox.Ok)
            self.sender().setValue(crmax)
            return
        else:
            self.parent.setColorRangeMin(x)

    @pyqtSlot(float)
    def on_update_crmax(self, x):
        crmin = self.cr_min_dSpinBox.value()
        try:
            assert crmin <= x
        except AssertionError:
            QMessageBox.warning(self, "Input Color Range",
                    "Color range input is invalid: {0:.3f} !<= {1:.3f}, reset it to {2:.3f}.".format(crmin, x, crmin),
                    QMessageBox.Ok)
            self.sender().setValue(crmin)
            return
        else:
            self.parent.setColorRangeMax(x)

    @pyqtSlot()
    def reset_color_range(self):
        """Reset color range.
        """
        cr_min0, cr_max0 = self._color_range0
        self.cr_min_dSpinBox.setValue(cr_min0)
        self.cr_max_dSpinBox.setValue(cr_max0)

    def set_image_config(self):
        # colormap
        cmap = self.parent.getColorMap()
        rcmap = self.parent._rcmap
        rcmap_toggle = self.parent.getReverseCMapToggle()

        for k, v in COLORMAPS_DICT.items():
            if cmap in v:
                current_cmap_class = k

        self.cmap_class_cbb.setCurrentText(current_cmap_class)
        self.cmap_cbb.setCurrentText(cmap)

        self.reverse_cmap_chkbox.setChecked(rcmap_toggle)

        # color range
        self._set_color_range()

        # colorbar on/off
        self.show_colorbar_chkbox.setChecked(self.parent.getColorBarToggle())
        # colorbar orientation
        self.cb_orientation_cbb.setCurrentText(self.parent.getColorBarOrientation())
        # auto clim
        self.auto_clim_chkbox.setChecked(self.parent.getAutoColorLimit())

    def _set_color_range(self):
        # set color range.
        cr_min0, cr_max0 = get_array_range(self.parent.z)
        if np.ma.is_masked(cr_min0):
            return
        self._color_range0 = (cr_min0, cr_max0)
        cr_min = cr_min0 - (cr_max0 - cr_min0) * 10.0
        cr_max = cr_max0 + (cr_max0 - cr_min0) * 10.0
        single_step = (cr_max0 - cr_min0) / 100
        a, b, c = int(cr_min * 1000) / 1000, int(cr_max * 1000) / 1000, \
                  int(single_step * 1000) / 1000
        self.cr_min_dSpinBox.setDecimals(3)
        self.cr_max_dSpinBox.setDecimals(3)
        self.cr_min_dSpinBox.setRange(a, b)
        self.cr_max_dSpinBox.setRange(a, b)
        self.cr_min_dSpinBox.setSingleStep(c)
        self.cr_max_dSpinBox.setSingleStep(c)
        # initial values
        self.cr_min_dSpinBox.setValue(self.parent.getColorRangeMin())
        self.cr_max_dSpinBox.setValue(self.parent.getColorRangeMax())

    @pyqtSlot('QString')
    def on_cmap_class_changed(self, c):
        """Colormap class is changed.
        """
        self.cmap_cbb.currentTextChanged.disconnect(self.on_cmap_changed)
        self.cmap_cbb.clear()
        self.cmap_cbb.currentTextChanged.connect(self.on_cmap_changed)
        self.cmap_cbb.addItems(COLORMAPS_DICT.get(c))

    @pyqtSlot('QString')
    def on_cmap_changed(self, c):
        """Colormap is changed.
        """
        self.cm_image.set_cmap(c)

    @pyqtSlot(bool)
    def on_reverse_cmap(self, f):
        self.cm_image.set_reverse_cmap(f)


class MatplotlibConfigBarPanel(MatplotlibConfigCurvePanel):
    # eb color
    figEbLineColorChanged = pyqtSignal(QColor)
    # eb alpha
    figEbLineAlphaChanged = pyqtSignal(float)
    # eb lw
    figEbLineWidthChanged = pyqtSignal(float)
    # bar color
    figBarColorChanged = pyqtSignal(QColor)
    # bar alpha
    figBarAlphaChanged = pyqtSignal(float)
    # bar width
    figBarWidthChanged = pyqtSignal(float)

    # annotation config
    figAnnoteConfigChanged = pyqtSignal()

    def __init__(self, parent=None):
        super(MatplotlibConfigBarPanel, self).__init__(parent)
        self._post_setup()

    def _post_setup(self):
        """enable/disable controls
        """
        # show barchart tab
        self.config_tabWidget.setTabEnabled(
            self.config_tabWidget.indexOf(self.barchart_tab), True)

        self.ebline_width_lineEdit.setValidator(QDoubleValidator(0, 50, 1, self))
        self.bar_width_lineEdit.setValidator(QDoubleValidator(0, 50, 1, self))

        # events
        # ebline color
        self.figEbLineColorChanged[QColor].connect(self.set_ebline_color_btn)
        self.figEbLineColorChanged[QColor].connect(self.parent.setEbLineColor)
        self.ebline_color_btn.clicked.connect(self.set_ebline_color)

        # ebline opacity
        self.ebline_opacity_slider.valueChanged.connect(
            lambda i: self.ebline_opacity_lbl.setText('{}%'.format(i)))
        self.ebline_opacity_slider.valueChanged.connect(self.set_ebline_opacity)
        self.figEbLineAlphaChanged[float].connect(self.parent.setEbLineAlpha)

        # ebline linewidth
        self.ebline_width_lineEdit.textChanged.connect(self.set_ebline_width)
        self.figEbLineWidthChanged[float].connect(self.parent.setEbLineWidth)

        # ebline linestyle
        self.ebline_style_cbb.currentTextChanged['QString'].connect(
            self.parent.setEbLineStyle)

        # label
        self.label_lineEdit.textChanged.connect(self.parent.setLabel)

        # bar color
        self.figBarColorChanged[QColor].connect(self.set_bar_color_btn)
        self.figBarColorChanged[QColor].connect(self.parent.setBarColor)
        self.bar_color_btn.clicked.connect(self.set_bar_color)

        # bar opacity
        self.bar_opacity_slider.valueChanged.connect(
            lambda i: self.bar_opacity_lbl.setText('{}%'.format(i)))
        self.bar_opacity_slider.valueChanged.connect(self.set_bar_opacity)
        self.figBarAlphaChanged[float].connect(self.parent.setBarAlpha)

        # bar width
        self.bar_width_lineEdit.textChanged.connect(self.set_bar_width)
        self.figBarWidthChanged[float].connect(self.parent.setBarWidth)

        # annotation config
        self.annote_fontsize_sbox.valueChanged.connect(self.set_annote_fontsize)
        self.annote_angle_dsbox.valueChanged.connect(self.set_annote_angle)
        self.annote_bbox_alpha_dsbox.valueChanged.connect(self.set_annote_bbox_alpha)
        self.annote_fmt_lineEdit.returnPressed.connect(self.set_annote_fmt)
        self.figAnnoteConfigChanged.connect(self.parent.on_annote_config_changed)
        # reset annote fmt
        self.reset_annote_fmt_btn.clicked.connect(self.on_reset_annote_fmt)

        # set config
        self._set_barchart_config_panel(self.parent.get_barchart_config())

    @pyqtSlot()
    def on_reset_annote_fmt(self):
        self.annote_fmt_lineEdit.setText(self.parent._default_annote_fmt)
        self.annote_fmt_lineEdit.returnPressed.emit()

    @pyqtSlot(int)
    def set_annote_fontsize(self, i):
        """Update annotation font size.
        """
        self.parent.update_annote_config_dict(size=i)
        self.figAnnoteConfigChanged.emit()

    @pyqtSlot(float)
    def set_annote_angle(self, x):
        """Update annotation rotation angle in degree.
        """
        self.parent.update_annote_config_dict(rotation=x)
        self.figAnnoteConfigChanged.emit()

    @pyqtSlot(float)
    def set_annote_bbox_alpha(self, x):
        """Update annotation bbox alpha.
        """
        bbox_dict = self.parent._annote_config_dict.get('bbox_dict')
        bbox_dict.update({'alpha': x})
        self.parent.update_annote_config_dict(bbox_dict=bbox_dict)
        self.figAnnoteConfigChanged.emit()

    @pyqtSlot()
    def set_annote_fmt(self):
        self.parent.update_annote_config_dict(
                fmt=self.annote_fmt_lineEdit.text())
        self.figAnnoteConfigChanged.emit()

    @pyqtSlot('QString')
    def set_ebline_width(self, s):
        if s == '': return
        w = max(float(s), 0.05)
        self.figEbLineWidthChanged.emit(w)

    @pyqtSlot('QString')
    def set_bar_width(self, s):
        if s == '': return
        w = max(float(s), 0.05)
        self.figBarWidthChanged.emit(w)

    @pyqtSlot(int)
    def set_ebline_opacity(self, i):
        self.figEbLineAlphaChanged.emit(i / 100.0)

    @pyqtSlot(int)
    def set_bar_opacity(self, i):
        self.figBarAlphaChanged.emit(i / 100.0)

    @pyqtSlot()
    def set_ebline_color(self):
        color = QColorDialog.getColor(self.parent.getEbLineColor())
        if color.isValid():
            self.figEbLineColorChanged.emit(color)

    @pyqtSlot()
    def set_bar_color(self):
        color = QColorDialog.getColor(self.parent.getBarColor())
        if color.isValid():
            self.figBarColorChanged.emit(color)

    @pyqtSlot(QColor)
    def set_ebline_color_btn(self, color):
        self.set_btn_color(self.ebline_color_btn, color)

    @pyqtSlot(QColor)
    def set_bar_color_btn(self, color):
        self.set_btn_color(self.bar_color_btn, color)

    def _set_barchart_config_panel(self, config):
        eb_color = mplcolor2hex(config.get('eb_color'))
        eb_alpha = config.get('eb_alpha')
        eb_lw = config.get('eb_lw')
        eb_ls = config.get('eb_ls')
        bar_color = mplcolor2hex(config.get('bar_color'))
        bar_alpha = config.get('bar_alpha')
        bar_width = config.get('bar_width')
        label = config.get('label')
        annote_config = config.get('annote_config')

        eb_opacity = 100 if eb_alpha is None else eb_alpha * 100
        bar_opacity = 100 if bar_alpha is None else bar_alpha * 100

        # eb color
        self.figEbLineColorChanged.emit(QColor(eb_color))
        # eb alpha
        self.ebline_opacity_slider.setValue(eb_opacity)
        # eb lw
        self.ebline_width_lineEdit.setText('{}'.format(eb_lw))
        # eb ls
        self.ebline_style_cbb.setCurrentText(eb_ls)
        # label
        self.label_lineEdit.setText('{}'.format(label))
        # bar color
        self.figBarColorChanged.emit(QColor(bar_color))
        # bar alpha
        self.bar_opacity_slider.setValue(bar_opacity)
        # bar width
        self.bar_width_lineEdit.setText('{}'.format(bar_width))

        # annotations
        fontsize = annote_config['size']
        angle = annote_config['rotation']
        bbox_alpha = annote_config['bbox_dict']['alpha']
        fmt = annote_config['fmt']
        self.annote_fontsize_sbox.setValue(fontsize)
        self.annote_angle_dsbox.setValue(angle)
        self.annote_bbox_alpha_dsbox.setValue(bbox_alpha)
        self.annote_fmt_lineEdit.setText(fmt)


def select_font(obj, current_font, options=None):
    """Select font slot.

    Parameters
    ----------
    obj :
        Widget object, which is the parent of the font dialog.
    current_font : QFont
        Current font, which is the initial font of font dialog.
    options :
        QFont options, see QFontDialog.FontDialogOptions.
    """
    if options is None:
        options = QFontDialog.FontDialogOptions(0)
    font, ok = QFontDialog.getFont(current_font, obj, "", options)
    return font, ok


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    frame = MatplotlibConfigPanel()
    frame.show()
    sys.exit(app.exec_())
