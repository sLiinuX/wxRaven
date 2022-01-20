'''
Created on 20 déc. 2021

@author: slinux
'''

import requests
from libs.RVNpyRPC import RVNpyRPC
import enum
from email._header_value_parser import AddressList
import re





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

_ASSET_VERIFY_REGEXP_ = {
    "MAINASSET":"^[A-Z0-9._]{3,}$",
    "SUBASSET":"^[A-Z0-9._]+$",
    "UNIQUEASSET":"^[-A-Za-z0-9@$%&*()[\\]{}_.?:]+$",
    "MESSAGINGCHANNELASSET":"^[A-Za-z0-9_]+$",
    "QUALIFIERASSET":"#[A-Z0-9._]{3,}$",
    "SUBQUALIFIERASSET":"#[A-Z0-9._]+$",
    "RESTRICTEDASSET":"\\$[A-Z0-9._]{3,}$",
    }

"""

// min lengths are expressed by quantifiers
static const std::regex ROOT_NAME_CHARACTERS("^[A-Z0-9._]{3,}$");
static const std::regex SUB_NAME_CHARACTERS("^[A-Z0-9._]+$");
static const std::regex UNIQUE_TAG_CHARACTERS("^[-A-Za-z0-9@$%&*()[\\]{}_.?:]+$");
static const std::regex MSG_CHANNEL_TAG_CHARACTERS("^[A-Za-z0-9_]+$");
static const std::regex VOTE_TAG_CHARACTERS("^[A-Z0-9._]+$");

// Restricted assets
static const std::regex QUALIFIER_NAME_CHARACTERS("#[A-Z0-9._]{3,}$");
static const std::regex SUB_QUALIFIER_NAME_CHARACTERS("#[A-Z0-9._]+$");
static const std::regex RESTRICTED_NAME_CHARACTERS("\\$[A-Z0-9._]{3,}$");


"""


