'''
Created on 1 janv. 2022

@author: slinux
'''


from .wxRavenIPFSDesign import *
from wxRavenGUI.application.wxcustom.CustomLoading import *
import wx.html2 as webview
import sys



class wxRavenIPFSWebHomepage(wxRavenIPFSWebView):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Ravencoin IPFS Home"
    view_name = "Ravencoin IPFS Home"
    parent_frame = None
    default_position = "main"
    icon = 'raven_ipfs'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parentFrame, position = "main", viewName= "Ravencoin IPFS Home", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Ravencoin IPFS Home"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self._loadingPanel = None
        
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
        
        self.vw=None
        is_windows = hasattr(sys, 'getwindowsversion')
        if is_windows:  
            self.wv = webview.WebView.New(self, backend=webview.WebViewBackendEdge)
        else:
            self.wv= webview.WebView.New(self)
        
        
        self.bSizer1 = wx.BoxSizer( wx.VERTICAL )
        self.bSizer1.Add( self.wv, 1, wx.ALL|wx.EXPAND, 5 )
        self.SetSizer( self.bSizer1 )
        self.Layout()
         
        self.LoadRavencoinIPFS()
    
    
    """
    
    def WindowsSetup(self):
        
        self.wv.Destroy()
        print("Windows Special setup")
        self.wv = webview.WebView.New(self,backend=wx.html2.WebViewBackendEdge )
        self.bSizer1 = wx.BoxSizer( wx.VERTICAL )
        self.bSizer1.Add( self.wv, 1, wx.ALL|wx.EXPAND, 5 )
        self.SetSizer( self.bSizer1 )
        self.Layout()
        print("Windows Special setup")
    
    
    """
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self):
        
        #self.UpdateDataFromPluginDatas()
        self.Layout()
    
    
        
    def LoadRavencoinIPFS(self):
        self.ShowLoading()
        #self.wv.LoadURL(url)
        plugin = self.parent_frame.GetPlugin("IPFS")
        hp=plugin.PLUGIN_SETTINGS['homepage_url']
        self.wv.LoadURL(hp)  
        self.wv.Hide()
        print("hide")
        self.Layout()
        self.m_timer1.Start(2000)
        
        
        
    
    
    def OnTick(self,evt):
        self.wv.Show()   
        self.m_timer1.Stop()  
        print("show")
        self.Layout()
        self.HideLoading()
    
    def OnWebViewLoaded(self, evt):
        # The full document has loaded
        self.current = evt.GetURL()
        #self.location.SetValue(self.current)
        self.HideLoading()    
        
        
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