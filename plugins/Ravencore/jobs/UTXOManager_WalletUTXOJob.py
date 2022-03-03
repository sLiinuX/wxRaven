'''
Created on 28 févr. 2022

@author: slinux
'''

from wxRavenGUI.application.pluginsframework import *


class Job_WalletUTXO(Job):
    '''
    classdocs
    '''


    def __init__(self,plugin, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        self.jobName = f"Wallet UTXOs"        #self._run_safe = True
        self.jobId = f"{self.jobName} - {self.parentFrame.ConnexionManager.getCurrent()}"
        
        
    def JobProcess(self):
        
        
        
        ravencoin = self.parentFrame.getRvnRPC()
        _DatasUtxo = {'RVN':[],'ASSETS':[] }
        self.setMax(2)
        
        
        ravencoin = self.parentFrame.getRvnRPC()
        
        try:
            
            
            self.setCurrent(0)  
            self.setProgress(f'Retreiving RVN UTXOs (0 / 2)')
            
            
            
            _listRaw = ravencoin.wallet.GetUnspentList(_OnlySpendable=True, _ExlcudeAddresses=[],_IncludeOnlyAddresses=[], _fullDatas=True , _includeLocked=True)
            _DatasUtxo = self.plugin.getData('_AllUTXOs')
            _DatasUtxo['RVN'] = _listRaw
            
            self.setCurrent(1)  
            self.setProgress(f'Retreiving Assets UTXOs (1 / 2)')
            
            
            _ListAsset = ravencoin.asset.GetAssetUnspentList(assetname='', _fullDatas=True, _includeLocked=True)
            _DatasUtxo['ASSETS'] = _ListAsset
            
            #print(f"_DatasUtxo {_DatasUtxo['ASSETS']}")
            #wx.CallAfter(self.UpdateActiveViews, ())
    
            self.setCurrent(2)  
            self.setProgress(f'Complete')
        
    
        except Exception as e:
            self.plugin.RaisePluginLog( "Unable to update UTXO List : "+ str(e), type="error")
            self.setError(e)
            #raise Exception(f"{e}")
        
        
        #self.setData("_AllUTXOs", _DatasUtxo)
        
        self.setResult(_DatasUtxo)
        
    
    
    
    def SaveResult(self):
        self.plugin.setData("_AllUTXOs", self.getResult())
        
        
        
        
        
        