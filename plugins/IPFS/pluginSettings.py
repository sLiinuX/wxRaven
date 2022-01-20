'''
Created on 15 janv. 2022

@author: slinux
'''


from wxRavenGUI.application.pluginsframework import PluginSettingsPanelObject
from .wxRavenIPFSDesign import wxRavenIPFS_SettingsPanel
import wx

from wxRavenGUI.application.wxcustom import *

class MyIPFSSettingPanel_WithLogic(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRavenIPFS_SettingsPanel(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
    
    
        
        self._Panel.m_ipfsHomepage.Bind( wx.EVT_TEXT, self.OnChanged )
        self._Panel.m_ipfsRPC.Bind( wx.EVT_TEXT, self.OnChanged )
        self._Panel.m_ipfsAPI.Bind( wx.EVT_TEXT, self.OnChanged )
        
        self._Panel.m_button3.Bind( wx.EVT_BUTTON, self.OnDoCheckIPFS )
    
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        
        
        #now its up to the dev to chose how to take this information
        #in our demo lets do simple and just change the  booleansetting in PLUGIN_SETTINGS
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
       
        homepage_url = self._Panel.m_ipfsHomepage.GetValue()
        myPlugin.PLUGIN_SETTINGS['homepage_url'] = homepage_url
        
        ipfs_rpc_api_ip = self._Panel.m_ipfsRPC.GetValue()
        myPlugin.PLUGIN_SETTINGS['ipfs_rpc_api_ip'] = ipfs_rpc_api_ip
        
        ipfs_direct_api_ip = self._Panel.m_ipfsAPI.GetValue()
        myPlugin.PLUGIN_SETTINGS['ipfs_direct_api_ip'] = ipfs_direct_api_ip
    
    
        
        ipfs_rpc_api_ip_bis = self._Panel.m_ipfsRPC2.GetValue()
        myPlugin.PLUGIN_SETTINGS['ipfs_rpc_api_ip_bis'] = ipfs_rpc_api_ip_bis
    
    
    
        print("SavePanelSettings" )
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        
        
        homepage_url = myPlugin.PLUGIN_SETTINGS['homepage_url']
        self._Panel.m_ipfsHomepage.SetValue(homepage_url)
        
        ipfs_rpc_api_ip = myPlugin.PLUGIN_SETTINGS['ipfs_rpc_api_ip']
        self._Panel.m_ipfsRPC.SetValue(ipfs_rpc_api_ip)
        
        ipfs_rpc_api_ip_bis = myPlugin.PLUGIN_SETTINGS['ipfs_rpc_api_ip_bis']
        self._Panel.m_ipfsRPC2.SetValue(ipfs_rpc_api_ip_bis)
        
        
        
        ipfs_direct_api_ip = myPlugin.PLUGIN_SETTINGS['ipfs_direct_api_ip']
        self._Panel.m_ipfsAPI.SetValue(ipfs_direct_api_ip)
        
        
        
        
        
        
        
        print("LoadPanelSettings")
        
    
    def OnDoCheckIPFS(self, evt=None):
        
        
        print("OnDoCheckIPFS")
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        
        ipfsCheck=  myPlugin.DoTestRPC()
        UserInfo(self._Panel, str(ipfsCheck))
        print("OnDoCheckIPFS")
    
        
        _oneNotNone = False
        
        for k in ipfsCheck:
            if ipfsCheck[k] != None:
                _oneNotNone = True
                
                
        if _oneNotNone :
            self._Panel.m_bitmap3111.SetBitmap(self.parentFrame.RessourcesProvider.GetImage('passed'))
        else:
            self._Panel.m_bitmap3111.SetBitmap(self.parentFrame.RessourcesProvider.GetImage('warning_2'))
        
    #
    #
    # method called when closing in case of thread or anything
    #     
    def safeClose(self):
        pass    
        
        
        