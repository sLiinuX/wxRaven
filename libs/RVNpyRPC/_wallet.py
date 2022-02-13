'''
Created on 11 déc. 2021

@author: slinux
'''
import logging
import requests
import time

#import datetime
from datetime import date, datetime

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
        self.logger = logging.getLogger('wxRaven')
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
    
    
    def GetWalletTransactionList(self, categorie='', filter_addresses=[], start_date=None, stop_date=None):
        _maxTxWallet = self.RPCconnexion.getwalletinfo()['result']['txcount']
    
        self.logger.info(f" wallet tx count : {_maxTxWallet}")
        _allTransactions = self.RPCconnexion.listtransactions('*', _maxTxWallet, 0)['result']
        
        _startDateInt=0
        _stopDateInt=time.time()
        
        
        #self.logger.info(f" y {start_date.year} m {start_date.month} d {start_date.day}")
        
        if start_date != None:
            #_startDateInt = start_date.timestamp()
            self.logger.info(f" y {start_date.year} m {start_date.month} d {start_date.day}")
            
            dt = datetime(
                    year=start_date.year,
                    month=start_date.month+1,
                    day=start_date.day
                 )
            #timestamp = int(dt.timestamp())
            _startDateInt= int(dt.timestamp())
            
        if stop_date != None:
            self.logger.info(f" y {stop_date.year} m {stop_date.month} d {stop_date.day}")
            
            dt = datetime(
                    year=stop_date.year,
                    month=stop_date.month+1,
                    day=stop_date.day
                 )
            _stopDateInt = int(dt.timestamp())
            
        
        
        _transactions_list = {}
        _transactions_count= 0
            
        for _tx in _allTransactions:
            
            #self.logger.info(f'TX = {_tx}')
            if categorie != '':
                if not _tx['category']  ==   categorie:
                    continue
                
            if len(filter_addresses) > 0:
                if not filter_addresses.__contains__(_tx['address']):
                    continue
            
            
            #self.logger.info(f'TXb = {_tx["blocktime"]}')
            if  _tx['blocktime'] < _startDateInt:
                continue
            
            
            if _tx['blocktime'] > _stopDateInt:
                continue
                #break ?
            
            
            _tx['datetime'] = datetime.fromtimestamp(_tx['blocktime']).strftime('%Y-%m-%d %H:%M:%S')
            
            _transactions_list[_transactions_count] = _tx
            _transactions_count = _transactions_count + 1
        
        
        return _transactions_list
        #INT TO DATE
        #ts = datetime.datetime.fromtimestamp(blockDateTime).strftime('%Y-%m-%d %H:%M:%S')
        #
        #DATE TO INT
        #datetimeobj.timestamp()
        #
    
    def GetBalance(self):
        return self.RPCconnexion.getbalance()['result'] 
    
    
    
    #def getAllNamedAccountAddresses(self):
    #    return self.getAllWalletAddresses(includeUnspent=False, includeEmptyName=False)
    
    
    def getAllWalletAddresses(self, includeUnspent=False, includeEmptyName=False):
        _allAccountsDatas = self.getAllAccounts(displayAddress=True, includeEmptyName=includeEmptyName)
            
        allAddresses = []
        for ac in _allAccountsDatas:
            dataAc = _allAccountsDatas[ac]
            if dataAc['address'] != []:
                allAddresses = allAddresses+dataAc['address']
                
                if includeUnspent:
                    for _checkAd in dataAc['address']:
                        _changes = self.checkaddresseUnspent(_checkAd)
                        if _changes != []:
                            allAddresses = allAddresses+_changes
                            
                            
        allAddressesClean = []
        for a in allAddresses:
            if not allAddressesClean.__contains__(str(a)):
                allAddressesClean.append(str(a))
        allAddresses =  allAddressesClean   
        
        return allAddresses
          
    
    
    def getAllAccounts(self,displayAddress=False, displayAssets=False, includeEmptyName=False):
        r = self.RPCconnexion.listaccounts()
        
        
        allAccounts = r["result"]
        allAccountsClean = {}
        
        
        if displayAssets:
            displayAddress = True
        
        
        
        
        for ac in allAccounts: 
            acBalance = allAccounts[ac]
            
            if not includeEmptyName and ac =='':
                continue
            
            
            cleanRow = {}
            
            
            adAccount = "?"
            
            if displayAddress:
                ra = self.RPCconnexion.getaddressesbyaccount(ac)
                adAccount = ra["result"]
            
            
            cleanRowBalance = {}
            
            if displayAssets:
                rba = self.getaddressbalance(adAccount)
                cleanRowBalance = rba["result"]
                #self.logger.info(cleanRowBalance)
            else:
                cleanRowBalance = [{'assetName': 'RVN', 'balance': acBalance, 'received': -1}]
        
        
        
            cleanRow = {'name':ac, 'address':adAccount, 'balance':cleanRowBalance}
            
        
            allAccountsClean[ac] = cleanRow
        
        
        #self.logger.info(allAccountsClean)
        
        
        
        return allAccountsClean
    
    
    
    
    def getAllAccountAssets(self):
        return self.getAllAccounts(displayAddress=True, displayAssets=True, includeEmptyName=True)
    
    
    
    
    def getAddressAssetsBalance(self, walletAdress=[]):
        
        #self.logger.info(f"getAddressAssetsBalance {walletAdress}")
        
        allAssetsInAddress = self.getaddressbalance(walletAdress=walletAdress, showAsset=True)['result']
        
        #self.logger.info(allAssetsInAddress)
        
        
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
        
        self.logger.info("adrress="+str(adrress))
        
        return response['result']
    
    
    
    
    
    
    
    #
    #
    #
    #
    #
    #   TX part
    #
    #
    #
    
    
    
    
    
    def sendRVN(self,  toAd, amount, fromAd="", pwd=""):
        
        
        sent=False
        validDest = self.validateaddress(toAd)
        
        self.logger.info("Valide="+str(validDest))
        
        if validDest['isvalid']:
            
            
            if pwd !="":
                response = self.RPCconnexion.walletpassphrase(pwd)
            
            
            
            if fromAd != "":
                
                response = self.RPCconnexion.sendfromaddress(fromAd,toAd , amount)
                #sendfromaddress "from_address" "to_address" amount
                sent=response['result']
                self.logger.info("sendfromaddress="+str(response))
            else:
                
                response = self.RPCconnexion.sendtoaddress(toAd , amount)
                sent=response['result']
                
                self.logger.info("sendto="+str(response))
            
            
            if  sent == None:
                sent=response['error']['message']
                  
    
    
        return sent
    
    
    
    
    
    
    
    
    def sendAsset(self, AssetName, toAd, amount, pwd=""):
        
        sent=False
        validDest = self.validateaddress(toAd)
        
        self.logger.info("Valide="+str(validDest))
        
        if validDest['isvalid']:
               
            if pwd !="":
                response = self.RPCconnexion.walletpassphrase(pwd)

            response = self.RPCconnexion.transfer(AssetName, amount, toAd,"QmRL252afAwiaGwGgs7g3iYZJJFius66gVSbSd5UV1N1aK", 200000000)
                #response = self.RPCconnexion.sendfromaddress(fromAd,toAd , amount)
                #sendfromaddress "from_address" "to_address" amount
            sent=response['result']
            self.logger.info("sendfromaddress="+str(response))
            
            if  sent == None:
                sent=response['error']['message']

        return sent
    
    
    
    
    
    
    
    
    def LockUTXO(self, txoutArray, lock=True):
        self.logger.info(f"Locking UTXO [{lock}] = {txoutArray}")
        _unlock = not lock
        _res = self.RPCconnexion.lockunspent(_unlock,txoutArray)['result']
        self.logger.info(f"Locking Result : [{_res}] ")
        return _res
    
    
    def UnlockUTXO(self,txoutArray ):
        return self.LockUTXO(txoutArray, False)
    
    
    def GetLockedUnspentList(self, _ExlcudeAddresses=[],_IncludeOnlyAddresses=[], _fullDatas=True):
        _res =[]
        #print(f'GetLockedUnspentList >{_IncludeOnlyAddresses}')
        _allmatch= self.RPCconnexion.listlockunspent()['result']
        #print(f'GetLockedUnspentList > {_allmatch}')
        for _i in _allmatch:
            
            
            #print(f'GetLockedUnspentList > {_i}')
            if _fullDatas:
                
                #print(f'FM > {_i}')
                
                try:
                    #print(f'gettxout > {_i["txid"]} {}')
                    _txDetails = self.RPCconnexion.gettxout(_i['txid'], _i['vout'])['result']
                    #print(f"txout = {_txDetails}")
                    if _txDetails != None:
                        _txDetails['txid'] = _i['txid']
                        _txDetails['vout'] = _i['vout']
                        _txDetails['locked'] = True
                        _txDetails['amount'] =  _txDetails['value']
                        _txDetails['utxo_type'] = 'rvn'
                        try:
                            _txDetails['address'] =  _txDetails['scriptPubKey']['addresses'][0]
                        except Exception as e:
                            _txDetails['address'] = '?'
                       
                       
                            
                        if   _txDetails['value'] == 0.0:  
                            #ASSET SO WE SKIP IN THIS FUNCTION
                            continue
                            '''
                            try:
                                _txDetails['amount'] =  _txDetails['scriptPubKey']['asset']['amount']
                                _txDetails['account'] =  _txDetails['scriptPubKey']['asset']['name']
                                _txDetails['utxo_type'] = 'asset'
                            except Exception as e:
                                _txDetails['account'] = ''
                        
                            '''
                        
                        _exclude=False
                        
                        if len(_ExlcudeAddresses)>0:
                            for excl in _ExlcudeAddresses:
                                if _txDetails['address'].__contains__(excl):
                                    _exclude = True
                                    #print('GetLockedUnspentList > exclide')
                                    break
                        
                        _matchAd = True
                        if len(_IncludeOnlyAddresses) > 0:
                            _matchAd = False
                            for incl in _IncludeOnlyAddresses:
                                if _txDetails['address'].__contains__(incl):
                                    _matchAd = True
                                    #print('GetLockedUnspentList > exclide')
                                    break
                            
                        if not _exclude and _matchAd:
                            _res.append(_txDetails)
                    
                    
                except Exception as e:
                    self.logger.error(f"Unable to gettxout  Transaction : {e}")
            
            
            else:
                _i['locked'] = True
                _i['utxo_type'] = '?'
                _res.append(_i)
                #gettxout 
            '''
            if _i['spendable'] == False and _OnlySpendable:
                continue
            
            
            if _ExlcudeAddresses.__contains__(_i['address']) :
                continue
            
            if len(_IncludeOnlyAddresses) > 0:
                if not _IncludeOnlyAddresses.__contains__(_i['address']) :
                    continue
            
            if not _fullDatas:
                _res.append({'txid':_i['txid'], 'vout':_i['vout'],'amount':_i['amount'],})
            else:
                _res.append(_i)
    
            '''
                
        #print(_res)
        return _res
    
    #Get all Unspent and NON locked
    def GetUnspentList(self, _OnlySpendable=True, _ExlcudeAddresses=[],_IncludeOnlyAddresses=[], _fullDatas=False , _includeLocked=False):
        
        _res =[]
        
        _allmatch= self.RPCconnexion.listunspent()['result']
        
        for _i in _allmatch:
            if _i['spendable'] == False and _OnlySpendable:
                continue
            
            
            if _ExlcudeAddresses.__contains__(_i['address']) :
                continue
            
            if len(_IncludeOnlyAddresses) > 0:
                if not _IncludeOnlyAddresses.__contains__(_i['address']) :
                    continue
            
            if not _fullDatas:
                _res.append({'txid':_i['txid'], 'vout':_i['vout'],'amount':_i['amount'],'utxo_type':'rvn' , 'locked':False})
            else:
                _i['locked'] = False
                _i['utxo_type'] = 'rvn'
                _res.append(_i)
        
        
        if _includeLocked :
            _addRes=self.GetLockedUnspentList(_ExlcudeAddresses, _IncludeOnlyAddresses, _fullDatas)
            
            if _addRes != None:
                _res = _res + _addRes
        
        #print("_allmatch")
        #print(_allmatch)
        #_res = _allmatch[assetname]
        
            #print(f"OK {_res}")
            #print(f"A {_allmatch[assetname]}")
        return _res
        #listunspent 
    
    def GetRavenUnspentTx(self, _amount,_takeBiggest=True, _OneTx=False, _OnlySpendable=True, _ExlcudeAddresses=[],_IncludeOnlyAddresses=[]):
        _list =self.GetUnspentList(_OnlySpendable,_ExlcudeAddresses,_IncludeOnlyAddresses  )
    
        
        _feasible = True
        _txId = []
        _filled = False
        
        delta=0
        _max=0
        _feasible = True
        for _i in _list:
            _max = _max + float(_i['amount'])
        
        
        
        if _max< _amount:
            _feasible = False
            #print(' UNFFEASIBLE')
        else:
            pass
            #print(' FEASIBLE')
        
        if _feasible:
        
            _max=0.0
            _maxId = ''
            _maxVout = 1
            
            for _i in _list:
                #print(_i['amount'])
                if _i['amount'] > _max:
                    _max = _i['amount']
                    _maxId = _i['txid']
                    _maxVout = _i['vout']
            
            #self.logger.info(f'_max {_max}')        
        
            if _OneTx and _max <_amount:
                _feasible = False
                #print(' UNFFEASIBLE 2 ')
            
            
            if _feasible:
                #_txId.append(_maxId)
                _txId.append({'txid':_maxId, 'vout':_maxVout})
                delta = _amount-_max
                _filled=False
                
                #print(f"delta {delta}")
            
            if _max >= _amount:
                _filled = True
        

            
            if not _OneTx and _feasible and not _filled:
                
                
                #print(f"DElta = {delta}")
                while delta > 0:
                    for _i in _list['outpoints']:
                        if _i['txid'] != _maxId:
                            _add = _i['amount']
                            _txId.append({'txid':_i['txid'], 'vout':_i['vout']})
                            
                            
                            #print(f"DElta - = {_add}")
                            #print(f"DElta - = {delta}")
                            delta = delta - _add
                            
                            if delta < 0:
                                break
                            
                            
        else:
            pass
            #print(' UNFFEASIBLE')                    
        
        print(_txId)
        self.logger.info(f"GetRavenUnspentTx _feasible {_feasible} , delta {delta}")
        
        return _feasible,_txId, delta
    

    
    
    def TestTxInMempool(self,hexArray):
        _allowed= False
        try:
            self.logger.info(f"TestTxInMempool {hexArray} ")
            res = self.RPCconnexion.testmempoolaccept(hexArray)['result'][0]
            
            if res != None:
                self.logger.info(f"TestTxInMempool R {res} ")
                _allowed = res['result'][0]['allowed']
                
            self.logger.info(f"TestTxInMempool {_allowed} ")
            #_allowed = res['allowed']
            
            if not _allowed:
                self.logger.error(f"TestTxInMempool NOT ALLOWED : {res['reject-reason']} ")

        except Exception as e:
            self.logger.error(f"Unable to TestTxInMempool : {e}")
        return _allowed
    
    def CombineTransaction(self, txs , _fund=True, _sign=True, _execute=True):
        _combined=None
        _resultOk = True
        try:
            res = self.RPCconnexion.combinerawtransaction (txs)
            
            if res['result'] != None:
                _combined = res['result']
            else:
                _combined = res['error']    
                _resultOk = False
                
                
                
                
                if _fund and _resultOk:
                    res = self.RPCconnexion.fundrawtransaction (_combined)
                    if res['result'] != None:
                        _combined = res['result']['hex']
                    else:
                        _combined = res['error']    
                        _resultOk = False    
                
                
                if _sign and _resultOk:
                    res = self.RPCconnexion.signrawtransaction (_combined)
                    if res['result'] != None:
                        _combined = res['result']['hex']
                    else:
                        _combined = res['error']    
                        _resultOk = False  
                        
                        
                if _execute and _resultOk:
                    res = self.RPCconnexion.sendrawtransaction (_combined)
                    if res['result'] != None:
                        _combined = res['result']
                    else:
                        _combined = res['error']    
                        _resultOk = False  
                    
            
            
        except Exception as e:
            self.logger.error(f"Unable to create Transaction : {e}")
            _combined = e
            
            
        return _resultOk, _combined
    
    
    
    
    def GenerateAdress(self, count=1):
        _adGenerated= []
        self.logger.info(f"GenerateAdress : {count}")  
        
        for i in range(0,count):
            _nAddress= self.RPCconnexion.getnewaddress()['result']
            _adGenerated.append(_nAddress)
        
        self.logger.info(f"Generated Adress len : {len(_adGenerated)}")  
        return _adGenerated
        
    
    def CreateTransaction(self, _input, _outputs, _changeAddress='',_fund=True, _sign=True):
        return self.DoTransaction( _input, _outputs, _changeAddress='',_fund=_fund, _sign=_sign, _execute=False)
    
    
    def DoTransaction(self, _input, _outputs, _changeAddress='', _fund=True, _sign=True, _execute=True):
        
        self.logger.info(f"DoTransaction :_sign={_sign}  _execute={_execute}")  
        self.logger.info(f"_input : {_input}")  
        self.logger.info(f"_outputs : {_outputs}")  
        
        _isResultOk = True
        txResult = None
        txError = None
        
        if True:    
            
            try:
                
                
                #res = self.RPCconnexion.createrawtransaction(_input,_outputs)
                
                self.logger.info(f" > createrawtransaction")  
                res= self.RVNpyRPC.do_rpc("createrawtransaction", inputs=_input,outputs= _outputs)
                self.logger.info(f" > createrawtransaction result : {res}")  
                txResult=res
                
                #if res['error'] != None:
                #    txError = res['error']
                
                
                
                if res!= None and _fund:
                    
                    
                    if _changeAddress == '':
                        _changeAddress= self.RPCconnexion.getrawchangeaddress()['result']
                    
                    
                    
                    try:
                        
                        self.TestTxInMempool([res])
                        
                        
                        self.logger.info(f"> fundrawtransaction")  
                        res= self.RVNpyRPC.do_rpc("fundrawtransaction",hexstring=res, options={"changeAddress"  :_changeAddress,"changePosition" :0})
                        self.logger.info(f" > fundrawtransaction result : {res}")   
                        if res.__contains__('error'):
                            if res['error'] != None:
                                txError = res['error']
                                return False,txError
                                 
                        txResult=res['hex']
                        res = res['hex']
                        
                        
                        
                    except Exception as e:
                        self.logger.error(f"Unable to fund transaction: {e}")  
                        res=None
                
                
                
                
                    
                if res!= None and _sign:
                    
                    try:
                        self.logger.info(f"> signrawtransaction") 
                        self.TestTxInMempool([res])
                        
                        res = self.RPCconnexion.signrawtransaction(res) 
                        self.logger.info(f" > signrawtransaction result : {res}")
                        
                        if res.__contains__('error'):
                            if res['error'] != None:
                                txError = res['error']
                                return False,txError
                            
                        txResult=res['result'] 
                        res = res['result']['hex']
                    
                    except Exception as e:
                        self.logger.error(f"Unable to sign transaction: {e}") 
                
                
  
                if res!= None and _execute:
                    
                    try:
                        self.logger.info(f"> sendrawtransaction") 
                        res = self.RPCconnexion.sendrawtransaction(res) 
                        self.logger.info(f" > sendrawtransaction result : {res}")
                        txResult=res['result']
                        
                        if res['error'] != None:
                            txError = res['error']
                            return False,txError
                        
                        
                    except Exception as e:
                        self.logger.error(f"Unable to send transaction: {e}")
                        
                
 
                
                
            except Exception as e:
                self.logger.error(f"Unable to create Transaction : {e}")    
                _isResultOk = False
                txResult = e
    
        
        if txError != None:
            self.logger.error(f"Unable to create , and send Transaction")
            txResult = txError 
            _isResultOk = False
            
    
        return _isResultOk, txResult
    
    
    
    
    
    
    def sendRVN_Many(self, amounts={}, pwd='', _changeAddress='', _takeBiggest=True, _OneTx=False, _OnlySpendable=True, _ExlcudeAddresses=[],_IncludeOnlyAddresses=[], _fund=True, _sign=True, _execute=True):
    
    
        print("sendRVN_Many")
        sent=False
        
        totalRvn=0.0
        for ad in amounts:
            qt = amounts[ad]
            totalRvn = totalRvn + float(qt)
             
            
        print("sendRVN_Many ="+str(amounts))
        print("totalRvn ="+str(totalRvn))
        
        
        _input = []
        _outputs = {}
           
            
        if pwd !="":
            response = self.RPCconnexion.walletpassphrase(pwd)
            
        
        
        _done = False
        _feasible, _ids, _delta = self.RVNpyRPC.wallet.GetRavenUnspentTx(totalRvn,_takeBiggest, _OneTx, _OnlySpendable, _ExlcudeAddresses,_IncludeOnlyAddresses)
        
        print(f"_feasible {_feasible}")
        print(f"_ids {_ids}")
        print(f"_delta {_delta.__abs__()}")
        
        if _feasible:
            _input = []
            _input =  _ids
            
            
            _outputs[_changeAddress]= float( _delta.__abs__()).__round__(8)
            for ad in amounts:
                _outputs[ad] = float(amounts[ad]).__round__(8) 
                
            return self.DoTransaction(_input, _outputs, _changeAddress, _fund, _sign, _execute)
            
    
        return sent, 'RVN TX not feasible'
    
    
    def sendSameRVN_Many(self, amount, adresses=[], pwd='', _changeAddress='', _fund=True, _sign=True, _execute=True):
        
        _amounts = {}
        for ad in adresses:
            _amounts[ad] = amount
            
        return self.sendRVN_Many(_amounts, pwd, _changeAddress, _fund, _sign, _execute)
    
    
    
    def sendAsset_Many(self, assetname, amounts={}, pwd='', _changeAddress='', _fund=True, _sign=True, _execute=True):
        totalRaven = 0.5
        print("sendAsset_Many ="+str(amounts))
        _feasible, _rvnids, _delta = self.RVNpyRPC.wallet.GetRavenUnspentTx(totalRaven,_takeBiggest=False, _OneTx=True, _OnlySpendable=True, _ExlcudeAddresses=[],_IncludeOnlyAddresses=[])
        
    
        print(f'_feasible RVN {_feasible} - {_rvnids} ')
        print(f'Detlat RVN {_delta} ')

        totalQt=0.0
        for ad in amounts:
            qt = amounts[ad]
            totalQt = totalQt + float(qt)
        
        
        _done = False
        _feasible, _ids, delta = self.RVNpyRPC.asset.GetAssetUnspentTx(assetname,totalQt )
        if _feasible:
            _input = _ids
            _outputs = {}
            _outputs[_changeAddress] =  float(0.0002).__round__(8)
            if delta >0:
                _outputs[_changeAddress] = {"transfer": {f"{assetname}": float(delta).__round__(8)  }}
            
            for ad in amounts:
                _outputs[ad] = {"transfer": {f"{assetname}": float(amounts[ad]).__round__(8)  }}
                
            return self.DoTransaction(_input, _outputs,_changeAddress, _fund, _sign, _execute)
        
        return False, "Asset TX not feasible"
    
    def sendSameAsset_Many(self, assetname, amount, adresses=[], pwd='', _changeAddress='', _fund=True, _sign=True, _execute=True):
        
        _amounts = {}
        for ad in adresses:
            _amounts[ad] = amount
            
        return self.sendAsset_Many(assetname, _amounts, pwd, _changeAddress, _fund, _sign, _execute)
    
    
    
    
    
    
    def TEST_SendMultiRaven(self):
        _res = self.sendSameRVN_Many(10.00, ['moKtQws16N6jZRhzHpW1VuP8bJZUqPaKwp','n4e3opUm6sRsbwmkQrHBy82U73o19Dq4hL'], '', 'munRj4MDDka4nv9FnxUrSq6KF55DPpdCCi')
        self.logger.info(f"TEST_SendMultiRaven result : {_res}")
        return _res
    
    
    def TEST_SendMultiAssets(self):
        _res = self.sendSameAsset_Many("WXRAVEN/P2P_MARKETPLACE/TEST", 10.00,  ['moKtQws16N6jZRhzHpW1VuP8bJZUqPaKwp','n4e3opUm6sRsbwmkQrHBy82U73o19Dq4hL'], '', 'munRj4MDDka4nv9FnxUrSq6KF55DPpdCCi')
        self.logger.info(f"TEST_SendMultiRaven result : {_res}")
        return _res
    
    
    
    #
    # Do not use
    #
    def TEST_SendMultiAssetsCombine(self):
        _resOne = self.sendSameAsset_Many("WXRAVEN/P2P_MARKETPLACE/TEST", 10.00,  ['moKtQws16N6jZRhzHpW1VuP8bJZUqPaKwp','n4e3opUm6sRsbwmkQrHBy82U73o19Dq4hL', 'mvdHRpBif1hAFiNX8fbeQFLEWwjiNbXyn6', 'mvhFhxfUmYTHY3hVL1wZzh4sJTQJoMRFWo'], '', 'munRj4MDDka4nv9FnxUrSq6KF55DPpdCCi', _fund=False, _sign=True, _execute=False)
        _resTwo = self.sendSameAsset_Many("WXRAVEN/P2P_MARKETPLACE/TEST", 10.00,  ['moKtQws16N6jZRhzHpW1VuP8bJZUqPaKwp','n4e3opUm6sRsbwmkQrHBy82U73o19Dq4hL', 'mvdHRpBif1hAFiNX8fbeQFLEWwjiNbXyn6', 'mvhFhxfUmYTHY3hVL1wZzh4sJTQJoMRFWo'], '', 'munRj4MDDka4nv9FnxUrSq6KF55DPpdCCi', _fund=False, _sign=True, _execute=False)
        
        self.logger.info(f"R1 : {_resOne}")
        self.logger.info(f"R2 : {_resTwo}")
        _res=None
        if _resOne != None and _resTwo != None:
            _res= self.CombineTransaction([_resOne['hex'], _resTwo['hex']],_fund=True, _sign=True, _execute=True)
            
        self.logger.info(f"TEST_SendMultiRaven result : {_res}")
        return _res
    #
    #
    #
    #
    #
    #   offline and various
    #
    #
    #
    
    
    """
    
    RPC Low level, will return json raw data most of the time
    
    """
    def getBalanceOffline(self, walletAddress):
        baseURL = "https://ravencoin.network/api/addr/"
        
        url = baseURL + walletAddress
        
        try:
                resp = requests.get(url=url)
        except:
                self.logger.error("ERROR : getBalanceOffline() - Unable to parse endpoint")
                
        jsonData = resp.json()
        
        rvnBalance = jsonData['balance']
        return rvnBalance
    
    
    
    
    
    def getaddressbalance(self,walletAdress="*", showAsset=True):
        
        
        
        
        #self.logger.info(f" Wallet addres input ({str(type(walletAdress))})= {walletAdress}")
        
        #self.logger.info(self.RPCconnexion)
        
        searchAdressListJSON = {"addresses":[]}
        searchAdressList = []
        
        #dself.logger.info("getaddressbalance " + walletAdress)

        if walletAdress=="*" or walletAdress == None:
            searchAdressList.append('*')
        
        if str(type(walletAdress)) == "<class 'str'>":
            if walletAdress.__contains__(","):
                self.logger.info(f"CHECK STRING {walletAdress}")
                #for i in walletAdress.split(","): 
                    #self.logger.info(i) 
                    #searchAdressList.append(i)  
            else:
                searchAdressList.append(walletAdress) 
        else:
                searchAdressList = walletAdress
        searchAdressListJSON["addresses"] = searchAdressList    
        #self.logger.info(searchAdressListJSON)
        #response = self.__runRPCmethod__("getaddressbalance", [searchAdressListJSON ,showAsset])
        response = self.RPCconnexion.getaddressbalance(searchAdressListJSON ,showAsset)
        return response    
    
    
    
    
    
    
    
    
    
    def checkaddresseUnspent(self, walletAdress, specificAsset="RVN"):
        searchAdressListJSON = {"addresses":[walletAdress],"assetName":specificAsset}
        response = self.RPCconnexion.getaddressdeltas(searchAdressListJSON)['result']
        
        #self.logger.info("checkaddresseUnspent :" + str(walletAdress))
        
        _matchs = []
        
        for _transactions in response:
            if _transactions['satoshis'] < 0:
                
                _txid = _transactions['txid']
                #self.logger.info("Scan TX with negative value")
                #_transactionDetails = self.RPCconnexion.gettransaction(_txid)['result']
                
                _count = 1
                _lastTx  = self.RPCconnexion.gettxout(_txid,0)
                
                #self.logger.info(_lastTx)
                while _lastTx != None:
                    
                    #self.logger.info(f"Scan TX {_count} with negative value")
                    
                    if _lastTx.__contains__("result"):
                        if _lastTx['result'] != None:
                            try:
                                _lastTxData = _lastTx['result']['scriptPubKey']['addresses']
                                
                                for ad in _lastTxData:
                                    if _count > 1:
                                        
                                        if not _matchs.__contains__(ad):
                                            _matchs.append(ad)
                                        #self.logger.info(f"add {ad} ")
                                    
                                    
                            except Exception as e:
                                pass
                                #self.logger.info(f"error in transaction {_count} scan {e}")
                        else:
                            break        
                    
                    _count = _count+1 
                    _lastTx  = self.RPCconnexion.gettxout(_txid,_count)
                    #self.logger.info(_lastTx)
                            
                            
                            
                #_matchs = _lastTx
                
                
                    
        return  _matchs          
                    
                    
                    
                    