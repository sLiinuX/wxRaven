'''
Created on 19 déc. 2021

@author: slinux
'''


"""

    Simple utils for buttons and coloring, hovering event


"""


import wx

#
# Simple 
#
class wxRavenButton(wx.Button):
    def __init__(self, obj):
        #btn ().__init__( parent, wx.ID_ANY, Label, wx.DefaultPosition, wx.DefaultSize,0)
        self.obj = obj
        self._bt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        
        
        


class wxRavenColorButton(wx.Button):
    
    
    _backColors = []
    
    def __init__(self,obj, backgroundColors=[]):
        self.obj = obj
        self._backColors = backgroundColors
        obj.Bind( wx.EVT_ENTER_WINDOW, self.OnHover )
        obj.Bind( wx.EVT_LEAVE_WINDOW, self.OnLeaveHover )
        




    def OnHover(self, event):
        if self.obj.GetBackgroundColour() != self._backColors[0] and self.obj.IsEnabled():
            self.obj.SetBackgroundColour(self._backColors[0])
            self.obj.Refresh()
    
    def OnLeaveHover(self, evt):
        if self.obj.GetBackgroundColour() != self._backColors[0] and evt.IsEnabled():
            self.obj.SetBackgroundColour(self._backColors[0])
            self.obj.Refresh()








class wxRavenApplyButton(wxRavenColorButton):
    '''
    classdocs
    '''
    
    def __init__(self, obj ):
        '''
        Constructor
        '''  
        _fgColor = wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW )
        _bgColor = wx.Colour( 0, 159, 0 )
        wxRavenColorButton( obj, [_bgColor])

        
    
        
        
class wxRavenCancelButon(wxRavenColorButton):
    '''
    classdocs
    '''
    def __init__(self,obj):
        '''
        Constructor
        '''
        _fgColor = wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW )
        _bgColor = wx.Colour( 255, 159, 159 ) 
        wxRavenColorButton( obj, [_bgColor])
        
        
        
        