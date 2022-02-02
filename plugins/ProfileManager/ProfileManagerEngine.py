'''
Created on 30 janv. 2022

@author: slinux
'''
import os
import pickle
import logging
import shutil



class wxRavenProfileEngine(object):
    '''
    classdocs
    '''

    profile_list = {}
    application_root = ''
    profile_cache_file = ''
    profile_cache_default_name = 'profiles.p'
    
    default_profile_path = ''

    def __init__(self,  ApplicationRoot='', profileFileCache=None):
        '''
        Constructor
        '''
        self.logger = logging.getLogger()
        self.application_root = ApplicationRoot
        
        if ApplicationRoot == '':
            self.application_root = os.getcwd() + '/'
        
        self.default_profile_path = self.application_root + 'plugins/ProfileManager/default_profile/'
        
        if profileFileCache == None:
            self.profile_cache_file = self.application_root + self.profile_cache_default_name
        
        
        else:
            self.profile_cache_file =  profileFileCache
            
            
        if self.__LoadProfiles__():
            self.__verifyList__()
        
        if len(self.profile_list)==0:
            self.profile_list = {'localuser':self.application_root}
            
            
            
    
    
    def CheckProfilePath(self, path, register=True):
        
        dirname = os.path.basename(path)
        
        
        _valid = False
        if os.path.isdir(path+'/userdata'):
            if os.path.isdir(path+'/config'):
                _valid = True
                if register:
                    self.profile_list[dirname] = path
                    self.__saveProfiles__()
                
        return _valid
            
    
    def CreateProfileInPath(self, path, profilename):
        try:
            shutil.copytree(self.default_profile_path, path + '/' + profilename )
            self.profile_list[profilename] = path + '/' + profilename
            self.__saveProfiles__()
            return True
        except Exception as e:
            self.logger.error(e) 
            return False
    
    def __saveProfiles__(self):
        try:
            
            pickle.dump( self.profile_list, open(self.profile_cache_file, "wb" ) )
        except Exception as e:
            self.logger.error(e) 
    
    def __LoadProfiles__(self):
        result = {'localuser':self.application_root}
        loaded=False
        self.profile_list = result
        try:
            result = pickle.load( open(self.profile_cache_file, "rb" ) )
            self.profile_list = result
            loaded = True
        except Exception as e:
            self.logger.error(e) 
        
        return loaded        
    
    
    def __verifyList__(self):
        
        _invalids = []
        for _p in self.profile_list:
            _isV = self.CheckProfilePath(self.profile_list[_p], register=False)
            if not _isV:
                _invalids.append(_p)
                
                
        for _i in _invalids:
            self.profile_list.pop(_i)
    