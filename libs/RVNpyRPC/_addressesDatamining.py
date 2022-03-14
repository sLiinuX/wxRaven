'''
Created on 3 mars 2022

@author: slinux
'''
import datetime
import logging
from datetime import date, datetime as dt

class AddressesDataMining(object):
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
        
        
        
    def IdentifyCommonInputs(self, inspectedTxList):
        
        _commonInputs = []
        
        for _tx in inspectedTxList:
            #addresses_in
            #category
            
            if _tx['category'] == "send":
                _allIns = _tx['addresses_in']
                
                if len(_allIns) > 0:
                    _commonInputs = _commonInputs + _allIns
                    
        return _commonInputs
    
    
    def IdentifyProbableOutputs(self, inspectedTxList):
        pass
    
    
    def IdentifyProbableGroups(self, inspectedTxList):
        pass