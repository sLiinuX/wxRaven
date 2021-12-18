'''
Created on 11 déc. 2021

@author: slinux
'''

import requests
from .RVNpyRPC import RavenpyRPC

class RVNpyRPC_Wallet(RavenpyRPC):
    '''
    classdocs
    '''
    RPCconnexion = None
    
    def __init__(self,connexion):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.RPCconnexion = connexion
    
    
    """
    
    End user and sys, return direct usable datas most of the time
    
    """
    
    
    def info(self):
        pass
    
    
    def __repr__(self): 
        return ""
    
    def __str__(self): 
        return  ""
    
    
    def RVN_balance_friendly(self,balance):
        uRVNTORVN = 100000000
        balanceValue = float(balance)/uRVNTORVN
        balanceValue = balanceValue.__round__(4)
        return balanceValue    
    
    
    def getAllAccounts(self,displayAddress=False, displayAssets=False):
        r = self.RPCconnexion.listaccounts()
        
        
        allAccounts = r["result"]
        allAccountsClean = {}
        
        
        if displayAssets:
            displayAddress = True
        
        
        
        
        for ac in allAccounts: 
            acBalance = allAccounts[ac]
            
            cleanRow = {}
            
            
            adAccount = "?"
            
            if displayAddress:
                ra = self.RPCconnexion.getaddressesbyaccount(ac)
                adAccount = ra["result"]
            
            
            cleanRowBalance = {}
            
            if displayAssets:
                rba = self.getaddressbalance(adAccount)
                cleanRowBalance = rba["result"]
                #print(cleanRowBalance)
            else:
                cleanRowBalance = [{'assetName': 'RVN', 'balance': acBalance, 'received': -1}]
        
        
        
            cleanRow = {'name':ac, 'address':adAccount, 'balance':cleanRowBalance}
            
        
            allAccountsClean[ac] = cleanRow
        
        
        
        
        
        
        return allAccountsClean
    
    
    
    def getAllAccountAssets(self):
        return self.getAllAccounts(displayAddress=True, displayAssets=True)
    
    
    
    
    def getAddressAssetsBalance(self, walletAdress=[]):
        allAssetsInAddress = self.getaddressbalance(walletAdress=walletAdress, showAsset=True)['result']
        
        
        tableAssetData= []
        
        for asset in allAssetsInAddress:
            an = asset['assetName']
            ab=   str(  self.RVN_balance_friendly(asset['balance']) )
            
            tableAssetData.append([an, ab])
            
            
        return tableAssetData
    
    
    def validateaddress(self, adrress: str=""):
        response = self.RPCconnexion.validateaddress(adrress)
        
        print("adrress="+str(adrress))
        
        return response['result']
    
    
    def sendRVN(self,  toAd, amount, fromAd="", pwd=""):
        
        
        
        sent=False
        validDest = self.validateaddress(toAd)
        
        print("Valide="+str(validDest))
        
        if validDest['isvalid']:
            
            
            if pwd !="":
                response = self.RPCconnexion.walletpassphrase(pwd)
            
            
            
            if fromAd != "":
                
                response = self.RPCconnexion.sendfromaddress(fromAd,toAd , amount)
                #sendfromaddress "from_address" "to_address" amount
                sent=response['result']
                print("sendfromaddress="+str(response))
            else:
                
                response = self.RPCconnexion.sendtoaddress(toAd , amount)
                sent=response['result']
                
                print("sendto="+str(response))
            
            
            if  sent == None:
                sent=response['error']['message']
                  
    
    
        return sent
    
    
    
    """
    
    RPC Low level, will return json raw data most of the time
    
    """
    def getBalanceOffline(self, walletAddress):
        baseURL = "https://ravencoin.network/api/addr/"
        
        url = baseURL + walletAddress
        
        try:
                resp = requests.get(url=url)
        except:
                print("ERROR : getBalanceOffline() - Unable to parse endpoint")
                
        jsonData = resp.json()
        
        rvnBalance = jsonData['balance']
        return rvnBalance
    
    
    
    
    
    def getaddressbalance(self,walletAdress="*", showAsset=True):
        
        
        #print(self.RPCconnexion)
        
        searchAdressListJSON = {"addresses":[]}
        searchAdressList = []
        
        #dPrint("getaddressbalance " + walletAdress)

        if walletAdress=="*" or walletAdress == None:
            searchAdressList.append('*')
        
        
        if walletAdress.__contains__(","):
            for i in walletAdress.split(","): 
                #print(i) 
                searchAdressList.append(i)   
        else:
            if str(type(walletAdress)) == "<class 'str'>":
                searchAdressList.append(walletAdress)
            else:
                searchAdressList = walletAdress
        searchAdressListJSON["addresses"] = searchAdressList    
        #print(searchAdressListJSON)
        #response = self.__runRPCmethod__("getaddressbalance", [searchAdressListJSON ,showAsset])
        response = self.RPCconnexion.getaddressbalance(searchAdressListJSON ,showAsset)
        return response    