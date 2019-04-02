# -*- coding: utf-8 -*-

"""
Navigation toolbar for matplotlib widgets
"""

from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.path import Path
from matplotlib.widgets import LassoSelector
import numpy as np

from mpl4qt.icons import exit_tool_icon
from mpl4qt.icons import home_tool_icon
from mpl4qt.icons import pan_tool_icon
from mpl4qt.icons import zoom_tool_icon
from mpl4qt.icons import save_tool_icon
from mpl4qt.icons import lasso_tool_icon
from mpl4qt.icons import repos_tool_icon
from mpl4qt.icons import cross_tool_icon
from mpl4qt.icons import dock_tool_icon
from mpl4qt.icons import popup_tool_icon
from mpl4qt.icons import backward_tool_icon
from mpl4qt.icons import forward_tool_icon
from mpl4qt.icons import autox_tool_icon
from mpl4qt.icons import autoy_tool_icon
from mpl4qt.icons import autoxy_tool_icon

TBSTY_FLOATING ="""
QToolBar {
    background-color: white;
    border-radius: 6px;
    border-bottom: 2px solid #8f8f91;
    border-top: 2px solid #8f8f91;
    spacing: 5px;
    padding: 10px;
}
"""

TBSTY_NONFLOATING ="""
QToolBar {{
    background-color: {};
    border-radius: 2px;
    border-bottom: 1px solid #8f8f91;
    border-top: 1px solid #8f8f91;
    spacing: 4px;
    padding: 2px;
}}
"""

