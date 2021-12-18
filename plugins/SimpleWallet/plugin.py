
'''
Created on 10 déc. 2021

@author: slinux
'''

import threading
import datetime
from .wxRavenWalletDesign import *
from .wxRavenWalletLogic import *
from plugins.pluginObjectTemplate import *


class wxRavenPlugin(PluginObject):
    
    
    def __init__(self, parentFrame, position="mgr"):
        PluginObject.__init__(self, parentFrame, position=position)
        
        
        self.PLUGIN_NAME = "SimpleWallet"
        self.PLUGIN_ICON = wx.Bitmap( u"res/default_style/normal/wallet.png", wx.BITMAP_TYPE_ANY )
        self.PLUGINS_VIEWS= [ 
                    {
                     'viewid':'Simple Wallet', 
                     'name':'Simple Wallet', 
                     'title':'Simple Wallet', 
                     'position':position, 
                     'icon':self.PLUGIN_ICON, 
                     'class': walletMainPanel ,
                     'default':False,
                     'multipleViewAllowed':False
                     
                     }
                    
                ]

        self.ALLOW_MULTIPLE_VIEWS_INSTANCE = False
        self.parentFrame = parentFrame
        self.parentFrame.ConnexionManager.RegisterOnConnexionChanged(self.OnNetworkChanged_T)
        
        self.LoadPluginFrames()



        #For test purpose
    
    
    
    
    '''
    
    Plugin Triggers for data update , DO NOT CALL WX UPDATE OUT OUF wx.CallAfter(cb, param)
    '''
        
        
        
        
        
        
    def OnNetworkChanged_T(self, networkName=""):    
        t=threading.Thread(target=self.OnNetworkChanged)
        t.start()
        
        
    def OnNetworkChanged(self):
        
        self.setData("globalBalance", 0.0)
        self.setData("allAccountsDatas", [])
        self.setData("globalAssetBalance", [])
        self.setData("allAddresses", [])
        
        
        #self.setData("_icon", wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY ))
        #self.setData("_dataTimeStamp", '')
        
        
        
        try:
            
            
            _globalBalance = self.parentFrame.getNetwork().getbalance()['result']
            _allAccountsDatas = self.parentFrame.getRvnRPC().wallet.getAllAccounts(displayAddress=True)
            
            allAddresses = []
            
        

            for ac in _allAccountsDatas:
                dataAc = _allAccountsDatas[ac]
                if dataAc['address'] != "?":
                    allAddresses = allAddresses+dataAc['address']
                    
                    
            _globalAssetBalance = self.parentFrame.getRvnRPC().wallet.getAddressAssetsBalance(allAddresses)
            

            self.setData("globalBalance", _globalBalance)
            self.setData("allAccountsDatas", _allAccountsDatas)
            self.setData("globalAssetBalance", _globalAssetBalance)
            self.setData("allAddresses", allAddresses)
            
            
            
            
            
            wx.CallAfter(self.UpdateActiveViews, ())



        except Exception as e:
            print(self.PLUGIN_NAME + " > OnNetworkChanged " + str(e))






"""
PLUGIN_NAME = "SimpleWallet"
PLUGIN_ICON = wx.Bitmap( u"res/default_style/normal/wallet.png", wx.BITMAP_TYPE_ANY )



PLUGINS_VIEWS = [ 
                    {'name':'Simple Wallet', 
                     'icon':PLUGIN_ICON, 
                     'class': walletMainPanel 
                     }
                    
                ]


ALLOW_MULTIPLE_VIEWS_INSTANCE = False




def init(parentFrame, position = "main"):
    return walletMainPanel(parentFrame=parentFrame, position=position)

def getIcon():
    return PLUGIN_ICON

def getViews():
    return PLUGINS_VIEWS
"""