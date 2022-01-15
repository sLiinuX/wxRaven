'''
Created on 11 déc. 2021

@author: slinux
'''

import requests

class RVNpyRPC_Wallet():
    '''
    classdocs
    '''
    RPCconnexion = None
    
    def __init__(self,connexion, parent):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.RPCconnexion = connexion
        self.RVNpyRPC = parent
    
    """
    
    End user and sys, return direct usable datas most of the time
    
    """
    
    
    def info(self):
        pass
    
    
    def __repr__(self): 
        return ""
    
    def __str__(self): 
        return  ""
    
    
    def __requires_unlock__(self):
        #returns None if no password set
        phrase_test = self.RPCconnexion.help("walletpassphrase")['result']
        return phrase_test and phrase_test.startswith("walletpassphrase")
    
    def __check_unlock__(self, _passphrase , timeout = 10):
        if self.requires_unlock():
            self.RPCconnexion.walletpassphrase(passphrase=_passphrase, timeout=timeout)
    
    
    def __UnlockAll__(self):
        allTx = self.RPCconnexion.listlockunspent()['result']
        
        if allTx != None:
            return self.RPCconnexion.lockunspent(False, allTx)
                
    
    def RVN_balance_friendly(self,balance):
        uRVNTORVN = 100000000
        balanceValue = float(balance)/uRVNTORVN
        balanceValue = balanceValue.__round__(4)
        return balanceValue    
    
    
    
    def getAllWalletAddresses(self, includeUnspent=False):
        _allAccountsDatas = self.getAllAccounts(displayAddress=True)
            
        allAddresses = []
        for ac in _allAccountsDatas:
            dataAc = _allAccountsDatas[ac]
            if dataAc['address'] != []:
                allAddresses = allAddresses+dataAc['address']
                
                if includeUnspent:
                    for _checkAd in dataAc['address']:
                        _changes = self.parentFrame.getRvnRPC().wallet.checkaddresseUnspent(_checkAd)
                        if _changes != []:
                            allAddresses = allAddresses+_changes
                            
                            
        allAddressesClean = []
        for a in allAddresses:
            if not allAddressesClean.__contains__(str(a)):
                allAddressesClean.append(str(a))
        allAddresses =  allAddressesClean   
        
        return allAddresses
          
    
    
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
        
        
        #print(allAccountsClean)
        
        
        
        return allAccountsClean
    
    
    
    def getAllAccountAssets(self):
        return self.getAllAccounts(displayAddress=True, displayAssets=True)
    
    
    
    
    def getAddressAssetsBalance(self, walletAdress=[]):
        
        #print(f"getAddressAssetsBalance {walletAdress}")
        
        allAssetsInAddress = self.getaddressbalance(walletAdress=walletAdress, showAsset=True)['result']
        
        #print(allAssetsInAddress)
        
        
        tableAssetData= []
        
        for asset in allAssetsInAddress:
            an = asset['assetName']
            ab=  str(  asset['balance'] )
            #if asset['balance'] > 100000000:
            #ab=   str(  self.RVN_balance_friendly(asset['balance']) )
            
            
            
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
        
        
        
        
        #print(f" Wallet addres input ({str(type(walletAdress))})= {walletAdress}")
        
        #print(self.RPCconnexion)
        
        searchAdressListJSON = {"addresses":[]}
        searchAdressList = []
        
        #dPrint("getaddressbalance " + walletAdress)

        if walletAdress=="*" or walletAdress == None:
            searchAdressList.append('*')
        
        if str(type(walletAdress)) == "<class 'str'>":
            if walletAdress.__contains__(","):
                print(f"CHECK STRING {walletAdress}")
                #for i in walletAdress.split(","): 
                    #print(i) 
                    #searchAdressList.append(i)  
            else:
                searchAdressList.append(walletAdress) 
        else:
                searchAdressList = walletAdress
        searchAdressListJSON["addresses"] = searchAdressList    
        #print(searchAdressListJSON)
        #response = self.__runRPCmethod__("getaddressbalance", [searchAdressListJSON ,showAsset])
        response = self.RPCconnexion.getaddressbalance(searchAdressListJSON ,showAsset)
        return response    
    
    
    
    
    
    
    
    
    
    def checkaddresseUnspent(self, walletAdress, specificAsset="RVN"):
        searchAdressListJSON = {"addresses":[walletAdress],"assetName":specificAsset}
        response = self.RPCconnexion.getaddressdeltas(searchAdressListJSON)['result']
        
        #print("checkaddresseUnspent :" + str(walletAdress))
        
        _matchs = []
        
        for _transactions in response:
            if _transactions['satoshis'] < 0:
                
                _txid = _transactions['txid']
                #print("Scan TX with negative value")
                #_transactionDetails = self.RPCconnexion.gettransaction(_txid)['result']
                
                _count = 1
                _lastTx  = self.RPCconnexion.gettxout(_txid,0)
                
                #print(_lastTx)
                while _lastTx != None:
                    
                    #print(f"Scan TX {_count} with negative value")
                    
                    if _lastTx.__contains__("result"):
                        if _lastTx['result'] != None:
                            try:
                                _lastTxData = _lastTx['result']['scriptPubKey']['addresses']
                                
                                for ad in _lastTxData:
                                    if _count > 1:
                                        
                                        if not _matchs.__contains__(ad):
                                            _matchs.append(ad)
                                        #print(f"add {ad} ")
                                    
                                    
                            except Exception as e:
                                pass
                                #print(f"error in transaction {_count} scan {e}")
                        else:
                            break        
                    
                    _count = _count+1 
                    _lastTx  = self.RPCconnexion.gettxout(_txid,_count)
                    #print(_lastTx)
                            
                            
                            
                #_matchs = _lastTx
                
                
                    
        return  _matchs          
                    
                    
                    
                    