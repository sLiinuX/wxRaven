'''
Created on 8 févr. 2022

@author: slinux
'''
from wxRavenGUI.application.pluginsframework import PluginSettingsPanelObject
from .wxRavenWebServicesDesign import wxRaven_Webservices_SettingsPanel

import wx
import secrets


class wxRaven_Webservices_SettingsPanelLogic(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRaven_Webservices_SettingsPanel(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
    
        _Panel.SetBackgroundColour( wx.Colour( 217, 228, 255 ) )
        _Panel.m_bpButtonGenerateAdmin.Bind( wx.EVT_BUTTON, self.OnGenerateToken )
        
        self._settingsHasChanged =True
        
        #_Panel.Bind( wx.EVT_BUTTON, self.OnAddProvider,id = _Panel.bookmark_addbt.GetId()  )
        #_Panel.Bind( wx.EVT_BUTTON, self.OnRemoveProvider,id = _Panel.bookmark_rembt.GetId()  )
        #_Panel.Bind( wx.EVT_BUTTON, self.OnMoveProviderUp,id = _Panel.ipfs_provider_upbt.GetId()  )
        
        
        """
        _Panel.ipfs_provider_addbt.Bind( wx.EVT_BUTTON, self.OnChanged )
        #_Panel.ipfs_provider_upbt.Bind( wx.EVT_BUTTON, self.OnChanged )
        _Panel.ipfs_provider_rembt.Bind( wx.EVT_BUTTON, self.OnRemoveProvider )
        
        
        _Panel.ipfs_provider_upbt.Bind( wx.EVT_BUTTON, self.OnMoveProviderUp )
        """
    
        self._Panel.Bind( wx.EVT_TIMER, self.OnRefreshStatus, id=wx.ID_ANY )
        self._Panel.Bind( wx.EVT_BUTTON, self.OnChangeServiceStatus, id=self._Panel.m_bpButton1.GetId()  )
        self._Panel.m_forceNetwork.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        
        self._Panel.m_checkList1.Bind( wx.EVT_CHECKLISTBOX, self.OnChanged )
    
    def safeClose(self):
        self._Panel.m_timer2.Stop()
    
    
    def OnGenerateToken(self, evt):
        self._settingsHasChanged=True
        
        _newToken = secrets.token_urlsafe(16)
        self._Panel.m_textAdminToken.SetValue(_newToken)
    
    def OnChangeServiceStatus(self, evt):
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        statusTxt = myPlugin.getData("_status")
        
        
        if statusTxt == "STOPPED" :
            myPlugin._stop=False
            print('STARTBT')
            myPlugin.StartWebService()
            
        else:
            print('STOPBT')
            myPlugin.StopWebService()
    
    
    
    
    
    def OnRefreshStatus(self,evt):
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        statusTxt = myPlugin.getData("_status")
        self._Panel.m_serviceStatusText.SetLabel(statusTxt)
        
        
        stateBtIcons = {}
        stateBtIcons['STARTED'] = self.parentFrame.RessourcesProvider.GetImage('process_pause')
        stateBtIcons['RUNNING'] = self.parentFrame.RessourcesProvider.GetImage('process_stop')
        stateBtIcons['STOPPED'] = self.parentFrame.RessourcesProvider.GetImage('process_run')
        stateBtIcons['WAITING'] = self.parentFrame.RessourcesProvider.GetImage('process_run')
        stateBtIcons['ERROR'] = self.parentFrame.RessourcesProvider.GetImage('process_run')
        
        
        self._Panel.m_bpButton1.SetBitmap(stateBtIcons[statusTxt])
        
        
        if statusTxt == "RUNNING":
            self.LockSetting()
        else:
            self.LockSetting(False)
        
        self._Panel.Layout()
    
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        #_newValueForBoolSetting = self._Panel.booleansetting.IsChecked()
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
    
        allProviders = []
        
        #for i in range(0, self._Panel.bookmark_list.Count):
        #    allProviders.append(self._Panel.bookmark_list.GetString(i)) 
    
        #myPlugin.PLUGIN_SETTINGS["webservice_server_allowed_calls"] = allProviders
        
        
        
        
        myPlugin.PLUGIN_SETTINGS["webservice_server_ip"] = self._Panel.m_serverIP.GetValue()
        myPlugin.PLUGIN_SETTINGS["webservice_server_port"] = self._Panel.m_serverPort.GetValue()
        myPlugin.PLUGIN_SETTINGS["webservice_server_path"] = str(self._Panel.m_filePickerService.GetPath())
        #myPlugin.PLUGIN_SETTINGS["webservice_server_path"] = str(self._Panel.m_dirPicker1.GetPath())
        myPlugin.PLUGIN_SETTINGS["webservice_server_enable"] = self._Panel.m_enableService.GetValue()
        
        
        myPlugin.PLUGIN_SETTINGS["webservice_server_admin_token"] = self._Panel.m_textAdminToken.GetValue()
        
        
        force_network = self._Panel.m_forceNetwork.GetValue()    
        force_network_value = self._Panel.m_NetworkChoice.GetString(self._Panel.m_NetworkChoice.GetCurrentSelection())      
        print(force_network_value)
        if not force_network:
            force_network_value = ''
        print(force_network_value)    
        myPlugin.PLUGIN_SETTINGS["webservice_force_network"]  = force_network_value
            
        
        
        
        
        
        _currentDisableValueIndex = self._Panel.m_checkList1.GetCheckedStrings()
        
        
        print(_currentDisableValueIndex)
        
        
        _toSaveArray = []
        
        for _val in _currentDisableValueIndex:
            _toSaveArray.append(_val)
        
        myPlugin.PLUGIN_SETTINGS['webservice_exclude_services'] = _toSaveArray
        '''
        allProviders = []
        
        for i in range(0, self._Panel.bookmark_list.Count):
            allProviders.append(self._Panel.bookmark_list.GetString(i)) 
        
        
        #default =    allProviders[0] 
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #myPlugin.PLUGIN_SETTINGS["ipfsgateway_default"]    = default
        myPlugin.PLUGIN_SETTINGS["table_asset_list"]  = allProviders
        #print(allProviders)
        #print(default)
        '''
        
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        
        webservice_server_ip = myPlugin.PLUGIN_SETTINGS["webservice_server_ip"]
        webservice_server_port = myPlugin.PLUGIN_SETTINGS["webservice_server_port"]
        webservice_server_daemon = myPlugin.PLUGIN_SETTINGS["webservice_server_path"]
        #webservice_server_path = myPlugin.PLUGIN_SETTINGS["webservice_server_path"]
        #webservice_server_allowed_calls = myPlugin.PLUGIN_SETTINGS["webservice_server_allowed_calls"]
        webservice_server_enable = myPlugin.PLUGIN_SETTINGS["webservice_server_enable"]
         
        force_network = myPlugin.PLUGIN_SETTINGS["webservice_force_network"]
        
        
        
        admin_token = myPlugin.PLUGIN_SETTINGS["webservice_server_admin_token"]
        
        
        
        
        
        #self._Panel.bookmark_list.InsertItems(webservice_server_allowed_calls, 0)
        self._Panel.m_serverIP.SetValue(webservice_server_ip)
        self._Panel.m_serverPort.SetValue(str(webservice_server_port))
        self._Panel.m_filePickerService.SetPath(webservice_server_daemon)
        
        self._Panel.m_textAdminToken.SetValue(admin_token)
        #self._Panel.m_dirPicker1.SetPath(webservice_server_path)
        
        self._Panel.m_enableService.SetValue(webservice_server_enable)
        
        
        allNetworks = self.parentFrame.ConnexionManager.getAllConnexions()
        for net in allNetworks:
            self._Panel.m_NetworkChoice.Append(net)
            
            
            
        if force_network != '':
            self._Panel.m_forceNetwork.SetValue(True)
            self._Panel.m_NetworkChoice.Enable(True)
            
            _dc = self._Panel.m_NetworkChoice.FindString(force_network)
            if _dc != wx.NOT_FOUND:
                self._Panel.m_NetworkChoice.SetSelection(_dc)
                
        
        
        #
        # Aloowed services
        #
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        _currentDisableValue = myPlugin.PLUGIN_SETTINGS['webservice_exclude_services']
        
        _currentPluginList = myPlugin.GetServicesList()
        
        self._Panel.m_checkList1.InsertItems(_currentPluginList, 0) 
        
        iList=[]
        for disable in _currentDisableValue:
            i = self._Panel.m_checkList1.FindString(disable)
            if i != -1:
                iList.append(i)
        
        #print(iList)
        self._Panel.m_checkList1.SetCheckedItems(iList)
        
        
        
                
                
        self._Panel.Layout()
        
        """
        
        'webservice_server_ip' : '127.0.0.1',
        'webservice_server_port' : '9000',
        'webservice_server_log' : '',
        'webservice_server_allowed_calls' : ['listassets'],
        
        
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #ipfsgateway_default = myPlugin.PLUGIN_SETTINGS["ipfsgateway_default"]
        bookmark_list_s =  myPlugin.PLUGIN_SETTINGS["table_asset_list"] 
        
        #for i in ipfsgateway_providers:
        self._Panel.bookmark_list.InsertItems(bookmark_list_s, 0)
        
        #print("LoadPanelSettings")     
        
        
        self._Panel.Layout()
        """
    def LockSetting(self, lockMode=True): 
          
        _enable =   not lockMode
          
        self._Panel.m_enableService.Enable(_enable) 
        self._Panel.m_forceNetwork.Enable(_enable)
        self._Panel.m_NetworkChoice.Enable(_enable)
        self._Panel.m_serverIP.Enable(_enable) 
        self._Panel.m_serverPort.Enable(_enable) 
        
        self._Panel.m_filePickerService.Enable(_enable) 
        self._Panel.m_checkList1.Enable(_enable)
        self._Panel.m_bpButtonGenerateAdmin.Enable(_enable)
        self._Panel.m_textAdminToken.Enable(_enable)
        
        
        #self._Panel.m_dirPicker1.Enable(_enable) 
        
        
    def OnAddProvider(self, evt):    
        
        newp  = self._Panel.table_text_area.GetValue()
        self._Panel.bookmark_list.InsertItems([newp], self._Panel.bookmark_list.Count)
        self._settingsHasChanged = True
        self._Panel.Layout()
        
        
    def OnRemoveProvider(self, evt):    
        x = self._Panel.bookmark_list.GetSelection()
        self._Panel.bookmark_list.Delete(x)
        self._settingsHasChanged = True
        self._Panel.Layout()
        
    '''    
    def OnMoveProviderUp(self, evt): 
        x = self._Panel.bookmark_list.GetSelection()
        #self._Panel.ipfs_provider_list.SetFirstItem(x)
        #print(x)
        
        _itemTopromote = self._Panel.bookmark_list.GetString(x)
        self._Panel.table_list.Delete(x)
        
        self._Panel.table_list.InsertItems([_itemTopromote], 0)
        
        self._settingsHasChanged = True
        self._Panel.Layout()    
                
    '''    
        