class NavigationToolbar(NavigationToolbar2QT):
    def __init__(self, canvas, parent=None):
        super(self.__class__, self).__init__(canvas, parent)
        self.tb = parent
        self.mpl = self.tb.parent

    def release_zoom(self, e):
        NavigationToolbar2QT.release_zoom(self, e)
        xlim = self.mpl.axes.get_xlim()
        ylim = self.mpl.axes.get_ylim()
        self.tb.zoom_roi_changed.emit(xlim, ylim)


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

    # toolbar floatable status
    floatable_changed = pyqtSignal(bool)

    # zoomed ROI changed
    zoom_roi_changed = pyqtSignal(tuple, tuple)

    def __init__(self, canvas, parent=None):
        super(MToolbar, self).__init__()
        self.parent = parent
        self.canvas = canvas

        self.init_ui()
        # window flags
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self._bgcolor = self.parent.getFigureBgColor().name()

    def show_toolbar(self):
        self.move(self.get_pos())
        self.show()
        self.raise_()

    @pyqtSlot(bool)
    def on_floatable_changed(self, f):
        if f:  # floatable
            if self.parent.vbox.count() > 1:
                w = self.parent.vbox.takeAt(0).widget()
                self.parent.vbox.removeWidget(w)
            else:
                w = self
            w.setStyleSheet(TBSTY_FLOATING)
            w.setParent(None)
            w.dock_act.setIcon(QIcon(QPixmap(dock_tool_icon)))
            w.dock_act.setToolTip("Dock toolbar")
            w.show_toolbar()
        else:  # non-floatable
            self.setStyleSheet(TBSTY_NONFLOATING.format(self._bgcolor))
            self.setSizePolicy(
                QSizePolicy.Expanding, QSizePolicy.Preferred)
            self.parent.vbox.insertWidget(0, self)
            self.dock_act.setIcon(QIcon(QPixmap(popup_tool_icon)))
            self.dock_act.setToolTip("Undock toolbar")
        self._floating = f

    def init_ui(self):
        #
        self._floating = True
        self.floatable_changed.connect(self.on_floatable_changed)

        # bg
        self.parent.bgColorChanged.connect(self.update_bgcolor)

        self.tb = tb = NavigationToolbar(self.canvas, self)
        tb.hide()

        # zoom tool
        zoom_act = QAction(QIcon(QPixmap(zoom_tool_icon)), "Zoom", self)
        zoom_act.setCheckable(True)
        self.zoom_act = zoom_act
        zoom_act.setToolTip("Zoom into selected region")

        # home tool
        home_act = QAction(QIcon(QPixmap(home_tool_icon)), "Home", self)
        home_act.setToolTip("Reset to original view")

        # backward
        backward_act = QAction(QIcon(QPixmap(backward_tool_icon)),
                              "Backward", self)
        backward_act.setToolTip("Backward view")

        # forward
        forward_act = QAction(QIcon(QPixmap(forward_tool_icon)),
                              "Forward", self)
        forward_act.setToolTip("Forward view")

        # auto scale tool
        auto_scale_act = QAction(QIcon(QPixmap(autoxy_tool_icon)), "Auto Scale", self)
        auto_scale_act.setToolTip("Auto Scale")

        # auto xscale tool
        auto_xscale_act = QAction(QIcon(QPixmap(autox_tool_icon)), "Auto X-Scale", self)
        auto_xscale_act.setToolTip("Auto X-Scale")

        # auto yscale tool
        auto_yscale_act = QAction(QIcon(QPixmap(autoy_tool_icon)), "Auto Y-Scale", self)
        auto_yscale_act.setToolTip("Auto Y-Scale")

        # pan tool
        pan_act = QAction(QIcon(QPixmap(pan_tool_icon)), "Pan", self)
        pan_act.setCheckable(True)
        self.pan_act = pan_act
        pan_act.setToolTip("Pan axes with left mouse")

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

        # dock tool
        dock_act = QAction(QIcon(QPixmap(dock_tool_icon)), "Dock", self)
        self.dock_act = dock_act
        dock_act.setToolTip("Dock toolbar")

        # repos to center (toolbar) tool
        repos_act = QAction(QIcon(QPixmap(repos_tool_icon)), "Repos", self)
        repos_act.setToolTip(
            "Reposition toolbar wrt figure widget, drag & move to otherwhere")

        # pos display tool
        self.pos_lbl = QLabel(self)
        self.pos_lbl.setSizePolicy(
                QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        self.pos_lbl.setToolTip("Pointed (x, y) coordinate")
        self.pos_lbl.setStyleSheet("""
            QLabel {
                font-family: monospace;
                color: black;
            }
            """)
        self.parent.xyposUpdated.connect(self.on_update_xypos)

        # widgets in toolbar
        self.addAction(dock_act)
        self.addAction(repos_act)
        self.addSeparator()

        self.addAction(home_act)
        self.addAction(backward_act)
        self.addAction(forward_act)
        self.addSeparator()

        self.addAction(auto_scale_act)
        self.addAction(auto_xscale_act)
        self.addAction(auto_yscale_act)
        self.addSeparator()

        self.addAction(pan_act)
        self.addAction(zoom_act)
        self.addAction(lasso_act)
        self.addAction(cross_act)
        self.addAction(save_act)
        self.addSeparator()

        self.addWidget(self.pos_lbl)
        self.addSeparator()

        self.addAction(exit_act)

        # events
        home_act.triggered.connect(self.home)
        forward_act.triggered.connect(self.forward)
        backward_act.triggered.connect(self.backward)
        auto_scale_act.triggered.connect(self.auto_scale)
        auto_xscale_act.triggered.connect(self.auto_xscale)
        auto_yscale_act.triggered.connect(self.auto_yscale)
        pan_act.toggled.connect(self.pan)
        zoom_act.toggled.connect(self.zoom)
        lasso_act.toggled.connect(self.lasso)
        cross_act.toggled.connect(self.cross_ruler)
        save_act.triggered.connect(self.save)
        repos_act.triggered.connect(self.repos_toolbar)
        exit_act.triggered.connect(self.close)
        dock_act.triggered.connect(self.dock)

        #
        self.floatable_changed.emit(self._floating)

    def update_bgcolor(self, color):
        if not self._floating:
            self._bgcolor = color.name()
            self.setStyleSheet(TBSTY_NONFLOATING.format(self._bgcolor))

    @pyqtSlot()
    def cross_ruler(self):
        # parent widget defines how to draw cross ruler.
        self.parent._ruler_on = self.sender().isChecked()

    @pyqtSlot()
    def repos_toolbar(self):
        self.move(self.get_pos())
        self.adjustSize()

    @pyqtSlot(list)
    def on_update_xypos(self, coord):
        if len(coord) == 2:
            x, y = coord
            self.pos_lbl.setText(
                "<html><sup>(x,y)</sup>({0:<.4g},{1:<.4g})</html>".format(x, y))
        elif len(coord) == 3:
            x, y, z = coord
            self.pos_lbl.setText(
                    "<html><sup>(x,y,z)</sup>({0:<.4g},{1:<.4g},{2:<.4g})</html>".format(x, y, z))

    @pyqtSlot()
    def zoom(self):
        self.tb.zoom()

    @pyqtSlot()
    def pan(self):
        self.tb.pan()

    @pyqtSlot()
    def home(self):
        self.tb.home()

    @pyqtSlot()
    def forward(self):
        self.tb.forward()

    @pyqtSlot()
    def backward(self):
        self.tb.back()

    @pyqtSlot()
    def auto_scale(self):
        self.parent.set_autoscale()

    @pyqtSlot()
    def auto_xscale(self):
        self.parent.set_autoscale('x')

    @pyqtSlot()
    def auto_xscale(self):
        self.parent.set_autoscale('x')

    @pyqtSlot()
    def auto_yscale(self):
        self.parent.set_autoscale('y')

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

    @pyqtSlot()
    def dock(self):
        # dock tb to mplwidget or undock
        self.floatable_changed.emit(not self._floating)

    @pyqtSlot(QVariant, QVariant)
    def update_selected_indices(self, ind, pts):
        """Emit selected indice list and points.
        """
        if ind.size == 0:
            return
        self.selectedIndicesUpdated.emit(ind, pts)

    def closeEvent(self, e):
        for o in (self.lasso_act, self.zoom_act, self.pan_act, ):
            if o.isChecked():
                o.setChecked(False)
        """
        if self.lasso_act.isChecked():
            self.lasso_act.setChecked(False)
        if self.zoom_act.isChecked():
            self.zoom_act.setChecked(False) # emit toggled
        """
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
