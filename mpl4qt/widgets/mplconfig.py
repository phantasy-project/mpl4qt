#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configuration widget for matplotlib.
"""
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtWidgets import QFontDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIntValidator
from PyQt5.QtGui import QDoubleValidator

from mpl4qt.ui.ui_mplconfig import Ui_Dialog
from .utils import mplcolor2hex
from .utils import MK_CODE
from .utils import MK_SYMBOL
from .utils import LINE_STY_DICT
from .utils import SCALE_STY_KEYS
from .utils import SCALE_STY_VALS
from .utils import generate_formatter
from .utils import AUTOFORMATTER
from .utils import AUTOFORMATTER_MATHTEXT


class MatplotlibConfigPanel(QDialog, Ui_Dialog):
    # fig size and color
    bgcolorChanged = pyqtSignal(QColor)
    figWidthChanged = pyqtSignal(int)
    figHeightChanged = pyqtSignal(int)
    figDpiChanged = pyqtSignal(int)

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

    # line id
    figLineIDChanged = pyqtSignal(int)

    # line
    figLineColorChanged = pyqtSignal(QColor)
    figLineWidthChanged = pyqtSignal(float)
    figLineVisibleChanged = pyqtSignal(bool)

    # marker
    figMkeColorChanged = pyqtSignal(QColor)
    figMkfColorChanged = pyqtSignal(QColor)
    figMkStyleChanged = pyqtSignal('QString')
    figMkSizeChanged = pyqtSignal(float)
    figMkWidthChanged = pyqtSignal(float)

    # legend
    figLegendToggleChanged = pyqtSignal(bool)

    # color opacity
    figLineAlphaChanged = pyqtSignal(float)

    def __init__(self, parent=None):
        super(MatplotlibConfigPanel, self).__init__()
        self.parent = parent
        #self.setParent(parent)

        # UI
        self.setupUi(self)
        self.setWindowTitle("Figure Configurations")

        # hide eb_tab or not
        self.config_tabWidget.setTabEnabled(
            self.config_tabWidget.indexOf(self.eb_tab), False)
        # set the style sheet
        self.setStyleSheet(
            "QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")

        self.figWidth_lineEdit.setValidator(QIntValidator(2, 20, self))
        self.figHeight_lineEdit.setValidator(QIntValidator(2, 20, self))
        self.figDpi_lineEdit.setValidator(QIntValidator(50, 500, self))
        self.line_width_lineEdit.setValidator(QDoubleValidator(0, 50, 1, self))
        self.mk_size_lineEdit.setValidator(QDoubleValidator(0, 50, 1, self))
        self.mk_width_lineEdit.setValidator(QDoubleValidator(0, 50, 1, self))

        # events
        self.bkgd_color_btn.clicked.connect(self.set_fig_bkgdcolor)
        self.ticks_color_btn.clicked.connect(self.set_fig_xyticks_color)
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
        # line visible
        self.line_hide_chkbox.stateChanged.connect(self.set_line_visible)
        # opacity
        self.opacity_val_slider.valueChanged.connect(
                lambda i: self.opacity_val_lbl.setText('{}%'.format(i)))
        self.opacity_val_slider.valueChanged.connect(self.set_line_opacity)

        # link to main mpl widget
        self.bgcolorChanged[QColor].connect(self.set_bgcolor_label)
        self.bgcolorChanged[QColor].connect(self.parent.setFigureBgColor)
        self.figWidthChanged[int].connect(self.parent.setFigureWidth)
        self.figHeightChanged[int].connect(self.parent.setFigureHeight)
        self.figDpiChanged[int].connect(self.parent.setFigureDpi)
        self.figAutoScaleChanged[bool].connect(self.parent.setFigureAutoScale)
        self.figTightLayoutChanged[bool].connect(
            self.parent.setTightLayoutToggle)
        self.figXminLimitChanged[float].connect(self.parent.setXLimitMin)
        self.figXmaxLimitChanged[float].connect(self.parent.setXLimitMax)
        self.figYminLimitChanged[float].connect(self.parent.setYLimitMin)
        self.figYmaxLimitChanged[float].connect(self.parent.setYLimitMax)
        self.figLineVisibleChanged[bool].connect(self.parent.setLineVisible)

        # line opacity
        self.figLineAlphaChanged[float].connect(self.parent.setLineAlpha)

        ## xy label
        self.figXYlabelFontChanged[QFont].connect(
            self.parent.setFigureXYlabelFont)
        self.fig_xlabel_lineEdit.textChanged.connect(
            self.parent.setFigureXlabel)
        self.fig_ylabel_lineEdit.textChanged.connect(
            self.parent.setFigureYlabel)

        ## title
        self.fig_title_lineEdit.textChanged.connect(self.parent.setFigureTitle)
        self.figTitleFontChanged.connect(self.parent.setFigureTitleFont)

        # xy ticks
        self.figXYticksFontChanged.connect(self.parent.setFigureXYticksFont)
        self.figXYticksColorChanged[QColor].connect(
            self.parent.setFigureXYticksColor)
        self.figXYticksColorChanged[QColor].connect(self.set_ticks_color_label)
        self.mticks_chkbox.stateChanged.connect(self.set_fig_mticks)
        self.figMTicksChanged[bool].connect(self.parent.setFigureMTicksToggle)

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
        self.figGridChanged[bool].connect(lambda x: self.parent.setFigureGridToggle(x, mticks=self.mticks_chkbox.isChecked()))
        self.figGridColorChanged[QColor].connect(lambda x: self.parent.setFigureGridColor(x, mticks=self.mticks_chkbox.isChecked(), toggle_checked=self.gridon_chkbox.isChecked()))
        self.figGridColorChanged[QColor].connect(self.set_grid_color_btn)
        self.gridon_chkbox.stateChanged.connect(self.set_fig_grid)
        self.grid_color_btn.clicked.connect(self.set_grid_color)

        # legend
        self.legend_on_chkbox.stateChanged.connect(self.set_legend)
        self.figLegendToggleChanged[bool].connect(self.parent.setLegendToggle)
        self.legend_loc_cbb.currentIndexChanged[int].connect(
            self.parent.setLegendLocation)

        # post UI update
        self.post_init_ui()

        # line id, put after post_init_ui, elliminate cb initialization disturb
        self.figLineIDChanged[int].connect(self.parent.setLineID)
        self.line_id_cbb.currentIndexChanged[int].connect(
            self.on_change_line_id)

        # line color
        self.figLineColorChanged[QColor].connect(self.set_line_color_btn)
        self.figLineColorChanged[QColor].connect(self.parent.setLineColor)
        self.line_color_btn.clicked.connect(self.set_line_color)
        # line style
        self.line_style_cbb.currentTextChanged['QString'].connect(
            self.parent.setLineStyle)
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
        self.figMkeColorChanged[QColor].connect(self.set_mec_btn)
        self.figMkeColorChanged[QColor].connect(self.parent.setMkEdgeColor)
        self.mk_edgecolor_btn.clicked.connect(self.set_mec)
        # marker: mfc
        self.figMkfColorChanged[QColor].connect(self.set_mfc_btn)
        self.figMkfColorChanged[QColor].connect(self.parent.setMkFaceColor)
        self.mk_facecolor_btn.clicked.connect(self.set_mfc)

        # axis scale
        self.xaxis_scale_cbb.currentIndexChanged.connect(
                lambda i: self.parent.setFigureXScale(SCALE_STY_VALS[i]))
        self.yaxis_scale_cbb.currentIndexChanged.connect(
                lambda i: self.parent.setFigureYScale(SCALE_STY_VALS[i]))

        # sizer
        self.adjustSize()

    def post_init_ui(self):
        self.set_bgcolor_label(self.parent.getFigureBgColor())
        self.set_ticks_color_label(self.parent.getFigureXYticksColor())
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
        self.gridon_chkbox.setChecked(self.parent.getFigureGridToggle())
        self.set_grid_color_btn(self.parent.getFigureGridColor())
        self.set_xylimits()
        # marker style
        self.mk_style_cbb.clear()
        self.mk_style_cbb.addItems(MK_CODE)
        # line id combo
        self.line_id_cbb.clear()
        self.line_id_cbb.addItems(
            [str(i) for i, l in enumerate(self.parent.get_all_curves())])
        current_line_id = self.parent.get_all_curves().index(self.parent._line)
        self.line_id_cbb.setCurrentIndex(current_line_id)
        self.on_change_line_id(current_line_id)
        # legend on/off
        self.legend_on_chkbox.setChecked(self.parent.getLegendToggle())
        self.legend_loc_cbb.setCurrentIndex(self.parent.getLegendLocation())
        # line visible
        self.line_hide_chkbox.setChecked(not self.parent.getLineVisible())
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
            QMessageBox.warning(self, "", "Empty input is not valid.", QMessageBox.Ok)
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
        self.set_line_color_btn(QColor(mplcolor2hex(config['c'])))
        self.set_mec_btn(QColor(mplcolor2hex(config['mec'])))
        self.set_mfc_btn(QColor(mplcolor2hex(config['mfc'])))
        # line style
        self.line_style_cbb.setCurrentText(LINE_STY_DICT[config['ls']])
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
        alpha = config['alpha']
        opacity = 100 if alpha is None else alpha*100
        self.opacity_val_slider.setValue(opacity)

    @pyqtSlot(int)
    def set_line_opacity(self, i):
        self.figLineAlphaChanged.emit(i/100.0)

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
            self.figYminLimitChanged.emit(float(s))
        except:
            pass

    @pyqtSlot('QString')
    def set_ylimit_max(self, s):
        try:
            x = float(s)
            self.figYmaxLimitChanged.emit(float(s))
        except:
            pass

    @pyqtSlot()
    def set_line_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.figLineColorChanged.emit(color)

    @pyqtSlot(QColor)
    def set_line_color_btn(self, color):
        self._set_btn_color(self.line_color_btn, color)

    @pyqtSlot()
    def set_mec(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.figMkeColorChanged.emit(color)

    @pyqtSlot(QColor)
    def set_mec_btn(self, color):
        self._set_btn_color(self.mk_edgecolor_btn, color)

    @pyqtSlot()
    def set_mfc(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.figMkfColorChanged.emit(color)

    @pyqtSlot(QColor)
    def set_mfc_btn(self, color):
        self._set_btn_color(self.mk_facecolor_btn, color)

    @pyqtSlot()
    def set_grid_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.figGridColorChanged.emit(color)

    @pyqtSlot(QColor)
    def set_grid_color_btn(self, color):
        self._set_btn_color(self.grid_color_btn, color)

    @staticmethod
    def _set_btn_color(btn, color):
        """Set the button with giving color.
        """
        btn.setStyleSheet("QPushButton {\n"
                          "  margin: 1px;\n"
                          "  border-color: rgb(0, 85, 0);\n"
                          "  border-style: outset;\n"
                          "  border-radius: 3px;\n"
                          "  border-width: 1px;\n"
                          "  color: black;\n"
                          "  background-color: %s;\n" % color.name() + "}\n"
                          "QPushButton:pressed {\n"
                          "  background-color: white;\n"
                          "}")

    @pyqtSlot(int)
    def set_fig_grid(self, state):
        self.figGridChanged.emit(state == Qt.Checked)

    @pyqtSlot(int)
    def set_legend(self, state):
        self.figLegendToggleChanged.emit(state == Qt.Checked)

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
    def set_fig_bkgdcolor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.bgcolorChanged.emit(color)

    @pyqtSlot()
    def set_fig_xyticks_color(self):
        color = QColorDialog.getColor()
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
        w = max(int(s), 2)
        self.figWidthChanged.emit(w)

    @pyqtSlot('QString')
    def set_figsize_height(self, s):
        if s == '': return
        h = max(int(s), 2)
        self.figHeightChanged.emit(h)

    @pyqtSlot('QString')
    def set_figdpi(self, s):
        if s == '': return
        d = max(int(s), 20)
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

    @pyqtSlot(int)
    def set_line_visible(self, state):
        self.figLineVisibleChanged.emit(state==Qt.Unchecked)

    @pyqtSlot(QColor)
    def set_bgcolor_label(self, color):
        self.bkgd_color_label.setText(color.name().upper())
        self.bkgd_color_label.setStyleSheet(
            "QLabel {\n"
            "  background-color: %s;\n" % color.name() +
            "  border-radius: 5px;\n"
            "}")

    @pyqtSlot(QColor)
    def set_ticks_color_label(self, color):
        self.ticks_color_label.setText(color.name().upper())
        self.ticks_color_label.setStyleSheet(
            "QLabel {\n"
            "  background-color: %s;\n" % color.name() +
            "  border-radius: 5px;\n"
            "}")


class MatplotlibConfigErrorbarPanel(MatplotlibConfigPanel):
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

        # hide eb_tab or not
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
        self.figEbLineVisibleChanged.emit(state==Qt.Unchecked)

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
        color = QColorDialog.getColor()
        if color.isValid():
            self.figEbMkeColorChanged.emit(color)

    @pyqtSlot(QColor)
    def set_eb_mec_btn(self, color):
        self._set_btn_color(self.eb_mk_edgecolor_btn, color)

    @pyqtSlot()
    def set_eb_mfc(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.figEbMkfColorChanged.emit(color)

    @pyqtSlot(QColor)
    def set_eb_mfc_btn(self, color):
        self._set_btn_color(self.eb_mk_facecolor_btn, color)

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
        #self.eb_line_style_cbb.setCurrentText(
        #        LINE_STY_DICT[str(config['line']['linestyle'])])

        # eb line visibility
        self.eb_line_hide_chkbox.setChecked(not yeb_line['visible'])

    @pyqtSlot()
    def set_eb_line_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.figEbLineColorChanged.emit(color)

    @pyqtSlot(QColor)
    def set_eb_line_color_btn(self, color):
        self._set_btn_color(self.eb_line_color_btn, color)


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
