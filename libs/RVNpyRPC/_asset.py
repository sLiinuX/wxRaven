'''
Created on 20 déc. 2021

@author: slinux
'''

import requests
from libs.RVNpyRPC import RVNpyRPC
import enum



#from plugins.AssetManager.databaseEngine.model import AssetType 

class AssetType(enum.Enum):
    MAINASSET = "MAINASSET"
    SUBASSET = "SUBASSET"
    UNIQUEASSET = "UNIQUEASSET"
    MESSAGINGCHANNELASSET = "MESSAGINGCHANNELASSET"
    QUALIFIERASSET = "QUALIFIERASSET"
    SUBQUALIFIERASSET = "SUBQUALIFIERASSET"
    RESTRICTEDASSET = "RESTRICTEDASSET"
    UNDEFINED = "UNDEFINED"





_ASSET_KEYCHAR_ = {
    "MAINASSET":'',
    "SUBASSET":'/',
    "UNIQUEASSET":'#',
    "MESSAGINGCHANNELASSET":'~',
    "QUALIFIERASSET":'#',
    "SUBQUALIFIERASSET":'/#',
    "RESTRICTEDASSET":'$',
    }

_ASSET_REGEXP_ = {
    "MAINASSET":'',
    "SUBASSET":'[.*]/[.*]',
    "UNIQUEASSET":'#[.*]',
    "MESSAGINGCHANNELASSET":'[.*]~[.*]',
    "QUALIFIERASSET":'^#[.*]',
    "SUBQUALIFIERASSET":'[.*]/#[.*]',
    "RESTRICTEDASSET":'^$[.*]',
    }









class RVNpyRPC_Asset():
    '''
    classdocs
    '''
    RPCconnexion = None
    
    def __init__(self,connexion, parent:RVNpyRPC):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.RPCconnexion = connexion
        self.RVNpyRPC = parent
    
    """
    
    End user and sys, return direct usable datas most of the time
    
    """
    
    
    def info(self):
        pass
    
    
    def __repr__(self): 
        return ""
    
    def __str__(self): 
        return  ""
    
    
    
    
    def __containsSpecialChar__(self, name):
        _hasKeyChar = False
        for _keyName in _ASSET_KEYCHAR_:
            _keyChar = _ASSET_KEYCHAR_[_keyName]
            if _keyChar=='':
                continue
            if name.__contains__(_keyChar):
                _hasKeyChar = True
        return _hasKeyChar
    
    
    
    def __getType__(self, name):
        _hasKeyChar = ""
        for _keyName in _ASSET_KEYCHAR_:
            _keyChar = _ASSET_KEYCHAR_[_keyName]
            if _keyChar=='':
                continue
            if name.__contains__(_keyChar):
                _hasKeyChar = _keyName
        return _hasKeyChar
    
    
    
    def __backwardName__(self, name):
        count = 1
        while not self.__containsSpecialChar__(name[-count:]):
            count = count+1
            #print(name[-count:])
        #special case to look if the special char is not "double"    
        if self.__containsSpecialChar__(name[-(count+1):-count]):
            count = count+1
        return name[-count:]
    
    
    
    def __parseFullname__(self, fullname):
        cursor = 0
        
        #while 
    
    
    def IdentifyAsset(self, _assetData ):
        
        AssetFullName = _assetData['name']
        
        _type = AssetType.UNDEFINED
        _AssetShortName = ""
        _AssetPath = ""
        
        
        
        _hasKeyChar = self.__containsSpecialChar__(AssetFullName)    
        
        if _hasKeyChar == False:
            _type = AssetType.MAINASSET
            _AssetShortName = AssetFullName
            
        else:
            
            _AssetShortName = self.__backwardName__(AssetFullName)
            _AssetType = self.__getType__(_AssetShortName)
            _type = AssetType[_AssetType]
            
            
            _AssetPath = AssetFullName.replace(_AssetShortName, '')
            
            
            #
            #if the path empty, it
            if _AssetPath == "":
                pass
            #
            #if the path contains still special char, means in it is nested sub
            if self.__containsSpecialChar__(_AssetPath) and _type == AssetType.QUALIFIERASSET:
                _type = AssetType.SUBQUALIFIERASSET
        
        
        
        _assetData['type'] = _type
        _assetData['shortname'] = _AssetShortName    
        _assetData['path'] = _AssetPath    
        
        return _assetData
    
    
    
    
    
    def SearchAsset(self, AssetName, limit=50, start=0 , details=True, datetime=True, skipChars=[]):
        

        _res =  self.RPCconnexion.listassets(AssetName ,details,limit, start )['result']
        _result= {}
        
        _index = 0
        
        for _asset in _res:
            
            _assetData = {}
            
            
            if details:
                _assetData = _res[_asset]
            else:
                _assetData['name'] = _asset
            
            
            _skipAsset = False
            
            
            
            
            
            if skipChars != None:
                for _c in skipChars:
                    if _assetData['name'].__contains__(_c):
                        _skipAsset = True
                        break
                    
            if _skipAsset:
                continue
            
            
            
            
            
            if not _skipAsset:
                
                
                _identifiedassetData = self.IdentifyAsset(_assetData)
                
                if datetime and details:
                    _assetDateTime = self.RVNpyRPC.utils.blockHeightToDate(_identifiedassetData['block_height'])
                    _identifiedassetData['datetime'] = _assetDateTime
                
                
                
                
                _assetData = _identifiedassetData
                
                
            
            _result[_index] = _assetData
            _index = _index+1
        
        
        
        return _result
        
        
        
        
        
        