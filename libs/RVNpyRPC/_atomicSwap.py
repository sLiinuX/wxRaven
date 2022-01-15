'''
Created on 8 janv. 2022

@author: slinux
'''
import requests
from libs.RVNpyRPC import RVNpyRPC
import json
#from jsonrpcclient.requests import Request
from requests import post, get
from decimal import *

import base64
import logging
import time
import os
from logging.handlers import TimedRotatingFileHandler

from ._atomicSwapWalletManager import AtomicSwapCacheStorage, WalletManager
from ._atomicSwapTradeAndTransactions import TransactionUtils, SwapTradeManager, SwapTransaction
from contextlib import contextmanager


class AtomicSwapManager():
    
    RPCconnexion = None
    RVNpyRPC = None
    Session = None
    
    def __init__(self,connexion, parent:RVNpyRPC , _walletPassPhrase="" ):
        self.RPCconnexion = connexion
        self.RVNpyRPC = parent 
        self.Session = None
        self._unlockAfter = False
    
    #
    # Init all the required object + log in order to do trading swap    
    #
    def NewTradeSession(self, _walletPassPhrase="", _Singleton=True, _timeStampIt=False, unlockAfter=False):    
        
        
        _existingSession = self.Session
        self._unlockAfter = unlockAfter
        
        if ( (_existingSession == None) or ( _existingSession != None and not _Singleton)  ):
            
            self.setup_logging(_timeStampIt)
            
            self.txUtils = TransactionUtils(self, _walletPassPhrase)
            self.CacheStorage = AtomicSwapCacheStorage(self, _timeStampIt=_timeStampIt)
            
            
            self.WalletMgr = WalletManager(self)
            
            self.CacheStorage.on_load()
            
            
            self.WalletMgr.invalidate_all()
            self.WalletMgr.on_load()
            
            
            
            self.TradeManager = SwapTradeManager(self)
            
            self.Session = True
            _existingSession = self.Session
        
            
        return _existingSession
        
    def CloseSession(self):  
        if self.Session:
            self.save()
            self.stop_logging()
            
            self.WalletMgr = None
            self.TradeManager = None
            self.txUtils = None
            self.CacheStorage = None
            
            self.Session = None

    
    @contextmanager
    def Session(self): 
        try:
            self.NewTradeSession()
            yield self.NewTradeSession()
        finally:
            self.CloseSession()
           
    def __enter__(self):
        self.NewTradeSession()
        return self

    def __exit__(self, *args):
        self.CloseSession()
        
        
    def ensure_directory(self,_dir):
        if not os.path.exists(_dir):
            os.makedirs(_dir)    
        
    def setup_logging(self, _timeStampIt=False):
        #self._timestamp = round(time.time() * 1000) 
        
        self.savepath = os.getcwd() + f"/userdata/atomicswap_session.log"
        if _timeStampIt:
            self._timestamp = round(time.time() * 1000) 
            self.savepath = os.getcwd() + f"/userdata/atomicswap_session_{self._timestamp}.log"
            
        path = os.path.expanduser(self.savepath)
        self.ensure_directory(os.path.dirname(path))
        self.logger = logging.getLogger()
        self.handler = TimedRotatingFileHandler(path, when='D', interval=1, backupCount=1)
        fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        formatter = logging.Formatter(fmt=fmt, datefmt='%m/%d/%Y %H:%M:%S')
        self.handler.setFormatter(formatter)
        self.handler.setLevel(logging.INFO)
        # tee output to console as well
        self.console = logging.StreamHandler()
        self.console.setFormatter(formatter)
        self.console.setLevel(logging.INFO)
        self.logger.addHandler(self.console)
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.INFO)
    
    
    def stop_logging(self):
        self.logger.removeHandler(self.console)
        self.logger.removeHandler(self.handler)
    
        
    def save(self):
        
        #self.WalletMgr.on_close()
        self.WalletMgr.save_data()
        self.CacheStorage.save_data()
        
        
                

class RVNpyRPC_AtomicSwap():

    RPCconnexion = None
    RVNpyRPC = None
    def __init__(self,connexion, parent:RVNpyRPC):
        
        self.RPCconnexion = connexion
        self.RVNpyRPC = parent
        self.SwapMgr = AtomicSwapManager(connexion, parent, "")
        
    def SetWalletPassphrase(self, pw):
        if self.SwapMgr.Session:
            self.SwapMgr.txUtils.setWalletPassphrase(pw)
        else:
            print('no session found to set wallet passphrase')
    
    
    def InitSessionIfNull(self):
        if self.SwapMgr.Session == None:
            self.SwapMgr.NewTradeSession()
            
    def CloseSession(self):
        if self.SwapMgr.Session != None:
            self.SwapMgr.CloseSession()
            
            
    
    
    #
    #
    #
    # Return RAW of the required atomic swap.
    #
    #
    
    def CreateAtomicBuy(self, total_price, asset_name,quantity , order_count=1, destination='', pw=''):
        
        
        with self.SwapMgr as SwapMgrSession:
            return SwapMgrSession.TradeManager.create_trade("buy", "rvn", total_price, asset_name, quantity, order_count, destination)
    
    
    def CreateAtomicSell(self, total_price, asset_name,quantity , order_count=1, destination='', pw=''):
        with self.SwapMgr as SwapMgrSession:
            return SwapMgrSession.TradeManager.create_trade("sell", asset_name, quantity, "rvn",total_price  ,  order_count, destination)
            
    
    
    def CreateAtomicSwap(self, own_asset_name, own_quantity, want_asset_name,want_quantity, order_count, destination, pw=''):
        with self.SwapMgr as SwapMgrSession:        
            return SwapMgrSession.TradeManager.create_trade("trade", own_asset_name, own_quantity, want_asset_name, want_quantity, order_count, destination)
            
    
    def GetAtomicSwap(self, raw):
          
        with self.SwapMgr as SwapMgrSession: 
            _newAtomicSwap = SwapTransaction({}, SwapMgrSession)
            return _newAtomicSwap.decode_swap(raw)
        
    
    def CompleteSwap(self, raw):    
        with self.SwapMgr as SwapMgrSession: 
            _newAtomicSwap = SwapTransaction({}, SwapMgrSession)
            _valid,_swap =   _newAtomicSwap.decode_swap(raw)
            if _valid :
                _hex =  _swap.complete_order()
                if _hex != "":
                    return self.RPCconnexion.sendrawtransaction(_hex)
        
        
        
        
        