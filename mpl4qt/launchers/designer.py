#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import platform

from PyQt5.QtCore import QProcessEnvironment
from PyQt5.QtCore import QProcess
from PyQt5.QtCore import QLibraryInfo

curdir = os.path.dirname(__file__)


def locate_designer():
    # PyQt5
    exec_name = 'designer'
    if 'PyQt5' in sys.modules:
        try:
            from pyqt5_tools.entrypoints import designer
        except ImportError:
            print("Please install pyqt5-tools if does not work.")
        else:
            exec_name = 'pyqt5designer'
    return exec_name


def main():

    plugin_path = os.path.abspath(os.path.join(curdir, '..', 'plugins'))
    exec_name = locate_designer()

    if exec_name in 'designer':
        # linux default (work with Debian)
        designer_bin = QLibraryInfo.location(QLibraryInfo.BinariesPath)
        designer = QProcess()
        env = QProcessEnvironment.systemEnvironment()
        env.insert('PYQTDESIGNERPATH', plugin_path)
        designer.setProcessEnvironment(env)

        designer_path = os.path.join(designer_bin, 'designer')
        designer.start(designer_path, sys.argv[1:])
        designer.waitForFinished(-1)

        sys.exit(designer.exitCode())

    elif exec_name == 'pyqt5designer':
        from pyqt5_tools.entrypoints import designer
        os.environ['PYQTDESIGNERPATH'] = plugin_path
        designer()


if __name__ == '__main__':
    main()
