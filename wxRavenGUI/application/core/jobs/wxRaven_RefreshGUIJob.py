'''
Created on 1 mars 2022

@author: slinux
'''
from wxRavenGUI.application.pluginsframework import *



class Job_RefreshGUI(Job):
    '''
    classdocs
    '''


    def __init__(self, plugin, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        
        self.jobName = f"RefreshGUI"
        self.jobId = f"{self.jobName} - {self.parentFrame.ConnexionManager.getCurrent()}"
        self.setExpiration(5)
        self.setDelays(2, 0)
        self.setNotification(False)
    
    def JobProcess(self):
        
        
        wx.CallAfter(self.parentFrame.MenusAndTool.refreshViewsListMenu, ())    
        wx.CallAfter(self.parentFrame.MenusAndTool.RefreshToolbar, ())    
        wx.CallAfter(self.parentFrame.Views.UpdateGUIManager, ())    
        self.setProgress(f'RefreshGUI complete')
        self.setResult(True)
        
    def SaveResult(self):
        pass