'''
Created on 27 févr. 2022

@author: slinux
'''


import threading
import logging
import wx
import time
from wxRavenGUI.application.wxcustom import *
import secrets
import math
from multiprocessing import Process
from threading import Thread, Lock
import ctypes
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
    _jobNetwork = None
    #_jobSize = 0
    
    
    _jobSaved = False

    _run_safe = True
    _notify_at_end = True
    
    _jobResultExpire = -1
    _jobStartTime = 0
    _jobStopTime = 0
    _jobElapsedTime = 0
    _jobMaxRunningTime = 1200 #20Minutes for the standard job 
    
    _jobDelayBefore = 0
    _jobDelayAfter = 0
    
    _jobNumber = 0
    
    _jobOtherJobRequirements = []
    
    
    _jobDirectCallBack = None
    _daemonize_job = True
    
    _export_params_list= []
    _jobUniqueId = None
    _JobAllowRemoteExecution = False
    
    _jobNetworkCompatibility = ['RPC']
    _jobReusable = True
    _jobFromRemote = False
    
    
    _jobTxStandbyDescription = None
    _jobPaymentStandby = None
    _jobPaymentAmount = None
    _jobTxStandby = None
    _jobPaymentStatus = None
    
    
    _useMultiProcess = False


    def __init__(self ,parentFrame, plugin=None, viewCallback=None, safeMode=True, notifyAtEnd=True):
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
        
        
        
        _newToken = secrets.token_urlsafe(16)
        self._jobUniqueId = _newToken
        self._jobNetwork = None
        self._jobDirectCallBack = viewCallback
        self._jobDetailedProgress = "No manager assigned"
        
        self._notify_at_end = notifyAtEnd
        
        self._export_params_list=[]
        self.addExportParam('jobName')
        
        self._jobNetworkCompatibility = ['RPC']
    
        self.jobProcessInstance=None
        self._lock = Lock()
    
    #
    # Jsonify for Import Export through RPC
    #
    
    def ExportRemoteJobResultJson(self):
        return self._jobResult
    
    def ExportRemoteJobStatusJson(self, _withResult=False):
        
        self.__refreshProgessDatas__()
        
        _jsonData = {
            'jobName':self.jobName,
            '_jobStatus':self._jobStatus,
            '_jobRunning':self._jobRunning,
            '_jobDone':self._jobDone,
            '_jobMaxRunningTime':self._jobMaxRunningTime,
            
            '_jobProgressPercent':self._jobProgressPercent,
            '_jobDetailedProgress':self._jobDetailedProgress,
            '_jobDetailedProgress_max':self._jobDetailedProgress_max,
            '_jobDetailedProgress_cur':self._jobDetailedProgress_cur,
            
            
            '_jobStartTime': self._jobStartTime,
            '_jobElapsedTime': self._jobElapsedTime,
            '_jobStopTime':self._jobStopTime,
            
            '_jobTxStandby': self._jobTxStandby,
            '_jobPaymentStandby': self._jobPaymentStandby,
            '_jobTxStandbyDescription': self._jobTxStandbyDescription,
            '_jobPaymentAmount': self._jobPaymentAmount,
            '_jobPaymentStatus': self._jobPaymentStatus,
            
            
            

            }
        
        if  self._jobError == None:
            _jsonData['_jobError'] = None
        else:
            _jsonData['_jobError'] = str(self._jobError)
        
        if _withResult:
            _jsonData['_jobResult'] = self._jobResult
        else:
            _jsonData['_jobResult'] = None
        
        
        return _jsonData
    
    
    
    
    def ExportRemoteParametersJson(self):
        _jsonData = {}
        for _key in self._export_params_list:
            try:
                self.logger.info(f'{self.jobName} : exporting param {_key} ')
                _jsonData[_key] = getattr(self, _key)
            except Exception as e:
                self.logger.error(f'Unable to export {_key} in {self.jobName} : {e} ')
        
        return _jsonData    
    
    
    
    
    
    
    def RestoreParameters(self,_jsonData ):
        
        #do not allow this setting to change
        _sever_exceptions = ['_jobNetwork']
        
        for _k in _jsonData:
            
            if _k in _sever_exceptions:
                self.logger.warning(f'Invalid or Not authorized Job parameter : {_k}')
                continue
            
            self.logger.info(f'setting param {_k} ')
            try:
                setattr(self, _k, _jsonData[_k])
    
            except Exception as e:
                self.logger.error(f'Unable to RestoreParameters {_k} ')
        
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
                
        return True
        
    
    #
    #
    #
    # Jobs CORE
    #
    #
    #
    
    def DoJob(self):
        
         
        
        t=threading.Thread(target=self.__DoJob_T__, args=(), daemon=self._daemonize_job)
        t.start() 
        
        self.jobProcessInstance = t
    
    
    
    
    
    def __refreshProgessDatas__(self):
        self._lock.acquire()
        if self._jobRunning:
            try:
                self._jobElapsedTime = float(time.time() - self._jobStartTime).__round__(2)
            except Exception as e:
                pass  
        
        '''
        if self._jobResult != None:
            self._jobSize = self.__convert_size__(sys.getsizeof(str(self._jobResult)))
        '''    
    
        try:
            _max = self._jobDetailedProgress_max
            _cur = self._jobDetailedProgress_cur
            self._jobProgressPercent = float(( _cur/_max)*100).__round__(2)
        except Exception as e:
            pass  
        
        self._lock.release()  
            
    
    def __waitJobRequirements__(self):
        _allDone = False
        self.setProgress(f'Waiting Requirement Jobs : {self._jobOtherJobRequirements}')
        while not _allDone:
            self._jobStatus='Waiting'
            
            _allDone = True
            for _jNum in self._jobOtherJobRequirements:
                
                _j = _jNum
                if not _j._jobRunning and _j._jobDone:
                    _allDone = _allDone and True
            
            if not _allDone:
                time.sleep(5)

    def __DoJob_T__(self, evt=None):
        #self.jobId = f"{self.jobName} - {self.getNetworkName()}"
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
                
                _jobRunningTimeout = self._jobMaxRunningTime
                
                
                    
                    #self.setProgress(f'Start Job in same thread')
                self.logger.info(f'{self.jobName} started in the same thread.' )
                self.JobProcess()
                '''    
                else:
                    self.logger.error(f'MULTIPROCESSING NOT IMPLEMENTED' )
                    
                    self.logger.info(f'{self.jobName} started in a new process for timeout management, no progress report available.' )
                    
                    jobProcessInstance = Process(target=self.JobProcess, name=f'JobProcess : {self.jobName}')
                    jobProcessInstance.start()
                    self.jobProcessInstance = jobProcessInstance
                    
                    self.setProgress(f'Process Running...')
                    
                    jobProcessInstance.join(timeout=_jobRunningTimeout)
                    if jobProcessInstance.exitcode != 0:
                        
                        jobProcessInstance.terminate()
                        
                        self.logger.error(f'JOB ERROR : Job Running Time exceeded')
                        self._jobError = f'JOB ERROR : Job Running Time exceeded'
                        self._jobStatus='error'
                        self.setProgress(f'JOB ERROR : Job Running Time exceeded')
                        #raise('JOB ERROR : Job Running Time exceeded')
                       
                '''
                
                
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
           
            #UserSystemNotification(self.parentFrame, title=_t, message=_m, _type=_type)
            wx.CallAfter(UserSystemNotification,self.parentFrame, title=_t, message=_m, _type=_type )
        
        if self._jobError == None:
            self.setProgress(f"Job Complete ({self._jobElapsedTime} seconds)")
        
        
        self._jobRunning = False
    
    
    
    def __RemoteProtection__(self):
        if self._jobFromRemote:
            _SafeGuardMessage = f"The requested job(s) is not allowed on the remote relay : {self._initalJobRequest}"  
            self.setProgress(f'{_SafeGuardMessage}')
            self.setError(_SafeGuardMessage)
            
        return self._jobFromRemote
    
    
    def __GetThreadId__(self):
        if self.jobProcessInstance != None:
            # returns id of the respective thread
            if hasattr(self.jobProcessInstance, '_thread_id'):
                return self.jobProcessInstance._thread_id
            for id, thread in threading._active.items():
                if thread is self.jobProcessInstance:
                    return id
    
    
    def __KillJob__(self, reason="Job Killed (no reason)."):
        if self.jobProcessInstance != None:
            #self.jobProcessInstance.terminate()
            self._lock.acquire()
            #self.jobProcessInstance._set_tstate_lock()
            #self.jobProcessInstance._stop()
            self._jobStatus='Error'
            self.setProgress(f'{reason}')
            self.setError(f'{reason}')
            #f"Job Manager : {j.jobName} as exceeded the maximum running time ({j._jobMaxRunningTime} seconds), killing thread..."
            #self.setProgress(f'Running Time exceeded ({self._jobMaxRunningTime} seconds), Job aborded.')
            thread_id = self.__GetThreadId__()
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                  ctypes.py_object(SystemExit))
            if res > 1:
                ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
                #print('Exception raise failure')
            
            self._jobRunning = False
            self._lock.release()
            return True
        return False
            
    
    def __MainThreadCall__(self, function, *args):
        try:
            wx.CallAfter(function, *args)
        except Exception as e:
            self.logger.exception(f'JOB ERROR __MainThreadCall__ : {e}')
    
    
    def __convert_size__(self,size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])  
    
    """
     '_jobTxStandby': self._jobTxStandby,
            '_jobPaymentStandby': self._jobPaymentStandby,
            '_jobTxStandbyDescription': self._jobTxStandbyDescription,
    """
    def setPaymentStandby(self, PaymentDatas, PaymentDescription, PaymentAmount='1 RVN', PaymentTx=None, PaymentStatus=''):
        self._jobTxStandby = PaymentTx
        self._jobPaymentStandby = PaymentDatas
        self._jobTxStandbyDescription = PaymentDescription
        self._jobPaymentAmount = PaymentAmount
        self._jobPaymentStatus = PaymentStatus
        
    def setPaymentDone(self, PaymentTxId=None):
        self._jobTxStandby = PaymentTxId
        self._jobPaymentStandby = '-'
        #self._jobTxStandbyDescription = PaymentDescription
        self._jobPaymentAmount = '0 RVN'
        self._jobPaymentStatus = 'Transaction Complete'
    
    def setReusable(self, Reusable=True):
        self._jobReusable = Reusable
    
    def removeNetworkCompatibility(self, val):
        if self._jobNetworkCompatibility.__contains__(val):
            self._jobNetworkCompatibility.remove(val)
        
        
    def addNetworkCompatibility(self, val):
        self._jobNetworkCompatibility.append(val)
        
    def setAllowRemoteExecution(self, val):
        self.addNetworkCompatibility('WS-RPC')
        self._JobAllowRemoteExecution = val
    
    def __setJobNumber__(self, jobNum):
        self._jobNumber = jobNum
    
    def addJobRequirement(self, jobObj):
        self._jobOtherJobRequirements.append(jobObj)
    
    def setMaxRunningTime(self, seconds):
        self._jobMaxRunningTime = seconds
    
    
    def __checkRunningTimeout__(self):
        _timeout=False
        if self._jobMaxRunningTime > 0:
            self.__refreshProgessDatas__()
            if self._jobElapsedTime > self._jobMaxRunningTime :
                _timeout=True
                
        return _timeout
    
    #
    # Special function to handle network on tasks 
    #    
    def getNetworkName(self):
        _returnNetwork = self._jobNetwork
        if self._jobNetwork == None:
            _returnNetwork = self.parentFrame.getNetworkName()
        return self._jobNetwork
    
    
    
    def setNetwork(self, val=None):
        self._jobNetwork = val
        self.jobId = f"{self.jobName} - {self._jobNetwork}"
    
    
    
    def getNetworkRPC(self):
        return self.parentFrame.getNetwork(self.getNetworkName())
    
    def getNetworkRavencoin(self):
        return self.parentFrame.getRavencoin(self.getNetworkName())
    
    
    
    
    
    def setFromRemote(self, val):
        self._jobFromRemote = True
    
    def setDelays(self, before=0, after=0): 
        self._jobDelayAfter = after
        self._jobDelayBefore  = before 
        
    
    def addExportParam(self, paramname):
        self._export_params_list.append(paramname)
    
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
    
    def getResultRPCStyle(self):
        _errRpc = None
        _resultRpc = self._jobResult
        if self._jobError != None:
            _errRpc = {'code':-1, 'message': self._jobError}
        return {'result':_resultRpc, 'error':_errRpc}
        
    
    def getUniqueKey(self):
        return self._jobUniqueId
    
    def setStatus(self, newState):
        self._jobStatus = newState
        
    def getStatus(self):
        return self._jobStatus    
    
    
    def getJobFriendlyName(self):
        _prefix = ''
        if self._jobFromRemote:
            _prefix = 'R'
            
        _jobName = f'[{_prefix}'+str(self._jobNumber).zfill(4)+'] ' + self.jobName
        return _jobName
    
    
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
    