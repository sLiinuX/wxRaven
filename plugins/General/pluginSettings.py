'''
Created on 20 déc. 2021

@author: slinux
'''



from .wxRavenGeneralDesign import GeneralSettingPanel, ApplicationSettingPanel, wxRavenConnexionSettings_SettingPanel, wxRavenPluginsSettings_SettingPanel

from wxRavenGUI.application.pluginsframework import PluginSettingsPanelObject



import wx

class wxRavenApplicationSettingPanel(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _panel = ApplicationSettingPanel(parent)
        self._parent = parent
        self.parentFrame = parentFrame
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(_panel)
        PluginSettingsPanelObject.__init__(self,_panel, parentFrame, pluginName)
    
        self._Panel = _panel
        self._panel = _panel
        
        
        self._viewMode = 0
        self._defaultArea = "main"
    
        self._Panel.m_radioBox1.Bind( wx.EVT_RADIOBOX, self.OnModeSelectionChange )
        self._Panel.Bind(wx.EVT_CHOICE, self.OnModeDefaultAreaChange, self._panel.defaultAreaChoiceList)
        
        #self._Panel.m_radioBox1.Bind( wx.EVT_RADIOBOX, self.OnChanged )
    
        self.textAdv = """The advanced mode few containers areas which provide additional options in the display :

The Manager place the view at the Top level (same as main and toolbox)
The Manager and Toolbox are Floatable panels.


Closing a view in those area do not completely close the view.
Views and perspective in those areas are resumed at next session.
            """
        self.textSimple = """The simple mode provide only one main areas where all views will be instanciated as a new tab in the notebook.

The main notebook allow simple placement of the different views, 
but doesn't allow to create Floating panels.

Closing a notebook page close completely the view.
Notebook perspective is not saved yet between sessions.
            """
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        if self._viewMode == 0:
            self.parentFrame.Settings.forceinprincipalauimanager = True
        else:
            self.parentFrame.Settings.forceinprincipalauimanager = False
    
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)  
        myPlugin.PLUGIN_SETTINGS['defaultviewarea'] = self._defaultArea
        
        
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)  
        
        
        
        forceinprincipalauimanager = self.parentFrame.Settings.forceinprincipalauimanager
        """
        if forceinprincipalauimanager :
            
            self._panel.m_radioBox1.SetSelection(0)
            self._panel.descriptionText.SetLabel(self.textSimple)
            self._panel.defaultAreaOptionPanel.Hide()
            
        else:
            self._panel.m_radioBox1.SetSelection(1)
            self._panel.descriptionText.SetLabel(self.textAdv)
            self._panel.defaultAreaOptionPanel.Show()
        """
        
        self._panel.defaultAreaOptionPanel.Layout()
        defaultArea = myPlugin.PLUGIN_SETTINGS['defaultviewarea']
        self._defaultArea = defaultArea
        id  = self._panel.defaultAreaChoiceList.FindString(defaultArea)
        self._panel.defaultAreaChoiceList.SetSelection(id)
        
        
        if not forceinprincipalauimanager:
            self._panel.m_radioBox1.SetSelection(1)
            self.OnModeSelectionChange(evt=None,Override=1 )
        else:
            self._panel.m_radioBox1.SetSelection(0)
            self.OnModeSelectionChange(evt=None,Override=0 )
            
    def OnModeDefaultAreaChange(self, evt):
        self._defaultArea = evt.GetString()
        self.OnChanged(evt)
    
    def OnModeSelectionChange(self, evt=None, Override=-1):
        _newNode= None
        
         
        if Override != -1:
            _newNode = Override
            print("Called override")
        else:
            _newNode = evt.GetInt()
            print("Called normal")
        #print(_newNode)
        self._viewMode = _newNode
        
        
        
        if _newNode == 1:
            
            self._panel.defaultAreaOptionPanel.Show()
            self._panel.descriptionText.SetLabel(self.textAdv)
            self._panel.modeIllustrationBmp.SetBitmap(self.parentFrame.RessourcesProvider.GetImage('app_avanced_mode'))
        else:
            self._panel.modeIllustrationBmp.SetBitmap(self.parentFrame.RessourcesProvider.GetImage('app_simple_mode'))
            self._panel.defaultAreaOptionPanel.Hide()
            #self._panel.m_radioBox1.SetSelection(0)
            self._panel.descriptionText.SetLabel(self.textSimple)
        
        #myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        if Override==-1:
            self.OnChanged(evt)
        #self.Layout()
        #_parent
        self._panel.Layout()  
        self._panel.defaultAreaOptionPanel.Layout()
        self._parent.Layout()  
        #modeIllustrationBmp


