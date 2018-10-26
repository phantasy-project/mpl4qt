# -*- coding: utf-8 -*-

import matplotlib.colors as colors
from matplotlib.ticker import FuncFormatter
from collections import OrderedDict
import json
from copy import deepcopy
import re
from math import log10

try:
    basestring
except NameError:
    basestring = str


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
MK_CODE = [v['code'] for k,v in MK_STY_DICT.items()]
# use by mpl
MK_SYMBOL = [v['symbol'] for k,v in MK_STY_DICT.items()]

# line style
LINE_STY_DICT = {
    '-': 'solid',
    '--': 'dashed',
    '-.': 'dashdot',
    ':': 'dotted',
    'None': 'None',
}

# axis scale mapping
SCALE_STY_DICT = OrderedDict([
    ('Linear Scale', 'linear'),
    ('Log Transform', 'log'),
    ('Symmetrical Log Transform', 'symlog'),
    #('Logistic Transform', 'logit'),
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
DEFAULT_LINE_COLOR = "#FF0000"
DEFAULT_LINE_WIDTH = 1.0
DEFAULT_MK_STYLE = 'o'
DEFAULT_MEC = "#0055FF"
DEFAULT_MFC = "#FFFFFF"
DEFAULT_MK_SIZE = 6.0
DEFAULT_MK_WIDTH = 1.0
DEFAULT_LINE_LABEL = "line1"
DEFAULT_FIG_WIDTH = 4
DEFAULT_FIG_HEIGHT = 3
DEFAULT_FIG_DPI = 120
DEFAULT_BKGD_COLOR = "#EDECEB"
DEFAULT_MTICKS_ON = False
DEFAULT_MTICKS_FONT = "Sans Serif,10,-1,5,50,0,0,0,0,0"
DEFAULT_MTICKS_COLOR = "#AA00FF"
DEFAULT_LAYOUT_TIGHT_ON = False
DEFAULT_LAYOUT_GRID_ON = False
DEFAULT_LAYOUT_GRID_COLOR = "#808080"


AUTOFORMATTER = FuncFormatter(lambda v,_:'{:g}'.format(v))
AUTOFORMATTER_MATHTEXT = FuncFormatter(lambda v,_:'${:g}$'.format(v))


def pyformat_from_cformat(s, math_text=False):
    """Convert string format specifier from C style to Python style,
    which could be used by `str.format()` function.
    """
    islog = False
    r = re.match('(.*)%(.*)', s)
    if r is None:
        return None, None
    prefix, specifier = r.group(1), r.group(2)
    if 'n' in specifier: # log scale
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
    >>> color_to_hex('r')
    '#FF0000'
    >>> color_to_hex('red')
    '#FF0000'
    >>> color_to_hex('#FF0000')
    '#FF0000'
    >>> color_to_hex((1.0, 0.0, 0.0, 1.0))
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

    def write(self, path=None):
        """Write settings into a JSON file, if path is not defined
        """
        path = 'mplcurve_default_settings.json' if path is None else path
        with open(path, 'w') as fp:
            json.dump(self, fp, indent=2, sort_keys=True)

    @staticmethod
    def default_settings():
        """Default settings.
        """
        s = OrderedDict()

        # figure tab
        sfig = OrderedDict()
        sfig.update({'title': {'value': DEFAULT_TITLE, 'font': DEFAULT_TITLE_FONT}})
        sfig.update({'labels': {'xlabel': DEFAULT_XLABEL, 'ylabel': DEFAULT_YLABEL,
                                'font': DEFAULT_LABELS_FONT}})
        sfig.update({'xy_range': {'auto_scale': DEFAULT_AUTOSCALE,
                                  'xmin': DEFAULT_XMIN, 'xmax': DEFAULT_XMAX,
                                  'ymin': DEFAULT_YMIN, 'ymax': DEFAULT_YMAX}})
        sfig.update({'legend': {'show': DEFAULT_LEGEND_SHOW,
                                'location': DEFAULT_LEGEND_LOC}})
        s.update({'figure': sfig})

        # curve tab (single curve)
        scurve = OrderedDict()
        scurve.update({'line': {'style': DEFAULT_LINE_STYLE,
                                'color': DEFAULT_LINE_COLOR,
                                'width': DEFAULT_LINE_WIDTH}})
        scurve.update({'marker': {'style': DEFAULT_MK_STYLE,
                                  'edgecolor': DEFAULT_MEC,
                                  'facecolor': DEFAULT_MFC,
                                  'size': DEFAULT_MK_SIZE,
                                  'width': DEFAULT_MK_WIDTH}})
        scurve.update({'label': DEFAULT_LINE_LABEL})
        scurve.update({'line_id': DEFAULT_LINE_ID})

        s.update({'curve': [scurve]})

        # style tab
        sstyle = OrderedDict()
        sstyle.update({'figsize': {
            'width': DEFAULT_FIG_WIDTH,
            'height': DEFAULT_FIG_HEIGHT,
            'dpi': DEFAULT_FIG_DPI}})
        sstyle.update({'background': {
            'color': DEFAULT_BKGD_COLOR}})
        sstyle.update({'ticks': {
            'mticks_on': DEFAULT_MTICKS_ON,
            'font': DEFAULT_MTICKS_FONT,
            'color': DEFAULT_MTICKS_COLOR,
            }})
        sstyle.update({'layout': {
            'tight_on': DEFAULT_LAYOUT_TIGHT_ON,
            'grid_on': DEFAULT_LAYOUT_GRID_ON,
            'grid_color': DEFAULT_LAYOUT_GRID_COLOR,
            }})

        s.update({'style': sstyle})

        return s


# default mpl figure settings
DEFAULT_MPL_SETTINGS = MatplotlibCurveWidgetSettings.default_settings()


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
