'''
Created on 20 déc. 2021

@author: slinux
'''

from plugins.configurations import  __wxraven_configurations_list__, __wxraven_configurations_icons__

from .wxRavenGeneralDesign import GeneralSettingPanel, ApplicationSettingPanel, wxRavenConnexionSettings_SettingPanel, wxRavenPluginsSettings_SettingPanel, wxRaven_General_WalletSettings, wxRavenConnexionRelaysSettings_SettingPanel

from wxRavenGUI.application.pluginsframework import PluginSettingsPanelObject


from wxRavenGUI.application.wxcustom import *


import wx
from wxRavenGUI.application.wxcustom.CustomUserIO import UserAdvancedMessage

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
        self._parent = parent
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
     
        self._Panel.m_checkBoxDisclaimer.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        self._Panel.m_checkBoxWelcome.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        self._Panel.m_checkBoxResume.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        self._Panel.m_checkBoxPurgeOnClose.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        self._Panel.m_checkBoxSaveSession.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        self._Panel.m_spinJobMax.Bind( wx.EVT_SPINCTRL, self.OnChanged )
        
        self._Panel.m_UseRemoteJob.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        self._Panel.m_AllowRemoteJobs.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        
        
        self._parent = parent
        self._Panel = _panel
        self._panel = _panel
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)  
        
        
        myPlugin.PLUGIN_SETTINGS['show_disclaimer'] = not self._Panel.m_checkBoxDisclaimer.GetValue()
        myPlugin.PLUGIN_SETTINGS['show_welcome'] = not self._Panel.m_checkBoxWelcome.GetValue()
        
        myPlugin.PLUGIN_SETTINGS['purge_on_close'] = not self._Panel.m_checkBoxPurgeOnClose.GetValue()
        
        
        myPlugin.PLUGIN_SETTINGS['log_mode'] =  self._Panel.m_checkBoxLogSession.GetValue()
        myPlugin.PLUGIN_SETTINGS['debug_mode'] =  self._Panel.m_checkBoxDebugSession.GetValue()
    
        myPlugin.PLUGIN_SETTINGS['max_running_jobs'] =  self._Panel.m_spinJobMax.GetValue()
        
        
        myPlugin.PLUGIN_SETTINGS['authorize_remote_jobs']  =  self._Panel.m_AllowRemoteJobs.GetValue()
        myPlugin.PLUGIN_SETTINGS['use_remote_jobs']  =  self._Panel.m_UseRemoteJob.GetValue()
        
    
        self.parentFrame.PerspectiveManager.ToggleResumeViewSettings(self._Panel.m_checkBoxResume.GetValue())
        self.parentFrame.PerspectiveManager.ToggleSaveViewSettings(self._Panel.m_checkBoxSaveSession.GetValue())
        
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)  
        
        
        hide_disclaimer = not myPlugin.PLUGIN_SETTINGS['show_disclaimer']
        self._Panel.m_checkBoxDisclaimer.SetValue(hide_disclaimer)    
        
        dont_load_welcome = not myPlugin.PLUGIN_SETTINGS['show_welcome']
        self._Panel.m_checkBoxWelcome.SetValue(dont_load_welcome)    
        
        purge_on_close = myPlugin.PLUGIN_SETTINGS['purge_on_close']
        self._Panel.m_checkBoxPurgeOnClose.SetValue(purge_on_close)    
        
        
        save_on_close= myPlugin.PLUGIN_SETTINGS['save_on_close']
        self._Panel.m_checkBoxSaveSession.SetValue(save_on_close)  
        
        
        log_mode= myPlugin.PLUGIN_SETTINGS['log_mode']
        self._Panel.m_checkBoxLogSession.SetValue(log_mode)  
        
        
        debug_mode= myPlugin.PLUGIN_SETTINGS['debug_mode']
        self._Panel.m_checkBoxDebugSession.SetValue(debug_mode)  
        
          
        max_running_jobs = myPlugin.PLUGIN_SETTINGS['max_running_jobs'] 
        self._Panel.m_spinJobMax.SetValue(max_running_jobs)
        
        
        
        use_remote_jobs = myPlugin.PLUGIN_SETTINGS['use_remote_jobs'] 
        self._Panel.m_UseRemoteJob.SetValue(use_remote_jobs)
        
        authorize_remote_jobs = myPlugin.PLUGIN_SETTINGS['authorize_remote_jobs'] 
        self._Panel.m_AllowRemoteJobs.SetValue(authorize_remote_jobs)
        
        
        
        self._Panel.m_checkBoxResume.SetValue(self.parentFrame.Settings.resumeviewonstartup )   
       
        self._Panel.Layout()  
        self._parent.Layout()  
         
        
    
    
    
    
    


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
                _name = _conArr[0].replace(' ', '')
                _val = _conArr[1].replace(' ', '')
                
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
        if len(_dispArray)>0:
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
        
        
        
















