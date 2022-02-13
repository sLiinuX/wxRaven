'''
Created on 7 févr. 2022

@author: slinux
'''

import re
from .wxRavenRavencoreDesign import wxRaven_RavencoreAsset_OwnerListExporter
import threading
import time 
import wx 
from wxRavenGUI.application.wxcustom import *
from wxRavenGUI.application.wxcustom.CustomLoading import *
from wxRavenGUI.application.wxcustom.CustomUserIO import UserQuestion


class wxRaven_Ravencore_AssetOwnerExporterLogic(wxRaven_RavencoreAsset_OwnerListExporter):
    '''
    classdocs
    '''


    view_base_name = "Asset Owner Exporter"
    view_name = "Asset Owner Exporter"
    parent_frame = None
    default_position = "dialog"
    icon = 'ownerlist'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent, parentFrame, position = "dialog", viewName= "Asset Owner Exporter", isInternalPluginView=True):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Asset Owner Exporter"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.parent = parent
        self.exportList= []
        self.filepath = ''
        
        
        self._max=0
        self._running=False
        self._stopRequested=False
        
        self.currentAsset = ''
        self.addressesRawCount = 0
        
        self.assetIndexFilter= '*'
        
        ravencoin = self.parent_frame.getRvnRPC()
        self.waitApplicationReady()
        
        
        
    
    
    
    
    
    
    def OnStartFullIndex(self, event):
        if self._running:
            self._stopRequested=True
            self.m_button1.Enable(False)
        else:
            self.m_button1.Enable(False)
            self.DoStartIndex()
            
    
    
    
    def SetAssetAndStart(self, assetname):
        self.assetIndexFilter = assetname
        self.DoStartIndex()
        
        
        
    def DoStartIndex(self):
        
        self.m_button1.SetLabel('Stop')
        self.m_button1.Enable(True)
        
        if self.assetIndexFilter == '':
            self.assetIndexFilter = RequestUserTextInput(self, "Choose Asset(s) to index, '*' for all", 'Asset Filter')
        t=threading.Thread(target=self.__DoIndex_T__, args=(self.UpdateView,))
        t.start()
    
    
    def SetupMax(self, m):
        self._max=m
        self.m_gauge1.SetRange(m)
    
    def ReportProgress(self, p, evt=None):
        self.m_staticText15.SetLabel(f' {p} / {self._max}')
        self.m_gauge1.SetValue(p)
    
    
    
    def ReportDetails(self, evt=None):
        self.m_staticText34.SetLabel(f' : [{self.currentAsset}]')
        self.m_staticText35.SetLabel(f'{self.addressesRawCount} Addresses found !')
        #self.m_gauge1.SetValue(p)
    
    
    def __stopped__(self):
        self._running = False
        self._stopRequested = False
        self.m_button1.SetLabel('Start')
        self.m_button1.Enable(True)
    
    
    
    def __DoAsset__(self, assetName, position=1, max=1, simulation=False):
        
        print(assetName)
        self.currentAsset=assetName
        #self.logger.info(f' Scanning {_assetName}')
        if not simulation:
            ravencoin = self.parent_frame.getRvnRPC()
            _adListAsset = ravencoin.directories.GetAssetOwnerAddressList(assetName)
            #_db = self.parent_frame.GetPluginData("DatabaseManager","_database")
            
            if len(_adListAsset) >0:
                
                self.addressesRawCount = self.addressesRawCount + len(_adListAsset)
                
                self.exportList = self.exportList+ _adListAsset
                    
                    #_batchList = []
                    #for ad in _adListAsset:
                    
                #_db.update_addresse_asset_balance_virtual_batch(assetName, _adListAsset)
                        
    
                '''
                    
                    for ad in _adListAsset:
                        #bal= _adListAsset[ad]
                        _db.update_addresse_asset_balance(ad, assetName,0.0, _hasChange=False, alias="", virtual=True)
                    #_adList = _adList+_adListAsset
                    
                '''
                    
                
                
                
                
        wx.CallAfter(self.SetupMax, (max))    
        wx.CallAfter(self.ReportProgress, (position))
        wx.CallAfter(self.ReportDetails, ())
    
    
    
    
    def ConfirmDone(self, evt=None):
        UserAdvancedMessage(self.parent_frame, f"Export done in {self.filepath}", "success")
    
    def __DoIndex_T__(self,callback):
        if self._running:
            return
        
        self.exportList = []
        _SIMULATION = False
        _FETCH_BUT_NO_UPDATE = True
        
        ravencoin = self.parent_frame.getRvnRPC()
        self._running=True
        
        _assetIndexFilter = self.assetIndexFilter
        if _assetIndexFilter == "":
            _assetIndexFilter = '*'
        
        if True:
        #try:
            #_db = self.parent_frame.GetPluginData("DatabaseManager","_database")
            #_knownList = _db.existing_addresse_asset_balance_virtual_assetlist()
            
            _adList = []
            _allResultAsset = ravencoin.asset.SearchAsset(_assetIndexFilter, limit=999999, details=False, datetime=False)
            _max = len(_allResultAsset)
            _cur = 0
            
            #wx.CallAfter()
            for _asset in _allResultAsset:
                _assetName = _allResultAsset[_asset]['name']
                _skipAsset = False
                
                
                if self._stopRequested:
                    wx.CallAfter(self.__stopped__)
                    return 
                
                
                #if _FETCH_BUT_NO_UPDATE and _knownList.__contains__(_assetName):
                #    _skipAsset = True
                    
                if  _SIMULATION:
                    _skipAsset = True
                       
                
                
                
                self.__DoAsset__(_assetName, _cur,_max , _skipAsset)
                _cur = _cur+1
        
        _assetIndexFilter = _assetIndexFilter.replace('*', '_with_childs')    
        _assetIndexFilter = _assetIndexFilter.replace('#', '_QUALIFIER_') 
        _assetIndexFilter = _assetIndexFilter.replace('$', '_RESTRICTED_')   
        _assetIndexFilter = _assetIndexFilter.replace('!', '_ADMIN_')   
        _assetIndexFilter = _assetIndexFilter.replace('.', '_')    
            
        fnam =  re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", _assetIndexFilter)        
        self.filepath = self.parent_frame.GetPath('USERDATA') + fnam + '.owners'
        #except Exception as e:
        #    pass
        with open(self.filepath, 'w') as file_handler:
            for item in self.exportList:
                file_handler.write("{}\n".format(item))
        
        wx.CallAfter(self.ReportProgress, (_cur))
        wx.CallAfter(self.ReportDetails, ())
        
        wx.CallAfter(self.ConfirmDone, ())
        
        self._running=False
        self.__stopped__()
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.UpdateView,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(1)
            
        wx.CallAfter(callback, ()) 
    
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self, evt=None):
        
        self.UpdateDataFromPluginDatas()
        self.Layout()
        
        
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self, evt=None): 
        pass