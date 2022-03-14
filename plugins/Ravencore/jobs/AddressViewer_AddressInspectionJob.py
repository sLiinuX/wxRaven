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
        
        self._add = self.plugin.getData('_address_viewer_current_address_text') 
        
        self.addExportParam('_add')
        
        self.setAllowRemoteExecution(True)
        self.jobName = f"Address Inspection : {self._add}"
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        #self._run_safe = False
        
        
    
    def JobProcess(self):
        
        #_add = self.plugin.getData('_address_viewer_current_address_text') 
        _add = self._add
        #ravencoin = self.parentFrame.getRvnRPC()
        ravencoin = self.getNetworkRavencoin()
        _DatasHistory = []
        
        #self.setError(e)
        
        
        
        
        if _add == "":
                return
            
        _addressList = _add.split(',')
        
        
        self.logger.info(f'JobProcess - Job_AddressInspection : {_addressList}')
        #_DatasHistory = ravencoin.directories.GetAddressTransactionList(_addressList, _fullScan=True)
        
        
        self.setProgress(f'Retreiving list of transactions...')
        
        
        #if True:
        try:
            _DatasHistoryList = ravencoin.directories.GetAddressTransactionList(_addressList, _fullScan=False)
            _cursor = 0
            _max = len(_DatasHistoryList)
                
            self.setMax(_max)
                
                
            for _item in _DatasHistoryList:
                try:
                    self.setCurrent(_cursor)  
                    self.setProgress(f'Inspecting Transactions ({_cursor} / {_max})')
                    _txInspected = ravencoin.utils.GetAndScanRawTransaction(_item, _addressList, cleanData=True)
                    _DatasHistory.append(_txInspected)
                    
                    _cursor = _cursor+1
                except Exception as e:
                    self.logger.exception(f'JobProcess - Exception : {e}')
            
            self.setProgress(f'Address Inspection complete {_max} TX')
            self.setResult(_DatasHistory)
        except Exception as e:
            wx.CallAfter(self.plugin.RaisePluginLog, ( "Unable to update address transaction List : "+ str(e)))
            #self.plugin.RaisePluginLog( "Unable to update address transaction List : "+ str(e), type="error")
            self.setError(e)
            
        #no need to call save result it autosave
        
        
    def SaveResult(self):
        self.plugin.setData("_address_viewer_datas_tx_history", self.getResult())
        #wx.CallAfter(self.plugin.UpdateActiveViews, ())
        
        