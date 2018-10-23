# -*- coding: utf-8 -*-

"""
Navigation toolbar for matplotlib widgets
"""

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as Toolbar
from matplotlib.path import Path
from matplotlib.widgets import LassoSelector
import numpy as np

from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QVariant, QObject
from mpl4qt.icons import exit_tool_icon
from mpl4qt.icons import home_tool_icon
from mpl4qt.icons import zoom_tool_icon
from mpl4qt.icons import save_tool_icon
from mpl4qt.icons import lasso_tool_icon


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

        # lasso tool
        lasso_btn = QPushButton("", self)
        lasso_icon = QIcon(QPixmap(lasso_tool_icon))
        lasso_btn.setIcon(lasso_icon)
        lasso_btn.setCheckable(True)
        lasso_btn.setToolTip("Select point(s) by lasso")

        # layout
        hbox = QHBoxLayout()
        hbox.addWidget(tb)
        hbox.addWidget(home_btn)
        hbox.addWidget(zoom_btn)
        hbox.addWidget(lasso_btn)
        hbox.addWidget(save_btn)
        hbox.addWidget(exit_btn)
        self.setLayout(hbox)

        # events
        home_btn.clicked.connect(self.home)
        zoom_btn.toggled.connect(self.zoom)
        lasso_btn.clicked.connect(self.lasso)
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

    @pyqtSlot()
    def lasso(self):
        if self.sender().isChecked():
            _x = self.parent.getXData()
            _y = self.parent.getYData()
            pts = np.vstack([_x, _y]).T
            ax = self.parent.axes
            self.selector = SelectFromPoints(ax, pts)
            self.selector.selectedIndicesReady.connect(self.show_selected_indices)
        else:
            self.selector.disconnect()
            self.selector.selectedIndicesReady.disconnect()

    @pyqtSlot(QVariant)
    def show_selected_indices(self, x):
        print(x)

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


class SelectFromPoints(QObject):
    """Select indices from points using `LassoSelector`.
    """
    selectedIndicesReady = pyqtSignal(QVariant)
    def __init__(self, ax, points, alpha_other=0.3, radius=0):
        super(SelectFromPoints, self).__init__()
        self.canvas = ax.figure.canvas
        self.points = points
        self.alpha_other = alpha_other
        self.radius = radius

        self.lasso = LassoSelector(ax, onselect=self.on_select)

    def on_select(self, verts):
        path = Path(verts)
        ind = np.nonzero(
                path.contains_points(self.points, radius=self.radius))[0]
        self.canvas.draw_idle()
        self.selectedIndicesReady.emit(ind)

    def disconnect(self):
        self.lasso.disconnect_events()
        self.canvas.draw_idle()
