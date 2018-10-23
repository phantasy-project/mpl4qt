# -*- coding: utf-8 -*-

"""
Navigation toolbar for matplotlib widgets
"""

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as Toolbar
from matplotlib.path import Path
from matplotlib.widgets import LassoSelector
import numpy as np

from PyQt5.QtWidgets import QToolBar, QAction
from PyQt5.QtGui import QIcon, QPixmap
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


class MToolbar(QToolBar):

    def __init__(self, canvas, parent=None):
        super(MToolbar, self).__init__()
        self.parent = parent
        self.canvas = canvas

        self.init_ui()
        self.show_toolbar()

    def show_toolbar(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMovable(True)
        self.setFloatable(True)
        self.show()
        self.move(self.get_pos())

    def init_ui(self):

        self.setStyleSheet("""
                QToolBar {
                    background-color: white;
                    border-radius: 6px;
                    border-bottom: 2px solid #8f8f91;
                    border-top: 2px solid #8f8f91;
                    spacing: 5px;
                }
                """)

        self.tb = tb = NavigationToolbar(self.canvas, self)
        tb.hide()

        # zoom tool
        zoom_act = QAction(QIcon(QPixmap(zoom_tool_icon)), "Zoom", self)
        zoom_act.setCheckable(True)
        self.zoom_act = zoom_act
        zoom_act.setToolTip("Zoom into selected region")

        # home tool
        home_act = QAction(QIcon(QPixmap(home_tool_icon)), "Home", self)
        home_act.setToolTip("Reset to original")

        # save tool
        save_act = QAction(QIcon(QPixmap(save_tool_icon)), "Save", self)
        save_act.setToolTip("Save figure as file")

        # lasso tool
        lasso_act = QAction(QIcon(QPixmap(lasso_tool_icon)), "Selector", self)
        self.lasso_act = lasso_act
        lasso_act.setCheckable(True)
        lasso_act.setToolTip("Select point(s) by lasso")

        # exit tool
        exit_act = QAction(QIcon(QPixmap(exit_tool_icon)), "Exit", self)
        exit_act.setToolTip("Exit this toolbar")

        self.addAction(home_act)
        self.addAction(zoom_act)
        self.addAction(lasso_act)
        self.addAction(save_act)
        self.addSeparator()
        self.addAction(exit_act)

        # events
        home_act.triggered.connect(self.home)
        zoom_act.toggled.connect(self.zoom)
        lasso_act.toggled.connect(self.lasso)
        save_act.triggered.connect(self.save)
        exit_act.triggered.connect(self.close)

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
        """
        """
        print(x)

    def closeEvent(self, e):
        if self.lasso_act.isChecked():
            self.lasso_act.setChecked(False)
        if self.zoom_act.isChecked():
            self.zoom_act.setChecked(False) # emit toggled
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
