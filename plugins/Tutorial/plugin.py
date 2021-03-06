'''
Created on 18 déc. 2021

@author: slinux



This file contains the main class to define the plugin
Each plugin must have a plugin.py file which declare a class wxRavenPlugin(PluginObject)


'''


#import the class form above level, it contains predefined functions to overwrite.
#from plugins.pluginObjectTemplate import * 
from wxRavenGUI.application.pluginsframework import *
#import the design of your plugin made in FormBuilder
from .wxRavenTutorialPluginDesign import *
#import the logic of your plugin (inherit design class with logic)
from .wxRavenTutorialPluginLogic import *

#import the plugin setting panels, from another file to be more simple
from .pluginSettings import MyTutorialSettingPanel_WithLogic


#used for long datas requests
import threading



class wxRavenPlugin(PluginObject):
    '''
    classdocs
    '''


    def __init__(self, parentFrame, position="mgr"):
        
        
        #Call the parent class with ParentFrame and Position
        #This object is the plugin instance and will manage all views internally.
        PluginObject.__init__(self, parentFrame, position=position)
        
        
        #
        #ParentFrame is used to refer to the main app
        #Position is used to refer to the defaut position views are open.
        #
        
        
        
        #Define your plugin meta-datas :
        #
        # Name : Name of the plugin, It match the Plugin Folder name (not verified in other cases)
        # Icon
        # Views : All the views that contains the plugin
        
       
        self.PLUGIN_NAME = "Tutorial"
        self.PLUGIN_ICON = self.RessourcesProvider.GetImage('help_view') #wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
        
        
        
        
        #
        #    View Object declare all the 'Views' that can be instanciated
        #    {
        #             'viewid':                  a unique id for the view
        #             'name':                    a name for the view
        #             'title':                   a title id for the view
        #             'position':, 
        #             'icon':
        #             'class': 
        #             'default':                 Boolean to determine if the view is open by default at startup
        #             'multipleViewAllowed':     Boolean to determine if the view allow multiple instance of it 
        #}
        #        
        
        
        self.PLUGINS_VIEWS= [ 
                    
                    
                    {
                     'viewid':'Tutorial View', 
                     'name':'Tutorial View', 
                     'title':'Tutorial View', 
                     'position':position, 
                     'icon':self.PLUGIN_ICON, 
                     'class': MyTutorialView_WithLogic ,
                     'default':False,
                     'multipleViewAllowed':True
                     }
                    
        
                    
                ]
        

        
        #
        #    Setting Object declare all the 'default settings' 
        #    Once the plugin loaded for the first time, those settings will be saved
        #    in the config.ini file in a dedicated section when app close.
        #
        #    On next plugin load, if the config file contains plugins settings
        #    those will be overwritten in the _LoadPluginSettings() function
        #    
        #    you need to declare your own function as later in the file to CAST datas 
        #    that come from the ConfigParser in String only
        #
        #    {
        #             'key':                 value
        #    }
        #        
        
        
        self.PLUGIN_SETTINGS = {
                'booleansetting' : True,
                'showerror' : ['error','message']
            }
        
        
        
        
        #
        # Lets put some setting pannels from pluginsetting file (to define as well)
        #
        self.PLUGIN_SETTINGS_GUI = []
        
        _prefIcon = self.RessourcesProvider.GetImage('wizard-prefs')
        _MyTutorialSettingPanel_WithLogic = PluginSettingsTreeObject("Tutorial", _prefIcon, classPanel=MyTutorialSettingPanel_WithLogic, _childs=None)
        self.PLUGIN_SETTINGS_GUI.append(_MyTutorialSettingPanel_WithLogic)

        
        
        
        #
        # Datas : In order to avoid each view to individually request the same data through RPC,
        #         the plugin can contains Global vars / datas shared to the views
        #         it also allow to request those big datas through thread and call update after
        #
        self.setData("myPluginData", {})
        self.setData("myPluginData2", False)
        
        
        #
        # Plugin can Register on callbacks like Connexion change in this case, it will start a thread to get datas
        #
        self.parentFrame.ConnexionManager.RegisterOnConnexionChanged(self.OnNetworkChanged_T)
        
        
        #
        # Finally, this last line is MANDATORY to load the default views.
        # REMOVED AND REPLACED BY AN AUTO LOAD
        #self.LoadPluginFrames()
        
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
        pass
    
    
    
    """
    
    Plugins setting management
    
    Note, this method must be overwritten on plugins that use settings since
    config parser only use STRING values.
    
    
    """
    
    #
    # Seems not mandatory with new LoadSetting Generic function but in case of specific
    # Types, better redeclare it!
    #
    
    """
    def _LoadPluginSettings(self):
        _recordedSettings = self.parentFrame.Settings._GetPluginSettings(self.PLUGIN_NAME)
        
        
        for key in _recordedSettings:
            
            
            #
            # _recordedSettings[key] Return string only, do your own mapping for complex datastructure
            #
            self.PLUGIN_SETTINGS[key] = _recordedSettings[key]
            
            
    """        
                
        
    '''
    
    Plugin Triggers / Callbacks for data update , DO NOT CALL WX UPDATE OUT OUF wx.CallAfter(cb, param)
     
    '''
        
            
        
    def OnNetworkChanged_T(self, networkName=""):   
        if not self.parentFrame._isReady:
            return None  
        t=threading.Thread(target=self.OnNetworkChanged)
        t.start()
        
        
    def OnNetworkChanged(self):
        
        self.setData("myPluginData", {})
        self.setData("myPluginData2", False)
        
        try:
            
            
            myPluginData = self.parentFrame.ConnexionManager.getAllConnexions()
            myPluginData2 = self.parentFrame.ConnexionManager.getCurrent()
            
            
            self.setData("myPluginData", myPluginData)
            self.setData("myPluginData2", myPluginData2)

            #When datas are loaded, add a call after to trigger plugins view update
            wx.CallAfter(self.UpdateActiveViews, ())
            
        except Exception as e:
            self.RaisePluginLog( "Unable to retreive connexion informations :"+ str(e), type="error")
            
            
        
        
        