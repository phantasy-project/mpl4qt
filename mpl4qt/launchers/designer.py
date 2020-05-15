#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import platform
import shutil

from PyQt5.QtCore import QProcessEnvironment
from PyQt5.QtCore import QProcess
from PyQt5.QtCore import QLibraryInfo

curdir = os.path.dirname(__file__)


def locate_designer():
    exec_name = 'designer'
    if platform.system() == "Windows":
        if 'PyQt5' in sys.modules:
            exec_name = 'pyqt5designer'
        elif 'PySide2' in sys.modules:
            exec_name = 'pyside2-designer'
    return shutil.which(exec_name)


def main():
    env = QProcessEnvironment.systemEnvironment()
    plugin_path = os.path.abspath(os.path.join(curdir, '..', 'plugins'))
    env.insert('PYQTDESIGNERPATH', plugin_path)

    designer = QProcess()
    designer.setProcessEnvironment(env)
    designer.start(locate_designer(), sys.argv[1:])
    designer.waitForFinished(-1)

    sys.exit(designer.exitCode())


if __name__ == '__main__':
    main()
