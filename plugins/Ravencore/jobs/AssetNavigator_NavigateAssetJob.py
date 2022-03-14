'''
Created on 28 févr. 2022

@author: slinux
'''

from wxRavenGUI.application.pluginsframework import *


class Job_AssetNavigator_Explore(Job):
    '''
    classdocs
    '''


    def __init__(self,plugin, library='', viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
        if library == "":
            library = "My Assets"
            
        self.library = library    
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        self.jobName = f"Navigate Asset {library}"        #self._run_safe = True
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        
        
        self._virtualReorganizationButtonState = plugin.PLUGIN_SETTINGS['tree_display_virtual_sort']
        self._organizeByMainAssetButtonState  = plugin.PLUGIN_SETTINGS['tree_display_regroupby_main']
        
        
        self.addExportParam('library') 
        self.addExportParam('_virtualReorganizationButtonState') 
        self.addExportParam('_organizeByMainAssetButtonState') 
        
        self.setAllowRemoteExecution(True)
        if self.library == "My Assets":
            self.setAllowRemoteExecution(False)
        
        
        
    def JobProcess(self):
        
        library = self.library
        _resultData = None 
        
        _allLibs = self.plugin.getData("_AssetLibraryList")
        
        
        navigation_use_cache = self.plugin.PLUGIN_SETTINGS['navigation_use_cache']
        
        
        _virtualReorganizationButtonState = self._virtualReorganizationButtonState
        _organizeByMainAssetButtonState = self._organizeByMainAssetButtonState
        
        #ravencoin = self.parentFrame.getRvnRPC()
        ravencoin = self.getNetworkRavencoin()
        
        
        if navigation_use_cache:
            if _allLibs.__contains__(library):
                if _allLibs[library] != None:
                    #wx.CallAfter(self.UpdateActiveViews, ())
                    return
        
        
        try:
            self.setProgress(f'Exploring...')
            if library == "My Assets":
                _resultData = ravencoin.asset.ExploreWalletAsset(OrganizeByMainAsset=_organizeByMainAssetButtonState)
                _allLibs[library] = _resultData
               
            else:
                _resultData = ravencoin.asset.ExploreAsset(library, _limit=99999, _skipchars=[])
                
                
                if _virtualReorganizationButtonState:
                    #print("EXPERIMENTAL =  TRY TO REORGANIZE DATAS")
                    _resultData.Reorganize_Series(regularExp="^#[a-zA-Z0-9]+" , minOccurence=1)
                    #print(_resultData)
                
                _allLibs[library] = _resultData
            
            
            self.setProgress(f'Complete')
            self.setResult(_allLibs)
            #self.setData("_AssetLibraryList", _allLibs)
            #self.setData("_CurrentLibrary", library)
            
            
        
        except Exception as e:
            self.plugin.RaisePluginLog( "Unable to Explore asset : "+ str(e), type="error")
            self.setError(e)
            
            
        
        
        
    
    def SaveResult(self):
        library = self.library
        _allLibs = self.getResult()
        '''
        _resultData = _allLibs[library]
        _virtualReorganizationButtonState = self.plugin.PLUGIN_SETTINGS['tree_display_virtual_sort']
        if _virtualReorganizationButtonState:
                    #print("EXPERIMENTAL =  TRY TO REORGANIZE DATAS")
            _resultData.Reorganize_Series(regularExp="^#[a-zA-Z0-9]+" , minOccurence=1)
                    #print(_resultData)
            _allLibs[library] = _resultData
        '''
        self.plugin.setData("_AssetLibraryList", _allLibs)
        