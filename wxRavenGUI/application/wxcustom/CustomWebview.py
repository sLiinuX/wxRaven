'''
Created on 1 janv. 2022

@author: slinux
'''
import sys
import wx
import wx.html2 as webview


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
        
        is_windows = hasattr(sys, 'getwindowsversion')
        if is_windows:  
            
            self = webview.WebView.New(parent, backend=webview.WebViewBackendEdge)
        else:
            self= webview.WebView.New(parent)