'''
Created on 5 mars 2022

@author: slinux
'''
import flask
from flask import request, jsonify
from .wxFlaskCustomView import * 
from flask_classful import route
import functools
from flask import Flask, redirect, url_for






class MeCoView(wxCustomFlaskView):
    route_base = '/api/'
    

    decorators = [login_required]
    _assetPayoutAddress = 'mu36AD8YxCMEVar3Jh4GkFb1fqchWxh6pE'
    #_assetPayoutAddress = 'ms3u9iYcy4A5G4GEX4NfdGWTccqzwG5Smp'
    
    
    
    
    
    
    
    
    
    
    
    @route('/v1/meco/checktx')     
    def CheckTx(self, txId='', assetName=''):
        query_parameters = request.args
        args = extract_parameters(request.args)
        txId = args.get('txId')
        assetName = args.get('assetName')
        
        #GetRawTransaction
        #self.wxRavenInstance.Get
        network = self.daemon.getNetwork()
        ravencoin = self.daemon.getRavencoin()
        
        #ravencoin:RavenpyRPC
        if txId == None or assetName==None: 
            return self.returnJSONError(f"Invalid TxId : '{txId}' or assetName '{assetName}'.")
        
        
        txDatas = ravencoin.utils.GetRawTransaction( txId, decoded=True, addressesPOV=[] , inspect=False)
        
        
        
        if txDatas!= None:
            if txDatas['confirmations'] > 1:
                
                _checkIfReceived, _unspentList = ravencoin.wallet.SearchUnspentTxfromTxId(txId, [self._assetPayoutAddress])
                if not _checkIfReceived:
                    return self.returnJSONError(f"TxId : '{txId}' found with {len(_unspentList)} results for internal address, make sure you sent the RVN to the following address : {self._assetPayoutAddress}")
            
                
                
                else:
                    #return self.returnJSONError(f"TxId : '{txId}' found with {len(_unspentList)} results")
                    #
                    # FAKE ISSUE
                    #
                    #
                    return self.returnJSON(f"BINGO : TXID OF ASSET")
                    #return self.returnJSON(f"TxId : '{txId}' found with {len(_unspentList)} results.\nasset issued : txId")
                    #pass
            
            
            
            else:
                
                return self.returnJSONError(f"TxId : '{txId}' found but not confirmed yet.")
        
        else:
            return self.returnJSONError(f"Invalid TxId : '{txId}'.")
        
        
        
    
    @route('/v1/meco/checkuserwstoken')     
    def checkuserwstoken(self,checktoken='' ):
        query_parameters = request.args
        args = extract_parameters(request.args)
        checktoken = args.get('checktoken')
        _valid=False
        _res = 0
        _resFriendly = '0 Mb'
        if checktoken != None:
            _res = self.__GetUserTokenQueryCount__(checktoken)
            _resFriendly = self.daemon.convert_size(_res)
            if _res>0:
                _valid = True
        
            
            
        return self.returnJSON({'valid':_valid, 'size':_res , 'size_friendly':_resFriendly})
        
        
        
        