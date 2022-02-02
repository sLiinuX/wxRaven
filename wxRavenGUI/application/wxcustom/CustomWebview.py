'''
Created on 1 janv. 2022

@author: slinux
'''
import sys
import wx
import wx.html2 as webview
import logging

class wxRavenWebview(object):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        #backend=wx.html2.WebViewBackendEdge
        #self = None
        
        #print('here1')
        is_windows = hasattr(sys, 'getwindowsversion')
        if is_windows:  
            pass
            #self._webview = webview.WebView.New(parent, backend=self.GetAvailableBackend(_windows=True))
        else:
            pass
            #self._webview = webview.WebView.New(parent, backend=self.GetAvailableBackend(_windows=False))
            
    
    
    @staticmethod
    def GetWebView(parent):
        
        #print('here2')
        _backend = wxRavenWebview.GetAvailableBackend()
        #print(_backend)
        #print('here2b')    
        return webview.WebView.New(parent, backend=_backend)
            
    
            
    @staticmethod        
    def GetAvailableBackend( _windows=True):
        logger = logging.getLogger('wxRaven')
        backend = None#webview.WebViewBackendDefault
        if True: 
            backend = None
            backends = [
                
                (webview.WebViewBackendIE, 'WebViewBackendIE'),
                (webview.WebViewBackendWebKit, 'WebViewBackendWebKit'),
                (webview.WebViewBackendDefault, 'WebViewBackendDefault'),
            ]
            
            if hasattr(sys, 'getwindowsversion') :
                backends.append((webview.WebViewBackendEdge, 'WebViewBackendEdge'))
                webview.WebView.MSWSetEmulationLevel(webview.WEBVIEWIE_EMU_IE11)
                
                
            for id, name in backends:
                available = webview.WebView.IsBackendAvailable(id)
                
                if available and backend is None:
                    backend = id
                logger.info("Backend 'wx.html2.{}' availability: {}\n".format(name, available))
             
            #self.wv = webview.WebView.New(self, backend=webview.WebViewBackendEdge)
    
        return backend