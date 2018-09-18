# -*- coding: utf-8 -*-

"""
Navigation toolbar for matplotlib widgets
"""

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as Toolbar

from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt, pyqtSlot
from mpl4qt.icons import exit_tool_icon
from mpl4qt.icons import home_tool_icon
from mpl4qt.icons import zoom_tool_icon
from mpl4qt.icons import save_tool_icon


class NavigationToolbar(Toolbar):
    def __init__(self, canvas, parent=None):
        super(self.__class__, self).__init__(canvas, parent)


class ToolbarDialog(QDialog):
    def __init__(self, canvas, parent=None):
        super(ToolbarDialog, self).__init__()
        self.parent = parent
        self.canvas = canvas

        self.init_ui()
        self.show_dialog()

    def show_dialog(self):
        self.adjustSize()
        self.show()
        self.raise_()
        self.move(self.get_pos())

    def init_ui(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.tb = tb = NavigationToolbar(self.canvas, self)
        tb.hide()

        # exit tool
        exit_btn = QPushButton("", self)
        exit_icon = QIcon(QPixmap(exit_tool_icon))
        exit_btn.setIcon(exit_icon)
        exit_btn.setToolTip("Exit this toolbar")

        # zoom tool
        zoom_btn = QPushButton("", self)
        zoom_icon = QIcon(QPixmap(zoom_tool_icon))
        zoom_btn.setIcon(zoom_icon)
        zoom_btn.setCheckable(True)
        self.zoom_btn = zoom_btn
        zoom_btn.setToolTip("Zoom into selected region")

        # home tool
        home_btn = QPushButton("", self)
        home_icon = QIcon(QPixmap(home_tool_icon))
        home_btn.setIcon(home_icon)
        home_btn.setToolTip("Reset to original")

        # save tool
        save_btn = QPushButton("", self)
        save_icon = QIcon(QPixmap(save_tool_icon))
        save_btn.setIcon(save_icon)
        save_btn.setToolTip("Save figure as file")

        # layout
        hbox = QHBoxLayout()
        hbox.addWidget(tb)
        hbox.addWidget(home_btn)
        hbox.addWidget(zoom_btn)
        hbox.addWidget(save_btn)
        hbox.addWidget(exit_btn)
        self.setLayout(hbox)

        # events
        home_btn.clicked.connect(self.home)
        zoom_btn.toggled.connect(self.zoom)
        exit_btn.clicked.connect(self.close)
        save_btn.clicked.connect(self.save)

    @pyqtSlot()
    def zoom(self):
        self.tb.zoom()

    @pyqtSlot()
    def home(self):
        self.tb.home()

    @pyqtSlot()
    def save(self):
        self.tb.save_figure()

    def closeEvent(self, e):
        if self.zoom_btn.isChecked():
            self.zoom_btn.setChecked(False) # emit toggled
        self.close()

    def get_pos(self):
        """Get the position to put this dialog in the middle of the parent
        widget.
        """
        x = self.parent.geometry().x() + 0.5 * (
                self.parent.geometry().width() - self.geometry().width())
        y = self.parent.geometry().y()
        return self.parent.mapToGlobal(QPoint(x, y))