class wxRavenConnexionRelaysSettings_SettingLogic(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRavenConnexionRelaysSettings_SettingPanel(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
        self._needReboot = True
        
        #_Panel.SetBackgroundColour( wx.Colour( 217, 228, 255 ) )
        
        #self._Panel
        
        
        _Panel.Bind( wx.EVT_BUTTON, self.OnAddProvider,id = _Panel.bookmark_addbt.GetId()  )
        _Panel.Bind( wx.EVT_BUTTON, self.OnRemoveProvider,id = _Panel.bookmark_rembt.GetId()  )
        
        
        self._Panel.m_checkNoPublicAuth.Bind(wx.EVT_CHECKBOX, self.OnChanged)
        self._Panel.m_checkPrivateAuth.Bind(wx.EVT_CHECKBOX, self.OnChanged)
        self._Panel.m_textUserSessionToken.Bind(wx.EVT_TEXT, self.OnChanged)
        
        
     
        self.Layout()
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        allProviders = []
        myPlugin = self.parentFrame.GetPlugin(self.pluginName) 
        #appSettings = self.parentFrame.Settings
        _newList = {}
        _errorsParsing = False
        for i in range(0, self._Panel.bookmark_list.Count):
            
            
            _con = self._Panel.bookmark_list.GetString(i)
             
            try:
                _conArr = _con.split('=')
                _name = _conArr[0].replace(' ', '')
                _val = _conArr[1].replace(' ', '')
                
                _newList[_name] = _val

                
            except Exception as e:
                _errorsParsing = True
                print(f"erreur in the connexion '{_con}', data will not be saved")
            
        
        if not _errorsParsing:    
            myPlugin.PLUGIN_SETTINGS['webservices_relays'] = _newList
            
            
        
        myPlugin.PLUGIN_SETTINGS['relay_user_session_token'] = not self._Panel.m_checkNoPublicAuth.GetValue()
        
        myPlugin.PLUGIN_SETTINGS['relay_private_session_key'] = self._Panel.m_checkPrivateAuth.GetValue()
        
        myPlugin.PLUGIN_SETTINGS['relay_private_session_key_value'] = self._Panel.m_textUserSessionToken.GetValue()
        
        
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
        myPlugin = self.parentFrame.GetPlugin(self.pluginName) 
        allproviders = myPlugin.PLUGIN_SETTINGS['webservices_relays']
        
        _dispArray = []
        for key in allproviders:
            _val=allproviders[key]
            
            strCon = str(key) + " = " + str(_val)
            
            _dispArray.append(strCon)
        if len(_dispArray)>0:
            self._Panel.bookmark_list.InsertItems(_dispArray, 0)
            
            
            
        relay_user_session_token = not myPlugin.PLUGIN_SETTINGS['relay_user_session_token']
        self._Panel.m_checkNoPublicAuth.SetValue(relay_user_session_token)   
        
        relay_private_session_key = myPlugin.PLUGIN_SETTINGS['relay_private_session_key']
        self._Panel.m_checkPrivateAuth.SetValue(relay_private_session_key)   
        
        relay_private_session_key_value = myPlugin.PLUGIN_SETTINGS['relay_private_session_key_value']
        self._Panel.m_textUserSessionToken.SetValue(relay_private_session_key_value)   
        
        
        #if not relay_private_session_key:
        #    self._Panel.m_textUserSessionToken.Enable(False)
        
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
    
        self._Panel.m_choiceEdition.Bind( wx.EVT_CHOICE, self.EdditionChanged ) 
    
    
    
    
    
    
    
    
    
    
    def EdditionChanged(self, evt=None):
        if evt!=None:
            self._settingsHasChanged=True
        
        _edd= self._Panel.m_choiceEdition.GetString(self._Panel.m_choiceEdition.GetCurrentSelection())      
        
        
        if _edd != 'wxRaven : Developer/Server Edition':
            self._Panel.m_pluginCheckListbox.Enable(False)
        else:
            self._Panel.m_pluginCheckListbox.Enable(True)
            
            
        _editionIcon = __wxraven_configurations_icons__[_edd]
        
        self._Panel.m_bitmap19.SetBitmap(self.parentFrame.RessourcesProvider.GetImage(_editionIcon))
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
        
        
        
        _edd= self._Panel.m_choiceEdition.GetString(self._Panel.m_choiceEdition.GetCurrentSelection())      
        
        myPlugin.PLUGIN_SETTINGS['sw_configuration'] = _edd
        
        if _edd == 'wxRaven : Developer/Server Edition':
            myPlugin.PLUGIN_SETTINGS['disable_plugins'] = _toSaveArray
        else:
            myPlugin.PLUGIN_SETTINGS['disable_plugins'] = []
        
        
        
        
        print("SavePanelSettings")
        #myPlugin.PLUGIN_SETTINGS['booleansetting'] = _newValueForBoolSetting
    
        #print("SavePanelSettings" + str(_newValueForBoolSetting))
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        
        
        sw_configuration = myPlugin.PLUGIN_SETTINGS['sw_configuration']
        
        allAvailableEditions = list(__wxraven_configurations_list__.keys())
        for ed in allAvailableEditions:
            self._Panel.m_choiceEdition.Append(ed)
        
        _dc = self._Panel.m_choiceEdition.FindString(sw_configuration)
        if _dc != wx.NOT_FOUND:
            self._Panel.m_choiceEdition.SetSelection(_dc)
            
            
            
            
            
        
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
        self.EdditionChanged(None)
        
        
    #
    #
    # method called when closing in case of thread or anything
    #     
    def safeClose(self):
        pass    
        




        








        
        
class wxRaven_General_WalletSettingsLogic(PluginSettingsPanelObject):

    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRaven_General_WalletSettings(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
    
        #self._needReboot = True
        
        #self._Panel.m_pluginCheckListbox.Bind( wx.EVT_CHECKLISTBOX, self.OnChanged )
        self._Panel.m_NetworkChoice.Bind( wx.EVT_CHOICE, self.OnChangedNetwork )
        self._Panel.m_SaveNetwork.Bind(wx.EVT_BUTTON, self.DoSaveNetworkSettings )
    
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
        #_currentPluginList = self.parentFrame.Plugins.plugins
        # _currentDisableValue = myPlugin.PLUGIN_SETTINGS['disable_plugins']
        #_currentDisableValueIndex = self._Panel.m_pluginCheckListbox.GetCheckedStrings()
        
        
        #print(_currentDisableValueIndex)
        
        
        #_toSaveArray = []
        
        #for _val in _currentDisableValueIndex:
        #    _toSaveArray.append(_val)
        
        #myPlugin.PLUGIN_SETTINGS['disable_plugins'] = _toSaveArray
        print("SavePanelSettings")
        #myPlugin.PLUGIN_SETTINGS['booleansetting'] = _newValueForBoolSetting
    
        #print("SavePanelSettings" + str(_newValueForBoolSetting))
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #_currentDisableValue = myPlugin.PLUGIN_SETTINGS['disable_plugins']
        
        
        
        #
        #Connexion list
        allproviders = self.parentFrame.Settings.allconnexions 
        
        _dispArray = []
        for key in allproviders:
            self._Panel.m_NetworkChoice.Append(key)
        
        #_currentPluginList = self.parentFrame.Plugins._detected_plugin_list
        #_toArray = []
        
        #for key in _currentPluginList:
        #    _toArray.append(key)






    def DoSaveNetworkSettings(self, evt=None):
        _selected = self._Panel.m_NetworkChoice.GetString(self._Panel.m_NetworkChoice.GetCurrentSelection())
        
        favorite_send_addresses =  self._Panel.m_AddrSendChoice.GetString(self._Panel.m_AddrSendChoice.GetCurrentSelection())
        favorite_receive_addresses =  self._Panel.m_AddreReceiveChoice.GetString(self._Panel.m_AddreReceiveChoice.GetCurrentSelection())
        favorite_change_addresses =  self._Panel.m_AddrChangeChoice.GetString(self._Panel.m_AddrChangeChoice.GetCurrentSelection())
        

        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        myPlugin.PLUGIN_SETTINGS['favorite_send_addresses'][_selected] = favorite_send_addresses
        myPlugin.PLUGIN_SETTINGS['favorite_receive_addresses'][_selected]= favorite_receive_addresses
        myPlugin.PLUGIN_SETTINGS['favorite_change_addresses'][_selected]= favorite_change_addresses





    def OnChangedNetwork(self, evt):
        _selected = self._Panel.m_NetworkChoice.GetString(self._Panel.m_NetworkChoice.GetCurrentSelection())
        ravencoin = self.parentFrame.getRvnRPC(_selected)        
         
         
        if self._settingsHasChanged:
            _dosave = UserQuestion(self.parentFrame, "Settings unsaved, save now ?")
            
            if _dosave:
                self.DoSaveNetworkSettings()
        
        
        
        
        _allmyAddress = ravencoin.wallet.getAllWalletAddresses()
        
        self._Panel.m_AddrSendChoice.Clear()  
        self._Panel.m_AddreReceiveChoice.Clear() 
        self._Panel.m_AddrChangeChoice.Clear() 
        
        
        for ad in _allmyAddress :
            self._Panel.m_AddrSendChoice.Append(ad)
            self._Panel.m_AddreReceiveChoice.Append(ad)
            self._Panel.m_AddrChangeChoice.Append(ad)
        
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        favorite_send_addresses_all = myPlugin.PLUGIN_SETTINGS['favorite_send_addresses']
        favorite_receive_addresses_all = myPlugin.PLUGIN_SETTINGS['favorite_receive_addresses']
        favorite_change_addresses_all = myPlugin.PLUGIN_SETTINGS['favorite_change_addresses']
        
        favorite_send_addresses = ''
        favorite_receive_addresses = ''
        favorite_change_addresses = ''
        
        
        
        if favorite_send_addresses_all.__contains__(_selected):
            favorite_send_addresses = favorite_send_addresses_all[_selected]
            
            _dc = self._Panel.m_AddrSendChoice.FindString(favorite_send_addresses)
            if _dc != wx.NOT_FOUND:
                self._Panel.m_AddrSendChoice.SetSelection(_dc)
            
        
        if favorite_receive_addresses_all.__contains__(_selected):
            favorite_receive_addresses = favorite_receive_addresses_all[_selected]
            
            _dc = self._Panel.m_AddreReceiveChoice.FindString(favorite_receive_addresses)
            if _dc != wx.NOT_FOUND:
                self._Panel.m_AddreReceiveChoice.SetSelection(_dc)
                
                
                
        if favorite_change_addresses_all.__contains__(_selected):
            favorite_change_addresses = favorite_change_addresses_all[_selected]
            
            _dc = self._Panel.m_AddrChangeChoice.FindString(favorite_change_addresses)
            if _dc != wx.NOT_FOUND:
                self._Panel.m_AddrChangeChoice.SetSelection(_dc)
        '''    
        _dc = self._Panel.m_NetworkChoice.FindString(p2p_channel_asset_default)
        if _dc != wx.NOT_FOUND:
            self._Panel.m_NetworkChoice.SetSelection(_dc)
        '''
        #self._Panel.m_pluginCheckListbox.InsertItems(_toArray, 0) 
        
        #iList=[]
        #for disable in _currentDisableValue:
        #    i = self._Panel.m_pluginCheckListbox.FindString(disable)
        #    if i != -1:
        #        iList.append(i)
        
        #print(iList)
        #self._Panel.m_pluginCheckListbox.SetCheckedItems(iList)
        
        #self._Panel.booleansetting.SetValue(_currentValue)
        self.Layout()
        print("LoadPanelSettings")
        
        
    #
    #
    # method called when closing in case of thread or anything
    #     
    def safeClose(self):
        pass    
        
