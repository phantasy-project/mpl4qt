# -*- coding: utf-8 -*-

import matplotlib.colors as colors

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
    if isinstance(c, tuple):
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
