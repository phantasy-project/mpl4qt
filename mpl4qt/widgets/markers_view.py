# -*- coding: utf-8 -*-

import numpy as np
from functools import partial
from collections import deque

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTableWidgetItem

from mpl4qt.ui.ui_markers_view import Ui_Form

MAX_N_SELECT = 2


class MarkersView(QWidget, Ui_Form):

    # named marker is to remove.
    marker_removed = pyqtSignal('QString')

    # relocate marker, mk_name
    relocate_marker = pyqtSignal(['QString'], ['QString', float, float])

    # reset marker pos
    reset_marker_pos = pyqtSignal('QString')

    # shade area, mk1, mk2, is_shade
    shade_area_changed = pyqtSignal('QString', 'QString', bool)

    def __init__(self, markers, parent=None):
        super(MarkersView, self).__init__()
        self.parent = parent

        self.sel_dq = deque([], MAX_N_SELECT)

        self.setupUi(self)
        self.setWindowTitle("Cross Markers")
        self.tw = self.tableWidget
        self.set_data(markers)

        self.adjustSize()

    def _show(self):
        if self.tw.rowCount() < 2:
            pass
        else:
            self.shade_area_chkbox.setChecked(True)
            for i in range(2):
                self.tw.selectRow(i)
        self.show()

    def set_data(self, markers):
        self.data = markers
        self.show_data()

    def set_row(self, irow, x, y, name):
        # name, x, y, del, repos
        item0 = QTableWidgetItem(name)
        item0.setFlags(item0.flags() & ~Qt.ItemIsEditable)
        self.tw.setItem(irow, 0, item0)
        item1 = QTableWidgetItem("{0:g}".format(x))
        self.tw.setItem(irow, 1, item1)
        item2 = QTableWidgetItem("{0:g}".format(y))
        self.tw.setItem(irow, 2, item2)

        pos_btn = QToolButton(self)
        pos_btn.setIcon(QIcon(QPixmap(":/tools/set_marker.png")))
        pos_btn.setToolTip("Update marker (x, y) pos")
        pos_btn.clicked.connect(partial(self.on_repos_marker, name))
        self.tw.setCellWidget(irow, 3, pos_btn)

        repos_btn = QToolButton(self)
        repos_btn.setIcon(QIcon(QPixmap(":/tools/edit_marker.png")))
        repos_btn.setToolTip("Relocate current marker")
        repos_btn.clicked.connect(partial(self.on_relocate, name))
        self.tw.setCellWidget(irow, 4, repos_btn)

        del_btn = QToolButton(self)
        del_btn.setIcon(QIcon(QPixmap(":/icons/delete.png")))
        del_btn.setToolTip("Delete current marker")
        del_btn.clicked.connect(partial(self.on_delete, name))
        self.tw.setCellWidget(irow, 5, del_btn)

    def show_data(self):
        if self.data == []:
            self._reset_table()
            return
        self._preset_table()
        for i, (name, (_, _, _, _, (x, y))) in enumerate(self.data.items()):
            self.set_row(i, x, y, name)
        self._postset_table()

    @pyqtSlot()
    def on_delete(self, mk_name):
        # delete marker.
        for i in self.tw.findItems(mk_name, Qt.MatchExactly):
            self.marker_removed.emit(i.text())
            self.tw.removeRow(i.row())

    @pyqtSlot()
    def on_relocate(self, mk_name):
        # relocate marker.
        self.relocate_marker['QString'].emit(mk_name)

    @pyqtSlot()
    def on_repos_marker(self, mk_name):
        it = self.tw.findItems(mk_name, Qt.MatchExactly)[0]
        ir = it.row()
        sx, sy = self.tw.item(ir, 1), self.tw.item(ir, 2)
        try:
            x, y = float(sx.text()), float(sy.text())
        except ValueError:
            self.reset_marker_pos.emit(mk_name)
        else:
            self.relocate_marker['QString', float, float].emit(mk_name, x, y)

    @pyqtSlot(bool, float, float, 'QString')
    def on_add_marker(self, is_new_marker, x, y, mk_name):
        # added a new marker, update (x,y)
        if is_new_marker:
            irow = self.tw.rowCount()
            self.tw.insertRow(irow)
            self.set_row(irow, x, y, mk_name)
        else:
            item0 = self.tw.findItems(mk_name, Qt.MatchExactly)[0]
            self.tw.item(item0.row(), 1).setText("{0:g}".format(x))
            self.tw.item(item0.row(), 2).setText("{0:g}".format(y))
        self._postset_table()
        self.update_stats()

    def _postset_table(self):
        self.tw.resizeColumnsToContents()
        self.hheader.setSectionResizeMode(1, QHeaderView.Stretch)
        self.hheader.setSectionResizeMode(2, QHeaderView.Stretch)

    def _preset_table(self):
        """Set horizontal header labels, row/column size.
        """
        header = ['Name', 'X', 'Y', '', '', '']
        self.tw.setColumnCount(len(header))
        self.tw.setRowCount(len(self.data))
        self.tw.setHorizontalHeaderLabels(header)
        self.tw.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tw.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.hheader = self.tw.horizontalHeader()
        self.hheader.setStretchLastSection(False)

    def _reset_table(self):
        """Reset table without data.
        """
        self._preset_table()
        self._postset_table()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def on_press(self, i, j):
        if QGuiApplication.mouseButtons() == Qt.MiddleButton:
            cb = QGuiApplication.clipboard()
            if cb.supportsSelection():
                cb.setText(self.tw.item(i, j).text(), cb.Selection)

    @pyqtSlot()
    def on_selection_changed(self):
        # selection changed.
        cit = self.tw.currentItem()
        if cit is None:
            return
        self.sel_dq.append(cit.row())
        self.update_row_selection()
        self.update_stats()

    def update_row_selection(self):
        self.tw.itemSelectionChanged.disconnect()
        self.tw.clearSelection()
        for i in self.sel_dq:
            self.tw.selectRow(i)
        self.tw.itemSelectionChanged.connect(self.on_selection_changed)

    def update_stats(self):
        # update stats.
        if len(self.sel_dq) < MAX_N_SELECT or self.tw.rowCount() < len(self.sel_dq):
            return
        pt_array = np.zeros((2, 2))
        sel_namelist = ['', '']
        for i, irow in enumerate(self.sel_dq):
            sel_namelist[i] = self.tw.item(irow, 0).text()
            pt_array[i][0] = float(self.tw.item(irow, 1).text())
            pt_array[i][1] = float(self.tw.item(irow, 2).text())
        pt_mean = pt_array.mean(axis=0)
        dx = pt_array[0, 0] - pt_array[1, 0]
        dy = pt_array[0, 1] - pt_array[1, 1]
        area = abs(dx * dy)
        pt_dis = np.sqrt(dx ** 2.0 + dy ** 2.0)
        for i in range(1, 6):
            getattr(self, 'selected_pts_lbl_{}'.format(i)).setText(', '.join(sel_namelist) + ' is')
        self.mid_point_lbl.setText("<pre>X = {a[0]:g}, Y = {a[1]:g}</pre>".format(a=pt_mean))
        self.dx_lbl.setText("<pre>&Delta;X = {0:g}</pre>".format(dx))
        self.dy_lbl.setText("<pre>&Delta;Y = {0:g}</pre>".format(dy))
        self.distance_lbl.setText("<pre>&Delta;L = {0:g}</pre>".format(pt_dis))
        self.area_lbl.setText("<pre>Area = {0:g}</pre>".format(area))
        # area shade?
        if self.shade_area_chkbox.isChecked():
            self.shade_area_chkbox.setChecked(False)
            self.shade_area_chkbox.setChecked(True)

    def sizeHint(self):
        return QSize(400, 600)

    @pyqtSlot(bool)
    def on_shade_area(self, is_shade):
        # shade area or not.
        if len(self.sel_dq) < MAX_N_SELECT or self.tw.rowCount() < len(self.sel_dq):
            return
        mk_name1, mk_name2 = [self.tw.item(i, 0).text() for i in self.sel_dq]
        self.shade_area_changed.emit(mk_name1, mk_name2, is_shade)
