'''
Created on 8 mars 2022

@author: slinux
'''
'''
Created on 8 mars 2022

@author: slinux
'''
from wxRavenGUI.application.pluginsframework import *



class Job_TemplateJob(Job):
    '''
    classdocs
    '''


    def __init__(self, plugin, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        
        self.jobName = f"JobManager - New Private WS Token"
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        #self.setReusable(False)
        #self.setExpiration(5)
        #self._initalJobRequest = ''
        #self.addExportParam('_initalJobRequest') 
        #self.setDelays(1, 0)
        #self.setNotification(False)
        #self.addNetworkCompatibility('WS-RPC')
        #self.addNetworkCompatibility('SQL')
        
        
    def JobProcess(self):
        '''
        Process here without interacting with HMI outside of MainThreadCall
        '''
        pass
    
    
    
    
    def SaveResult(self):
        pass
    
    
    
    
    
    