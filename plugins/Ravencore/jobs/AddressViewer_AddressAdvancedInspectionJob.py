'''
Created on 27 févr. 2022

@author: slinux
'''


from wxRavenGUI.application.pluginsframework import *
from .AddressViewer_AddressInspectionJob import *
#from plugins.Ravencore.jobs.AddressViewer_AddressInspectionJob import Job_AddressInspection


class Job_AddressInspectionAdvanced(Job):
    '''
    classdocs
    '''


    def __init__(self,plugin, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        
        self._add = self.plugin.getData('_address_viewer_current_address_text')
        
        
        self._address_viewer_check_inputs = self.plugin.getData('_address_viewer_check_inputs')
        self._address_viewer_check_iterations = self.plugin.getData('_address_viewer_check_iterations')
        
        
        self.addExportParam('_add')
        self.addExportParam('_address_viewer_check_inputs')
        self.addExportParam('_address_viewer_check_iterations')
        
        self.setAllowRemoteExecution(True)
        
        """
        self.setData("_address_viewer_advanced_mode", False) 
        self.setData("_address_viewer_check_inputs", False) 
        self.setData("_address_viewer_check_iterations", 1) 
        
        """ 
        
        self.jobName = f"Address Adv. Inspection : {self._add}"
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        #self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        #self._run_safe = False
        
        
    
    def JobProcess(self):
        
        #_add = self.plugin.getData('_address_viewer_current_address_text') 
        _add = self._add
        
        #ravencoin = self.parentFrame.getRvnRPC()
        ravencoin = self.getNetworkRavencoin()
        _DatasHistory = []
        
        
        _allCommonAddresses = []
        
        
        if _add == "":
                return
            
        _addressList = _add.split(',')
        #_DatasHistory = ravencoin.directories.GetAddressTransactionList(_addressList, _fullScan=True)
        _commonAddressesCount = len(_addressList)
        _allCommonAddresses = _addressList
        
        
        self.setProgress(f'Initializing Job...')
        
        
        try:
            for i in range(0,self._address_viewer_check_iterations):
                #_newPassJob = Job_AddressInspection()
                ScanJob = Job_AddressInspection(self.plugin, self._jobDirectCallBack, safeMode=True)
                jnum = self.parentFrame.NewJob(ScanJob)
                
                _subJobResult = None
                
                while _subJobResult == None:
                    self.setProgress(f'Inspection in progress {i} / {self._address_viewer_check_iterations} , Waiting Job:[{jnum}]...')
                    _found, _subJobResult = self.parentFrame.JobManager.GetJobResultFromNumber(jnum)
                    
                    time.sleep(5)
                    
                _commonAddresses = ravencoin.utils.AddressesDatamining.IdentifyCommonInputs(_subJobResult)
                
                
                _allCommonAddresses = _allCommonAddresses + _commonAddresses
                _allCommonAddresses = list(dict.fromkeys(_allCommonAddresses))
                
                
                _c = 0
                
                
                if len(_allCommonAddresses) > _commonAddressesCount:
                    _commonAddressesCount = len(_allCommonAddresses)
                    
                    _str = ''
                    for a in _allCommonAddresses:
                        
                        if _c > 0:
                            _str = _str +','
                        
                        _str = _str + str(a)
                        
                        _c = _c+1
                    
                    self.plugin.setData('_address_viewer_current_address_text', _str) 
                else:
                    break
            
            
            self.setProgress(f'Inspection done : {len(_allCommonAddresses)} addresses...')    
            #self.setResult(_allCommonAddresses)    
            self.setError(f'Inspection done : {len(_allCommonAddresses)} addresses...')    
            print(_allCommonAddresses)    
        
        
        except Exception as e:
            wx.CallAfter(self.plugin.RaisePluginLog, ( "Unable to update address transaction List : "+ str(e)))
            #self.plugin.RaisePluginLog( "Unable to update address transaction List : "+ str(e), type="error")
            self.setError(e)
        
     
        #no need to call save result it autosave
        
        
    def SaveResult(self):
        self.plugin.setData("_address_viewer_datas_tx_history", self.getResult())
        #wx.CallAfter(self.plugin.UpdateActiveViews, ())
        
        