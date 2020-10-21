# -*- coding: utf-8 -*-

import json
import re
from collections import OrderedDict
from copy import deepcopy
from itertools import cycle

import matplotlib.colors as colors
import numpy as np
from PyQt5.QtGui import QFont
from math import log10
import matplotlib as mpl
from matplotlib.font_manager import stretch_dict
from matplotlib.font_manager import weight_dict
from matplotlib.ticker import FuncFormatter
from matplotlib.transforms import BboxTransform, Bbox

try:
    basestring
except NameError:
    basestring = str

BOOTSTRAP_GREEN = "#28A745"
BOOTSTRAP_RED = "#DC3545"
BOOTSTRAP_BLUE = "#007BFF"
BOOTSTRAP_YELLOW = "#FFC107"
BOOTSTRAP_GRAY = "#6C757D"
BOOTSTRAP_WHITE = "#F8F9FA"
BOOTSTRAP_BLACK = "#343A40"

# marker style
MK_STY_DICT = {
    'none': {
        'code': u'none',
        'symbol': 'None'
    },
    'point': {
        'code': u'\N{BLACK CIRCLE}',
        'symbol': '.'
    },
    'circle': {
        'code': u'\N{WHITE CIRCLE}',
        'symbol': 'o'
    },
    'square': {
        'code': u'\N{WHITE LARGE SQUARE}',
        'symbol': 's'
    },
    'pentagon': {
        'code': u'\N{WHITE PENTAGON}',
        'symbol': 'p'
    },
    'hexagon1': {
        'code': u'\N{WHITE HEXAGON}',
        'symbol': 'h'
    },
    'diamond': {
        'code': u'\N{WHITE DIAMOND}',
        'symbol': 'D'
    },
    'tdiamond': {
        'code': u'\N{LOZENGE}',
        'symbol': 'd'
    },
    'star': {
        'code': u'\N{STAR OPERATOR}',
        'symbol': '*'
    },
    'cross': {
        'code': u'\N{VECTOR OR CROSS PRODUCT}',
        'symbol': 'x'
    },
    'plus': {
        'code': u'\N{PLUS SIGN}',
        'symbol': '+'
    },
    'hline': {
        'code': u'\N{MINUS SIGN}',
        'symbol': '_'
    },
    'vline': {
        'code': u'\N{DIVIDES}',
        'symbol': '|'
    },
    'tri_down': {
        'code': u'\N{WHITE DOWN-POINTING TRIANGLE}',
        'symbol': 'v'
    },
    'tri_up': {
        'code': u'\N{WHITE UP-POINTING TRIANGLE}',
        'symbol': '^'
    },
    'tri_right': {
        'code': u'\N{WHITE RIGHT-POINTING TRIANGLE}',
        'symbol': '>'
    },
    'tri_left': {
        'code': u'\N{WHITE LEFT-POINTING TRIANGLE}',
        'symbol': '<'
    },
}
# represent as symbol
MK_CODE = [v['code'] for k, v in MK_STY_DICT.items()]
# use by mpl
MK_SYMBOL = [v['symbol'] for k, v in MK_STY_DICT.items()]

# line style
LINE_STY_DICT = {
    '-': 'solid',
    '--': 'dashed',
    '-.': 'dashdot',
    ':': 'dotted',
    'None': 'None',
}
LINE_STY_VALS = set(LINE_STY_DICT)
LINE_STY_VALS.update(LINE_STY_DICT.values())

# line draw style
LINE_DS_DICT = {
    'Line': 'default',
    'Steps': 'steps',
    'Mid-Steps': 'steps-mid',
    'Post-Steps': 'steps-post',
}
LINE_DS_VALS = set(LINE_DS_DICT.values())
LINE_DS_DICT_R = {v: k for k,v in LINE_DS_DICT.items()}
LINE_DS_DICT_R['steps-pre'] = 'Steps'

# axis scale mapping
SCALE_STY_DICT = OrderedDict([
    ('Linear Scale', 'linear'),
    ('Log Transform', 'log'),
    ('Symmetrical Log Transform', 'symlog'),
    # ('Logistic Transform', 'logit'),
])
SCALE_STY_KEYS = [k for k in SCALE_STY_DICT]
SCALE_STY_VALS = [v for v in SCALE_STY_DICT.values()]

