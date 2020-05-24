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
    # PyQt5 > PySide2
    exec_name = 'designer'
    if 'PyQt5' in sys.modules:
        try:
            from pyqt5_tools.entrypoints import pyqt5designer
        except ImportError:
            print("Please install pyqt5-tools if does not work.")
            if 'PySide2' in sys.modules:
                exec_name = 'pyside2-designer'
        else:
            exec_name = 'pyqt5designer'
    elif 'PySide2' in sys.modules:
        exec_name = 'pyside2-designer'
    return exec_name


def main():
    env = QProcessEnvironment.systemEnvironment()
    plugin_path = os.path.abspath(os.path.join(curdir, '..', 'plugins'))
    env.insert('PYQTDESIGNERPATH', plugin_path)

    exec_name = locate_designer()

    if exec_name in 'designer':
        # linux default
        designer_bin = QLibraryInfo.location(QLibraryInfo.BinariesPath)
    elif exec_name == 'pyside2-designer':
        import PySide2
        designer_bin = PySide2.__path__[0]
    elif exec_name == 'pyqt5designer':
        import pyqt5_tools
        designer_bin = os.path.join(pyqt5_tools.__path__[0], "Qt", "bin")
        env.insert('QT_DEBUG_PLUGINS', '1')
        env.insert('QT_PLUGIN_PATH',
                   os.path.join(pyqt5_tools.__path__[0], "Qt", "plugins"))
        if platform.system() == "Windows":
            pypath = ';'.join(sys.path) + ';' + os.path.abspath(
                    os.path.join(curdir, '..', '..'))
        else:
            pypath = ':'.join(sys.path) + ':' + os.path.abspath(
                    os.path.join(curdir, '..', '..'))
        env.insert('PYTHONPATH', pypath)

    designer = QProcess()
    designer.setProcessEnvironment(env)

    designer_path = os.path.join(designer_bin, 'designer')
    designer.start(designer_path, sys.argv[1:])
    designer.waitForFinished(-1)

    sys.exit(designer.exitCode())


if __name__ == '__main__':
    main()
