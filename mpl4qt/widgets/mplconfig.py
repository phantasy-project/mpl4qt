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

from mpl4qt.ui.ui_mplconfig import Ui_Dialog


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
        self.figTightLayoutChanged[bool].connect(self.parent.setTightLayoutToggle)
        self.figXminLimitChanged[float].connect(self.parent.setXLimitMin)
        self.figXmaxLimitChanged[float].connect(self.parent.setXLimitMax)
        self.figYminLimitChanged[float].connect(self.parent.setYLimitMin)
        self.figYmaxLimitChanged[float].connect(self.parent.setYLimitMax)

        ## xy label
        self.figXYlabelFontChanged[QFont].connect(self.parent.setFigureXYlabelFont)
        self.fig_xlabel_lineEdit.textChanged.connect(self.parent.setFigureXlabel)
        self.fig_ylabel_lineEdit.textChanged.connect(self.parent.setFigureYlabel)

        ## title
        self.fig_title_lineEdit.textChanged.connect(self.parent.setFigureTitle)
        self.figTitleFontChanged.connect(self.parent.setFigureTitleFont)

        # xy ticks
        self.figXYticksFontChanged.connect(self.parent.setFigureXYticksFont)
        self.figXYticksColorChanged[QColor].connect(self.parent.setFigureXYticksColor)
        self.figXYticksColorChanged[QColor].connect(self.set_ticks_color_label)
        self.mticks_chkbox.stateChanged.connect(self.set_fig_mticks)
        self.figMTicksChanged[bool].connect(self.parent.setFigureMTicksToggle)

        # grid
        self.figGridChanged[bool].connect(lambda x: self.parent.setFigureGridToggle(x, mticks=self.mticks_chkbox.isChecked()))
        self.figGridColorChanged[QColor].connect(lambda x: self.parent.setFigureGridColor(x, mticks=self.mticks_chkbox.isChecked(), toggle_checked=self.gridon_chkbox.isChecked()))
        self.figGridColorChanged[QColor].connect(self.set_grid_color_btn)
        self.gridon_chkbox.stateChanged.connect(self.set_fig_grid)
        self.grid_color_btn.clicked.connect(self.set_grid_color)

        # post UI update
        self.post_init_ui()

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

    def set_xylimits(self, xlim=None, ylim=None):
        """Set xy limits.
        """
        xmin, xmax = self.parent.get_xlim()
        ymin, ymax = self.parent.get_ylim()
        self.xmin_lineEdit.setText('{0:3g}'.format(xmin))
        self.xmax_lineEdit.setText('{0:3g}'.format(xmax))
        self.ymin_lineEdit.setText('{0:3g}'.format(ymin))
        self.ymax_lineEdit.setText('{0:3g}'.format(ymax))

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
    def set_grid_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.figGridColorChanged.emit(color)

    @pyqtSlot(QColor)
    def set_grid_color_btn(self, color):
        self.grid_color_btn.setStyleSheet(
            "QPushButton {\n"
            "  margin: 1px;\n"
            "  border-color: rgb(0, 85, 0);\n"
            "  border-style: outset;\n"
            "  border-radius: 3px;\n"
            "  border-width: 1px;\n"
            "  color: black;\n"
            "  background-color: %s;\n" % color.name() +
            "}\n"
            "QPushButton:pressed {\n"
            "  background-color: white;\n"
            "}")

    @pyqtSlot(int)
    def set_fig_grid(self, state):
        self.figGridChanged.emit(state==Qt.Checked)

    @pyqtSlot(int)
    def set_fig_mticks(self, state):
        self.figMTicksChanged.emit(state==Qt.Checked)

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
        if s=='': return
        w = max(int(s), 2)
        self.figWidthChanged.emit(w)

    @pyqtSlot('QString')
    def set_figsize_height(self, s):
        if s=='': return
        h = max(int(s), 2)
        self.figHeightChanged.emit(h)

    @pyqtSlot('QString')
    def set_figdpi(self, s):
        if s=='': return
        d = max(int(s), 20)
        self.figDpiChanged.emit(d)

    @pyqtSlot(int)
    def set_fig_autoscale(self, state):
        self.figAutoScaleChanged.emit(state==Qt.Checked)
        self.show_xyrange_box(state!=Qt.Checked)

    def show_xyrange_box(self, b):
        """Show widgets in xyrange box or not.
        """
        widgets = (self.xmin_lbl, self.xmax_lbl,
                   self.ymin_lbl, self.ymax_lbl,
                   self.xmin_lineEdit, self.xmax_lineEdit,
                   self.ymin_lineEdit, self.ymax_lineEdit)
        [w.setEnabled(b) for w in widgets]

    @pyqtSlot(int)
    def set_fig_tightlayout(self, state):
        self.figTightLayoutChanged.emit(state==Qt.Checked)

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
