'''
Created on 28 févr. 2022

@author: slinux
'''

from wxRavenGUI.application.pluginsframework import *


class Job_DecodeTx(Job):
    '''
    classdocs
    '''


    def __init__(self,plugin,txid='', hex='', viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        self.txid = txid
        self.hex = hex
        
        
        self.LastTx = None
        self.LastDecode = None
        
        if txid != '':
            self.jobName = f"Decode TX : {self.txid}"
        if hex != '':
            self.jobName = f"Decode TX : <HEX>"
        
        if txid != '':    
            self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        else:
            self.jobId = f"{self.hex} - {self.parentFrame.ConnexionManager.getCurrent()}"
            
        
        self.setAllowRemoteExecution(True)
        self.addExportParam('txid') 
        self.addExportParam('hex') 
        #self._run_safe = True
        
        
    def JobProcess(self):
        
        self.logger.info(f'Job_DecodeTx ')
        
        _txDatas = None
        try:
            #self.parentFrame
            #ravencoin = self.parentFrame.getRvnRPC()
            ravencoin = self.getNetworkRavencoin()
            
            
            if self.txid != '':
                self.LastTx = ravencoin.utils.GetRawTransaction(self.txid, inspect=True )
                _txDatas =  self.LastTx   
            
            
            elif self.hex != '':
                self.LastDecode = ravencoin.utils.DecodeTransaction(self.hex )
                self.txid = self.LastDecode['txid']
                
                self.LastTx = ravencoin.utils.GetRawTransaction(self.txid, inspect=True )
                
                _txDatas =  self.LastTx   
            
            else:
                self.setError('No parameter given to decode tx')
                pass
            
            
        except Exception as e:
            self.plugin.RaisePluginLog( "Unable to update decode tx : "+ str(e), type="error")
            self.setError(e)
            #raise Exception(f"{e}")
        
        
        self.setProgress(f'Tx Decoded')
        self.setResult(_txDatas)
        
    
    
    
    def SaveResult(self):
        self.plugin.setData("_last_tx_decoded", self.getResult())
        
        
        
        