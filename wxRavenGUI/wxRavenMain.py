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
import wx.adv
import sys



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
        self.logEnable = False
        self.logger = None
        print("> SHOW splashscreen")
        self.splash = SplashScreenMgr(self, parentframe=None, profile=profile)
        
        if hasattr(sys, 'getwindowsversion') :
            x = threading.Thread(target=self.intro_sound, daemon=True)
            x.start()
            
        
        #data = open(_intropath, 'rb').read()
        #intro = wx.adv.Sound(_intropath)
        #print(intro.IsOk())
        #isOk = wx.adv.Sound.CreateFromData(intro, data)
        #print(intro.IsOk())
        #
        #if intro.IsOk():
        #    intro.Play(wx.adv.SOUND_ASYNC)
        #self.userpath = self.splash.
        print("> INIT END splashscreen")
        #self.appmainframe  = wxRavenAppMainFrame()
        #self.splash.SetParent(self.appmainframe)


    def intro_sound(self):
        _currentPath = os.getcwd()
        _intropath = _currentPath + f'/res/default_style/sounds/start.wav'
        
        try:
            #playsound(_intropath)
            intro = wx.adv.Sound(_intropath)
            intro.Play(wx.adv.SOUND_ASYNC)
        except Exception as e:
            pass


    def setup_logging(self, forcePath='',_debugMode=False):
        #self._timestamp = round(time.time() * 1000) 
        

        #self._timestamp = round(time.time() * 1000) 
        
        
        
        _root = os.getcwd()
        if forcePath :
            _root = forcePath
        
        
        #self.tradepath = _root + f"/userdata/atomicswap_session.log"
        self.savepath = _root + f"/userdata/wxraven_last_session.log"
        self.debugpath = _root + f"/userdata/wxraven_last_session-DEBUG.log"
        
  
        
        '''
        try:
            os.remove(self.savepath )  
            os.remove(self.tradepath )    
        except Exception as e:
            pass
        
        '''
        
        
        path = os.path.expanduser(self.savepath)
        
        
        if _debugMode:
            logging.basicConfig(filename=self.debugpath, level=logging.DEBUG, format=f'%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(name)s %(threadName)s : %(message)s')

        
        
        
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
        
        self.logEnable = True
        
        
    
    
    def stop_logging(self):
        if self.logger !=None:
            self.logger.removeHandler(self.console)
            self.logger.removeHandler(self.handler)
            #remove internal loggin handlers.
            for handler in logging.root.handlers[:]:
                logging.root.removeHandler(handler)
        
        self.logEnable = False

    def getApp(self):
        return self.appmainframe

        
    def runApp(self, forcePath=''):
        #self.appmainframe.Show()
        self.setup_logging(forcePath=forcePath)
        
        self.app.MainLoop() 
        print("End MainLoop, Goodbye wxUser !")
        if self.logEnable: 
            self.stop_logging()
         
    