# -*- coding: utf-8 -*-

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as Toolbar


class NavigationToolbar(Toolbar):
    def __init__(self, canvas):
        super(self.__class__, self).__init__(canvas)

#        self.user_tools = {}
#
#        icon1 = wx.ArtProvider.GetBitmap(wx.ART_QUIT, wx.ART_OTHER)
#        self.add_user_tool('lasso', 6, icon1, True, 'Lasso')
#
#    def add_user_tool(self, mode, pos, bmp, is_toggle=True, shortHelp=''):
#        tool_id = wx.NewId()
#        self.user_tools[mode] = self.InsertSimpleTool(pos, tool_id, bmp,
#                isToggle=is_toggle, shortHelpString=shortHelp)
#        self.Bind(wx.EVT_TOOL, self.on_toggle_user_tool, self.user_tools[mode])
#
#    def on_toggle_user_tool(self, e):
#        if e.Checked():
#            for tool in self.user_tools.values():
#                if tool.Id != e.Id:
#                    self.ToggleTool(tool.Id, False)
#
