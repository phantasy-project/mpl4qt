#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from PyQt5.QtCore import QProcessEnvironment
from PyQt5.QtCore import QProcess
from PyQt5.QtCore import QLibraryInfo

curdir = os.path.dirname(__file__)

def main():
    env = QProcessEnvironment.systemEnvironment()
    plugin_path = os.path.abspath(os.path.join(curdir, '..', 'plugins'))
    env.insert('PYQTDESIGNERPATH', plugin_path)

    designer = QProcess()
    designer.setProcessEnvironment(env)
    designer_bin = QLibraryInfo.location(QLibraryInfo.BinariesPath)

    designer.start(os.path.join(designer_bin, 'designer'))
    designer.waitForFinished(-1)

    sys.exit(designer.exitCode())


if __name__ == '__main__':
    main()
