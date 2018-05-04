#!/usr/bin/env python

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin

from mpl4qt.widgets.siggenwidget import SignalGeneratorWidget
from mpl4qt.icons.logos import mplcurve_logo


class SignalGeneratorWidgetPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(SignalGeneratorWidgetPlugin, self).__init__(parent)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return
        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return SignalGeneratorWidget(parent)

    def name(self):
        return "SignalGeneratorWidget"

    def group(self):
        return "FRIB Collection"

    def icon(self):
        return QIcon(_logo_pixmap)

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def domXml(self):
        return '<widget class="SignalGeneratorWidget" name="signalgeneratorWidget" />\n'

    def includeFile(self):
        return "mpl4qt.widgets.siggenwidget"

# Define the image used for the icon.
_logo_pixmap = QPixmap(mplcurve_logo)
