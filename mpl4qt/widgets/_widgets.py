from PyQt5.QtWidgets import QTabBar
from PyQt5.QtWidgets import QStylePainter
from PyQt5.QtWidgets import QStyleOptionTab
from PyQt5.QtWidgets import QStyle
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtCore import QPoint, QRect


class TabBar(QTabBar):
    def __init__(self, *args, **kws):
        super(self.__class__, self).__init__(*args, **kws)

    def tabSizeHint(self, i):
        s = QTabBar.tabSizeHint(self, i)
        s.transpose()
        return s

    def paintEvent(self, e):
        painter = QStylePainter(self)
        opt = QStyleOptionTab()

        for i in range(self.count()):

            self.initStyleOption(opt, i)
            painter.drawControl(QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QRect(QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = QPoint(self.tabRect(i).center())
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QStyle.CE_TabBarTabLabel, opt)
            painter.restore()
        QWidget.paintEvent(self, e)


class TabWidget(QTabWidget):
    def __init__(self, *args, **kws):
        super(self.__class__, self).__init__(*args, **kws)
        self.setTabBar(TabBar())
        self.setTabPosition(QTabWidget.West)
