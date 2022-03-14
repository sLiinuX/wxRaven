'''
Created on 5 mars 2022

@author: slinux
'''


from wxRavenGUI.application.pluginsframework import *



class Job_NotAllowedRemoteJob(Job):
    '''
    classdocs
    '''


    def __init__(self, plugin, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        
        self.jobName = f"JobManager - Not Allowed Job(s)"
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        self.setExpiration(5)
        self._initalJobRequest = ''
        self.addExportParam('_initalJobRequest') 
        #self.setDelays(1, 0)
        self.setNotification(False)
        #self.setAllowRemoteExecution(True)
        #self.setReusable(False)
        #self.addNetworkCompatibility('WS-RPC')
        #self.addNetworkCompatibility('SQL')
    
    def JobProcess(self):
        
        
        _SafeGuardMessage = f"The requested job(s) is not allowed on the remote relay : {self._initalJobRequest}"
        
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





#
#
# Variant job for error as experimental
# Experiment : the setResult function as a diferent behaviour in Remote or from client.
# This cannot work as the client call another job, as result the callback code is different
#




class Job_NotAllowedRemoteJobAlternate(Job):
    '''
    classdocs
    '''


    def __init__(self, plugin, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        
        self.jobName = f"JobManager - Not Allowed Job(s)"
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        self.setExpiration(5)
        self._initalJobRequest = ''
        #self.addExportParam('_initalJobRequest') 
        #self.setDelays(1, 0)
        self.setNotification(False)
        #self.setAllowRemoteExecution(True)
        #self.setReusable(False)
        #self.addNetworkCompatibility('WS-RPC')
        #self.addNetworkCompatibility('SQL')
    
    def JobProcess(self):
        
        
        _SafeGuardMessage = f"The requested job(s) is not allowed on the remote relay : {self._initalJobRequest}"
        
        #listStr = ''
        
        #for i in listRej:
        #    listStr = listStr+f'- {i}\n'
        
        #wx.CallAfter(UserAdvancedMessage, self.parentFrame, _SafeGuardMessage, 'warning', listStr)    
        self.setProgress(f'{_SafeGuardMessage}')
        self.setResult(_SafeGuardMessage)
        
    def SaveResult(self):
        if self._jobFromRemote :
            pass
        else:
            UserWarning(self.parentFrame, self.getResult())
        '''
        self.logger(f"Job_NotAllowedRemoteJob SaveResult _jobFromRemote {self._jobFromRemote}")
        if self._jobFromRemote == False:
            wx.CallAfter(UserAdvancedMessage, self.parentFrame, self.getResult(), 'warning') 
        '''
        
    