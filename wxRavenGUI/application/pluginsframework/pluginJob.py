'''
Created on 27 févr. 2022

@author: slinux
'''


import threading
import logging
import wx
import time
from wxRavenGUI.application.wxcustom import *


#
#
# Plugin Job is a class for WxRaven JobManager that execute background task to improve userexperience
#



class Job(object):
    '''
    classdocs
    '''
    jobName = 'UnknownJob'
    jobId = 'UnknownJobId'
    _jobRunning = False
    _jobDone = False
    _jobProgressPercent = 0
    _jobDetailedProgress = ''
    _jobDetailedProgress_max = 0
    _jobDetailedProgress_cur = 0
    
    
    _jobResult = None
    _jobError = None
    _jobStatus = 'New'
    
    _jobSaved = False

    _run_safe = True
    _notify_at_end = True
    
    _jobResultExpire = -1
    _jobStartTime = 0
    _jobStopTime = 0
    _jobElapsedTime = 0
    
    _jobDelayBefore = 0
    _jobDelayAfter = 0
    
    
    _jobOtherJobRequirements = []
    
    
    _jobDirectCallBack = None
    _daemonize_job = True

    def __init__(self ,parentFrame, plugin=None, resultDirectCallback=None, safeMode=True, notifyAtEnd=True):
        '''
        Constructor
        '''
        self._run_safe= safeMode
        self.logger = logging.getLogger('wxRaven')
        self.parentFrame = parentFrame
        self.plugin = plugin
        self.source = 'Unknown'
        if plugin !=None:
            self.source = plugin.PLUGIN_NAME
        self.jobName = 'UnknownJob'
        self.jobId = 'UnknownJob'
        
        
        self._jobDirectCallBack = resultDirectCallback
        self._jobDetailedProgress = "No manager assigned"
        self._notify_at_end = notifyAtEnd
    
    def DoJob(self):
        
         
        
        t=threading.Thread(target=self.__DoJob_T__, args=(), daemon=self._daemonize_job)
        t.start() 
    
    
    
    
    def __waitJobRequirements__(self):
        _allDone = False
        
        while not _allDone:
            self._jobStatus='Waiting'
            _allDone = True
            for _j in self._jobOtherJobRequirements:
                if not _j._jobRunning and _j._jobDone:
                    _allDone = _allDone and True
            
            if not _allDone:
                time.sleep(5)

    def __DoJob_T__(self, evt=None):
        #self.jobId = f"{self.jobName} - {self.parentFrame.ConnexionManager.getCurrent()}"
        #self.logger.info(f'JOB : {self.jobId}')
        if self._jobRunning :
            return
        self._jobRunning = True
        self._jobStatus='Running'
        
        if len(self._jobOtherJobRequirements) > 0 :
            self.__waitJobRequirements__()
            
        
        
        
        
        self._jobStatus='Running'
        self._jobStartTime = time.time()
        
        
        
        
        #
        #Delay Before to manage spam request
        if self._jobDelayBefore > 0:
            time.sleep(self._jobDelayBefore)
        
        
        
        #
        # Process
        #
        if not self._run_safe:
            self.JobProcess()
            
        else:
            try:
                self.JobProcess()
            except Exception as e:
                self.logger.exception(f'JOB ERROR : {e}')
                self._jobError = f'JOB ERROR : {e}'
                self._jobStatus='error'
                self.setProgress(f'JOB ERROR : {e}')
        
        
        
        #
        #Delay After to manage ?
        if self._jobDelayAfter > 0 and self._jobError == None:
            time.sleep(self._jobDelayAfter)
        
        
        if self._jobError == None:     
            if not self._jobSaved:
                self.SaveResult()
            
            self._jobDone=True
            self._jobStatus='Done'
                
            self.ExecuteCallbacks()
        
        
        
        #
        #Notification if activated or error
        #
        self._jobStopTime = time.time()
        self._jobElapsedTime = float(self._jobStopTime - self._jobStartTime).__round__(2)
        
        
        
        
        if self._notify_at_end or self._jobError != None: 
            _type = 'success'
            
            _t = f"Job Done ! "
            _m = f"{self.jobName}" 
            
            if self._jobError != None:
                _t = f"{self.jobName}" 
                _m = f"{self._jobError}" 
                _type = 'error'
           
            UserSystemNotification(self.parentFrame, title=_t, message=_m, _type=_type)
        
        
        if self._jobError == None:
            self.setProgress(f"Job Complete ({self._jobElapsedTime} seconds)")
        
        
        self._jobRunning = False
        
    
    
    def addJobRequirement(self, jobObj):
        self._jobOtherJobRequirements.append(jobObj)
    
    
    def setDelays(self, before=0, after=0): 
        self._jobDelayAfter = after
        self._jobDelayBefore  = before 
        
    
    def setNotification(self, enabl=True):  
        self._notify_at_end =  enabl     
        
    def setExpiration(self, seconds=-1):  
        self._jobResultExpire =  seconds 
    
    def setMax(self,max):
        self._jobDetailedProgress_max=max
    
    def setCurrent(self, cur):
        self._jobDetailedProgress_cur = cur
        
        
    def setRange(self, cur, max): 
        self.setMax(max)
        self.setCurrent(cur)
        
    def setProgress(self, msg):
        self._jobDetailedProgress = msg
    
    def setError(self, err):
        self._jobError = err
        
    def setResult(self, res):
        self._jobResult = res
        
    def getResult(self):
        return self._jobResult
    
    def setStatus(self, newState):
        self._jobStatus = newState
        
    def getStatus(self):
        return self._jobStatus    
    
    
    def JobProcess(self):
        '''
        #User to define this
        '''
        
        pass
    
    def SaveResult(self):
        self._jobSaved = True
        '''
        #user to define this and store in plugin data through this method,
        #it can be usefull then for calling only the result and not the entire process
        '''
        pass
    
    
    def ExecuteCallbacks(self):
        '''
        #User to define this for the callback management
        # by default it will do what was done before, aka self.plugin.UpdateActiveViews
        '''
        
        try:
                
            
            if self._jobDirectCallBack != None:
                wx.CallAfter(self._jobDirectCallBack, ())
                
            else:
                wx.CallAfter(self.plugin.UpdateActiveViews, ())
            
                
        except Exception as e:
            self.logger.exception(f'JOB CALLBACK ERROR : {e}')
            #_jobError = f'JOB CALLBACK ERROR : {e}'
    