'''
Created on 9 déc. 2021

@author: slinux
'''
import wx

from wxRavenGUI.application import * 



class wxRavenMainApp(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self.app = wx.App()
        
        self.appmainframe = None
        self.splash = SplashScreenMgr(self, None)
        
        #self.appmainframe  = wxRavenAppMainFrame()
        #self.splash.SetParent(self.appmainframe)

    def getApp(self):
        return self.appmainframe


        
    def runApp(self):
        #self.appmainframe.Show()
        self.app.MainLoop()  
         
    