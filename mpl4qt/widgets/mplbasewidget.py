# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import numpy as np

from mpl4qt.widgets.mpltoolbar import NavigationToolbar


class BasePlotWidget(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, **kws):
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.figure.add_subplot(111)
        self.init_figure()
        super(BasePlotWidget, self).__init__(self.figure)
        self.setParent(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sys_bg_color = self.palette().color(QPalette.Background)
        self.post_style_figure()
        self.adjustSize()

    def post_style_figure(self):
        self.set_figure_color()

    def init_figure(self):
        raise NotImplementedError

    def update_figure(self):
        self.figure.canvas.draw_idle()
        self.update()

    def set_figure_color(self, color=None):
        if color is None:
            color = self.sys_bg_color.getRgbF()
        self.figure.set_facecolor(color)
        self.figure.set_edgecolor(color)
        self.axes.set_axis_bgcolor(color)

    def update_canvas(self):
        self.draw_idle()

    #def resizeEvent(self, e):
    #    print(self.size())
    #    self.updateGeometry()
    #    #self.resize(self.size())
    #    QWidget.resizeEvent(self, e)
        #self.figure.subplots_adjust(
        #        top=0.9999, bottom=0.0001, left=0.0001, right=0.9999)
        
#class BasePlotWidget(QWidget):
#    """Base class for figure plot panel.
#
#    Parameters
#    ----------
#    parent:
#        Parent of this panel.
#    figsize:
#        Figure size, `(w, h)`.
#    dpi:
#        Figure dpi.
#
#    Keyword Arguments
#    -----------------
#    bgcolor:
#        Background color of figure and canvas.
#    show_toolbar:
#        Show navigation toolbar or not, default is not.
#    aspect:
#        Axes aspect, float number or 'auto' by default.
#    other options of `wx.Panel`.
#    """
#    def __init__(self, parent, figsize=None, dpi=None, **kwargs):
#        self.parent = parent
#        self.figsize = figsize
#        self.dpi = dpi
#
#        self.bgcolor = kwargs.get('bgcolor', None)
#        self.show_toolbar = kwargs.get('show_toolbar', False)
#        self.aspect = kwargs.get('aspect', 'auto')
#        kws = {k:v for k,v in kwargs.items()
#               if k not in ('bgcolor', 'show_toolbar', 'aspect')}
#        super(BasePlotWidget, self).__init__(parent, **kws)
#        
#        # initialize figure canvas
#        self.init_figure()
#
#        # initialize plot onto figure canvas
#        self.init_plot()
#
#        # figure background color
#        #self.set_color(self.bgcolor)
#
#        # set layout
#        self.set_layout()
#
#        # post-initialization
#        #self.post_init()
#
#        # binding events
#        self.canvas.mpl_connect('button_press_event', self.on_press)
#        self.canvas.mpl_connect('button_release_event', self.on_release)
#        self.canvas.mpl_connect('motion_notify_event', self.on_motion)
#        self.canvas.mpl_connect('pick_event', self.on_pick)
#
#        #self.xylim_choice.Bind(wx.EVT_CHOICE, self.xylim_choiceOnChoice)
#        #self.minlim_tc.Bind(wx.EVT_TEXT_ENTER, self.minlim_tcOnTextEnter)
#        #self.maxlim_tc.Bind(wx.EVT_TEXT_ENTER, self.maxlim_tcOnTextEnter)
#        #self.Bind(wx.EVT_SIZE, self.on_size)
#
#    def init_figure(self):
#        """Figure canvas initialization.
#        """
#        self.figure = Figure(self.figsize, self.dpi)
#        self.canvas = FigureCanvas(self.figure)
#        if not hasattr(self, 'axes'):
#            self.axes = self.figure.add_subplot(111, aspect=self.aspect)
#
#    def init_plot(self):
#        """Initialize plot onto figure.
#        """
#        x = y = np.linspace(-np.pi, np.pi, 100)
#        self.x, self.y = np.meshgrid(x, y)
#        self.z = self._func_peaks(self.x, self.y)
#        self.image = self.axes.imshow(self.z)
#
#    def set_layout(self):
#        """Set GUI layout.
#        """
#        vbox = QVBoxLayout()
#        vbox.addWidget(self.canvas)
#
#        hbox = QHBoxLayout()
#
#        # set toolbar if defined
#        if self.show_toolbar:
#            self.toobar = NavigationToolbar(self.canvas)
#            self.toobar.Realize()
#            hbox.addWidget(self.toobar)
#            self.toobar.update()
#        
#        vbox.addLayout(hbox)
#        self.setLayout(vbox)
#
##        # add x[y]lim control
##        xylim_hbox = QHBoxLayout()
##
##        xy_vbox = QVBoxLayout()
##
##        xylim_choiceChoices = [u"X-Limit", u"Y-Limit", u"Auto"]
##        self.xylim_choice = wx.Choice(self, wx.ID_ANY,
##                                      wx.DefaultPosition,
##                                      wx.DefaultSize,
##                                      xylim_choiceChoices, 0)
##        self.xylim_choice.SetSelection(0)
##        xy_vbox.Add(self.xylim_choice, 0,
##                    wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
##
##        xylim_hbox.Add(xy_vbox, 0, wx.ALIGN_CENTER_VERTICAL, 1)
##
##        lim_vbox = wx.BoxSizer(wx.VERTICAL)
##
##        min_hbox = wx.BoxSizer(wx.HORIZONTAL)
##
##        self.minlim_st = wx.StaticText(self, wx.ID_ANY, u"Lower",
##                                       wx.DefaultPosition, wx.DefaultSize, 0)
##        self.minlim_st.Wrap(-1)
##        self.minlim_st.SetFont(wx.Font(FONTSIZE_TINY, 70, 90, 90, False, "Monospace"))
##
##        min_hbox.Add(self.minlim_st, 0,
##                     wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.TOP, 1)
##
##        self.minlim_tc = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
##                                     wx.DefaultPosition, wx.DefaultSize,
##                                     wx.TE_PROCESS_ENTER)
##        self.minlim_tc.SetFont(wx.Font(FONTSIZE_TINY, 70, 90, 90, False, "Monospace"))
##        self.minlim_tc.SetToolTipString(u"Lower Limit")
##
##        min_hbox.Add(self.minlim_tc, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP, 1)
##
##        lim_vbox.Add(min_hbox, 1, wx.EXPAND, 1)
##
##        max_hbox = wx.BoxSizer(wx.HORIZONTAL)
##
##        self.maxlim_st = wx.StaticText(self, wx.ID_ANY, u"Upper",
##                                       wx.DefaultPosition, wx.DefaultSize, 0)
##        self.maxlim_st.Wrap(-1)
##        self.maxlim_st.SetFont(wx.Font(FONTSIZE_TINY, 70, 90, 90, False, "Monospace"))
##
##        max_hbox.Add(self.maxlim_st, 0,
##                     wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.RIGHT | wx.TOP,
##                     1)
##
##        self.maxlim_tc = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
##                                     wx.DefaultPosition, wx.DefaultSize,
##                                     wx.TE_PROCESS_ENTER)
##        self.maxlim_tc.SetFont(wx.Font(FONTSIZE_TINY, 70, 90, 90, False, "Monospace"))
##        self.maxlim_tc.SetToolTipString(u"Upper Limit")
##
##        max_hbox.Add(self.maxlim_tc, 0,
##                     wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.TOP, 1)
##        lim_vbox.Add(max_hbox, 1, wx.EXPAND, 1)
##        xylim_hbox.Add(lim_vbox, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 1)
##
##        hbox.Add(xylim_hbox, 0, wx.EXPAND | wx.RIGHT, 5)
##
##        # (x, y) pos label
##        self.pos_st = wx.StaticText(self, label='')
##        hbox.Add(self.pos_st, 0, wx.ALIGN_CENTER_VERTICAL)
##        sizer.Add(hbox, 0, wx.EXPAND | wx.BOTTOM, 0)
##        self.SetSizerAndFit(sizer)
#
#    def post_init(self):
#        self._set_xylim_flag(self.xylim_choice.GetStringSelection())
#
#    def set_color(self, rgb_tuple):
#        """Set figure and canvas with the same color.
#
#        Parameters
#        ----------
#        rgb_tuple: tuple
#            `(r,g,b)` to define color, e.g. `(255, 255, 255)` is white color.
#        """
#        if rgb_tuple is None:
#            rgb_tuple = wx.SystemSettings.GetColour(DEFAULT_COLOR).Get()
#        color = [c / 255.0 for c in rgb_tuple]
#        self.figure.set_facecolor(color)
#        self.figure.set_edgecolor(color)
#        self.canvas.SetBackgroundColour(wx.Colour(*rgb_tuple))
#
#    def on_size(self, event):
#        self.fit_canvas()
#        self.canvas.draw_idle()
#        event.Skip()
#
#    def on_motion(self, event):
#        if event.inaxes is not None:
#            self.pos_st.SetLabel(
#                "({e.xdata:<.4f},{e.ydata:<.4f})".format(e=event))
#
#    def fit_canvas(self):
#        """Tight fit canvas layout.
#        """
#        #self.canvas.SetSize(self.GetSize())
#        self.figure.set_tight_layout(True)
#
#    def refresh(self):
#        self.canvas.draw_idle()
#
#    def xylim_choiceOnChoice(self, event):
#        sel_str = self.xylim_choice.GetStringSelection()
#        self._set_xylim_flag(sel_str)
#        if sel_str == 'Auto':
#            self.minlim_tc.Disable()
#            self.maxlim_tc.Disable()
#            self.minlim_st.Disable()
#            self.maxlim_st.Disable()
#
#            # auto set xy limit
#            min_list = [
#                np.vstack(line.get_data()).min(axis=1).tolist()
#                for line in self.axes.get_lines()
#            ]
#            max_list = [
#                np.vstack(line.get_data()).max(axis=1).tolist()
#                for line in self.axes.get_lines()
#            ]
#            xmin, ymin = np.array(min_list).min(axis=0)
#            xmax, ymax = np.array(max_list).max(axis=0)
#            x0, xhw = (xmin + xmax) * 0.5, (xmax - xmin) * 0.5
#            y0, yhw = (ymin + ymax) * 0.5, (ymax - ymin) * 0.5
#            _xmin, _xmax = x0 - xhw * 1.1, x0 + xhw * 1.1
#            _ymin, _ymax = y0 - yhw * 1.1, y0 + yhw * 1.1
#            self.axes.set_xlim([_xmin, _xmax])
#            self.axes.set_ylim([_ymin, _ymax])
#
#            self.refresh()
#        else:
#            self.minlim_tc.Enable()
#            self.maxlim_tc.Enable()
#            self.minlim_st.Enable()
#            self.maxlim_st.Enable()
#
#            try:
#                _xlim = self.axes.get_xlim()
#                _ylim = self.axes.get_ylim()
#            except:
#                _xlim = [0, 100]
#                _ylim = [0, 100]
#            self._set_default_minlim(_xlim, _ylim)
#            self._set_default_maxlim(_xlim, _ylim)
#
#    def _set_default_minlim(self, xlim_array, ylim_array):
#        if self._xylim_flag == 'X-Limit':
#            self.minlim_tc.SetValue("{xmin:.3g}".format(xmin=xlim_array[0]))
#        elif self._xylim_flag == 'Y-Limit':
#            self.minlim_tc.SetValue("{ymin:.3g}".format(ymin=ylim_array[0]))
#
#    def _set_default_maxlim(self, xlim_array, ylim_array):
#        if self._xylim_flag == 'X-Limit':
#            self.maxlim_tc.SetValue("{xmax:.3g}".format(xmax=xlim_array[1]))
#        elif self._xylim_flag == 'Y-Limit':
#            self.maxlim_tc.SetValue("{ymax:.3g}".format(ymax=ylim_array[1]))
#
#    def minlim_tcOnTextEnter(self, event):
#        xymin = float(self.minlim_tc.GetValue())
#        xymax = float(self.maxlim_tc.GetValue())
#        self._set_xylim_range(xymin, xymax)
#
#    def maxlim_tcOnTextEnter(self, event):
#        xymin = float(self.minlim_tc.GetValue())
#        xymax = float(self.maxlim_tc.GetValue())
#        self._set_xylim_range(xymin, xymax)
#
#    def _set_xylim_flag(self, flag='X-Limit'):
#        """Control x/y limit to be set
#
#        Parameters
#        ----------
#        flag: str
#            'X-Limit' (default), 'Y-Limit', 'Auto'.
#        """
#        self._xylim_flag = flag
#
#    def _set_xylim_range(self, vmin, vmax):
#        """Set x/y limit according to `_xylim_flag` value.
#        
#        Parameters
#        ----------
#        vmin: float
#            Lower limit.
#        vmax: float
#            Upper limit.
#        """
#        if self._xylim_flag == 'X-Limit':
#            self.axes.set_xlim([vmin, vmax])
#        elif self._xylim_flag == 'Y-Limit':
#            self.axes.set_ylim([vmin, vmax])
#        self.refresh()
#
#    def _func_peaks(self, x, y):
#        return 3.0 * (1.0 - x)**2.0 * np.exp(-(x**2) - (y+1)**2) \
#             - 10*(x/5 - x**3 - y**5) * np.exp(-x**2-y**2) \
#             - 1.0/3.0*np.exp(-(x+1)**2 - y**2)
#
#    def on_press(self, event):
#        raise NotImplementedError
#
#    def on_release(self, event):
#        raise NotImplementedError
#
#    def on_pick(self, event):
#        raise NotImplementedError
