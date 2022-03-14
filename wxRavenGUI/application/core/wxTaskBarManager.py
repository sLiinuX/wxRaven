'''
Created on 2 mars 2022

@author: slinux
'''
import wx
from wx.adv import TaskBarIcon as TaskBarIcon


class wxRavenTaskBarManager(TaskBarIcon):
    def __init__(self, parentframe):
        TaskBarIcon.__init__(self)

        self.frame = parentframe
        _icon = parentframe.RessourcesProvider.GetIcon('wxraven_icon')
        self.SetIcon(_icon, 'wxRaven')

        #------------
        
        self.Bind(wx.EVT_MENU, self.OnTaskBarActivate, id=1)
        self.Bind(wx.EVT_MENU, self.OnTaskBarDeactivate, id=2)
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=3)

    #-----------------------------------------------------------------------
        
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(1, 'Show')
        menu.Append(2, 'Hide')
        menu.Append(3, 'Close')

        return menu


    def OnTaskBarClose(self, event):
        self.frame.Close()


    def OnTaskBarActivate(self, event):
        if not self.frame.IsShown():
            self.frame.Show()


    def OnTaskBarDeactivate(self, event):
        if self.frame.IsShown():
            self.frame.Hide()