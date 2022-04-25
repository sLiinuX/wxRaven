'''
Created on 27 févr. 2022

@author: slinux
'''
import logging
import threading
import time
from threading import Thread, Lock

import wx
import wx.adv

from wxRavenGUI.application.pluginsframework import Job

import importlib
from wxRavenGUI.application.core.jobs.wxRaven_RemoteJob import Job_RemoteJob

from .jobs import *
from wxRavenGUI.application.wxcustom import *

class JobManager(object):
    '''
    classdocs
    '''

    _queue_list = []
    _running_list = []
    _done_list = []
    _canceled_list = []
    
    
    #_ws_queue_list = []
    
    _callBacks = []
    
    _running = False
    _stopRequest = False
    
    _max_running_job = 1
    _jobCounter = 1
    
    #DO NOT SET TO FALSE!
    _AutoRemoteJob = True
    _AllowRemoteJob = False
    
    
    _RemoteForceNetwork = None


    def __init__(self, parentframe):
        '''
        Constructor
        '''
        self.parentframe = parentframe
        self._running = False
        self._stopRequest = False
        self.logger = logging.getLogger('wxRaven')
        
        self._lock = Lock()
        
        
        
    def StartJobManager(self):
        
        t=threading.Thread(target=self.__JobManagerWatcherLoop__, args=(), daemon=True)
        t.start() 
    
    
    def StopJobManager(self, purgeJobs=False):
        self.logger.info("Job Manager : Stop Request")
        self._callBacks = []
        self._stopRequest = True
    
    
    def PurgeCompleteJob(self, jobObj=None):
        _foundsimilarInComplete = False
        _foundJob = None
        
        
        if jobObj != None:
            for d in  self._done_list.copy():
                if d.jobId == jobObj.jobId:
                    _foundsimilarInComplete = True
                    _foundJob = d
                    break
                
        else:
            self._lock.acquire()
            self._done_list = []
            self._lock.release()
            return True
        
        if _foundJob!=None:
            self._lock.acquire()
            self._done_list.remove(_foundJob)
            #self.logger.info("Job Manager : Job Purged")
            self._lock.release()
            return True
         
        
        return False
    
    def PurgeCanceledJob(self, jobObj=None):
        _foundsimilarInComplete = False
        _foundJob = None
        
        
        if jobObj != None:
            for d in  self._canceled_list.copy():
                if d.jobId == jobObj.jobId:
                    _foundsimilarInComplete = True
                    _foundJob = d
                    break
                
        else:
            self._lock.acquire()
            self._canceled_list = []
            self._lock.release()
            return True
        
        if _foundJob!=None:
            self._lock.acquire()
            self._canceled_list.remove(_foundJob)
            #self.logger.info("Job Manager : Job Purged")
            self._lock.release()
            return True
         
        
        return False
    

    
    def ToggleAutoRemoteJobs(self,forceValue=None):
        if  forceValue != None:
            self._AutoRemoteJob = forceValue
        else:
            self._AutoRemoteJob = not self._AutoRemoteJob    
        
        return self._AutoRemoteJob
        
    def RefreshSettings(self):
        self._max_running_job = self.parentframe.GetPluginSetting('General',  "max_running_jobs")
        self._AllowRemoteJob = self.parentframe.GetPluginSetting('General',  "authorize_remote_jobs")
        self._AutoRemoteJob = self.parentframe.GetPluginSetting('General',  "use_remote_jobs")
        
        remoteNetwork = self.parentframe.GetPluginSetting('Webservices','webservice_force_network')
        if remoteNetwork != None:
            if remoteNetwork != '':
                self._RemoteForceNetwork = remoteNetwork
    
    
    def GetJobFromUniqueId(self, uniqueId, lists=[]):
        _foundJob = None
        _foundsimilar = False
        
        if lists == []:
            lists = [self._queue_list.copy(), self._running_list.copy(), self._done_list.copy(),self._canceled_list.copy()] 
        
        for l in lists:
            
            for d in  l:
                if d._jobUniqueId == uniqueId:
                    _foundsimilar = True
                    _foundJob = d
                    _jobList= l
                    break
        
        return _foundsimilar,_foundJob
    
    
    def GetJobFromNumber(self, num, lists=[]):
        _foundJob = None
        _foundsimilar = False
        
        if lists == []:
            lists = [self._queue_list.copy(), self._running_list.copy(), self._done_list.copy(),self._canceled_list.copy()] 
        
        for l in lists:
            
            for d in  l:
                if d._jobNumber == num:
                    _foundsimilar = True
                    _foundJob = d
                    _jobList= l
                    break
        
        return _foundsimilar,_foundJob
    
    
    
    def GetJobs(self, lists=[]):
        _foundJob = None
        _foundsimilar = False
        
        if lists == []:
            lists = [self._queue_list.copy(), self._running_list.copy(), self._done_list.copy(),self._canceled_list.copy()] 
        
        _jlist= []
        
        for l in lists:
            
            for d in  l:
                _jlist.append(d)
        
        return _jlist
    
    
    
    
    
    def GetJobResultFromNumber(self, jobNumber):
        _found, _j  =self.GetJobFromNumber(jobNumber, lists=[self._done_list.copy()])
        if _found:
            return _found, _j.getResult()
        else:
            return _found, None
    
    
    def __searchJob__(self, jobObj):
        _foundsimilar = False
        _foundJob = None
        _jobList = None
        for p in self._queue_list.copy():
            if p.jobId == jobObj.jobId:
                
                print(f"DOUNF QUEUE = {p.jobId} == {jobObj.jobId}")
                _foundsimilar = True
                _foundJob = p
                _jobList= self._queue_list.copy()
                break
        
        for r in  self._running_list:
            if r.jobId == jobObj.jobId:
                print(f"FOUND RUNNING = {r.jobId} == {jobObj.jobId}")
                _foundJob = r
                _foundsimilar = True
                _jobList= self._running_list.copy()
                break
        
        
        for d in  self._done_list:
            if d.jobId == jobObj.jobId:
                print(f"FOUND DONE = {r.jobId} == {jobObj.jobId}")
                _foundsimilar = True
                _foundJob = d
                _jobList= self._running_list.copy()
                break
            
        return _foundJob, _jobList
    
    
    
    
    
    
    
    
    
    
    
    def __isRelayConnexion__(self):
        test= self.parentframe.getNetwork()._type=='WS-RPC'
        return test
    
    
    def __isCompatibleConnexion__(self, jobObj):
        currentMode = self.parentframe.getNetwork()._type
        _compatible = False
        if currentMode in jobObj._jobNetworkCompatibility:
            _compatible= True
        else:
            _compatible= False
        return _compatible
    
    
    def __rejectJob__(self, _rejectedJob):
        p=self.parentframe.GetPlugin('General')
        listRej = p.getData('_RejectedJobList')
        listRej.append(_rejectedJob.jobName)
        p.setData('_RejectedJobList', listRej)
    
        errorJob = Job_DisplayRejectJob(p, viewCallback=self.doNothing, safeMode=True)
        return errorJob
    
    #
    #
    #   MAIN MANAGER FOR INPUT JOB (MAINTHREAD)
    #
    #
    def SubmitNewJob(self, jobObj, _retAttr='_jobNumber', _reuseIfExist=True ,_executeCallBackIfFound=True, _allowErrorJob=True):
        
        self.logger.info(f'SubmitNewJob : {jobObj.jobId}!')
        #
        # check existing running jobs
        #
        _foundsimilarInQueue= False
        _foundsimilarInPending= False
        _foundsimilarInComplete = False
        _foundJob = None
        _jobNum = None
        
        #Lock datas
        self._lock.acquire()
        
        for p in self._queue_list.copy():
            if p.jobId == jobObj.jobId:
                
                #print(f"{p.jobId} == {jobObj.jobId}")
                _foundsimilarInQueue = True
                _foundJob = p
                break
        
        if _foundJob == None:
            for r in  self._running_list.copy():
                if r.jobId == jobObj.jobId:
                    #print(f"{r.jobId} == {jobObj.jobId}")
                    _foundsimilarInPending = True
                    _foundJob = r
                    break
        
        
        if _foundJob == None:
            for d in  self._done_list.copy():
                if d.jobId == jobObj.jobId:
                    _foundsimilarInComplete = True
                    _foundJob = d
                    break
        
        
        #
        # Check if found job is reusable
        #
        if _foundJob != None:
            if _foundJob._jobReusable == False:
                _reuseIfExist = False
        
        #
        #End search
        
        if _foundJob == None or (_foundJob!=None and not _reuseIfExist):
            
            
            _SafeGuardNoExecute = False
            _SafeGuardMessage = ''
            
            
            _jobToExecute = jobObj
            
            #
            #Safe Guard Check
            #
            if not self.__isCompatibleConnexion__(_jobToExecute):
               
                
                _SafeGuardNoExecute = True
                _SafeGuardMessage = "The requested job cannot be executed on the current connexion :"
                
                #_SafeGuardMessage = _SafeGuardMessage + "\n\nNOTE : if you are using a relay, each relay is independent and can restrict or allow certain Functionalities."
                #_SafeGuardMessage = _SafeGuardMessage + "\nContact your connexion provider or try on another connexion."
                _SafeGuardMessage = _SafeGuardMessage + f"\nCompatible(s) connexions for this job : {_jobToExecute._jobNetworkCompatibility}"
                
                errorJob = self.__rejectJob__(_jobToExecute)
                '''
                p=self.parentframe.GetPlugin('General')
                listRej = p.getData('_RejectedJobList')
                listRej.append(_jobToExecute.jobName)
                p.setData('_RejectedJobList', listRej)
                '''
                #errorJob = Job_DisplayRejectJob(p, viewCallback=self.doNothing, safeMode=True)
                #UserAdvancedMessage(self.parentframe, _SafeGuardMessage, 'warning', _jobToExecute.jobName)
                self._lock.release()
                if _allowErrorJob:
                    return self.SubmitNewJob(errorJob, _allowErrorJob=False)
                return None
            
            
            #
            # Relay Management
            #
            if self.__isRelayConnexion__() and self._AutoRemoteJob:
                
                if jobObj._JobAllowRemoteExecution == True:
                    _jobToExecute = self.CreateRemoteJob(jobObj)
            
            
            
            #
            #
            # Job Creation 
            #
            if (_foundJob!=None and not _reuseIfExist):
                self.logger.warning(f"A similar job pending/running has been found but REUSE IS DISABLED.")
            else:
                self.logger.info('SubmitNewJob > No existing Job found !')
                
            _jobToExecute.setStatus('Waiting')
            _jobToExecute._jobDetailedProgress = 'Waiting for available thread...'
                    
                    
            _jobNum = self._jobCounter
            _jobToExecute.__setJobNumber__(_jobNum)
            self._jobCounter = self._jobCounter +1
                    
            self._queue_list.append(_jobToExecute)
                
                
            _jobNum = getattr(_jobToExecute, _retAttr)     
        
        else :
            self.logger.info('SubmitNewJob > Existing Job found !')
            
            if _foundsimilarInQueue or _foundsimilarInPending:
                _jobNum = getattr(_foundJob, _retAttr)   
                self.logger.info(f"A similar job pending/running has been found : {_jobNum}.")
        
            elif _foundsimilarInComplete:
                _jobNum = getattr(_foundJob, _retAttr)   
                self.logger.info(f"A similar job COMPLETE has been found : {_jobNum}.")
                if _executeCallBackIfFound:
                    _foundJob.SaveResult()
                    jobObj.ExecuteCallbacks()
                    self.logger.info("job result reused.")
                
            else:
                _jobNum = getattr(_foundJob, _retAttr)   
                self.logger.info(f"A similar job pending/running has been found : {_jobNum}.")
        
        
        #Unlock all
        self._lock.release()
        
        
            
        return _jobNum
    
    def __doCallbacks__(self):
        for _c in self._callBacks:
            try:
                wx.CallAfter(_c)
                
            except Exception as e:
                pass
    
    def __JobManagerWatcherLoop__(self):
        
        
        
        if self._running:
            self.logger.warning('JobManager Already running')
            return
        
        self._running = True
        
        
        while self.parentframe._isReady == False:
            time.sleep(2)
            
        self.logger.warning('JobManager Starting with delay : 2 sec')   
        time.sleep(1)    
            
        
        while not self._stopRequest:
            
            _changedNew=False
            _changedRun=False
            _changedComplete = False
            
            if self._stopRequest:
                break
            
            #
            # watch for new jobs
            #
            if len(self._queue_list) > 0:
                _changedNew = self.TreatNewJobs()
            
            
            if self._stopRequest:
                break
            
            #
            # report for current jobs
            #
            if len(self._running_list) > 0:
                self.TreatRunningJobs()
                _changedRun = True
            
            
            
            if self._stopRequest:
                break
            
            #
            # clean old jobs
            #
            
            
            _changedComplete = self.TreatCompleteJobs()
            
            if self._stopRequest:
                break
            
            #
            # Callbacks if changed
            #
            _changed = _changedNew or _changedRun or _changedComplete
            #callbacks will be managed in the view directly
            
            if _changed:
                self.__doCallbacks__()
                #self.UserNotification()
                
            if self._stopRequest:
                break
            
            time.sleep(2)
        
        
        self.logger.info("Job Manager : Stopped.")
        self._running = False
        self._stopRequest = False   
        
        
        
        
    def TreatCompleteJobs(self):
        _changed = False
        nowTime = time.time()
        _toPurgeResult = []
        if len(self._done_list)>0:
            
            for d in self._done_list.copy():
                
                #
                #look for expired/expirable results
                #
                if d._jobResultExpire > -1:
                    
                    _jobExpireTime = d._jobResultExpire
                    _jobFinnishTime = d._jobStopTime
                    
                    
                    _elapsedSince = nowTime - _jobFinnishTime
                    if _elapsedSince > _jobExpireTime:
                        _toPurgeResult.append(d)
                        
                    
                    
            if  len(_toPurgeResult) > 0:       
                for d in _toPurgeResult:
                    self.PurgeCompleteJob(d)
                    _changed = True
                    
                    
        return _changed
    
    
    def TreatRunningJobs(self):  
        self.logger.info("Job Manager : TreatRunningJobs.")  
        _tomoveInDone = []
        _tomoveInStooped = []
        _changed = False
        if len(self._running_list)>0:
            
            for j in self._running_list.copy():
                
                
                #self.logger.info("Job Manager : TreatRunningJobs.")
                
                if j._jobDone:
                    _tomoveInDone.append(j)
                    #self.logger.info("Job Manager : found job done.")  
                    
                elif j._jobError != None:
                    _tomoveInStooped.append(j)
                    #self.logger.info("Job Manager : found job error.")  
                    
                else:
                    #The job is stillRunning, checking job Thread 
                    
                    
                    j.__refreshProgessDatas__()
                    if j._jobMaxRunningTime > 0 and (j._jobElapsedTime > j._jobMaxRunningTime):
                        
                        
                        self.logger.error(f"Job Manager : {j.jobName} as exceeded the maximum running time ({j._jobMaxRunningTime} seconds), killing thread...")  
                        _killReason = f"Job Manager : {j.jobName} as exceeded the maximum running time ({j._jobMaxRunningTime} seconds), killing thread..."
                        j.__KillJob__(_killReason)
                        
                        self.parentframe.Log(f'Job Manager : {j.jobName} as exceeded the maximum running time allowed ({j._jobMaxRunningTime} seconds)' ,  type="error")
                        #_jobThread= j.jobProcessInstance
                        #_jobThread.__KillJob__()
                    
                    
                    
        
        self._lock.acquire()
        
        for i in _tomoveInDone:
            #self.logger.info("Job Manager : _tomoveInDone.")  
            i.setStatus('Done')
            #i._jobDetailedProgress = 'waiting for available thread...'
            self._done_list.append(i)
            self._running_list.remove(i)
            
            _changed = True
            
        for i in _tomoveInStooped:
            i.setStatus('Error')
            #self.logger.info("Job Manager : _tomoveInStooped.")  
            #i._jobDetailedProgress = 'waiting for available thread...'
            self._canceled_list.append(i)
            self._running_list.remove(i)
            
            _changed = True    
        
        
        self._lock.release()
        
        #self.logger.info("Job Manager : TreatRunningJobs done.")      
        return _changed
        
        
    def TreatNewJobs(self):
        _changed = False
        if not len(self._running_list) > self._max_running_job:
            
            
            self._lock.acquire()
            try:
                
                
            
                if len(self._queue_list) > 0:
                    
                    #self.logger.info(f"TreatNewJobs : Taking first in list {len(self._queue_list)}.")   
                    
                    njob = self._queue_list[0]
                    
                    
                    #njob.__setNumber__(str(self._jobCounter).zfill(4))
                    
                    #
                    #self.logger.info(f"TreatNewJobs : Adding in running.")   
                    
                    self._running_list.append(njob)
                    
                    #self.logger.info(f"TreatNewJobs : removing from queue.")   
                    self._queue_list.remove(njob)
                    
                    #self.logger.info(f"TreatNewJobs : starting.")  
                    njob.DoJob()
                    #self.logger.info(f"TreatNewJobs : started.")  
                    _changed = True
                    #if len(self._running_list) >= self._max_running_job:
                    #    break
            
                
                
                
            except Exception as e:
                self.logger.error(f"Error in TreatNewJobs : {e}")
                
                
        
        
        self._lock.release()
        return _changed    
    
    
    
    
    
    
    
    #
    # Job Discovery
    #
    def discoverAvailableJobs(self):
        pList= self.parentframe.Plugins.getAllAvailablePlugins()
        
        JobList = []
        for plugin in  pList:
            
            pJobs = self.parentframe.GetPlugin(plugin).getAvailableJobs()
            
            for _jClass in pJobs:
                strName = str(_jClass.__module__) + "."+ str(_jClass.__name__)
                JobList.append(strName)
        
        
        return JobList
    
    
    #
    # Job Creator Part
    #
    
    
    def doNothing(self, evnt=None):
        pass
    
    
    #
    #Create a job object from names (alternative of instanciating it)
    #
    def CreateJob(self,_pluginName, _class , _module , _jobparams={}, _localJob=True):
        self.logger.info(f"CreateJob p={_pluginName}  c={_class}  m={_module}")
        
        if _pluginName == None or _class == None or _module==None:
            self.parentframe.Log(message="Invalid Job Received" , source="CreateJob", timestamp=None, type="error")
            return None
        
        JobModule = importlib.import_module(_module)
        JobClass = getattr(JobModule, _class)
        
        Plugin = self.parentframe.GetPlugin(_pluginName)
        
        
        newJobInstance = JobClass( plugin=Plugin, viewCallback=self.doNothing)
        newJobInstance.RestoreParameters(_jobparams)
        
        if not _localJob:
            newJobInstance.setFromRemote(True)
            
            if self._RemoteForceNetwork != None:
                self.logger.info(f"CreateJob : Forced on network : {self._RemoteForceNetwork}")
                newJobInstance.setNetwork(self._RemoteForceNetwork)
                
                
            #
            # To add the webservices jobs settings
            #    
            
        '''
        for _key in _jobparams:
            newJobInstance.__setattr__(_key, _jobparams[_key])
        '''    
        return newJobInstance
    
    #
    # Create the remote job equivalence class of a job
    #
    def CreateRemoteJob(self, jobObj:Job):
        rpc_con = self.parentframe.getNetwork()
        Plugin = self.parentframe.GetPlugin('General')
        
        self.logger.info(f"CreateRemoteJob ")
        newLocalJob = None
        if rpc_con._type!='WS-RPC':
            self.logger.error(f'Wrong connexion type {rpc_con._type} for Remote Job')
        else:
            newLocalJob = Job_RemoteJob(Plugin, jobObj)
        
        return newLocalJob   
    
    
    #
    # Submit a job SPECIFICALLY from remote, to contains the safeguards and return a different key mechanism.
    #
    def NewJobFromRemote(self, jobObj:Job, _admin=False):
        #print('NewJobFromRemote')
        self.logger.info(f"NewJobFromRemote ")
        if not self._AllowRemoteJob:
            Plugin = self.parentframe.GetPlugin('General')
            self.logger.warning(f"Settings does not allow Remote Job. Generating an error job.")
            jobObj = Job_RemoteJobDisabled(Plugin) 
            jobObj.setFromRemote(True)
        
        return self.SubmitNewJob(jobObj,_retAttr='_jobUniqueId', _reuseIfExist=True ,_executeCallBackIfFound=False)
        #module = importlib.import_module(module_path)
        #plugin_init_class = getattr(plugin_module, 'wxRavenPlugin')
    
            