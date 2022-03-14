'''
Created on 3 mars 2022

@author: slinux
'''

from wxRavenGUI.application.pluginsframework import *



class Job_RemoteJob(Job):
    '''
    classdocs
    '''


    def __init__(self,plugin, jobObj:Job):
        '''
        Constructor
        '''
        
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback=jobObj._jobDirectCallBack, safeMode=True)
        self._localJob=jobObj
        self.jobName = f"[Remote Job] - {jobObj.jobName}"
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        self.addNetworkCompatibility('WS-RPC')
        self.addNetworkCompatibility('SQL')
    
    def JobProcess(self):
        
        
        rpc_con = self.parentFrame.getNetwork()
        
        if rpc_con._type!='WS-RPC':
            self.setError(f"Error : {rpc_con._type} Is not compatible for RemoteJob")
            return
        
        _allParams = {}
        try:
            _allParams = self._localJob.ExportRemoteParametersJson()
        except Exception as e:
            self.logger.error(f'ERROR IN PARAM :  {e}')
        self.logger.info(f'Job _allParams :  {_allParams}')
        
        
        rjResult = rpc_con.CreateJob(self._localJob.plugin.PLUGIN_NAME, self._localJob.__class__.__name__ , self._localJob.__class__.__module__ , _jobparams=_allParams)
        
        _jobUniqueKey = 'N/A'
        
        if rjResult.__contains__('result'):
            _jobUniqueKey = rjResult['result']
            if _jobUniqueKey == None:
                _jobUniqueKey = 'N/A'
        
        
        _jobMaxRetry = 5
        _jobCurrentRetry = 0
        _interrupted = False
        _lastExcept = ''
        
        self.logger.info(f'Job Unique Key :  {_jobUniqueKey}')
        
        if _jobUniqueKey != 'N/A' :
        
            #
            #
            #
            # Job Process In Remote, waitloop
            #
            #
            #
            
            _jobDone = False
            while not _jobDone:
                
                rpc_con = self.parentFrame.getNetwork()
                #print(rpc_con._type!='WS-RPC')
                
                self.logger.info(f'Remote Job While Loop ...')
                        
                
                
                try:
                    self.logger.info(f'Remote Job  GetJob Infos ...')
                    _jobInRemote = rpc_con.GetJob(uniqueKey=_jobUniqueKey)
                    self.logger.info(f'Remote Job  GetJob Infos OK...')
                    #self.logger.info(f'Remote Job = {_jobInRemote} ...')
                    
                    
                    
                    if _jobInRemote['result']['_jobRunning'] == False:
                        self.logger.error(f'Remote Job is not running ...')
                        
                        if _jobInRemote['result']['_jobStatus'] != 'Waiting':
                            self.logger.error(f'Remote Job Waiting ...')
                            self.setStatus("Waiting")
                            self.setProgress(_jobInRemote['result']['_jobDetailedProgress'])
                            
                        if _jobInRemote['result']['_jobDone'] != False:
                            self.logger.error(f'Remote Job _jobDone != None ...')
                            _jobDone = True
                            
                            
                            self.logger.info(f'Remote Job Downloading Result ...')
                            
                            
                            
                            _jobInRemoteResult = rpc_con.GetJobResult(uniqueKey=_jobUniqueKey)
                            
                            if _jobInRemoteResult['error'] != None:
                                self.setProgress(_jobInRemoteResult['error']['message'])
                                _jobDone = True
                                err = _jobInRemoteResult['error']['message']
                                self.setError(err)
                                self.logger.error(f'Remote Job Downloading Result ERROR : {err}...')
                                break
                                #ReportRPCResult(parentf, resultObj, _type, bypassMessage, bypassError, _showCancel)
                            
                            else:
                                self.setResult(_jobInRemoteResult['result'])
                                self.logger.info(f'Remote Job Downloading Result DONE...')
                            
                            
                            
                            
                            break
                        
                        
                            
                        if _jobInRemote['result']['_jobError'] != None:
                            self.logger.error(f'Remote Job _jobError != None ...')
                            _jobDone = True
                            self.setError(_jobInRemote['result']['_jobError'])
                            break
                        
                    else:
                        self.logger.error(f'Remote Job is RUNNING ...')
                        self.setProgress(_jobInRemote['result']['_jobDetailedProgress'])
                    
                    time.sleep(5)
                
                except Exception as e:
                    self.logger.error(f'Unable to retreive Job informations : {_jobUniqueKey} ')
                    _lastExcept = str(e)
                    _jobCurrentRetry = _jobCurrentRetry+1
                    
                    
                    if _jobCurrentRetry > _jobMaxRetry:
                        _interrupted = True
                        break
            
            
                
            #self.parentFrame.NewJob()
            
            
            
            if not _interrupted:
                pass
                #self.setResult(_jobInRemote['result']['_jobResult'])
        
            else:
                if _lastExcept != '':
                    self.setError(f'ERROR : {_lastExcept}')
        
        
        else:
            self.setError('ERROR')
        
        
        self.logger.error(f'Remote Job END ...')
        
        
        
        
    def SaveResult(self):
        self._localJob.setResult(self.getResult())
        self._localJob.SaveResult()
    
    
    