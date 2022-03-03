'''
Created on 27 févr. 2022

@author: slinux
'''
import logging
import threading
import time


import wx
import wx.adv

class JobManager(object):
    '''
    classdocs
    '''

    _queue_list = []
    _running_list = []
    _done_list = []
    _canceled_list = []
    
    
    _callBacks = []
    
    _running = False
    _stopRequest = False
    
    _max_running_job = 1


    def __init__(self, parentframe):
        '''
        Constructor
        '''
        self.parentframe = parentframe
        self._running = False
        self._stopRequest = False
        self.logger = logging.getLogger('wxRaven')
        
        
        
    def StartJobManager(self):
        
        t=threading.Thread(target=self.__JobManagerWatcherLoop__, args=(), daemon=True)
        t.start() 
    
    
    def StopJobManager(self, purgeJobs=False):
        self.logger.info("Job Manager : Stop Request")
        self._callBacks = []
        self._stopRequest = True
    
    
    def PurgeCompleteJob(self, jobObj):
        _foundsimilarInComplete = False
        _foundJob = None
        
        for d in  self._done_list:
            if d.jobId == jobObj.jobId:
                _foundsimilarInComplete = True
                _foundJob = d
                break
        
        if _foundJob!=None:
            self._done_list.remove(_foundJob)
            self.logger.info("Job Manager : Job Purged")
            return True
        else:
            return False
        
    def RefreshSettings(self):
        self._max_running_job = self.parentframe.GetPluginSetting('General',  "max_running_jobs")
    
    
    
    
    def __searchJob__(self, jobObj):
        _foundsimilar = False
        _foundJob = None
        _jobList = None
        for p in self._queue_list:
            if p.jobId == jobObj.jobId:
                
                print(f"{p.jobId} == {jobObj.jobId}")
                _foundsimilar = True
                _foundJob = p
                _jobList= self._queue_list
                break
        
        for r in  self._running_list:
            if r.jobId == jobObj.jobId:
                print(f"{r.jobId} == {jobObj.jobId}")
                _foundJob = r
                _foundsimilar = True
                _jobList= self._running_list
                break
        
        
        for d in  self._done_list:
            if d.jobId == jobObj.jobId:
                _foundsimilar = True
                _foundJob = d
                _jobList= self._running_list
                break
            
        return _foundJob, _jobList
    
    
    
    
    def SubmitNewJob(self, jobObj):
        #
        # check existing running jobs
        #
        
        _foundsimilarInPending= False
        _foundsimilarInComplete = False
        _foundJob = None
        
        for p in self._queue_list:
            if p.jobId == jobObj.jobId:
                
                print(f"{p.jobId} == {jobObj.jobId}")
                _foundsimilarInPending = True
                break
        
        if not _foundsimilarInPending:
            for r in  self._running_list:
                if r.jobId == jobObj.jobId:
                    print(f"{r.jobId} == {jobObj.jobId}")
                    _foundsimilarInPending = True
                    break
        
        
        if not _foundsimilarInPending:
            for d in  self._done_list:
                if d.jobId == jobObj.jobId:
                    _foundsimilarInComplete = True
                    _foundJob = d
                    break
        
        
        
        if not _foundsimilarInPending:
            
            
            if not _foundsimilarInComplete:
                jobObj.setStatus('Waiting')
                jobObj._jobDetailedProgress = 'waiting for available thread...'
                self._queue_list.append(jobObj)
            else:
                #reuse job ?
                try:
                    _foundJob.SaveResult()
                    jobObj.ExecuteCallbacks()
                    self.logger.info("job result reused.")
                except Exception as e:
                    self.logger.error(f"Error in reuse job : {e}")
            
            
        else:
            self.logger.error("A similar job pending/running has been found.")
    
    def __doCallbacks__(self):
        for _c in self._callBacks:
            try:
                wx.CallAfter(_c)
                
            except Exception as e:
                pass
    
    def __JobManagerWatcherLoop__(self):
        
        while self.parentframe._isReady == False:
            time.sleep(2)
        
        if self._running:
            self.logger.warning('JobManager Already running')
            return
        
        self._running = True
        
        
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
            
            time.sleep(1)
        
        
        self.logger.info("Job Manager : Stopped.")
        self._running = False
        self._stopRequest = False   
        
        
        
        
    def TreatCompleteJobs(self):
        _changed = False
        nowTime = time.time()
        _toPurgeResult = []
        if len(self._done_list)>0:
            
            for d in self._done_list:
                
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
        _tomoveInDone = []
        _tomoveInStooped = []
        _changed = False
        if len(self._running_list)>0:
            
            for j in self._running_list:
                
                if j._jobDone:
                    _tomoveInDone.append(j)
                    
                elif j._jobError != None:
                    _tomoveInStooped.append(j)
                    
                else:
                    pass
        
        
        for i in _tomoveInDone:
            i.setStatus('Done')
            #i._jobDetailedProgress = 'waiting for available thread...'
            self._running_list.remove(i)
            self._done_list.append(i)
            _changed = True
            
        for i in _tomoveInStooped:
            #i.setStatus('done')
            #i._jobDetailedProgress = 'waiting for available thread...'
            self._running_list.remove(i)
            self._canceled_list.append(i)
            _changed = True    
        
            
        return _changed
        
        
    def TreatNewJobs(self):
        _changed = False
        if not len(self._running_list) > self._max_running_job:
            
            while len(self._queue_list) > 0:
                
                
                njob = self._queue_list[0]
                self._queue_list.remove(njob)
                njob.DoJob()
                self._running_list.append(njob)
                _changed = True
                if len(self._running_list) >= self._max_running_job:
                    break
        
        
        
        return _changed    
    
    
    
    
    
    
    
    
    
            