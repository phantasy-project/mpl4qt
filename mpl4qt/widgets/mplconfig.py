#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configuration widget for matplotlib.
"""
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtWidgets import QFontDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIntValidator
from PyQt5.QtGui import QDoubleValidator

from mpl4qt.ui.ui_mplconfig import Ui_Dialog
from .utils import mplcolor2hex
from .utils import MK_CODE
from .utils import MK_SYMBOL
from .utils import LINE_STY_DICT


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

    # marker
    figMkeColorChanged = pyqtSignal(QColor)
    figMkfColorChanged = pyqtSignal(QColor)
    figMkStyleChanged = pyqtSignal('QString')
    figMkSizeChanged = pyqtSignal(float)
    figMkWidthChanged = pyqtSignal(float)

    # legend
    figLegendToggleChanged = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(MatplotlibConfigPanel, self).__init__()
        self.parent = parent
        #self.setParent(parent)

        # UI
        self.setupUi(self)
        self.setWindowTitle("Figure Configurations")

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
        font, ok = QFontDialog(self.parent.getFigureXYlabelFont()).getFont()
        if ok:
            self.figXYlabelFontChanged.emit(font)

    @pyqtSlot()
    def set_xy_ticks_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.xy_ticks_sample_lbl.setFont(font)
            self.figXYticksFontChanged.emit(font)

    @pyqtSlot()
    def set_title_font(self):
        current_font = self.parent.getFigureTitleFont()
        d = QFontDialog()
        d.setCurrentFont(current_font)  # does not work
        font, ok = d.getFont()
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


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    frame = MatplotlibConfigPanel()
    frame.show()
    sys.exit(app.exec_())
