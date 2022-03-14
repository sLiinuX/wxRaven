'''
Created on 5 mars 2022

@author: slinux
'''


from wxRavenGUI.application.pluginsframework import *



class Job_RemoteJobDisabled(Job):
    '''
    classdocs
    '''


    def __init__(self, plugin, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        
        self.jobName = f"JobManager - Remote Job Disabled"
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        self.setExpiration(5)
        self._initalJobRequest = ''
        #self.addExportParam('_initalJobRequest') 
        #self.setDelays(1, 0)
        self.setNotification(False)
        #self.addNetworkCompatibility('WS-RPC')
        #self.addNetworkCompatibility('SQL')
    
    def JobProcess(self):
        
        
        _SafeGuardMessage = f"The current relay Remote Job(s) are disabled."
        
        #listStr = ''
        
        #for i in listRej:
        #    listStr = listStr+f'- {i}\n'
        
        #wx.CallAfter(UserAdvancedMessage, self.parentFrame, _SafeGuardMessage, 'warning', listStr)    
        self.setProgress(f'{_SafeGuardMessage}')
        self.setError(_SafeGuardMessage)
        
    def SaveResult(self):
        pass
        '''
        self.logger(f"Job_NotAllowedRemoteJob SaveResult _jobFromRemote {self._jobFromRemote}")
        if self._jobFromRemote == False:
            wx.CallAfter(UserAdvancedMessage, self.parentFrame, self.getResult(), 'warning') 
        '''
    
    