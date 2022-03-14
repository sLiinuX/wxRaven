'''
Created on 23 déc. 2021

@author: slinux
'''

import wx.html2 as webview
from .wxRavenRavencoreDesign import wxRavenHTMLViewer
from wxRavenGUI.application.wxcustom.CustomLoading import *
import logging
import sys
from wxRavenGUI.application.wxcustom import *


class RavencoreHTMLViewer(wxRavenHTMLViewer):
    '''
    classdocs
    '''

    view_base_name = "Asset Preview"
    view_name = "Asset Preview"
    parent_frame = None
    default_position = "main"
    icon = 'ravencoin'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parentFrame, assetUrl ,position = "main", viewName= "Asset Preview", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Asset Preview"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.allIcons = {}
        
        self._loadingPanel = None
        
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
        '''    
        is_windows = hasattr(sys, 'getwindowsversion')
        if is_windows:  
            self.WindowsSetup()
        else:
            self.wv = webview.WebView.New(self, backend=self.GetAvailableBackend(_windows=False))
            
        '''  
        #bSizer12 = wx.BoxSizer( wx.VERTICAL )  
        #bSizer12.Add( self.wv, 1, wx.ALL|wx.EXPAND, 5 ) 
        #self.SetSizer( bSizer12)
        #self.Layout()
        
        
        #self.parent_frame.Views.UpdateGUIManager()
        
        self.Bind(webview.EVT_WEBVIEW_LOADED, self.OnWebViewLoaded, self.wv)
        #self.wv.LoadURL(assetUrl)
        
        
    def WindowsSetup(self):
        
        #self.wv = webview.WebView.New(self,backend=wx.html2.WebViewBackendEdge )
        
        
        webview.WebView.MSWSetEmulationLevel(webview.WEBVIEWIE_EMU_IE11)
        _backend = self.GetAvailableBackend(_windows=True)
            
        if _backend == None:
            UserAdvancedMessage(self.parent_frame, "Unable to find a backend for the webview, \n please verify you do have the webview component or download it (url in details)", "Error", "https://developer.microsoft.com/en-us/microsoft-edge/webview2/", showCancel=False)
             
        self.wv = webview.WebView.New(self, backend=_backend)
        
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        bSizer1.Add( self.wv, 1, wx.ALL|wx.EXPAND, 5 )
        self.SetSizer( bSizer1 )
        self.Layout()
        
    def GetAvailableBackend(self, _windows=True):
        backend = webview.WebViewBackendDefault
        if _windows: 
            backend = None
            backends = [
                
                (webview.WebViewBackendIE, 'WebViewBackendIE'),
                (webview.WebViewBackendWebKit, 'WebViewBackendWebKit'),
                (webview.WebViewBackendDefault, 'WebViewBackendDefault'),
            ]
            
            if hasattr(sys, 'getwindowsversion') :
                backends.append((webview.WebViewBackendEdge, 'WebViewBackendEdge'))
                
                
            for id, name in backends:
                available = webview.WebView.IsBackendAvailable(id)
                if available and backend is None:
                    backend = id
                logging.info("Backend 'wx.html2.{}' availability: {}\n".format(name, available))
             
            #self.wv = webview.WebView.New(self, backend=webview.WebViewBackendEdge)
    
        return backend    
            
        
    def LoadAssetUrl(self,url):
        self.ShowLoading()
        self.wv.LoadURL(url)
        
        
        
    
    def OnWebViewLoaded(self, evt):
        # The full document has loaded
        self.current = evt.GetURL()
        #self.location.SetValue(self.current)
        self.HideLoading()
        
        
        #is_windows = hasattr(sys, 'getwindowsversion')
        #if is_windows:
        #    self.wv.SetZoomType(wx.html2.WEBVIEW_ZOOM_TYPE_LAYOUT)
        #    self.wv.SetZoom(wx.html2.WEBVIEW_ZOOM_SMALL)
        #    self.wv.SetZoomFactor(0.5)
        
    def ShowLoading(self):
        
        #print('LOADER ON !')
        
        if self._loadingPanel  == None:
            self._loadingPanel =  wxBackgroundWorkerAnimation(self)
        
        self._loadingPanel.Center()
        self._loadingPanel.Show(show=True)
        
        #self._loadingPanel.Popup()
        self.Layout()
        
    def HideLoading(self):
        if self._loadingPanel  != None:
            self._loadingPanel.Hide()
            self._loadingPanel.Center()
            self.Layout()
        