'''
Created on 4 mars 2022

@author: slinux
'''

from wxRavenGUI.application.pluginsframework import *



class Job_DisplayRejectJob(Job):
    '''
    classdocs
    '''


    def __init__(self, plugin, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        
        self.jobName = f"JobManager - Rejected Job(s)"
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        self.setExpiration(5)
        self.setDelays(1, 0)
        self.setNotification(False)
        self.addNetworkCompatibility('WS-RPC')
        self.addNetworkCompatibility('SQL')
    
    def JobProcess(self):
        
        listRej = self.plugin.getData('_RejectedJobList').copy()
        self.plugin.setData('_RejectedJobList',[])
        _SafeGuardMessage = "The requested job(s) cannot be executed on the current connexion."
        
        listStr = ''
        
        for i in listRej:
            listStr = listStr+f'- {i}\n'
        
        wx.CallAfter(UserAdvancedMessage, self.parentFrame, _SafeGuardMessage, 'warning', listStr)    
        self.setProgress(f'Task complete')
        self.setResult(True)
        
    def SaveResult(self):
        pass