# default values for mpl settings
DEFAULT_TITLE = "<title sample>"
DEFAULT_TITLE_FONT = "DejaVu Sans,16,-1,5,50,0,0,0,0,0"
DEFAULT_XLABEL = "<xlabel sample>"
DEFAULT_YLABEL = "<ylabel sample>"
DEFAULT_LABELS_FONT = "Sans Serif,14,-1,5,50,0,0,0,0,0"
DEFAULT_AUTOSCALE = True
DEFAULT_XMIN = 0
DEFAULT_XMAX = 1
DEFAULT_YMIN = 0
DEFAULT_YMAX = 1
DEFAULT_LEGEND_SHOW = False
DEFAULT_LEGEND_LOC = 0
DEFAULT_LINE_ID = 0
DEFAULT_LINE_STYLE = "--"
DEFAULT_LINE_DRAWSTYLE = "Line"
DEFAULT_LINE_COLOR = "#FF0000"
DEFAULT_LINE_WIDTH = 1.0
DEFAULT_MK_STYLE = 'o'
DEFAULT_MEC = "#0055FF"
DEFAULT_MFC = "#FFFFFF"
DEFAULT_MK_SIZE = 6.0
DEFAULT_MK_WIDTH = 1.0
DEFAULT_LINE_LABEL = "line1"
DEFAULT_LINE_ALPHA = 1.0
DEFAULT_FIG_WIDTH = 4
DEFAULT_FIG_HEIGHT = 3
DEFAULT_FIG_DPI = 100
DEFAULT_BKGD_COLOR = "#EDECEB"
DEFAULT_MTICKS_ON = False
DEFAULT_MTICKS_FONT = "Sans Serif,10,-1,5,50,0,0,0,0,0"
DEFAULT_MTICKS_COLOR = "#AA00FF"
DEFAULT_LAYOUT_TIGHT_ON = False
DEFAULT_LAYOUT_GRID_ON = False
DEFAULT_LAYOUT_GRID_COLOR = "#808080"

AUTOFORMATTER = FuncFormatter(lambda v, _: '{:g}'.format(v))
AUTOFORMATTER_MATHTEXT = FuncFormatter(lambda v, _: '${:g}$'.format(v))

