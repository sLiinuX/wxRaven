'''
Created on 13 janv. 2022

@author: slinux
'''


UNIT_TERA = 1000000000000
UNIT_GIGA = 1000000000
UNIT_MEGA = 1000000
UNIT_KILO = 1000





class RVNpyRPC_Network():
    '''
    classdocs
    '''
    RPCconnexion = None
    
    def __init__(self,connexion, parent):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.RPCconnexion = connexion
        self.RVNpyRPC = parent
    
    
    
    
    def GetMempoolUsage(self, percentage=True):
        _mempoolInfos =  self.RPCconnexion.getmempoolinfo()['result']
        _usage = _mempoolInfos['usage']
        _max = _mempoolInfos['maxmempool']
        _ratio = (_usage / _max) 
        _retval= _ratio * 100
        
        
        
        if not percentage:
            _retval = _ratio
        else:
            if _retval < 1:
                _retval = 0.0
            else:
                _retval = float(_retval).__round__(1)    
        
        
        
        return _ratio
        
        
    
        
        
    def GetNetworkInfos(self):
        #
        #{'blocks': 2102974, 'currentblockweight': 0, 'currentblocktx': 0, 'difficulty': 83255.50545680113, 
        # 'networkhashps': 5722312398548.8, 'hashespersec': 0, 'pooledtx': 6, 'chain': 'main', 'warnings': ''}
        
        
        
        _netInfos = self.RPCconnexion.getmininginfo()['result']
        _blockInfos = self.RPCconnexion.getblockchaininfo()['result']
        _mempoolInfos =  self.RPCconnexion.getmempoolinfo()['result']
        
        #_netInfos = self.RVNpyRPC.secure_call(self.RPCconnexion.getmininginfo)['result']
        
        
        _hashrate = _netInfos['networkhashps']
        _hashrate = self.RVN_hashrate_friendly(_hashrate)
        
        _difficulty = _netInfos['difficulty']
        _difficulty = self.RVN_hashrate_friendly(_difficulty)
        
        _netInfos['difficulty'] = _difficulty
        _netInfos['networkhashps'] = _hashrate
        
        _netInfos['headers'] = _blockInfos['headers']
        _netInfos['mempool_size'] = _mempoolInfos['size']
        _netInfos['mempool_usage'] = _mempoolInfos['usage']
        _netInfos['mempool_max'] = _mempoolInfos['maxmempool']
        
        _ratio = (_netInfos['mempool_usage'] / _netInfos['mempool_max'] ) 
        _retval= _ratio * 100
        
        if _retval < 1:
            _retval = 0.0
        else:
            _retval = float(_retval).__round__(1)
        
        _netInfos['mempool_usage_percentage'] = _retval
        _netInfos['mempool_usage_ratio'] = _ratio
        
        
        '''
        _memoryInfos =  self.RPCconnexion.getmemoryinfo()['result']
        _netInfos['memory_used'] = _memoryInfos['used']
        _netInfos['memory_free'] = _memoryInfos['free']
        _netInfos['memory_total'] = _memoryInfos['total']
        
        
        _ratio = (_netInfos['memory_used'] / _netInfos['memory_total'] ) 
        _retval= _ratio * 100
        
        if _retval < 1:
            _retval = 0.0
        else:
            _retval = float(_retval).__round__(1)
        
        _netInfos['memory__usage_percentage'] = _retval
        _netInfos['memory__usage_ratio'] = _ratio
        '''
        
        
        
        
        return _netInfos
        
    
    
    def UnstuckNode(self, rewindCount=1000):

        _stuckPosition=  self.RPCconnexion.getblockchaininfo()['result']['headers']
        _rewindPosition = _stuckPosition - rewindCount
        blockHash = self.RPCconnexion.getblockhash(_rewindPosition)['result']
        _response = self.RPCconnexion.invalidateblock(blockHash)['result']
        _response = self.RPCconnexion.reconsiderblock(blockHash)['result']
        return _response
    
    
        
        
    def RVN_hashrate_friendly(self,hashrate):
        #TH/s
        nethashValue = float(hashrate)
        nethashValueUnit = "H/s"
        nethashValueStr = ""
        
        
            
        if nethashValue / UNIT_TERA >= 1:
            nethashValue = nethashValue / UNIT_TERA
            nethashValueUnit = "TH/s"
        
        
        
        if nethashValue / UNIT_GIGA >= 1:
            nethashValue = nethashValue / UNIT_GIGA
            nethashValueUnit = "GH/s"
            
            
        if nethashValue / UNIT_MEGA >= 1:
            nethashValue = nethashValue / UNIT_MEGA
            nethashValueUnit = "MH/s"    
        
        
        
        nethashValue = nethashValue.__round__(3)
        nethashValueStr =  str(nethashValue) + " " +    nethashValueUnit
        return (nethashValue, nethashValueUnit, nethashValueStr)
    
    
    
    def RVN_difficulty_friendly(self,diff):
        #kH/s
        netDiffValue = float(diff)
        netDiffValueUnit = "H/s"
        netDiffValueStr = "" 
        
          
        if netDiffValue / UNIT_KILO  >= 1:
            netDiffValue = netDiffValue / UNIT_KILO
            netDiffValueStr = "" + str(netDiffValue) + "kH/s"
            netDiffValueUnit = "KH/s"
            
            
        netDiffValue = netDiffValue.__round__(3)
        netDiffValueStr =  str(netDiffValue) + " " +    netDiffValueUnit
        return (netDiffValue, netDiffValueUnit, netDiffValueStr)
    
    
    
    
    
    
    