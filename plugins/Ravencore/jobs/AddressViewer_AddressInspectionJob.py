'''
Created on 27 févr. 2022

@author: slinux
'''


from wxRavenGUI.application.pluginsframework import *


class Job_AddressInspection(Job):
    '''
    classdocs
    '''


    def __init__(self,plugin, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        
        _add = self.plugin.getData('_address_viewer_current_address_text') 
        
        self.jobName = f"Address Inspection : {_add}"
        self.jobId = f"{self.jobName} - {self.parentFrame.ConnexionManager.getCurrent()}"
        self._run_safe = False
        
        
    
    def JobProcess(self):
        
        _add = self.plugin.getData('_address_viewer_current_address_text') 
        ravencoin = self.parentFrame.getRvnRPC()
        _DatasHistory = []
        
        #self.setError(e)
        
        
        
        
        if _add == "":
                return
            
        _addressList = _add.split(',')
        #_DatasHistory = ravencoin.directories.GetAddressTransactionList(_addressList, _fullScan=True)
        
        
        self.setProgress(f'Retreiving list of transactions...')
        
        
        #if True:
        try:
            _DatasHistoryList = ravencoin.directories.GetAddressTransactionList(_addressList, _fullScan=False)
            _cursor = 0
            _max = len(_DatasHistoryList)
                
            self.setMax(_max)
                
                
            for _item in _DatasHistoryList:
            
                self.setCurrent(_cursor)  
                self.setProgress(f'Inspecting Transactions ({_cursor} / {_max})')
                _txInspected = ravencoin.utils.GetAndScanRawTransaction(_item, _addressList, cleanData=True)
                _DatasHistory.append(_txInspected)
                
                _cursor = _cursor+1
            
            
            self.setProgress(f'Address Inspection complete {_max} TX')
            self.setResult(_DatasHistory)
        except Exception as e:
            self.plugin.RaisePluginLog( "Unable to update address transaction List : "+ str(e), type="error")
            self.setError(e)
        #no need to call save result it autosave
        
        
    def SaveResult(self):
        self.plugin.setData("_address_viewer_datas_tx_history", self.getResult())
        #wx.CallAfter(self.plugin.UpdateActiveViews, ())
        
        