# -*- coding: utf-8 -*-

"""
Navigation toolbar for matplotlib widgets
"""

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as Toolbar
from matplotlib.path import Path
from matplotlib.widgets import LassoSelector
import numpy as np

from PyQt5.QtWidgets import QToolBar, QAction, QLabel
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QVariant, QObject
from mpl4qt.icons import exit_tool_icon
from mpl4qt.icons import home_tool_icon
from mpl4qt.icons import zoom_tool_icon
from mpl4qt.icons import save_tool_icon
from mpl4qt.icons import lasso_tool_icon
from mpl4qt.icons import repos_tool_icon
from mpl4qt.icons import cross_tool_icon


class NavigationToolbar(Toolbar):
    def __init__(self, canvas, parent=None):
        super(self.__class__, self).__init__(canvas, parent)


class MToolbarWidget(QWidget):
    def __init__(self, canvas, parent=None):
        super(MToolbarWidget, self).__init__()

        self.tb = MToolbar(canvas, parent)
        layout = QVBoxLayout()
        #layout.setMenuBar(self.tb)
        layout.addWidget(self.tb)

        self.setLayout(layout)

    def show_widget(self):
        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.move(self.tb.get_pos())
        self.show()
        self.raise_()


class MToolbar(QToolBar):
    """Toolbar for mpl widgets.

    Parameters
    ----------
    canvas :
        Canvas for drawing.
    parent :
        Mpl figure widget.
    """

    # indices list of points selected by lasso tool
    selectedIndicesUpdated = pyqtSignal(QVariant, QVariant)

    def __init__(self, canvas, parent=None):
        super(MToolbar, self).__init__()
        self.parent = parent
        self.canvas = canvas

        self.init_ui()
        # window flags
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

    def show_toolbar(self):
        self.move(self.get_pos())
        self.show()
        self.raise_()

    def init_ui(self):

        self.setStyleSheet("""
                QToolBar {
                    background-color: white;
                    border-radius: 6px;
                    border-bottom: 2px solid #8f8f91;
                    border-top: 2px solid #8f8f91;
                    spacing: 5px;
                    padding: 10px;
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
        lasso_act.setToolTip("Select point(s) by lassoing")

        # cross ruler tool
        cross_act = QAction(QIcon(QPixmap(cross_tool_icon)), "Cross ruler", self)
        cross_act.setCheckable(True)
        cross_act.setToolTip("Cross ruler for locating coordinate")

        # exit tool
        exit_act = QAction(QIcon(QPixmap(exit_tool_icon)), "Exit", self)
        exit_act.setToolTip("Exit toolbar")

        # repos to center (toolbar) tool
        repos_act = QAction(QIcon(QPixmap(repos_tool_icon)), "Repos", self)
        repos_act.setToolTip(
            "Reposition toolbar wrt figure widget, drag & move to otherwhere")

        # pos display tool
        self.pos_lbl = QLabel(self)
        self.pos_lbl.setToolTip("Pointed (x, y) coordinate")
        self.pos_lbl.setStyleSheet("""
            QLabel {
                font-family: monospace;
                color: black;
            }
            """)
        self.parent.xyposUpdated.connect(self.on_update_xypos)

        self.addAction(home_act)
        self.addAction(zoom_act)
        self.addAction(lasso_act)
        self.addAction(cross_act)
        self.addAction(save_act)
        self.addWidget(self.pos_lbl)
        self.addSeparator()
        self.addAction(repos_act)
        self.addAction(exit_act)

        # events
        home_act.triggered.connect(self.home)
        zoom_act.toggled.connect(self.zoom)
        lasso_act.toggled.connect(self.lasso)
        cross_act.toggled.connect(self.cross_ruler)
        save_act.triggered.connect(self.save)
        repos_act.triggered.connect(self.repos_toolbar)
        exit_act.triggered.connect(self.close)

    @pyqtSlot()
    def cross_ruler(self):
        # parent widget defines how to draw cross ruler.
        if self.sender().isChecked():
            self.parent.connect_button_press_event()
        else:
            self.parent.disconnect_button_press_event()

    @pyqtSlot()
    def repos_toolbar(self):
        self.move(self.get_pos())

    @pyqtSlot(float, float)
    def on_update_xypos(self, x, y):
        self.pos_lbl.setText(
            "<html><sup>(x, y)</sup>({0:<.4f}, {1:<.4f})</html>".format(x, y))
        self.adjustSize()

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
            self.selector.selectedIndicesReady.connect(self.update_selected_indices)
        else:
            self.selector.disconnect()
            self.selector.selectedIndicesReady.disconnect()

    @pyqtSlot(QVariant, QVariant)
    def update_selected_indices(self, ind, pts):
        """Emit selected indice list and points.
        """
        self.selectedIndicesUpdated.emit(ind, pts)

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

    def mousePressEvent(self, e):
        self.pos_x = e.x()
        self.pos_y = e.y()

    def mouseMoveEvent(self, e):
        try:
            self.move(e.globalX() - self.pos_x, e.globalY() - self.pos_y)
        except:
            pass


class SelectFromPoints(QObject):
    """Select indices from points using `LassoSelector`.
    """
    # selected points indices list and points list
    # ind: index of orginal xy points array,
    # pts: selected points
    selectedIndicesReady = pyqtSignal(QVariant, QVariant)
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
        self.selectedIndicesReady.emit(ind, self.points[ind])

    def disconnect(self):
        self.lasso.disconnect_events()
        self.canvas.draw_idle()
