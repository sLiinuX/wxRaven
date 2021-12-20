'''
Created on 14 déc. 2021

@author: slinux
'''
import os
from configparser import *
import inspect



from wxRavenGUI.view import  wxRavenSettingDialog
from wxRavenGUI.application.wxcustom.CustomTreeView import wxRavenTreeView
from wxRavenGUI.application.pluginsframework import *


import wx 
from wxRavenGUI.application.wxcustom import CustomTreeView    


class SettingsManager(object):
    '''
    classdocs
    '''
    
    CONFIG_PATH = os.getcwd() + "/config/"
    PLUGIN_PATH = os.getcwd() + "/plugins/"
    
    
    application_config_file = "config.ini"
    
    ConfigFileInstance = None
    
    
    
    resumeViewOnStartup = False
    forceInPrincipalAuiManager = False
    resumePluginState = True
    safeMode = True
    
    
    allconnexions = {}
    
    
    #parentframe = None
    
    
    
    
    
    

    def __init__(self, parentframe, configpath="", pluginpath="", cfgfile = "config.ini"):
        '''
        Constructor
        '''
        self.parentframe = parentframe
        
        
        if configpath!="":
            self.CONFIG_PATH = configpath
        else:
            self.CONFIG_PATH = os.getcwd() + "/config/"
        
        if pluginpath!="":
            self.PLUGIN_PATH = configpath
        else:
            self.PLUGIN_PATH = os.getcwd() + "/plugins/"
        
        self.application_config_file = cfgfile
        
        
        self.allconnexions = {}
        self.ConfigFileInstance = ConfigParser()
        
        try:
            self.LoadSettingsFromFile()
        except Exception as e:
            print(e)
            self.RaiseSettingsLog("Unable to load settings from file : " + str(e), "warning") 
        
    
    
    
    
    def RaiseSettingsLog(self, message, type="error"):
        try:
            _source = str(inspect.stack()[1][0])
            self.parentframe.Log( message, source=str(_source), type=type)
        except Exception as e:
            print("RaiseSettingsLog() " + str(e))  
            
            
            
            
            
            
    
    def SaveSettingsToFile(self):
        cfgfile = open(self.CONFIG_PATH+self.application_config_file ,'w')
        
        Config = ConfigParser()
        
        #Config.exist

        #resumeViewOnStartup = str(self.parentframe.wxRavenMenuBar_Window_Perspectives.IsChecked(self.parentframe.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.GetId()))
        #print("Save resumeViewOnStartup = " +resumeViewOnStartup)
        self._SaveGeneralSettings(Config)
        self._SaveConnexionSettings(Config)
        
        self._SaveAllPluginsSettings(Config)
        

        #Config.set('General','connexionChangedCallbackInSafeMode',str(self.connexionChangedCallbackInSafeMode))

        Config.write(cfgfile)
        cfgfile.close()
    
    
    def _SaveGeneralSettings(self, configObj):
        
        resumeViewOnStartup = str(self.parentframe.wxRavenMenuBar_Window_Perspectives.IsChecked(self.parentframe.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.GetId()))
        #print("Save resumeViewOnStartup = " +resumeViewOnStartup)
        
        configObj.add_section('Application')
        configObj.set('Application','resumeViewOnStartup',resumeViewOnStartup)
        configObj.set('Application','forceInPrincipalAuiManager',str(self.forceInPrincipalAuiManager))
        configObj.set('Application','resumePluginState',str(self.resumePluginState))
        configObj.set('Application','safeMode',str(self.safeMode))
        
        
        return configObj
        
        
    def _SaveConnexionSettings(self, configObj):
         
        
        configObj.add_section('Connexions')
        for key in self.allconnexions:
            
            data = self.allconnexions[key]
            configObj.set('Connexions',key,data)
    
    
    
    def _SavePluginSettings(self, pname, _pInstance, conf):
        
        
        for key in _pInstance.PLUGIN_SETTINGS:
            conf.set(pname,key,str(_pInstance.PLUGIN_SETTINGS[key]))
        
        
        return  conf   
    
    
    def _SaveAllPluginsSettings(self, configObj):
        
        
        for _p in self.parentframe.Plugins.plugins:
            
            _plugin_instance = self.parentframe.Plugins.GetPlugin(_p)
            if _plugin_instance != None:
                
                try:
                    configObj.add_section(_p)
                except:
                    pass
                
                
                self._SavePluginSettings(_p , _plugin_instance, configObj)
                
                
        return  configObj     
            
    
    
    
    
    
    def LoadSettingsFromFile(self):    
        
        Config = ConfigParser()
        Config.read(self.CONFIG_PATH+self.application_config_file)
        
        
        self._LoadGeneralConfig(Config)
        self._LoadConnexionSettings(Config)
    
        self.ConfigFileInstance = Config
    
    
    def _LoadGeneralConfig(self, configObj):
        #
        # View options
        #
        self.resumeViewOnStartup = configObj.getboolean("Application", "resumeViewOnStartup", fallback = False)
        self.parentframe.wxRavenMenuBar_Window_Perspectives.Check(self.parentframe.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.GetId(), self.resumeViewOnStartup )
        
        self.resumePluginState= configObj.getboolean("Application", "resumePluginState", fallback = True) 
        
        #
        # Hidden configuration for dev purpose
        #
        self.forceInPrincipalAuiManager = configObj.getboolean("Application", "forceInPrincipalAuiManager", fallback = False) 
        self.resumePluginState= configObj.getboolean("Application", "safeMode", fallback = True) 
    
    
    def _LoadConnexionSettings(self, configObj):
        #_raw = configObj.get('Connexions', fallback={}) 
        _raw = configObj['Connexions'] 
        self.allconnexions = _raw
    
    
    
    def _GetPluginSettings(self, pluginName):
        _pluginsSettings = {}
        
        
        if self.ConfigFileInstance.__contains__(pluginName):
            for key in self.ConfigFileInstance[pluginName]:
                _pluginsSettings[key] = self.ConfigFileInstance.get(pluginName, key)
    
        return _pluginsSettings
    
    
        
        
    def ConfigSectionMap(self, config, section):
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
                if dict1[option] == -1:
                    #DebugPrint("skip: %s" % option)
                    pass
            except:
                print("exception on %s!" % option)
                
                dict1[option] = None
        return dict1    
        
        
        
        
        
    def ShowSettingsDialog(self):
        settingsDialog = wxRavenSettingDialogLogic(self.parentframe)
        settingsDialog.Show()
        
        
        



        
