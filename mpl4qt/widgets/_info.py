# -*- coding: utf-8 -*-


def get_pkg_info():
    import mpl4qt
    ver = mpl4qt.__version__
    info = """
    <html>
    <h4>About mpl4qt</h4>
    <p>Data visualization widgets based on
    <a href="https://matplotlib.org">matplotlib</a> for PyQt5 applications, current version is {v}.
    </p>
    <p>Copyright (C) 2018-2020 <a href="mailto:zhangt@frib.msu.edu?subject=Questions about mpl4qt v{v}">Tong Zhang</a></p>
    </html>
    """.format(v=ver)
    return info


def get_pkg_info_short():
    import mpl4qt
    ver = mpl4qt.__version__
    info = """
    <html>
    <p><span>mpl4qt</span><span style="color:#888a85;"> - Dataviz widgets for PyQt5 apps, v{v}</span></p>
    </html>
    """.format(v=ver)
    return info
