'''
Created on 28 févr. 2022

@author: slinux
'''

from wxRavenGUI.application.pluginsframework import *


class Job_AddressUTXO(Job):
    '''
    classdocs
    '''


    def __init__(self,plugin, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        self._add = self.plugin.getData('_address_viewer_current_address_text') 
        
        self.jobName = f"Address UTXO : {self._add}"
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        
        self.addExportParam('_add') 
        self.setAllowRemoteExecution(True)
        
        
        #self._run_safe = False
        
        
    def JobProcess(self):
        #_add = self.plugin.getData('_address_viewer_current_address_text') 
        _add = self._add
        self.logger.info(f'Job_AddressUTXO {_add}')
        
        
        #ravencoin = self.parentFrame.getRvnRPC()
        ravencoin = self.getNetworkRavencoin()
        _DatasUtxo = {'RVN':[],'ASSETS':[] }
        self.setMax(2)
        
        #if True:
        try:
            
            if _add == "":
                return
            
            _addressList = _add.split(',')
            
            self.setCurrent(0)  
            self.setProgress(f'Retreiving RVN UTXOs (0 / 2)')
            
            _listRaw = ravencoin.directories.GetAddressUnspentList( _addressList, asset="RVN", _excludeAsset='')
            _DatasUtxo = self.plugin.getData('_address_viewer_datas_utxo')
            _DatasUtxo['RVN'] = _listRaw
            
            self.setCurrent(1)  
            self.setProgress(f'Retreiving Assets UTXOs (1 / 2)')
            
            _ListAsset = ravencoin.directories.GetAddressUnspentList(_addressList, asset='*', _excludeAsset='RVN')
            _DatasUtxo['ASSETS'] = _ListAsset
            
            #print(f"_DatasUtxo {_DatasUtxo['ASSETS']}")
            #wx.CallAfter(self.UpdateActiveViews, ())
            self.setCurrent(2)  
            self.setProgress(f'Complete')
    
        
    
        except Exception as e:
            self.plugin.RaisePluginLog( "Unable to update address UTXO List : "+ str(e), type="error")
            self.setError(e)
            #raise Exception(f"{e}")
        
        
        self.setProgress(f'Address UTXO List Complete')
        self.setResult(_DatasUtxo)
        
    
    
    
    def SaveResult(self):
        self.plugin.setData("_address_viewer_datas_utxo", self.getResult())
        
        
        
        
        