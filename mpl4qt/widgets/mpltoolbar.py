# -*- coding: utf-8 -*-

"""
Navigation toolbar for matplotlib widgets
"""
import numpy as np

from PyQt5.QtCore import QObject
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QVariant
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QWidgetAction

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.path import Path
from matplotlib.widgets import LassoSelector

from mpl4qt.widgets.utils import COLOR_CYCLE
from mpl4qt.widgets.markers_view import MarkersView

TBSTY_FLOATING = """
QToolBar {
    background-color: white;
    border-radius: 0px;
    border-bottom: 1px solid #8f8f91;
    border-top: 1px solid #8f8f91;
    spacing: 2px;
    padding: 4px;
}
"""

TBSTY_NONFLOATING = """
QToolBar {{
    background-color: {};
    border-radius: 0px;
    border-bottom: 0.5px solid #8f8f91;
    border-top: 0.5px solid #8f8f91;
    spacing: 0px;
    padding: 1px;
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

    # add marker tool is checked or not
    marker_add_checked = pyqtSignal(bool)

    # snap enabled or not, xydata
    snap_updated = pyqtSignal([bool], [bool, np.ndarray, np.ndarray])

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
            w.dock_act.setIcon(QIcon(QPixmap(":/tools/top_dock.png")))
            w.dock_act.setToolTip("Dock toolbar")
            w.show_toolbar()
        else:  # non-floatable
            self.setStyleSheet(TBSTY_NONFLOATING.format(self._bgcolor))
            self.setSizePolicy(
                QSizePolicy.Expanding, QSizePolicy.Preferred)
            self.parent.vbox.insertWidget(0, self)
            self.dock_act.setIcon(QIcon(QPixmap(":/tools/popup.png")))
            self.dock_act.setToolTip("Undock toolbar")
        self._floating = f

    def init_ui(self):
        self._isize = self.iconSize().height()
        #
        self._floating = True
        self.floatable_changed.connect(self.on_floatable_changed)

        # bg
        self.parent.bgColorChanged.connect(self.update_bgcolor)

        self.tb = tb = NavigationToolbar(self.canvas, self)
        tb.hide()

        # zoom tool
        zoom_act = QAction(QIcon(QPixmap(":/tools/zoom.png")), "Zoom", self)
        zoom_act.setCheckable(True)
        self.zoom_act = zoom_act
        zoom_act.setToolTip("Zoom into selected region")

        # home tool
        home_act = QAction(QIcon(QPixmap(":/tools/home.png")), "Home", self)
        home_act.setToolTip("Reset to original view")

        # backward
        backward_act = QAction(QIcon(QPixmap(":/tools/backward.png")),
                               "Backward", self)
        backward_act.setToolTip("Backward view")

        # forward
        forward_act = QAction(QIcon(QPixmap(":/tools/forward.png")),
                              "Forward", self)
        forward_act.setToolTip("Forward view")

        # auto scale tool
        auto_scale_act = QAction(QIcon(QPixmap(":/tools/auto-scale.png")), "Auto Scale", self)
        auto_scale_act.setToolTip("Auto Scale")

        # auto xscale tool
        auto_xscale_act = QAction(QIcon(QPixmap(":/tools/auto-xscale.png")), "Auto X-Scale", self)
        auto_xscale_act.setToolTip("Auto X-Scale")

        # auto yscale tool
        auto_yscale_act = QAction(QIcon(QPixmap(":/tools/auto-yscale.png")), "Auto Y-Scale", self)
        auto_yscale_act.setToolTip("Auto Y-Scale")

        # pan tool
        pan_act = QAction(QIcon(QPixmap(":/tools/pan.png")), "Pan", self)
        pan_act.setCheckable(True)
        self.pan_act = pan_act
        pan_act.setToolTip("Pan axes with left mouse")

        # save tool
        save_act = QAction(QIcon(QPixmap(":/tools/save.png")), "Save", self)
        save_act.setToolTip("Save figure as file")

        # lasso tool
        lasso_act = QAction(QIcon(QPixmap(":/tools/lasso.png")), "Selector", self)
        self.lasso_act = lasso_act
        lasso_act.setCheckable(True)
        lasso_act.setToolTip("Select point(s) by lassoing")

        # cross ruler tool
        self.snap_cursor = None
        cross_act = QAction(QIcon(QPixmap(":/tools/cross.png")), "Crosshair", self)
        cross_act.setCheckable(True)
        cross_act.setShortcut(Qt.CTRL + Qt.Key_R)
        cross_act.setToolTip("Coordinate locator (CTRL + R) and marker")

        cross_marker_text_act = QAction("Marker with (x, y)", self)
        cross_marker_text_act.setCheckable(True)
        cross_marker_text_act.setShortcut(Qt.SHIFT + Qt.Key_P)
        cross_marker_text_act.setToolTip("Check to mark with (x, y)")
        cross_marker_text_act.toggled.connect(self.on_marker_with_xy)

        cross_hide_act = QAction(QIcon(QPixmap(":/tools/visibility_off.png")), "Hide Markers", self)
        cross_hide_act.setShortcut(Qt.CTRL + Qt.Key_H)
        cross_hide_act.setToolTip("Click to hide crosshair markers.")
        cross_hide_act.triggered.connect(self.on_hide_crosses)

        cross_snap_act = QAction("Snap", self)
        self.cross_snap_act = cross_snap_act
        cross_snap_act.setShortcut(Qt.SHIFT + Qt.Key_S)
        cross_snap_act.setCheckable(True)
        cross_snap_act.setToolTip("Check to snap to point")
        cross_snap_act.toggled.connect(self.on_snap_cross)
        if self.parent.widget_type == '__BasePlotWidget':
            self._is_snap_point = False
        else:
            self._is_snap_point = True
        cross_snap_act.setChecked(self._is_snap_point)

        cross_marker_act = QAction(QIcon(QPixmap(":/tools/add_marker.png")), "Add Marker", self)
        cross_marker_act.setShortcut(Qt.CTRL + Qt.Key_M)
        cross_marker_act.setCheckable(True)
        cross_marker_act.setToolTip("Click to add a crosshair marker (CTRL + M)")
        cross_marker_act.toggled.connect(self.on_add_marker)
        self.marker_add_checked.connect(self.parent.on_marker_add_checked)

        self.mk_view = None
        cross_show_mk_act = QAction(QIcon(QPixmap(":/icons/view_list.png")), "Show Markers", self)
        cross_show_mk_act.setShortcut(Qt.CTRL + Qt.Key_V)
        cross_show_mk_act.setToolTip("Show all markers.")
        cross_show_mk_act.triggered.connect(self.on_show_mks)

        menu = QMenu(self)
        menu.setToolTipsVisible(True)
        menu.addAction(cross_snap_act)
        menu.addAction(cross_marker_act)
        menu.addAction(cross_marker_text_act)
        menu.addAction(cross_show_mk_act)
        menu.addAction(cross_hide_act)
        cross_act.setMenu(menu)

        # info tool
        info_act = QAction(QIcon(QPixmap(":/tools/info.png")), "About", self)
        info_act.setToolTip("About")

        # exit tool
        exit_act = QAction(QIcon(QPixmap(":/tools/exit.png")), "Exit", self)
        exit_act.setToolTip("Close toolbar")

        # tb config tool
        conf_act = QAction(QIcon(QPixmap(":/tools/preferences.png")), "Preferences", self)
        conf_act.setToolTip("Preferences")
        conf_isize_w = QWidget(self)
        conf_isize_box = QHBoxLayout()
        conf_isize_box.setContentsMargins(2, 0, 0, 0)
        conf_isize_sbox = QSpinBox(self)
        conf_isize_sbox.setToolTip("Adjust icon size")
        conf_isize_sbox.setValue(self._isize)
        conf_isize_sbox.setRange(6, 128)
        conf_isize_btn = QToolButton(self)
        conf_isize_btn.setToolTip("Reset icon size")
        conf_isize_btn.setIcon(QIcon(QPixmap(":/icons/reset_btn.png")))
        conf_isize_box.addWidget(QLabel("Icon Size", self))
        conf_isize_box.addWidget(conf_isize_sbox, 1)
        conf_isize_box.addWidget(conf_isize_btn)
        conf_isize_w.setLayout(conf_isize_box)
        conf_menu = QMenu(self)
        conf_menu.setToolTipsVisible(True)
        conf_isize_act = QWidgetAction(self)
        conf_isize_act.setDefaultWidget(conf_isize_w)
        conf_menu.addAction(conf_isize_act)
        conf_act.setMenu(conf_menu)

        # dock tool
        dock_act = QAction(QIcon(QPixmap(":/tools/top_dock.png")), "Dock", self)
        self.dock_act = dock_act
        dock_act.setToolTip("Dock toolbar")

        # repos to center (toolbar) tool
        repos_act = QAction(QIcon(QPixmap(":/tools/repos.png")), "Repos", self)
        repos_act.setToolTip(
            "Reposition toolbar wrt figure widget, drag & move to otherwhere")

        # pos display tool
        self.pos_lbl = QLabel(self)
        self.pos_lbl.setSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        self.pos_lbl.setToolTip("Pointed Cartesian coordinate")
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

        self.addAction(conf_act)
        self.addAction(info_act)
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
        info_act.triggered.connect(self.about_info)
        conf_isize_sbox.valueChanged.connect(self.on_update_isize)
        conf_isize_btn.clicked.connect(lambda:conf_isize_sbox.setValue(self._isize))

        #
        self.floatable_changed.emit(self._floating)

    @pyqtSlot(bool)
    def on_snap_cross(self, is_snap):
        # snap to point or not
        self._is_snap_point = is_snap
        if is_snap:
            self.snap_updated[bool, np.ndarray, np.ndarray].emit(
                    True, self.parent.getXData(), self.parent.getYData())
        else:
            self.snap_updated[bool].emit(False)

    def on_update_isize(self, i):
        """icon size
        """
        self.setIconSize(QSize(i, i))

    def update_bgcolor(self, color):
        if not self._floating:
            self._bgcolor = color.name()
            self.setStyleSheet(TBSTY_NONFLOATING.format(self._bgcolor))

    @pyqtSlot(bool)
    def on_marker_with_xy(self, marker_with_xy):
        """Marker the markers with (x,y) or literally with `M{i}`.
        """
        self.parent._marker_with_xy = marker_with_xy
        for mk_name, (_, _, _, pt, (x, y)) in self.parent._markers.items():
            if marker_with_xy:
                pt.set_text('{0:g},{1:g}'.format(x,y))
                self.sender().setToolTip("Uncheck to mark with literal names")
            else:
                pt.set_text(mk_name)
                self.sender().setToolTip("Check to mark with (x, y)")
        self.parent.update_figure()

    @pyqtSlot(bool)
    def cross_ruler(self, enabled):
        """Enable free crosshair tool.
        """
        if enabled:
            try:
                if self.snap_cursor is None:
                    if self._is_snap_point:
                        xdata = self.parent._x_data
                        ydata = self.parent._y_data
                        if xdata.size == 0:
                            raise SnapCursorNoDataProbe("No data to probe.")
                    else:
                        xdata = ydata = None
                    raise SnapCursorNotExist("SnapCursor does not exist.")
                else:
                    raise SnapCursorAlreadyExisted('SnapCursor is existed.')
            except SnapCursorNoDataProbe as err:
                QMessageBox.warning(self, 'Snap Cursor Tool',
                                    str(err), QMessageBox.Ok)
                self.sender().setChecked(False)
            except SnapCursorAlreadyExisted:
                self.snap_cursor.is_snap = self._is_snap_point
                self.parent.xyposUpdated.connect(self.snap_cursor.on_move)
                if self.parent.widget_type != '__BasePlotWidget':
                    self.parent.dataChanged.connect(self.snap_cursor.set_xydata)
                self.snap_updated[bool].connect(self.snap_cursor.snap_disabled)
                self.snap_updated[bool, np.ndarray, np.ndarray].connect(self.snap_cursor.snap_enabled)
            except SnapCursorNotExist:
                self.snap_cursor = SnapCursor(self.parent.axes, xdata, ydata,
                                              self._is_snap_point)
                self.parent.xyposUpdated.connect(self.snap_cursor.on_move)
                if self.parent.widget_type != '__BasePlotWidget':
                    self.parent.dataChanged.connect(self.snap_cursor.set_xydata)
                self.snap_updated[bool].connect(self.snap_cursor.snap_disabled)
                self.snap_updated[bool, np.ndarray, np.ndarray].connect(self.snap_cursor.snap_enabled)

        else:
            if self.snap_cursor is None:
                return
            self.parent.xyposUpdated.disconnect(self.snap_cursor.on_move)
            if self.parent.widget_type != '__BasePlotWidget':
                self.parent.dataChanged.disconnect(self.snap_cursor.set_xydata)
            self.snap_updated.disconnect()
            self.snap_cursor.delete()
            self.snap_cursor = None

    @pyqtSlot()
    def on_hide_crosses(self):
        # hide/show all markers
        if not self.parent._markers:
            return
        o = self.sender()
        show_flag = o.text() == "Show Markers"
        self.parent.set_visible_hvlines(show_flag)
        if show_flag:
            icon = QIcon(QPixmap(":/tools/visibility_off.png"))
            lbl = 'Hide Markers'
            tp = "Click to show crosshair markers."
        else:
            icon = QIcon(QPixmap(":/tools/visibility.png"))
            lbl = 'Show Markers'
            tp = "Click to hide crosshair markers."
        o.setIcon(icon)
        o.setText(lbl)
        o.setToolTip(tp)

    @pyqtSlot(bool)
    def on_add_marker(self, is_checked):
        # place a new cross marker if checked.
        self.parent._to_add_marker = is_checked
        self.marker_add_checked.emit(is_checked)
        if is_checked:
            self.parent._added_marker = False
            self.parent._mk_name = 'M{}'.format(self.parent._marker_id)
            self.parent._current_mc = next(COLOR_CYCLE)
            self.sender().setText("Adding Marker (click when done)")
            QGuiApplication.setOverrideCursor(Qt.CrossCursor)
        else:
            if not self.parent._added_marker:
                self.parent._marker_id -= 1
            else:
                self.parent._marker_id += 1
            self.sender().setText("Add Marker")

    @pyqtSlot('QString')
    def on_remove_marker(self, mk_name):
        # remove marker of the name *mk_name*, maintain marker_id/n_markers
        hl, vl, cp, pt, _ = self.parent._markers.pop(mk_name)
        [o.remove() for o in (hl, vl, cp, pt)]
        self.parent.update_figure()

    @pyqtSlot()
    def on_show_mks(self):
        # show all markers.
        if self.mk_view is None:
            self.mk_view = MarkersView(self.parent._markers, self)
            self.mk_view.marker_removed.connect(self.on_remove_marker)
            self.parent.markerUpdated.connect(self.mk_view.on_add_marker)
        self.mk_view.adjustSize()
        self.mk_view.show()

    @pyqtSlot()
    def repos_toolbar(self):
        self.move(self.get_pos())
        self.adjustSize()

    @pyqtSlot(list)
    def on_update_xypos(self, coord):
        if len(coord) == 2:
            x, y = coord
            self.pos_lbl.setText(
                "<html><pre><sup>(x,y)</sup>({0:<.4g},{1:<.4g})</pre></html>".format(x, y))
        elif len(coord) == 3:
            x, y, z = coord
            self.pos_lbl.setText(
                "<html><pre><sup>(x,y,z)</sup>({0:<.4g},{1:<.4g},{2:<.4g})</pre></html>".format(x, y, z))

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
            pts = self.parent.get_points()
            ax = self.parent.axes
            self.selector = SelectFromPoints(ax, pts)
            self.selector.selectedIndicesReady.connect(self.update_selected_indices)
        else:
            self.selector.disconnect()
            self.selector.selectedIndicesReady.disconnect()

    @pyqtSlot()
    def about_info(self):
        from ._info import get_pkg_info
        QMessageBox.about(self, 'About mpl4qt', get_pkg_info())

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
        for o in (self.lasso_act, self.zoom_act, self.pan_act,):
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


class SnapCursor(QObject):

    snap_enabled = pyqtSignal(bool, np.ndarray, np.ndarray)
    snap_disabled = pyqtSignal(bool)

    def __init__(self, ax, xdata=None, ydata=None, is_snap=True):
        super(SnapCursor, self).__init__()
        self.ax = ax
        self.canvas = ax.figure.canvas
        self.is_snap = is_snap
        if is_snap:
            self.set_xydata(xdata, ydata)
        self.init_cursor()
        self.snap_enabled.connect(self.on_enable_snap)
        self.snap_disabled.connect(self.on_disable_snap)

    @pyqtSlot(bool, np.ndarray, np.ndarray)
    def on_enable_snap(self, is_snap, x, y):
        # enable snap
        self.is_snap = is_snap
        self.set_xydata(x, y)

    @pyqtSlot(bool)
    def on_disable_snap(self, is_snap):
        self.is_snap = is_snap

    def init_cursor(self):
        x0, y0 = 0, 0
        self._hline = self.ax.axhline(color='#343A40', alpha=0.95)
        self._vline = self.ax.axvline(color='#343A40', alpha=0.95)
        self._text_x = self.ax.annotate('', xy=(x0, 1.005),
                                        ha='center', va='bottom',
                                        xycoords=('data', 'axes fraction'),
                                        rotation=90, color='w',
                                        bbox=dict(
                                            boxstyle='larrow,pad=0.25',
                                            fc='#007BFF', ec='b',
                                            lw=1.0, alpha=0.95))
        self._text_y = self.ax.annotate('', xy=(1.005, y0),
                                        ha='left', va='center',
                                        xycoords=('axes fraction', 'data'),
                                        color='w',
                                        bbox=dict(
                                            boxstyle='larrow,pad=0.25',
                                            fc='#007BFF', ec='b',
                                            lw=1.0, alpha=0.95))

    def set_xydata(self, xdata, ydata):
        # set x y array data.
        ascend_data = np.asarray(sorted(zip(xdata, ydata), key=lambda i:i[0]))
        self.xdata = ascend_data[:, 0]
        self.ydata = ascend_data[:, 1]

    def on_move(self, pos_tuple):
        x, y = pos_tuple
        if self.is_snap:
            idx = min(np.searchsorted(self.xdata, x), len(self.xdata) - 1)
            x, y = self.xdata[idx], self.ydata[idx]
        self._hline.set_ydata(y)
        self._vline.set_xdata(x)
        self._text_x.set_x(x)
        self._text_y.set_y(y)
        self._text_x.set_text("{0:.3f}".format(x))
        self._text_y.set_text("{0:.3f}".format(y))
        self.canvas.draw_idle()

    def delete(self):
        for o in (self._hline, self._vline, self._text_x, self._text_y):
            o.remove()
        self.canvas.draw_idle()


class SnapCursorNoDataProbe(Exception):
    def __init__(self, *args, **kws):
        super(self.__class__, self).__init__(*args, **kws)


class SnapCursorNotExist(Exception):
    def __init__(self, *args, **kws):
        super(self.__class__, self).__init__(*args, **kws)


class SnapCursorAlreadyExisted(Exception):
    def __init__(self, *args, **kws):
        super(self.__class__, self).__init__(*args, **kws)
