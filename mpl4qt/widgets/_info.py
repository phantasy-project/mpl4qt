# -*- coding: utf-8 -*-


def get_pkg_info():
    import mpl4qt
    import matplotlib
    mpl_ver = matplotlib.__version__
    ver = mpl4qt.__version__
    info = f"""<html>
    <h4>About mpl4qt</h4>
    <p><b>v{ver}</b></p>
    <p>Data visualization widgets based on
    <a href="https://matplotlib.org">matplotlib</a> (v{mpl_ver}) for PyQt5 application development.
    </p>
    <p>Copyright (C) 2018-2024 Facility for Rare Isotope Beams, Michigan State University.</p>
    <p>Contact: <a href="mailto:Tong%20Zhang<zhangt@frib.msu.edu>?subject=Questions about mpl4qt v{ver} with matplotlib v{mpl_ver}">Tong Zhang</a></p>
    </html>"""
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
