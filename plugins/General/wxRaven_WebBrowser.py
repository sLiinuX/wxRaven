'''
Created on 22 févr. 2022

@author: slinux
'''


from .wxRavenGeneralDesign import wxRavenWebBrowser
from wxRavenGUI.application.wxcustom.CustomLoading import *
from wxRavenGUI.application.wxcustom import *
import wx.html2 as webview
import sys
import logging
from wxRavenGUI.application.wxcustom.CustomUserIO import UserAdvancedMessage


class wxRaven_WebBrowserLogic(wxRavenWebBrowser):
    '''
    classdocs
    '''


    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "WebBrowser"
    view_name = "WebBrowser"
    parent_frame = None
    default_position = "main"
    icon = 'internal_browser'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parentFrame, position = "main", viewName= "WebBrowser", isInternalPluginView=False, url=''):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "WebBrowser"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self._loadingPanel = None
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
        
        
        #is_windows = hasattr(sys, 'getwindowsversion')
        #if is_windows:  
        #    self.WindowsSetup()
        
        
        self.wv=wxRavenWebview.GetWebView(self.m_webPan)
        '''
        is_windows = hasattr(sys, 'getwindowsversion')
        if is_windows:
             
            webview.WebView.MSWSetEmulationLevel(webview.WEBVIEWIE_EMU_IE11)
            _backend = self.GetAvailableBackend(_windows=True)
            
            if _backend == None:
                UserAdvancedMessage(parentFrame, "Unable to find a backend for the webview, \n please verify you do have the webview component or download it (url in details)", "Error", "https://developer.microsoft.com/en-us/microsoft-edge/webview2/", showCancel=False)
             
            self.wv = webview.WebView.New(self, backend=_backend)
        else:
            self.wv= webview.WebView.New(self)
        '''
        
        self.bSizer1 = wx.BoxSizer( wx.VERTICAL )
        self.bSizer1.Add( self.wv, 1, wx.ALL|wx.EXPAND, 5 )
        self.m_webPan.SetSizer( self.bSizer1 )
        self.Layout()
        
        
        self.m_buttonGo.Bind(wx.EVT_BUTTON,self.GetUrl )
        
        if url == '': 
            pass
            #self.LoadRavencoinIPFS()
        else:
            self.GetURL(url)
            
            
            
            
            
            
    def GetUrl(self, evt):
        url = self.m_textCtrlURL.GetValue()     
        self.wv.LoadURL(url)  
          