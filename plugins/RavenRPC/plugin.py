

'''
Created on 10 déc. 2021

@author: slinux
'''

import threading
from .wxRavenShellLogic import *
from wxRavenGUI.application.pluginsframework import *
import datetime

import re


from .pluginSettings import wxRavenRPCPluginSettings

class wxRavenPlugin(PluginObject):
    
    

    
    
    
    def __init__(self, parentFrame, position="mgr"):
        PluginObject.__init__(self, parentFrame, position=position)
        
        
        self.PLUGIN_NAME = "RavenRPC"
        self.PLUGIN_ICON = self.RessourcesProvider.GetImage('shell') 
        self.PLUGINS_VIEWS= [ 
                    {
                     'viewid':'RavenRPC Shell', 
                     'name':'RavenRPC Shell', 
                     'title':'RavenRPC Shell', 
                     'position':position, 
                     'icon':self.PLUGIN_ICON, 
                     'class': shellMainPanel ,
                     'default':False,
                     'multipleViewAllowed':True
                     },
                    
                     {
                     'viewid':'RavenRPC Advanced Shell', 
                     'name':'RavenRPC Advanced Shell', 
                     'title':'RavenRPC Advanced Shell', 
                     'position':position, 
                     'icon':wx.Bitmap( u"res/default_style/normal/shell_adv.png", wx.BITMAP_TYPE_ANY ), 
                     'class': shellAdvancedPanel ,
                     'default':False,
                     'multipleViewAllowed':True
                     },
                    
                     {
                     'viewid':'RPC Documentation Helper', 
                     'name':'RPC Documentation Helper', 
                     'title':'RPC Documentation Helper', 
                     'position':'main', 
                     'icon':wx.Bitmap( u"res/default_style/normal/bookmarks_view.png", wx.BITMAP_TYPE_ANY ), 
                     'class': ShellDocumentationHelper ,
                     'default':False,
                     'multipleViewAllowed':True
                     }
                    
                ]
        
        
        """
        ShellDocumentationHelper
        
        self.setData("all_connexion", [])
        self.setData("current_connexion", '')
        self.setData("_icon", wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY ))
        self.setData("_dataTimeStamp", '')
        """
        
        
        #
        # Lets put some setting pannels from pluginsetting file (to define as well)
        #
        self.PLUGIN_SETTINGS_GUI = []
        
        _Icon = self.RessourcesProvider.GetImage('shell')
        _setPanel = PluginSettingsTreeObject("RavenRPC", _Icon, classPanel=wxRavenRPCPluginSettings, _childs=None)
        self.PLUGIN_SETTINGS_GUI.append(_setPanel)
       
        self.setData("_icon", self.RessourcesProvider.GetImage('network') )
        
        self.setData("_CmdList", {})
        self.setData("_CmdListInCache", False)
        
        self.setData("_ShellLocalsAddins", {})
        
        self.ALLOW_MULTIPLE_VIEWS_INSTANCE = True
        self.parentFrame.ConnexionManager.RegisterOnConnexionChanged(self.OnNetworkChanged_T)
        #self.LoadPluginFrames()
        
        #self.LoadView(self.PLUGINS_VIEWS[1], 'mgr')
        
        #self.demoTest()
        
        #For test purpose
        self.waitApplicationReady()
    
    #
    # Run a thread and wait app to be fully loaded
    #
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.__applicationReady__,))
        t.start()
        
    #
    #  thread to wait
    #    
    def __waitLoop_T__(self,callback):
        while not self.parentFrame._isReady:
            time.sleep(1)
            
        wx.CallAfter(callback, ()) 
        
        
        #self.initializeAssetManagerBackgroundService()
    
    #
    #  thread callback
    #
    def __applicationReady__(self, evt=None):
        self.OnNetworkChanged_T()
    
    
    def demoTest(self):   
        self.LoadView(self.PLUGINS_VIEWS[0], 'mgr')
        self.LoadView(self.PLUGINS_VIEWS[0], 'mgr')
        self.LoadView(self.PLUGINS_VIEWS[0], 'mgr')
        self.LoadView(self.PLUGINS_VIEWS[0], 'mgr')
        self.LoadView(self.PLUGINS_VIEWS[0], 'main')
        self.LoadView(self.PLUGINS_VIEWS[0], 'toolbox1')
        self.LoadView(self.PLUGINS_VIEWS[0], 'toolbox2')
        self.LoadView(self.PLUGINS_VIEWS[0], 'toolbox2')
        self.LoadView(self.PLUGINS_VIEWS[0], 'toolbox3')
        
        #self.LoadView(self.PLUGINS_VIEWS[0])
        #self.LoadView(self.PLUGINS_VIEWS[0])
        
    
    
    """
     allow other plugins to add some locals var , warning this is dangerous !
    """
    
    #self.parent_frame.GetPlugin("RavenRPC").addLocalVarInShell( _data, _dataName)
    def addLocalVarInShell(self, _data, _dataName):
        
        _added=False
        _ShellLocalsAddins = self.getData("_ShellLocalsAddins")
        
        
        if not _ShellLocalsAddins.__contains__(_dataName):
        
            _ShellLocalsAddins[_dataName] = _data
            _added=True
        
        
        self.setData("_ShellLocalsAddins", _ShellLocalsAddins)
    
    
    def removeLocalVarInShell(self, _dataName):
        
        _added=False
        _ShellLocalsAddins = self.getData("_ShellLocalsAddins")
        
        
        if not _ShellLocalsAddins.__contains__(_dataName):
        
            _ShellLocalsAddins[_dataName] = None
            _added=True
        
        
        self.setData("_ShellLocalsAddins", _ShellLocalsAddins)
    
    
    def getAddinsLocals(self):
        _ShellLocalsAddins = self.getData("_ShellLocalsAddins")
        _addinsLocals= {}
        for key in _ShellLocalsAddins:
            
            _data = _ShellLocalsAddins[key]
            
            if _data != None:
                _addinsLocals[key] = _data
    
        return _addinsLocals
    '''
    
    Plugin Triggers for data update , DO NOT CALL WX UPDATE OUT OUF wx.CallAfter(cb, param)
    '''
        
            
        
    def OnNetworkChanged_T(self, networkName=""):    
        
        if not self.parentFrame._isReady:
            return None 
        
        t=threading.Thread(target=self.OnNetworkChanged)
        t.start()
        
        
    def OnNetworkChanged(self):
        
        self.setData("all_connexion", [])
        self.setData("current_connexion", '')
        self.setData("_icon", self.RessourcesProvider.GetImage('network') )
        self.setData("_dataTimeStamp", '')
        
        try:
            _data_all_connexion = self.parentFrame.ConnexionManager.getAllConnexions()
            _data_current_connexion = self.parentFrame.ConnexionManager.getCurrent()
            
            _icon = self.parentFrame.ConnexionManager.getIcon(_data_current_connexion)
            _dataTimeStamp = datetime.datetime.now()
            
            
            self.setData("all_connexion", _data_all_connexion)
            self.setData("current_connexion", _data_current_connexion)
            self.setData("_icon", _icon)
            self.setData("_dataTimeStamp", _dataTimeStamp)
            
            
            if self.getData("_CmdListInCache") == False:
                self.LoadRPCCommandsCache()
            
            wx.CallAfter(self.UpdateActiveViews, ())
            
        except Exception as e:
            self.RaisePluginLog( "Unable to retreive connexion informations :"+ str(e), type="error")
            #print(self.PLUGIN_NAME + " > OnNetworkChanged " + str(e))
            
            
    
    def LoadRPCCommandsCache(self):
        
        _CmdListInCache = False
        _CmdList = {}
        
        
        
        try:
            _globalHelp = self.parentFrame.getNetwork().help()['result']
            _allCommands = re.findall('[\n]([\S]*)',_globalHelp)
            
            
            for _cmd in _allCommands:
                
                if _cmd == "" or _cmd== "==":
                    continue
                try:
                    _cmdDesc = self.parentFrame.getNetwork().help(_cmd)['result']
                    _CmdList[_cmd] = _cmdDesc
                except Exception as e:
                    pass
                    #print(self.PLUGIN_NAME + " > error in command '"+_cmd+"' : "+ str(e))
        
        
            self.setData("_CmdList", _CmdList) 
            self.setData("_CmdListInCache", True) 
        
        except Exception as e:
            
            self.RaisePluginLog( "Unable to load RPC Commands list in cache", type="error")
            #print(self.PLUGIN_NAME + " > LoadRPCCommandsCache " + str(e))
        