import logging


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
        self.__search__cache__ = {}
        self.logger = logging.getLogger('wxRaven')
    """
    
    End user and sys, return direct usable datas most of the time
    
    """
    
    
    def __exist__(self, name):
        _exist = False
        _res = self.RPCconnexion.getassetdata(name)['result']
        if _res != None:
            _exist = True
        return _exist
    
    
    def __asset_details__(self, asset_name):
        admin = False
        if(asset_name[-1:] == "!"):
            admin = True
            asset_name = asset_name[:-1]  # Take all except !
        details = self.RPCconnexion.getassetdata(asset_name)['result']
        return (admin, details)
    
    
    def __verifyName__(self, name, type):
        _fullMatch = False
        _typeRegex = ""
        if type != "":
            _typeRegex = _ASSET_VERIFY_REGEXP_[type]
            r = re.fullmatch(_typeRegex, name)
            if r != None:
                _fullMatch = True
        
        return (_fullMatch, _typeRegex)
    
    
    def __isAdminAsset__(self, name):
        _idAdmin = False
        if name.__contains__('!'):
            _idAdmin = True
        return _idAdmin
    
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
            
            if count > len(name):
                break
            #self.logger.info(name[-count:])
        #special case to look if the special char is not "double"    
        if self.__containsSpecialChar__(name[-(count+1):-count]):
            count = count+1
        return name[-count:]
    
    
    
    
    
    def __isChildOf__(self, fathername, childname):
        _isChild=False
        #_childShortName = self.__backwardName__(childname)
 
        if childname.__contains__(fathername):
            _isChild =  True
        if fathername == childname:
            _isChild =  False
        
    
        return _isChild
    
    def __isDirectChildOf__(self, fathername, childname):
        _isChild=False
        _childShortName = self.__backwardName__(childname)
 
        _childPrefix = childname.replace(_childShortName, '')
        
        #self.logger.info("P=" + _childPrefix)
        #self.logger.info("F=" + fathername)
        if _childPrefix == fathername:
            _isChild =  True
    
        return _isChild
    
    
    def __identifyChildrenOf__(self, rawList):
        
        _relationship_list = {}
        
        for _elem in rawList:
            
            for _otherElem in rawList:
                
                if self.__isChildOf__(_otherElem, _elem):
                    _relationship_list[_elem] = _otherElem
            
        return _relationship_list  
    
    
    
    
    def GetAssetUnspentList(self, assetname):
        
        _res =[]
        
        _allmatch= self.RPCconnexion.listmyassets(assetname, True)['result']
        #self.logger.info("_allmatch")
        #self.logger.info(_allmatch)
        #_res = _allmatch[assetname]
        if _allmatch.__contains__(assetname):
            _res = _allmatch[assetname]
            #self.logger.info(f"OK {_res}")
            #self.logger.info(f"A {_allmatch[assetname]}")
        return _res

    
    
    def GetAssetUnspentTx(self, assetname, _amount,_takeBiggest=True, _OneTx=False):
        _list =self.GetAssetUnspentList(assetname)
        
        #self.logger.info(f'B {_list}')
        
        
        _txId = []
        _filled = False
        
        
        delta = 0
        _feasible = True
        if _list['balance'] < _amount:
            _feasible = False
            self.logger.info(' UNFFEASIBLE')
        else:
            self.logger.info(' FEASIBLE')
        
        if _feasible:
        
            _max=0.0
            _maxId = ''
            _maxVout = 1
            
            for _i in _list['outpoints']:
                #self.logger.info(_i['amount'])
                
                _iVal = _i['amount']
                _iVout =  _i['vout']
                _itxid = _i['txid']
                
                
                if _iVal > _max:
                    self.logger.info(f' NEW MAX : {_iVal}')
                    _max = _i['amount']
                    _maxId = _i['txid']
                    _maxVout = _i['vout']
                    
                self.logger.info(f' Ammout {_iVal}')
                self.logger.info(f' txid {_itxid}')
                self.logger.info(f' vout {_iVout}')
                    
        
            self.logger.info(f'_max {_max}')
        
        
            if _OneTx and _max <_amount:
                _feasible = False
                self.logger.info(' UNFFEASIBLE 2 ')
            
            
            if _feasible:
                #_txId.append(_maxId)
                _txId.append({'txid':_maxId, 'vout':_maxVout})
                delta = _amount-_max
                
                self.logger.info(f"DElta - = {delta.__abs__()}")
                _filled=False
            
            if _max >= _amount:
                _filled = True
        
            
            
            
            
            if not _OneTx and _feasible and not _filled:
                
                #delta = _amount-_max
                self.logger.info(f"DElta = {delta.__abs__()}")
                while delta > 0:
                    for _i in _list['outpoints']:
                        if _i['txid'] != _maxId:
                            _add = _i['amount']
                            _txId.append({'txid':_i['txid'], 'vout':_i['vout']})
                            
                            
                            self.logger.info(f"DElta - = {_add}")
                            self.logger.info(f"DElta - = {delta}")
                            delta = delta - _add
                            
                            if delta < 0:
                                break
                            
                            
        else:
            self.logger.info(' UNFFEASIBLE')                    
        
        self.logger.info(_txId)
        delta = delta.__abs__()
        
        return _feasible,_txId, delta
            
    
    
    
    def GetBalance(self, assetname):
        _balance = 0.0
        
        _res =  self.RPCconnexion.listmyassets(assetname,True)['result'] 
        
        if _res != None:
            if _res.__contains__(assetname):
                _balance = _res[assetname]['balance']
        return _balance
    
    
    
    def GetParent(self, assetName, nullIfMain=True):
        _assetShortName = self.__backwardName__(assetName)
        _childPrefix = assetName.replace(_assetShortName, '')
        
        if _childPrefix == "" and not nullIfMain:
            _childPrefix = assetName
                
                

        return _childPrefix


    def GetMainAsset(self, assetName):
        
        _oldParent = self.GetParent(assetName)
        _last = ""
        
        
        while _oldParent != "":
            _last = _oldParent
            _oldParent = self.GetParent(_oldParent)
            
        return _last
    
    
    def IdentifyAsset(self, _assetData ):
        
        AssetFullName = _assetData['name']
        
        _type = AssetType.UNDEFINED
        _AssetShortName = ""
        _AssetPath = ""
        _AssetParent = ""
        
        
        _hasKeyChar = self.__containsSpecialChar__(AssetFullName)    
        
        if _hasKeyChar == False:
            _type = AssetType.MAINASSET
            _AssetShortName = AssetFullName
            
        else:
            
            _AssetShortName = self.__backwardName__(AssetFullName)
            _AssetType = self.__getType__(_AssetShortName)
            _type = AssetType[_AssetType]
            
            
            _AssetParent = self.GetParent(AssetFullName, nullIfMain=True)
            
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
        _assetData['parent'] = _AssetParent   
        
        
        return _assetData
    
    
    
    def SearchAsset(self, AssetName, limit=50, start=0 , details=True, datetime=True, skipChars=[]):
        

        _res =  self.RPCconnexion.listassets(AssetName ,details,limit, start )['result']
        _result= {}
        
        _index = 0
        if _res != None:
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
                
                
                if details:
                    self.__search__cache__[_assetData['name']] = _assetData
                
                
                
                _result[_index] = _assetData
                _index = _index+1
            
            
        
        return _result
        
    
    
    def GetAssetData(self, _assetPartialData):
        
        _MyAssetData = {}
        
        if self.__search__cache__.__contains__(_assetPartialData['name']):
            _MyAssetData = self.__search__cache__[_assetPartialData['name']]
        
        else:
            res = self.SearchAsset(_assetPartialData['name'], 1, details=True, datetime=True)
            
            if len(res) > 0:
                _MyAssetData = res[0]
        
        if _MyAssetData != None:
            for attr in _MyAssetData:
                _assetPartialData[attr] = _MyAssetData[attr]
            
        return _assetPartialData
    
        """
        
            EXPLORER FUNCTION
        
        """
        
        
    def ExploreAsset(self, assetName, _limit=999999, _skipchars=[]): 
        
        #_assetMatchList = self.SearchAsset(assetName, limit=999999, start=0, details=False, datetime=False, skipChars=_skipchars)   
        
        
        _assetData = {'name':assetName}
        _identifiedassetData = self.IdentifyAsset(_assetData)
        _identifiedassetData = self.GetAssetData(_identifiedassetData)
        
        ObjTreeEmpty = AssetTreeObj(assetName, _assetData['shortname'], _assetData['path'], _assetData['type'], _identifiedassetData)

        
        ObjTree = self.__Explore__AssetTreeObj(ObjTreeEmpty, _limit)
        return ObjTree
    
    
    
    
    def __Explore__AssetTreeObj(self, _objTree, _limit=999999):
        
        _objTree.childs = []
        
        _queryChilds = self.GetAssetChilds(_objTree.name , allLevels=False, _limit=_limit)
        #self.logger.info(len(_queryChilds))
        
        if _queryChilds != None:
            for c in _queryChilds:
                _assetData = {'name':c}
                _identifiedassetChild = self.IdentifyAsset(_assetData)
                _identifiedassetChild = self.GetAssetData(_identifiedassetChild)
                _childTree= AssetTreeObj(c, _identifiedassetChild['shortname'], _identifiedassetChild['path'], _identifiedassetChild['type'], _identifiedassetChild)
                
                self.__Explore__AssetTreeObj(_childTree)
                
                _objTree.childs.append(_childTree)
                
        return _objTree
        
    
    def GetAssetChilds(self, assetname,allLevels=True,_limit=999999, _skipchars = []):
        _assetMatchList = self.SearchAsset(assetname+"*", limit=_limit, start=0, details=True, datetime=False, skipChars=_skipchars)   
        
        
        #self.logger.info(len(_assetMatchList))
        _allChilds = []
        for result in _assetMatchList:
            
            asset = _assetMatchList[result]
            if asset['name'] == assetname:
                continue
            
            
            if not allLevels:
                
                isDirectCh = self.__isDirectChildOf__(assetname, asset['name']) 
                if not isDirectCh:
                    #self.logger.info(asset['name'] + " is not direct child of " + assetname)
                    continue 
                
            _allChilds.append(asset['name'])
    
        return _allChilds

    
    
    
    #
    #
    # Walletr Exploring
    #
    
    
    
    
    
    
    
    def ExploreWalletAsset(self, _addressList=None, OrganizeByMainAsset=False):
        #if none address , then check LOCAL wallet
        
        _AssetRawList = []
        
        if _addressList == None:
            _res =  self.RPCconnexion.listmyassets("*",True)['result']
            for key in _res:
                _AssetRawList.append(key)
            #.listmyassets("*",True)
        else:
            
            for _ad in AddressList:
                _res =  self.RPCconnexion.listassetbalancesbyaddress(_ad,False)['result']
                for key in _res:
                    _AssetRawList.append(key)
                
                
             
        
        #x = {}
        #x.__contains__(key)
        
        if OrganizeByMainAsset:
            for _elem in _AssetRawList.copy():
                _elemMain = self.GetMainAsset(_elem)
                if _elemMain != "":
                    _AssetRawList.append(_elemMain)
        
        _AssetRawList = list(dict.fromkeys(_AssetRawList))
        
        
        ObjTreeEmpty = AssetTreeObj("Wallet", "Wallet", _addressList, None)
        ObjTreeEmpty._isVirtual = True
        
        FinalObjTreeEmpty = self.__ExploreWallet__AssetTreeObj__(ObjTreeEmpty, _AssetRawList)
        return FinalObjTreeEmpty
    
    
    
    
    def __ExploreWallet__AssetTreeObj__(self, objTree, _AssetRawList):    
        
        _relationship_list = self.__identifyChildrenOf__(_AssetRawList)
        
        
        
        
        
        for _assetName in _AssetRawList:
            
            #Skip childs of
            if _relationship_list.__contains__(_assetName):
                continue
            
            
            _assetData = {'name':_assetName}
            _identifiedassetChild = self.IdentifyAsset(_assetData)
            _identifiedassetChild = self.GetAssetData(_identifiedassetChild)
            _childTree = AssetTreeObj(_assetName, _identifiedassetChild['shortname'], _identifiedassetChild['path'], _identifiedassetChild['type'],_identifiedassetChild)
            
            _newRawList = []    
            for _child in _relationship_list:
                if self.__isChildOf__(_assetName, _child):
                    _newRawList.append(_child)
                    
                    """
                    
                    for _i in _relationship_list:
                        if _relationship_list[_i] == _child:
                            _newRawList.append(_i)
                    """    
                        
            _childTree = self.__ExploreWallet__AssetTreeObj__(_childTree, _newRawList)
                    
                    
            
            
            
            
            objTree.childs.append(_childTree)
           
            #_res =  self.RPCconnexion.listmyassets("*",True)['result']
            #.listassetbalancesbyaddress("RDyF4itWbfryV2nM4w2L99oJ4MvNptt82F",False)
    
    
    
    
        return objTree
    
    
    
    

        
    
    
    #
    #
    #
    #    Wallet Asset issue
    #
    #
    #
    
    def GetAllAdminAssets(self, _includeNonNestable=True):
        _AssetRawList = []
        
        
        _res =  self.RPCconnexion.listmyassets("*",True)['result']
        for key in _res:
                
            if self.__isAdminAsset__(key):
                
                _AssetRawList.append(key)
        
        
        return _AssetRawList
    
    
    
    def GetAllMyAssets(self, _excludeAdmin=False):
        _AssetRawList = []
        
        
        _res =  self.RPCconnexion.listmyassets("*",True)['result']
        for key in _res: 
            if self.__isAdminAsset__(key) and _excludeAdmin:
                continue
                 
            _AssetRawList.append(key)
        
        
        return _AssetRawList


