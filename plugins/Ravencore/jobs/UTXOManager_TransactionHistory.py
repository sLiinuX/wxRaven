'''
Created on 28 févr. 2022

@author: slinux
'''
from wxRavenGUI.application.pluginsframework import *


class Job_WalletHistory(Job):
    '''
    classdocs
    '''


    def __init__(self,plugin, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        self.jobName = f"Wallet Transaction History"        #self._run_safe = True
        self.jobId = f"{self.jobName} - {self.parentFrame.ConnexionManager.getCurrent()}"
        #self._run_safe = False
        
        
    def JobProcess(self):
        ravencoin = self.parentFrame.getRvnRPC()
        _DatasHistory = { }
        #if True:
        #if True:
        try:
            
            self.setProgress(f'in progress...')
            _categorie = self.plugin.getData("_tx_history_category") 
            _start_date = self.plugin.getData("_tx_history_start") 
            _stop_date = self.plugin.getData("_tx_history_stop") 
            _filter_addresses = self.plugin.getData("_tx_history_address_filter") 

            _DatasHistory = ravencoin.wallet.GetWalletTransactionList(categorie=_categorie, filter_addresses=_filter_addresses, start_date=_start_date, stop_date=_stop_date)
            self.setProgress(f'Complete')
            #_ListAsset = ravencoin.asset.GetAssetUnspentList(assetname='', _fullDatas=True, _includeLocked=True)
            #_DatasUtxo['ASSETS'] = _ListAsset
            
            #print(f"_DatasUtxo {_DatasUtxo['ASSETS']}")
            #wx.CallAfter(self.UpdateActiveViews, ())

        except Exception as e:
            self.plugin.RaisePluginLog( "Unable to update transaction List : "+ str(e), type="error")
            self.setError(e)
    
        self.setResult(_DatasHistory)
        #self.setData("_tx_history", _DatasHistory)
        
        
    def SaveResult(self):
        self.plugin.setData("_tx_history", self.getResult())
        
        