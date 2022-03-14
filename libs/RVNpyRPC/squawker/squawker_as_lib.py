'''
Created on 18 déc. 2021

@author: slinux
'''


"""


from .squawker_errors import *




class Squawker(object):
    '''
    classdocs
    '''
    rvn = None
    ASSETNAME = ""
    ipfs = None
    
    
    
    def __init__(self, ASSETNAME="POLITICON", RavencoinRPC=None, ipfs=None):
        '''
        Constructor
        '''
        self.ASSETNAME = ASSETNAME
        self.rvn = RavencoinRPC
        
        
        
    def find_latest_messages(self, count=50):
        
        
        from .squawker import find_latest_messages as flm
        
        return flm(self.ASSETNAME, count)
        
        
"""