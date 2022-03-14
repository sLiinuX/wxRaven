'''
Created on 28 févr. 2022

@author: slinux
'''
from wxRavenGUI.application.pluginsframework import *


class Job_AssetNavigator_Search(Job):
    '''
    classdocs
    '''


    def __init__(self,plugin, keyword='',limit=50, onlyMain=False, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
         
        
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        
        if keyword == "":
            keyword = "*"
            
        self.keyword = keyword  
        self.limit = limit     
        self.onlyMain = onlyMain 
        
        
        self.addExportParam('keyword') 
        self.addExportParam('limit') 
        self.addExportParam('onlyMain') 
        
        self.setAllowRemoteExecution(True)
        
        self.jobName = f"Search Asset {keyword}"        #self._run_safe = True
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        
        
    def JobProcess(self):
        
        
        keyword = self.keyword
        onlyMain = self.onlyMain 
        limit = self.limit 
        _AssetSearchResult = {}
        #try:
        try:
        #if True:    
            keyword = keyword.upper()

            self.setProgress(f'Searching {keyword}')
            #_lastSearch = self.plugin.getData("_LastSearch")
            
            #if _lastSearch == keyword:
            #    wx.CallAfter(self.UpdateActiveViews, ())
            #    return
            
            
            #if keyword == "":
            #    keyword =  self.getData("_LastSearch")
  
            _SkipChars = []
            if onlyMain:
                _SkipChars = ['#', "/", '$']
            #ravencoin = self.parentFrame.getRvnRPC()
            ravencoin = self.getNetworkRavencoin()
            
            _AssetSearchResult = ravencoin.asset.SearchAsset(AssetName=keyword,limit=limit,datetime=True, skipChars=_SkipChars ) 
            #myPluginData = self.parentFrame.ConnexionManager.getAllConnexions()
            #myPluginData2 = self.parentFrame.ConnexionManager.getCurrent()
            
            self.setResult(_AssetSearchResult)
            #self.setData("_AssetSearchResult", _AssetSearchResult)
            #self.setData("_LastSearch", keyword)
               
            #self.setData("myPluginData2", myPluginData2)

            #When datas are loaded, add a call after to trigger plugins view update
            #wx.CallAfter(self.UpdateActiveViews, ())
            
        except Exception as e:
            self.plugin.RaisePluginLog( "Unable to search asset :"+ str(e), type="error")
            self.setError(e)
            
        self.setProgress(f'Complete')
        
        
        
    
    def SaveResult(self):
        self.plugin.setData("_AssetSearchResult", self.getResult())
        
        