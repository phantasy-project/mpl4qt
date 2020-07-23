#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Help dialog pop up thru '?'.
"""

import platform

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QDialog

from mpl4qt.ui.ui_kbdhelp import Ui_Dialog


class KbdHelpDialog(QDialog, Ui_Dialog):
    """Dialog for '?' key short.
    """
    def __init__(self, parent=None):
        super(KbdHelpDialog, self).__init__(parent)

        # UI
        self.setupUi(self)
        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        #if platform.system() == "Linux":
        #    self.setAttribute(Qt.WA_TranslucentBackground)
        #else:
        #    self.setWindowOpacity(0.8)
        #    self.setStyleSheet("QDialog{background:#000000;}")
        self.adjustSize()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setOpacity(0.8)
        painter.setBrush(Qt.white)
        painter.setPen(QPen(Qt.white))
        painter.drawRect(self.rect())
