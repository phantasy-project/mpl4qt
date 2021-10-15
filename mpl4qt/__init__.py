# -*- coding: utf-8 -*-

import platform
import matplotlib
from .ui import resources_rc

try:
    d, v, _ = platform.linux_distribution()
except AttributeError:
    pass
else:
    if d == 'debian':
        matplotlib.rcParams['agg.path.chunksize'] = 2000
finally:
    # always use Qt5Agg for mpl < 2.0
    if matplotlib.__version__ < "2.0.0":
        matplotlib.use("Qt5Agg")
#

from .widgets import *

__authors__ = "Tong Zhang"
__copyright__ = "(c) 2018-2020, Facility for Rare Isotope beams," \
                " Michigan State University"
__contact__ = "Tong Zhang <zhangt@frib.msu.edu>"
__version__ = "2.7.4"
