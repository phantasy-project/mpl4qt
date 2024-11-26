from PyQt5.QtWidgets import (
    QGraphicsDropShadowEffect,
    QLabel,
    QSizePolicy,
    QStyle,
    QStyleOptionTab,
    QStylePainter,
    QTabBar,
    QTabWidget,
    QWidget
)
from PyQt5.QtCore import (
    QPoint,
    QRect,
    Qt
)


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


class KeyLabel(QLabel):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setStyleSheet("""
        QLabel {
            background-color: #FFFFFF;
            border: 1px solid #BDC3C7;
            border-radius: 1px;
            padding: 2px;
        }""")
        #
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(4)
        shadow.setOffset(2)
        self.setGraphicsEffect(shadow)


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
    from PyQt5.QtWidgets import QSpacerItem, QWidget
    import sys
    import string

    app = QApplication(sys.argv)
    w = QWidget()
    vbox = QVBoxLayout()
    w.setLayout(vbox)

    def add_keys(keys, w: int, h: int, maxlen: int = 32):
        hbox = QHBoxLayout()
        vbox.addLayout(hbox)
        for c in keys:
            key = KeyLabel()
            key.setText(c)
            key.setFixedWidth(w)
            key.setFixedHeight(h)
            hbox.addWidget(key)
        if len(keys) < maxlen:
            hbox.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding))

    add_keys(string.punctuation, 64, 64)
    add_keys(string.ascii_uppercase, 64, 64)
    add_keys(string.ascii_lowercase, 64, 64)
    add_keys(("Ctrl", "Shift", "Alt", "Enter"), 64, 108)

    w.show()
    sys.exit(app.exec_())
