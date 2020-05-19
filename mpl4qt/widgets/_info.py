# -*- coding: utf-8 -*-


def get_pkg_info():
    import mpl4qt
    ver = mpl4qt.__version__
    info = """
    <html>
    <h4>About mpl4qt</h4>
    <p>Data visualization widgets for Qt and designer, developed with
    <a href="https://matplotlib.org">matplotlib</a>, current version is {}.
    </p>
    <p>Copyright (C) 2018 Tong Zhang</p>
    </html>
    """.format(ver)
    return info
