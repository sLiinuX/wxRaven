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
    
    def __init__(self,connexion):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.RPCconnexion = connexion
        
        
    def GetNetworkInfos(self):
        #
        #{'blocks': 2102974, 'currentblockweight': 0, 'currentblocktx': 0, 'difficulty': 83255.50545680113, 
        # 'networkhashps': 5722312398548.8, 'hashespersec': 0, 'pooledtx': 6, 'chain': 'main', 'warnings': ''}
        
        _netInfos = self.RPCconnexion.getmininginfo()['result']
        
        _hashrate = _netInfos['networkhashps']
        _hashrate = self.RVN_hashrate_friendly(_hashrate)
        
        _difficulty = _netInfos['difficulty']
        _difficulty = self.RVN_hashrate_friendly(_difficulty)
        
        _netInfos['difficulty'] = _difficulty
        _netInfos['networkhashps'] = _hashrate
        
        
        return _netInfos
        
        
        
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
    
    
    
    
    
    
    