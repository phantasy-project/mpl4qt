# -*- coding: utf-8 -*-

import matplotlib.colors as colors

try:
    basestring
except NameError:
    basestring = str


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