# colormaps
COLORMAPS = [
    ('Sequential-Uniform', [
        'viridis', 'plasma', 'inferno', 'magma']),
    ('Sequential-I', [
        'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
        'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
        'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
    ('Sequential-II', [
        'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
        'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
        'hot', 'afmhot', 'gist_heat', 'copper']),
    ('Diverging', [
        'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
        'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
    ('Qualitative', [
        'Pastel1', 'Pastel2', 'Paired', 'Accent',
        'Dark2', 'Set1', 'Set2', 'Set3',
        'tab10', 'tab20', 'tab20b', 'tab20c']),
    ('Cyclic', [
        'twilight', 'twilight_shifted', 'hsv']),
    ('Miscellaneous', [
        'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
        'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
        'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'])
]

COLORMAPS_DICT = OrderedDict(COLORMAPS)

ALL_COLORMAPS = []
for k, v in COLORMAPS:
    ALL_COLORMAPS.extend(v)

COLOR_CYCLE = cycle(['#1f77b4', '#ff7f0e', '#2ca02c',
                     '#d62728', '#9467bd', '#8c564b',
                     '#e377c2', '#7f7f7f', '#bcbd22',
                     '#17becf'])

# font style
FONT_STYLE_Q2M = {
    QFont.StyleNormal: 'normal',
    QFont.StyleItalic: 'italic',
    QFont.StyleOblique: 'oblique',
}
FONT_STYLE_M2Q = {v: k for k, v in FONT_STYLE_Q2M.items()}

# font weight
FONT_WEIGHT_Q2M = {
    0: 100,
    12: 100,
    25: 200,
    50: 400,
    57: 500,
    63: 600,
    75: 700,
    81: 800,
    87: 900,
}
FONT_WEIGHT_M2Q = {v: k for k, v in FONT_WEIGHT_Q2M.items()}

# font stretch
FONT_STRETCH_Q2M = {
    50: 100,
    62: 200,
    75: 300,
    87: 400,
    100: 500,
    112: 600,
    125: 700,
    150: 800,
    200: 900,
}
FONT_STRETCH_M2Q = {v: k for k, v in FONT_STRETCH_Q2M.items()}


def set_font(obj, font):
    """Update the font of *obj* with *font*.

    Parameters
    ----------
    obj :
        Matplotlib object could be set font.
    font : QFont
        Font to set.
    """
    obj.set_size(font.pointSizeF())
    obj.set_family(font.family())
    obj.set_weight(FONT_WEIGHT_Q2M.get(font.weight(), 100))
    if font.stretch() == 0:
        font.setStretch(100)
    obj.set_stretch(FONT_STRETCH_Q2M[font.stretch()])
    obj.set_style(FONT_STYLE_Q2M[font.style()])


def mfont_to_qfont(pf):
    """Return QFont instance from mpl font property.

    Parameters
    ----------
    pf :
        Instance of Matplotlib FontProperties.

    Returns
    -------
    r :
        Instance of QFont.
    """
    family = pf.get_family()[0]
    size = pf.get_size_in_points()
    weight = weight_as_number(pf.get_weight())
    stretch = stretch_as_number(pf.get_stretch())
    style = pf.get_style()
    font = QFont(family, size)
    font.setStyle(FONT_STYLE_M2Q[style])
    font.setWeight(FONT_WEIGHT_M2Q[weight])
    font.setStretch(FONT_STRETCH_M2Q[stretch])
    return font


def weight_as_number(weight):
    """Return mpl font weight as a number.
    """
    # mpl 2.0.0, return weight as an int, while 2.1.1 return a str
    if isinstance(weight, (int, float)):
        return weight
    #
    return weight_dict[weight]


def stretch_as_number(stretch):
    """Return mpl font stretch as a number.
    """
    if isinstance(stretch, (int, float)):
        return stretch
    return stretch_dict[stretch]


def pyformat_from_cformat(s, math_text=False):
    """Convert string format specifier from C style to Python style,
    which could be used by `str.format()` function.
    """
    islog = False
    r = re.match('(.*)%(.*)', s)
    if r is None:
        return None, None
    prefix, specifier = r.group(1), r.group(2)
    if 'n' in specifier:  # log scale
        islog = True
        if prefix != '':
            fmt = prefix + '{{{:' + 'd' + '}}}'
        else:
            fmt = '{:' + 'd' + '}'
    else:
        fmt = prefix + '{:' + specifier + '}'
    if math_text:
        fmt = '${}$'.format(fmt)
    return fmt, islog


def generate_formatter(cfmt, math_text=False):
    """Return function formatter from c string format *cfmt*,
    if *math_text* is True, support latex math display.
    """
    pyfmt, islog = pyformat_from_cformat(cfmt, math_text=math_text)
    if pyfmt is None:
        return None
    if islog:
        def f(v, l):
            try:
                return pyfmt.format(int(log10(v)))
            except:
                # toggle autoscale,
                # change axis-scale to log
                return ''
    else:
        f = lambda v, _: pyfmt.format(v)
    return FuncFormatter(f)


def cycle_list_next(vlist, current_val):
    """Return the next element of *current_val* from *vlist*, if
    approaching the list boundary, starts from begining.
    """
    return vlist[(vlist.index(current_val) + 1) % len(vlist)]


def mplcolor2hex(c):
    """Convert matplotlib colors into hex string format.

    Parameters
    ----------
    c : str or tuple
        Color string or RGB tuple.

    Returns
    -------
    r : str
        Hex string for color.

    Examples
    --------
    >>> mplcolor2hex('r')
    '#FF0000'
    >>> mplcolor2hex('red')
    '#FF0000'
    >>> mplcolor2hex('#FF0000')
    '#FF0000'
    >>> mplcolor2hex((1.0, 0.0, 0.0, 1.0))
    '#FF0000'
    """
    if isinstance(c, (tuple, list)):
        clr = colors.rgb2hex(c)
    elif isinstance(c, basestring):
        if c.startswith('#'):
            clr = c
        else:
            try:
                clr = colors.rgb2hex(colors.colorConverter.colors[c])
            except:
                clr = colors.cnames[c]
    return clr.upper()


def is_cmap_valid(cmap):
    return hasattr(mpl.cm, cmap)


class MatplotlibCurveWidgetSettings(OrderedDict):
    def __init__(self, path=None):
        super(MatplotlibCurveWidgetSettings, self).__init__()
        if isinstance(path, basestring):
            with open(path, "r") as fp:
                self.read(fp)

    def read(self, fp):
        """Read settings from file-like object into JSON format.
        """
        self.update(json.load(fp, object_pairs_hook=OrderedDict))

    def __deepcopy__(self, memo):
        s = MatplotlibCurveWidgetSettings()
        s.update(deepcopy(list(self.items()), memo))
        return s

    def write(self, path=None, sort_keys=True):
        """Write settings into a JSON file, if path is not defined
        """
        path = 'mplcurve_default_settings.json' if path is None else path
        with open(path, 'w') as fp:
            json.dump(self, fp, indent=2, sort_keys=sort_keys)

    @staticmethod
    def default_settings():
        """Default settings.
        """
        s = OrderedDict()

        # figure tab
        sfig = OrderedDict()
        sfig.update([('title', OrderedDict({'value': DEFAULT_TITLE, 'font': DEFAULT_TITLE_FONT}))])
        sfig.update([('labels', OrderedDict({'xlabel': DEFAULT_XLABEL, 'ylabel': DEFAULT_YLABEL,
                                             'font': DEFAULT_LABELS_FONT}))])
        sfig.update([('xy_range', OrderedDict({'auto_scale': DEFAULT_AUTOSCALE,
                                               'xmin': DEFAULT_XMIN, 'xmax': DEFAULT_XMAX,
                                               'ymin': DEFAULT_YMIN, 'ymax': DEFAULT_YMAX}))])
        sfig.update([('legend', OrderedDict({'show': DEFAULT_LEGEND_SHOW,
                                             'location': DEFAULT_LEGEND_LOC}))])
        s.update([('figure', sfig)])

        # curve tab (single curve)
        scurve = OrderedDict()
        scurve.update({'label': DEFAULT_LINE_LABEL})
        scurve.update({'line_id': DEFAULT_LINE_ID})
        scurve.update([('line', OrderedDict({'style': DEFAULT_LINE_STYLE,
                                             'drawstyle': DEFAULT_LINE_DRAWSTYLE,
                                             'color': DEFAULT_LINE_COLOR,
                                             'width': DEFAULT_LINE_WIDTH,
                                             'alpha': DEFAULT_LINE_ALPHA}))])
        scurve.update([('marker', OrderedDict({'style': DEFAULT_MK_STYLE,
                                               'edgecolor': DEFAULT_MEC,
                                               'facecolor': DEFAULT_MFC,
                                               'size': DEFAULT_MK_SIZE,
                                               'width': DEFAULT_MK_WIDTH}))])

        s.update({'curve': [scurve]})

        # style tab
        sstyle = OrderedDict()
        sstyle.update([('figsize', OrderedDict({'width': DEFAULT_FIG_WIDTH,
                                                'height': DEFAULT_FIG_HEIGHT,
                                                'dpi': DEFAULT_FIG_DPI}))])
        sstyle.update([('background', {'color': DEFAULT_BKGD_COLOR})])
        sstyle.update([('ticks', OrderedDict({
            'mticks_on': DEFAULT_MTICKS_ON,
            'font': DEFAULT_MTICKS_FONT,
            'color': DEFAULT_MTICKS_COLOR}))])
        sstyle.update([('layout', OrderedDict({
            'tight_on': DEFAULT_LAYOUT_TIGHT_ON,
            'grid_on': DEFAULT_LAYOUT_GRID_ON,
            'grid_color': DEFAULT_LAYOUT_GRID_COLOR}))])

        s.update({'style': sstyle})

        return s


# default mpl figure settings
DEFAULT_MPL_SETTINGS = MatplotlibCurveWidgetSettings.default_settings()

# fig width, height, dpi
FIG_WIDTH_MIN, FIG_WIDTH_MAX = 2.0, 20.0
FIG_HEIGHT_MIN, FIG_HEIGHT_MAX = 2.0, 20.0
FIG_DPI_MIN, FIG_DPI_MAX = 50.0, 600.0
# line width
LINE_WIDTH_MIN, LINE_WIDTH_MAX = 0.0, 20.0
# marker size
MK_SIZE_MIN, MK_SIZE_MAX = 0.0, 50.0
# marker width
MK_WIDTH_MIN, MK_WIDTH_MAX = 0.0, 20.0


def get_cursor_data(im, x, y):
    xmin, xmax, ymin, ymax = im.get_extent()
    if im.origin == 'upper':
        ymin, ymax = ymax, ymin
    arr = im.get_array()
    data_extent = Bbox([[ymin, xmin], [ymax, xmax]])
    array_extent = Bbox([[0, 0], arr.shape[:2]])
    trans = BboxTransform(boxin=data_extent, boxout=array_extent)
    point = trans.transform_point([y, x])
    if any(np.isnan(point)):
        return None
    i, j = point.astype(int)
    if not (0 <= i < arr.shape[0]) or not (0 <= j < arr.shape[1]):
        return None
    else:
        return arr[i, j]


def get_array_range(z):
    """Return valid min and max of the input array *z*.
    """
    zz = np.ma.masked_invalid(z)
    return zz.min(), zz.max()


def func_peaks(x, y):
    return 3.0 * (1.0 - x) ** 2.0 * np.exp(-(x ** 2) - (y + 1) ** 2) \
           - 10 * (x / 5 - x ** 3 - y ** 5) * np.exp(-x ** 2 - y ** 2) \
           - 1.0 / 3.0 * np.exp(-(x + 1) ** 2 - y ** 2)


def main():
    import argparse
    import sys
    import os

    parser = argparse.ArgumentParser(description=
                                     "Generate default JSON settings for MatplotlibCurveWidget",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--path', dest='filepath', nargs='?',
                        help='path of the JSON settings file')
    parser.epilog = \
        """
Examples:
> {0} --path mplsettings.json
> {0}
""".format(os.path.basename(sys.argv[0]))

    args = parser.parse_args(sys.argv[1:])
    if args.filepath is None:
        path = "mplcurve_default_settings.json"
    else:
        path = args.filepath

    s = MatplotlibCurveWidgetSettings()
    s.update(s.default_settings())
    s.write(path)
    print("Generated JSON settings into {}.".format(path))


if __name__ == '__main__':
    main()