class wxRavenGeneralSettingPanel(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _panel = GeneralSettingPanel(parent)
        PluginSettingsPanelObject.__init__(self,_panel, parentFrame, pluginName)
     
    
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        pass
    
    
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        pass    
    
    
    
    
    
    


class wxRavenConexionsSettingPanel(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRavenConnexionSettings_SettingPanel(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
        self._needReboot = True
    
        #_Panel.SetBackgroundColour( wx.Colour( 217, 228, 255 ) )
        
        #self._Panel
        
        
        _Panel.Bind( wx.EVT_BUTTON, self.OnAddProvider,id = _Panel.bookmark_addbt.GetId()  )
        _Panel.Bind( wx.EVT_BUTTON, self.OnRemoveProvider,id = _Panel.bookmark_rembt.GetId()  )
     
        self.Layout()
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        allProviders = []
        
        appSettings = self.parentFrame.Settings
        _newList = {}
        _errorsParsing = False
        for i in range(0, self._Panel.bookmark_list.Count):
            
            
            _con = self._Panel.bookmark_list.GetString(i)
             
            try:
                _conArr = _con.split('=')
                _name = _conArr[0]
                _val = _conArr[1]
                
                _newList[_name] = _val

                
            except Exception as e:
                _errorsParsing = True
                print(f"erreur in the connexion '{_con}', data will not be saved")
            
        
        if not _errorsParsing:    
            appSettings.allconnexions = _newList   
            
        
        
        #default =    allProviders[0] 
        #Settings
        #myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #myPlugin.PLUGIN_SETTINGS["ipfsgateway_default"]    = default
        #myPlugin.PLUGIN_SETTINGS["bookmark_list"]  = allProviders
    
    
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        allproviders = self.parentFrame.Settings.allconnexions 
        
        _dispArray = []
        for key in allproviders:
            _val=allproviders[key]
            
            strCon = str(key) + " = " + str(_val)
            
            _dispArray.append(strCon)
        
        self._Panel.bookmark_list.InsertItems(_dispArray, 0)
        
        #print("LoadPanelSettings")     
        
        
        self._Panel.Layout()
        
    def OnAddProvider(self, evt):    
        
        newp  = self._Panel.bookmark_text_area.GetValue()
        self._Panel.bookmark_list.InsertItems([newp], self._Panel.bookmark_list.Count)
        self._settingsHasChanged = True
        self._Panel.Layout()
        
        
    def OnRemoveProvider(self, evt):    
        x = self._Panel.bookmark_list.GetSelection()
        self._Panel.bookmark_list.Delete(x)
        self._settingsHasChanged = True
        self._Panel.Layout()
        
        
    def OnMoveProviderUp(self, evt): 
        x = self._Panel.bookmark_list.GetSelection()
        #self._Panel.ipfs_provider_list.SetFirstItem(x)
        #print(x)
        
        _itemTopromote = self._Panel.bookmark_list.GetString(x)
        self._Panel.bookmark_list.Delete(x)
        
        self._Panel.bookmark_list.InsertItems([_itemTopromote], 0)
        
        self._settingsHasChanged = True
        self._Panel.Layout()
        
        
        
        
        
        
        
class wxRavenPluginsSettingPanel(PluginSettingsPanelObject):

    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRavenPluginsSettings_SettingPanel(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
    
        self._needReboot = True
        
        self._Panel.m_pluginCheckListbox.Bind( wx.EVT_CHECKLISTBOX, self.OnChanged )
    
    
    
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        #print("SavePanelSettings")
        #_newValueForBoolSetting = self._Panel.booleansetting.IsChecked()
        
        #now its up to the dev to chose how to take this information
        #in our demo lets do simple and just change the  booleansetting in PLUGIN_SETTINGS
 
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        _currentPluginList = self.parentFrame.Plugins.plugins
        # _currentDisableValue = myPlugin.PLUGIN_SETTINGS['disable_plugins']
        _currentDisableValueIndex = self._Panel.m_pluginCheckListbox.GetCheckedStrings()
        
        
        print(_currentDisableValueIndex)
        
        
        _toSaveArray = []
        
        for _val in _currentDisableValueIndex:
            _toSaveArray.append(_val)
        
        myPlugin.PLUGIN_SETTINGS['disable_plugins'] = _toSaveArray
        print("SavePanelSettings")
        #myPlugin.PLUGIN_SETTINGS['booleansetting'] = _newValueForBoolSetting
    
        #print("SavePanelSettings" + str(_newValueForBoolSetting))
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        _currentDisableValue = myPlugin.PLUGIN_SETTINGS['disable_plugins']
        
        
        _currentPluginList = self.parentFrame.Plugins._detected_plugin_list
        _toArray = []
        
        for key in _currentPluginList:
            _toArray.append(key)

            
            
        self._Panel.m_pluginCheckListbox.InsertItems(_toArray, 0) 
        
        iList=[]
        for disable in _currentDisableValue:
            i = self._Panel.m_pluginCheckListbox.FindString(disable)
            if i != -1:
                iList.append(i)
        
        print(iList)
        self._Panel.m_pluginCheckListbox.SetCheckedItems(iList)
        
        #self._Panel.booleansetting.SetValue(_currentValue)
        
        print("LoadPanelSettings" + str(_toArray))
        
        
    #
    #
    # method called when closing in case of thread or anything
    #     
    def safeClose(self):
        pass    
        





