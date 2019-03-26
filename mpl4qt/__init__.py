# -*- coding: utf-8 -*-


# always use Qt5Agg for mpl < 2.0
import matplotlib
if matplotlib.__version__ <= "2.0.0":
    matplotlib.use("Qt5Agg")
    matplotlib.rcParams['agg.path.chunksize'] = 2000
#

__authors__ = "Tong Zhang"
__copyright__ = "(c) 2018-2019, Facility for Rare Isotope beams," \
                " Michigan State University"
__contact__ = "Tong Zhang <zhangt@frib.msu.edu>"
__version__ = "2.4.0"
