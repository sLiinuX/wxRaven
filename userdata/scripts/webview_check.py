'''
Created on 29 janv. 2022

@author: slinux
'''
import wx.html2 as webview
import sys

backends = [
    (webview.WebViewBackendIE, 'WebViewBackendIE'),
    (webview.WebViewBackendWebKit, 'WebViewBackendWebKit'),
    (webview.WebViewBackendDefault, 'WebViewBackendDefault'),
]

is_windows = hasattr(sys, 'getwindowsversion')
try:
    if is_windows:
        backends.append((webview.WebViewBackendEdge, 'WebViewBackendEdge'))
except Exception as e:
    pass


for id, name in backends:
    available = webview.WebView.IsBackendAvailable(id)
    print("Backend 'wx.html2.{}' availability: {}\n".format(name, available))