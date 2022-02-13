'''
Created on 9 déc. 2021

@author: slinux
'''
import wx

from wxRavenGUI.application import * 
from logging.handlers import TimedRotatingFileHandler


import logging
import time
import os


class wxRavenMainApp(object):
    '''
    classdocs
    '''
    
    
    
    
    

    def __init__(self, profile=None):
        '''
        Constructor
        '''
        self.app = wx.App()
        self.doStart=False
        self.appmainframe = None
        print("> SHOW splashscreen")
        self.splash = SplashScreenMgr(self, parentframe=None, profile=profile)
        #self.userpath = self.splash.
        print("> INIT END splashscreen")
        #self.appmainframe  = wxRavenAppMainFrame()
        #self.splash.SetParent(self.appmainframe)


    def setup_logging(self, forcePath='',_timeStampIt=False):
        #self._timestamp = round(time.time() * 1000) 
        

        #self._timestamp = round(time.time() * 1000) 
        
        _root = os.getcwd()
        if forcePath :
            _root = forcePath
        
        
        self.tradepath = _root + f"/userdata/atomicswap_session.log"
        self.savepath = _root + f"/userdata/wxraven_last_session.log"
        
        '''
        try:
            os.remove(self.savepath )  
            os.remove(self.tradepath )    
        except Exception as e:
            pass
        
        '''
        
        
        path = os.path.expanduser(self.savepath)
        
        #self.ensure_directory(os.path.dirname(path))
        self.logger = logging.getLogger('wxRaven')
        self.handler = TimedRotatingFileHandler(path, when='D', interval=1, backupCount=1)
        fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        formatter = logging.Formatter(fmt=fmt, datefmt='%m/%d/%Y %H:%M:%S')
        self.handler.setFormatter(formatter)
        self.handler.setLevel(logging.INFO)
        # tee output to console as well
        self.console = logging.StreamHandler()
        self.console.setFormatter(formatter)
        self.console.setLevel(logging.INFO)
        self.logger.addHandler(self.console)
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.INFO)
    
    
    def stop_logging(self):
        self.logger.removeHandler(self.console)
        self.logger.removeHandler(self.handler)

    def getApp(self):
        return self.appmainframe

        
    def runApp(self, forcePath=''):
        #self.appmainframe.Show()
        self.setup_logging(forcePath=forcePath)
        
        self.app.MainLoop() 
         
        self.stop_logging()
         
    