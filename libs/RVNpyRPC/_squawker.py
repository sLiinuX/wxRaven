'''
Created on 18 déc. 2021

@author: slinux
'''
import requests



#from .squawker import squawker_as_lib

class RVNpyRPC_Squawker():
    '''
    classdocs
    '''
    RPCconnexion = None
    AssetName = ""
    
    SquawkerLib = None
    
    
    def __init__(self,connexion, assetName="POLITICOIN"):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.RPCconnexion = connexion
        self.AssetName = assetName
        
        #self.SquawkerLib = squawker_as_lib.SquawkerLib(self.AssetName, self.RPCconnexion, None)
    
    
    
    """
    def setAsset(self, assetName):
        self.AssetName = assetName
        self.SquawkerLib = squawker_as_lib.SquawkerLib(self.AssetName, self.RPCconnexion, None)
        
    """
    
    
    
    #
    #
    # Temporary Rewrite / Copypaste
    #
    
    def find_latest_messages(self, asset="", count=50):
        
        
        if asset == "":
            asset=self.AssetName
            
        rvn = self.RPCconnexion
        
        latest = []
        messages = dict()
        messages["addresses"] = list(rvn.listaddressesbyasset(asset, False)["result"])
        messages["assetName"] = asset
        deltas = rvn.getaddressdeltas(messages)["result"]
        for tx in deltas:
            if tx["satoshis"] == 100000000 and self.tx_to_self(tx):
                transaction = rvn.decoderawtransaction(rvn.getrawtransaction(tx["txid"])["result"])["result"]
                for vout in transaction["vout"]:
                    vout = vout["scriptPubKey"]
                    if vout["type"] == "transfer_asset" and vout["asset"]["name"] == asset and vout["asset"]["amount"] == 1.0:
                        kaw = {"address": vout["addresses"], "message": vout["asset"]["message"], "block": transaction["locktime"]}
                        latest.append(kaw)
        return sorted(latest[:count], key=lambda message: message["block"], reverse=True)
    
    
    def tx_to_self(self, tx, size=1):
        
        rvn = self.RPCconnexion
        
        messages = dict()
        messages["addresses"] = [tx["address"]]
        messages["assetName"] = tx["assetName"]
        deltas = rvn.getaddressdeltas(messages)["result"]
        neg_delta = [(a["satoshis"], a["address"]) for a in deltas if a["txid"] == tx["txid"] and a["satoshis"] < -((size * 100000000)-1)]
        return len(neg_delta)
    
    