class AssetTreeObj(object):
    
    
    name = ""
    shortname = ""
    path = ""
    type = ""
    
    datas = {}
    childs = []
    
    _isVirtual = False
    _isAdmin = False
    
    
    def __init__(self, assetname, shortname, path , type, datas=None):    
        
        self.name = assetname
        
        self.shortname = shortname
        self.path = path
        self.type = type
        self.datas = datas
        
        if assetname.__contains__('!'):
            self._isAdmin = True
        else:
            self._isAdmin = False
        
        self.childs = []

        
    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.name)+"\n"
        for child in self.childs:
            ret += child.__repr__(level+1)
        return ret    
        
        
    def __short__(self, level=0):
        ret = "\t"*level+repr(self.shortname)+"\n"
        for child in self.childs:
            ret += child.__repr__(level+1)
        return ret   
    
    def __path__(self, level=0):
        ret = "\t"*level+repr(self.path)+"\n"
        for child in self.childs:
            ret += child.__repr__(level+1)
        return ret   
    
    def __len__(self, count=0):
        count = count+1
        for child in self.childs:
            count = child.__len__(count)
            count = count+1
        return count
    
    
    def Reorganize_Series(self, regularExp="^#[a-zA-Z0-9]+" , minOccurence=2):
        pass
        
        _MatchItems = []
        
        _dictCount = {}
        
        for _c in self.childs:
            
            # re.findall("^[a-zA-Z0-9]+",x)
            #
            _isMatch = re.findall(regularExp,_c.shortname)
            
            _serie = ""
            if len(_isMatch) > 0:
                
                #self.logger.info(_isMatch)
                
                _serie = _isMatch[0]
                
                #self.logger.info(_serie)
                
            if _serie != "":
            
                if _dictCount.__contains__(_serie):
                    _matchCount = _dictCount[_serie]
                    _matchCount = _matchCount + 1
                    _dictCount[_serie] = _matchCount
                else:
                    _dictCount[_serie] = 1
                
                
        #self.logger.info(_dictCount)
        
        
        for _sKey in _dictCount:
            _cKey = _dictCount[_sKey]
            
            
            if _cKey >= minOccurence:
                #pass
                #AssetTreeObj(assetname, shortname, path, type, datas)
                _newSerieChildTree = AssetTreeObj(_sKey, _sKey, self.path, self.datas)
                _newSerieChildTree._isVirtual = True
                
                _toRemove = []
                
                
                for _c in self.childs:
                    if str(_c.shortname).__contains__(str(_sKey)):
                        _newSerieChildTree.childs.append(_c)
                        _toRemove.append(_c)
                        
                for _tr in _toRemove:
                    self.childs.remove(_tr)
            
                self.childs.append(_newSerieChildTree)
            
    
        
        
    






        