class wxRavenSettingDialogLogic(wxRavenSettingDialog):
    
    
    
    
    def __init__(self, parentFrame):
        
        
        wxRavenSettingDialog.__init__(self, parentFrame)
        
        self.parentFrame=parentFrame

        icon = wx.EmptyIcon()
        icon.CopyFromBitmap( parentFrame.RessourcesProvider.GetImage('wizard-prefs') )
        self.SetIcon(icon)
        
        self._currentPannel = None
        self._currentPannelText = ""
        
        self.OPEN_PANEL_CACHE = {}
        
        
        _icons = {
            'test':parentFrame.RessourcesProvider.GetImage('packagefolder_obj') ,
            'app': parentFrame.RessourcesProvider.GetImage('frame_default') ,
            'pref':parentFrame.RessourcesProvider.GetImage('wizard-prefs') ,
            'views': parentFrame.RessourcesProvider.GetImage('perspective_default')  ,
            'network': parentFrame.RessourcesProvider.GetImage('networks')  ,
            'person':parentFrame.RessourcesProvider.GetImage('person')  ,
            'wallet': parentFrame.RessourcesProvider.GetImage('wallet'),
            'console': parentFrame.RessourcesProvider.GetImage('console_view')  
            
            #console_view.png
            }
        
        
        self._pagesAndPluginsMapping = { }
        
        
        self.wxTree = wxRavenTreeView(self.settingsTreeCtrl, _icons, _fillTreeCallback=None, _onChangeCallback=self.onChangeTest)
        self.fillTree()
        
        
        #self.wxTree._tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.onChangeTest, self.wxTree._tree)
        
    def onChangeTest(self,evt):    
        
        
        toplabel = self.wxTree._currentText + str(self._pagesAndPluginsMapping[self.wxTree._currentText])
        
        
        self.settingNameLabel.SetLabel(self.wxTree._currentText)
        
        
        _currentData = self.wxTree._currentData

        if _currentData == None or _currentData == {}:
            _currentData = wxRavenNotAvailableSettingPanel
        
        
        self.switchSettingPanel(_currentData)
        
            
        
        
        self.Layout()
        
    
    
    
    
    
    def switchSettingPanel(self, _pannel):
        
        if self._currentPannel!=None:
            #self._currentPannel.Destroy()
            self.OPEN_PANEL_CACHE[self._currentPannelText] = self._currentPannel
            self._currentPannel.Hide()
        
        
        
        if not self.OPEN_PANEL_CACHE.__contains__(self.wxTree._currentText):
            
            
            _NewPanel = _pannel(self.settingContentPlaceHolderPannel,self.parentFrame , self._pagesAndPluginsMapping[self.wxTree._currentText])
            
            print(_NewPanel._Panel)
            
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(_NewPanel._Panel , 1, wx.EXPAND|wx.ALL, 5)
            self.settingContentPlaceHolderPannel.SetSizer(sizer)
        
            self._currentPannel = _NewPanel
            self._currentPannelText = self.wxTree._currentText
            
        else:
            self._currentPannel = self.OPEN_PANEL_CACHE[self.wxTree._currentText]
            self._currentPannelText = self.wxTree._currentText
            self._currentPannel.Show()
            
        
        self.Layout()
        
        
    def _addMapping(self, title, pluginname):
        self._pagesAndPluginsMapping[title] = pluginname    
        
    def setupRoot(self):
        
        _dummyData = {}
        
        _root = self.wxTree.addItem(None, "root", _dummyData, "app")
        _app = self.wxTree.addItem(_root, "Application", _dummyData, "app")
        self._root = _root
        
        self._addMapping("Application", "General")
        
        #print(self.parentFrame)
       
        #GeneralPlug = self.parentFrame.GetPlugin("General")
        self.loadPluginSettingTree(_app, "General")
       
        """
        _last = self.wxTree.addItem(_app, "General", _dummyData, "pref")
        _last = self.wxTree.addItem(_app, "Views", _dummyData, "views")
        _last = self.wxTree.addItem(_app, "Connexions", _dummyData, "network")
        _last = self.wxTree.addItem(_app, "Account", _dummyData, "person")
        
        
        
        
        
        _last = self.wxTree.addItem(_root, "Wallet", _dummyData, "wallet")
        _last = self.wxTree.addItem(_root, "Test 2 ", _dummyData, "console")
        _last = self.wxTree.addItem(_root, "Test 3 ", _dummyData, "test")
        """
    
    
    def loadChildsPlugins(self, _ParenttreeItem , _child, pluginname):
        self.wxTree.addImage( _child._name ,  _child._icon )
        _treeItem = self.wxTree.addItem(_ParenttreeItem, _child._name , _child._classPanel,  _child._name)
        self._addMapping(_child._name, pluginname)
        if _child._childs != None:   
            for c in _child._childs:
                self.loadChilds(_treeItem, c)
        
        
     
    def loadPluginSettingTree(self, _treeParentItem, _pNme):
        
        
        _plugin = self.parentFrame.GetPlugin( _pNme )
        for _item in _plugin.PLUGIN_SETTINGS_GUI  :
            self.wxTree.addImage( _item._name ,  _item._icon )
            _treeItem = self.wxTree.addItem(_treeParentItem, _item._name , _item._classPanel,  _item._name)
            self._addMapping(_item._name, _pNme)
            if _item._childs != None:
                for c in _item._childs:
                    self.loadChildsPlugins(_treeItem, c, _pNme )
              
              
        if _plugin.PLUGIN_SETTINGS_GUI.__len__() == 0:
            
        
            #_prefIcon = self.RessourcesProvider.GetImage('wizard-prefs') #PLUGIN_ICON
            #_generalPannel = PluginSettingsTreeObject(PluginObject.PLUGIN_NAME, _prefIcon, classPanel=None, _childs=None)
            try:
                
                
                print(_plugin.PLUGIN_NAME)
                print(_plugin.PLUGIN_ICON)
                
                self.wxTree.addImage(_plugin.PLUGIN_NAME, _plugin.PLUGIN_ICON)
                _treeItem = self.wxTree.addItem(_treeParentItem, _plugin.PLUGIN_NAME ,data= wxRavenNotAvailableSettingPanel, iconname_normal=_plugin.PLUGIN_NAME)
                self._addMapping(_plugin.PLUGIN_NAME, _pNme)
            
            #self.PLUGIN_SETTINGS_GUI.append(_generalPannel)
            except:
                print("exception tree" )
            
        
    def setupPluginsSettings(self):
        
        for p in self.parentFrame.Plugins.plugins:
            if p == "General":
                continue
            
            #_pInst = self.parentFrame.GetPlugin( p )
            
            self.loadPluginSettingTree(self._root, p)
    
    def fillTree(self):  
        self.setupRoot()  
        self.setupPluginsSettings()
        



    
    def OnCancel(self, event):
        #
        #
        #to implement the rest
        #
        self.Close(force=True)
    
    def OnApplyCloseButton(self, event):
        #
        #
        #to implement the rest
        #
        pass
