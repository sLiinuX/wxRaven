'''
Created on 17 déc. 2021

@author: slinux
'''


from .wxRavenSquawkerDesign import *
from .wxRavenSquawkerLogic import *
from wxRavenGUI.application.pluginsframework import *

import threading


#from .sq import squawker


class wxRavenPlugin(PluginObject):
    
    
    def __init__(self, parentFrame, position="mgr"):
        PluginObject.__init__(self, parentFrame, position=position)
        
        
        self.PLUGIN_NAME = "Squawker"
        self.PLUGIN_ICON = self.RessourcesProvider.GetImage('message') #wx.Bitmap( u"res/default_style/normal/message.png", wx.BITMAP_TYPE_ANY )
        self.PLUGINS_VIEWS= [ 
                    {
                     'viewid':'SquawkerTest', 
                     'name':'SquawkerTest', 
                     'title':'SquawkerTest', 
                     'position':position, 
                     'icon':self.PLUGIN_ICON, 
                     'class': testPanel ,
                     'default':False,
                     'multipleViewAllowed':False
                     
                     }
                    
                ]
        
        
        
        

        self.ALLOW_MULTIPLE_VIEWS_INSTANCE = False
        self.parentFrame = parentFrame
        #self.parentFrame.ConnexionManager.RegisterOnConnexionChanged(self.OnNetworkChanged_T)
        
        #self.LoadPluginFrames()
        
        
        self.MESAGE_TYPES_SATOSHIS= {
            'market':20000000,
            'msg':100000000
            }
        


    def OnNetworkChanged_T(self, networkName=""):    
        
        if not self.parentFrame._isReady:
            return None 
        
        t=threading.Thread(target=self.OnNetworkChanged)
        t.start()
        
    
    
    def OnNetworkChanged(self):
        
        self.setData("_lastMessage",[])
        
        
        try:
            
        #datas = squawker.find_latest_messages("asset", count=50)
        
            datas = self.find_latest_messages("POLITICOIN", 50)
            #datas = self.find_latest_messages("WXRAVEN/P2P_MARKETPLACE/TEST", 50, 20000000)
            
            self.setData("_lastMessage",datas)
            
            
            """
            
            As tentative of squawker lib porting
            
            _allAccountsDatas = self.parentFrame.getRvnRPC().squawker.** works too
            
            """
            
            
            
            #_globalBalance = self.parentFrame.getNetwork().getbalance()['result']
            
           
            
            wx.CallAfter(self.UpdateActiveViews, ())

        except Exception as e:
            self.RaisePluginLog("Unable to retreive Squawker datas :" + str(e) , type="warning")



    """
    
    squawker functions remapped to RPC class ;(
    Need to check how to better integrate this in the future !
    
    """
    

    def tx_to_self(self, tx, size=1):
        messages = dict()
        messages["addresses"] = [tx["address"]]
        messages["assetName"] = tx["assetName"]
        deltas = self.parentFrame.getNetwork().getaddressdeltas(messages)["result"]
        neg_delta = [(a["satoshis"], a["address"]) for a in deltas if a["txid"] == tx["txid"] and a["satoshis"] < -((size * 100000000)-1)]
        return len(neg_delta)
    
    
    
    def find_latest_messages(self, asset="ASSET", count=50, msgType = 100000000):
        
        latest = []
        messages = dict()
        messages["addresses"] = list(self.parentFrame.getNetwork().listaddressesbyasset(asset, False)["result"])
        messages["assetName"] = asset
        deltas = self.parentFrame.getNetwork().getaddressdeltas(messages)["result"]
        for tx in deltas:
            if tx["satoshis"] == msgType and self.tx_to_self(tx):
                transaction = self.parentFrame.getNetwork().decoderawtransaction(self.parentFrame.getNetwork().getrawtransaction(tx["txid"])["result"])["result"]
                for vout in transaction["vout"]:
                    vout = vout["scriptPubKey"]
                    if vout["type"] == "transfer_asset" and vout["asset"]["name"] == asset and vout["asset"]["amount"] == 1.0:
                        kaw = {"address": vout["addresses"], "message": vout["asset"]["message"], "block": transaction["locktime"]}
                        latest.append(kaw)
            else:
                print(f"excluded {tx['satoshis']}")
        return sorted(latest[:count], key=lambda message: message["block"], reverse=True)
        #except Exception as e:
        #    print(self.PLUGIN_NAME + " > OnNetworkChanged " + str(e))    
        
        