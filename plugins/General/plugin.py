'''
Created on 10 déc. 2021

@author: slinux
'''

from plugins.pluginObjectTemplate import *
import threading
from datetime import datetime
import inspect



from .wxRavenErrorLogConsoleLogic import *
from .wxNotebookToolbox import *


class wxRavenPlugin(PluginObject):
    
    
    
    
    def __init__(self, parentFrame, position="mgr"):
        PluginObject.__init__(self, parentFrame, position=position)
        
        
        self.PLUGIN_NAME = "General"
        self.PLUGIN_ICON = wx.Bitmap( u"res/default_style/normal/dialog_default.png", wx.BITMAP_TYPE_ANY )
        
        
        self.PLUGINS_VIEWS= [ 
                    {
                     'viewid':'Error Log Console', 
                     'name':'Error Log Console', 
                     'title':'Error Log Console', 
                     'position':'mgr', 
                     'icon':wx.Bitmap( u"res/default_style/normal/error_log.png", wx.BITMAP_TYPE_ANY ), 
                     'class': RavenErrorLogConsole ,
                     'default':True,
                     'multipleViewAllowed':True
                     },
                    
                    
                    {
                     'viewid':'Notebook Toolbox', 
                     'name':'Notebook Toolbox', 
                     'title':'Notebook Toolbox', 
                     'position':'mgr', 
                     'icon':wx.Bitmap( u"res/default_style/normal/tab_view.png", wx.BITMAP_TYPE_ANY ), 
                     'class': RavenNotebookToolbox ,
                     'default':False,
                     'multipleViewAllowed':True,
                     'isArea':True
                     
                     },
                    
                    
                    
                ]
        
        
        
        self.PLUGIN_SETTINGS = {
                'showError' : ['error','message']
            }
        

        self.ALLOW_MULTIPLE_VIEWS_INSTANCE = True
        
        
        self.parentFrame.ConnexionManager.RegisterOnConnexionChanged(self.OnNetworkChanged_T)
        
        self.setData("allLogs", {})
        self.setData("_cursor",0)
        
        
        self.LoadPluginFrames()
    
    
    
    
    
    
    
    
    
        
    '''
    
    Plugin Triggers for data update , DO NOT CALL WX UPDATE OUT OUF wx.CallAfter(cb, param)
    '''
  
        
    def OnNetworkChanged_T(self, networkName=""):    
        t=threading.Thread(target=self.OnNetworkChanged)
        t.start()
        
        
    def OnNetworkChanged(self):
        
        self.Log("Network Changed !")
        
        """
        self.setData("globalBalance", 0.0)
        self.setData("allAccountsDatas", [])
        self.setData("globalAssetBalance", [])
        self.setData("allAddresses", [])
        """
            
        
    def Log(self, message , source="", timestamp=None, type="info"):
        
        
        existingLogs = self.getData("allLogs")
        _cursor = self.getData("_cursor")
        
        if timestamp == None:
            now = datetime.now()
            timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
         
        #print(str(inspect.stack()[0][0].f_code.co_name))
        #print(str(inspect.stack()[1][0].f_code.co_name))
        #print(str(inspect.stack()[2][0].f_code.co_name))
        
        #print(str(inspect.stack()[0][0]))
        #print(str(inspect.stack()[1][0]))
        #print(str(inspect.stack()[2][0]))
        if source == "":
            source = str(inspect.stack()[1][0])
         
        newLogLine = [type,str(message), source, timestamp]
        existingLogs[_cursor] = newLogLine
        self.setData("allLogs", existingLogs)
        
        _cursor = _cursor+1
        self.setData("_cursor", _cursor)
        wx.CallAfter(self.UpdateActiveViews, ())
        