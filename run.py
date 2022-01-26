'''
Created on 9 déc. 2021

@author: slinux
'''

#
#
#
#    wxRaven from console or python
#
#
#
from wxRavenGUI import wxRavenMain



import wx
import sys, os
#sys.stderr = open(os.getcwd() + "session.log", "wb")
    

if __name__ == '__main__':
    Instance_wxRavenApplication = wxRavenMain.wxRavenMainApp()
    Instance_wxRavenApplication.runApp()
    #if Instance_wxRavenApplication.doStart:
    #    Instance_wxRavenApplication.runApp()
    #else:
    #    wx.Exit()