'''
Created on 6 janv. 2022

@author: slinux
'''


import wx
from .wxCustomComponentDesign import wxRavenDialogbox

class wxRavenCustomDialog(wxRavenDialogbox):
    '''
    classdocs
    '''


    def __init__(self, parentframe, _view, title="", icon=None):
        wxRavenDialogbox.__init__(self,parentframe)
        
        self.Sizer = wx.BoxSizer( wx.VERTICAL )
        
        print(_view)
        _viewName = _view['name']
        _viewIcon = _view['icon']
                
        _viewClass = _view['class']
        
        self._Panel= _viewClass(self,parentframe, isInternalPluginView=True )
        
        
        self.Sizer .Add( self._Panel, 1, wx.ALL|wx.EXPAND, 5 )
        self.parentframe = parentframe
        self.SetTitle(title)
        
        if icon == None:
            icon = self.parentframe.RessourcesProvider.GetImage('view_default_frame')
            
        iconObj = wx.EmptyIcon()
        #icon.CopyFromBitmap(wx.Bitmap( u"res/default_style/normal/ravencoin.png", wx.BITMAP_TYPE_ANY ))
        iconObj.CopyFromBitmap(icon)
        self.SetIcon(iconObj)
        parentframe.RessourcesProvider.ApplyThemeOnPanel(self)
        parentframe.RessourcesProvider.ApplyThemeOnPanel(self._Panel)
        #self.SetSizerAndFit(self.Sizer)
        
        
        self.Bind( wx.EVT_CLOSE, self.OnClose )
        
        
        
        self.ResizeDialog()
        
    
    def ResizeDialog(self, evt=None):
        
        
        #self._Panel.Layout()
        self._Panel.SetSizerAndFit(self._Panel.GetSizer())
        self.SetSizerAndFit(self.Sizer)
        
        self.Layout()
        
    def UpdateView(self, evt=None):
        print('wxRavenCustomDialog UpdateView')
        #self.SetSizerAndFit(self.Sizer)
        self._Panel.UpdateView()
        self.ResizeDialog()
        
        
        
        
    def OnClose(self, evt):
        print('wxRavenCustomDialog OnClose')
        try:
            self._Panel.OnClose()
        
        except Exception as e:
            print("wxRavenCustomDialog OnClose() " + str(e)) 
        
        self.Destroy()
        