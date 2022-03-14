'''
Created on 28 févr. 2022

@author: slinux
'''

from wxRavenGUI.application.pluginsframework import *


class Job_AssetNavigator_AssetOwner(Job):
    '''
    classdocs
    '''


    def __init__(self,plugin, asset='*', viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
        
            
        self.asset = asset    
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        self.jobName = f"Asset Owner List {asset}"        #self._run_safe = True
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        
        
        self.addExportParam('asset') 
        self.setAllowRemoteExecution(True)
        
    def JobProcess(self):
        
        try:
            #ravencoin = self.parentFrame.getRvnRPC()
            ravencoin = self.getNetworkRavencoin()
            _resultOwnerList = ravencoin.directories.GetAssetOwnerAddressList(self.asset, detailed=True)
            self.setProgress(f'Complete')
            self.setResult(_resultOwnerList)
            #self.setData("_AssetLibraryList", _allLibs)
            #self.setData("_CurrentLibrary", library)
            
            
        
        except Exception as e:
            self.plugin.RaisePluginLog( "Unable to Explore asset : "+ str(e), type="error")
            self.setError(e)
            
    def SaveResult(self):
        _newreesult = self.getResult()
        _AllOwners = self.plugin.getData('_AssetOwnerList')
        
        _AllOwners[self.asset] = _newreesult
        self.plugin.setData("_AssetOwnerList", _AllOwners)
        
        