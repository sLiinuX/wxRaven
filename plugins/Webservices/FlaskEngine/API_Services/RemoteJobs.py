'''
Created on 3 mars 2022

@author: slinux
'''

import flask
from flask import request, jsonify
from .wxFlaskCustomView import * 
from flask_classful import route
from plugins.Webservices.jobs.RemoteJobs_NotAllowedJob import Job_NotAllowedRemoteJob

#from sys import getsizeof
import sys







from sys import getsizeof
import math
 


def getJsonDataSize(jsondata):
    
    _baseSize = sys.getsizeof(jsondata)
    
    if isinstance(jsondata, dict):
        for _sub in jsondata:
            subSize = getJsonDataSize(jsondata[_sub])
            _baseSize = _baseSize + subSize
            

    if isinstance(jsondata, list):
        for _sub in jsondata:
            subSize = getJsonDataSize(_sub)
            _baseSize = _baseSize + subSize

    
    return _baseSize

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])
    #return s, size_name[i]


    
#
#
# This file must be imported WITHIN a specific context
#
#
class RemoteJobsView(wxCustomFlaskView):
    '''
    classdocs
    '''


    route_base = '/api/'
    default_methods = ['GET', 'POST']
    
    #MAX_RESULT_SIZE_BYTES = 25459834 # 24.28 MB
    #MAX_RESULT_SIZE_BYTES = 3145728 # 3Mo
    
    
    def __init__(self, daemon):
        wxCustomFlaskView.__init__(self, daemon)
        
        self.route_base = '/api/'
        self.default_methods = ['GET', 'POST']
        #self.MAX_RESULT_SIZE_BYTES =
        
        self.logger.info('Special constructor for RemoteJobsView, registering to daemon')
        self.daemon.__RegisterJobFactory__(self)
        
    
    
    
    
    
    @route('/v1/RemoteJob/GetJob')     
    def GetJob(self, uniqueKey=''):
        query_parameters = request.args
        args = extract_parameters(request.args)
        uniqueKey = args.get('uniqueKey')
        self.logger.info(f"GetJob : {uniqueKey}")
        _e, _j = self.wxRavenInstance.JobManager.GetJobFromUniqueId(uniqueKey)
        
        _jdata = None
        _jError = None
        if _e:
            _jdata = _j.ExportRemoteJobStatusJson()
            _jError = None
            
        else:
            _jdata = None
            _jError = {'code': -1, 'message': f'Job {uniqueKey} not found.'}
        
        return jsonify({'result':_jdata, 'error':_jError})  
    
    
    '''
    def __getJobResultSize__(self):
        pass
    '''
    
    @route('/v1/RemoteJob/GetJobResult')     
    def GetJobResult(self, uniqueKey=''):
        query_parameters = request.args
        args = extract_parameters(request.args)
        uniqueKey = args.get('uniqueKey')
        token = args.get('token')
        
        
        
        self.logger.info(f"GetJob : {uniqueKey}")
        _e, _j = self.wxRavenInstance.JobManager.GetJobFromUniqueId(uniqueKey)
        
        _jdata = None
        _jError = None
        if _e:
            
  
            _jdata = _j.ExportRemoteJobResultJson()
            _jError = None
            
            #Check Result size :
            #jdataSize = getJsonDataSize(_jdata)
            
            #
            # If not identified, limit the job
            #
            _bypass = not self.daemon.limit_jobs_results
            return jsonify(self.returnJSON_Measured(_jdata, _jError, _bypass))
            '''
            if not self.__isAuthentified__(token, _asAdmin=True):
            
                jdataSize = sys.getsizeof(str(_jdata))
                csize = convert_size(jdataSize)
                
                self.logger.info(f"JobSize : {jdataSize} Bytes / {csize}")
                
                if jdataSize > self.MAX_RESULT_SIZE_BYTES:
                    self.logger.warning(f"JobSize {csize} exceed the maximum allowed.")
                    _jdata = None
                    _jError = {'code': 99, 'message': f'Job Result Exceed Max Size Allowed (3Mo).'}
            '''
            
            
        else:
            _jdata = None
            _jError = {'code': -1, 'message': f'Job {uniqueKey} not found.'}
        
        
        return jsonify(self.returnJSON(_jdata, _jError))
        #return jsonify({'result':_jdata, 'error':_jError})  
        
    
    
    #def __CreateJob__(self):
    def __CreateServerSideJob__(self,_pluginName="General", _class='' , _module='' , _jobparams={}):
        self.logger.warning(f'__CreateServerSideJob__ : {_class}   in   {_module}')
        newJob = self.wxRavenInstance.JobManager.CreateJob(_pluginName, _class , _module , _jobparams=_jobparams, _localJob=True)
        _submitKey = None
        if newJob!=None:
            uk = newJob.getUniqueKey()
            self.logger.info(f'new server side job created {uk}')
            #Resuable serverside?
            _submitKey = uk
            _submitKey = self.wxRavenInstance.JobManager.NewJobFromRemote(newJob)
            self.logger.info(f'new server side job submited {_submitKey}')
        return  _submitKey 
            
    
    @route('/v1/RemoteJob/CreateJob')     
    def CreateJob(self,_pluginName="General", _class='' , _module='' , _jobparams={}):
        query_parameters = request.args
        
        #self.logger.info(f"request.args {request.args}")
        #self.logger.info(f"request.params {request.params}")
        
        args = extract_parameters(request.args)
        
        
        #self.logger.info(f"args {args}")
        #
        # CALL HERE THE RPC CLIENT EQUIVALENT METHOD
        # 
        _pluginName = args.get('_pluginName')
        _class = args.get('_class')
        _module = args.get('_module')
        _jobparams = args.get('_jobparams')
        
        
        
        #
        #
        # Check if allowed
        #
        _fullnameJob = _module + '.'+_class
        _notAllowedSettings = self.wxRavenInstance.GetPluginSetting('Webservices','webservice_exclude_remotejobs')
        _notAllowedRedirectionClass = self.wxRavenInstance.GetPluginSetting('Webservices','webservice_exclude_remotejobs_redirection')
        _pluginNameR = 'General'
        _moduleR, _classR= _notAllowedRedirectionClass.rsplit('.', maxsplit=1)
        
        _allowedClass = True
        
        if _fullnameJob in _notAllowedSettings:
            _allowedClass = False
        
            
        
        
        
        newJob=None
        #
        # Create if allowed.
        #
        if _allowedClass:
            self.logger.info(f"CreateJob : {args}")
            self.logger.info(f"_jobparams : {_jobparams}")
            newJob = self.wxRavenInstance.JobManager.CreateJob(_pluginName, _class , _module , _jobparams=_jobparams, _localJob=False)
            
        else:
            self.logger.info(f"CreateJob : {args}")
            self.logger.warning(f"REPLACED BY NOT ALLOWED JOB MESSAGE {_notAllowedRedirectionClass}")
            
            newJob = self.wxRavenInstance.JobManager.CreateJob(_pluginNameR, _classR , _moduleR , _jobparams={}, _localJob=False)
            
            
            #newJob = Job_NotAllowedRemoteJob(self.wxRavenInstance.GetPlugin(_pluginName))
            newJob._initalJobRequest = _fullnameJob
        #
        
        uk = None
        _error = {'code':-1,'message':'Unable to create Job'}
        
        
        
        
        
        
        
        if newJob != None:
            _error = None
            uk = newJob.getUniqueKey()
            
            self.logger.info(f"New Job Created {uk} : {newJob}")
            
            
            
            #
            # Send in JobManager to process it.
            #
            _submitKey = uk
            _submitKey = self.wxRavenInstance.JobManager.NewJobFromRemote(newJob)
            
            if _submitKey != uk:
                self.logger.info(f"Equivalent job found at submission :  {_submitKey}")
                uk = _submitKey
            
            
            '''
            command = args.get('command')
            network = self.daemon.getNetwork()
            if command == None:
                command = ''
                
            '''
                
                
        return jsonify({'result':uk, 'error':_error})  
    
    
    
    
    
    
    
    
    
    
    
    #
    #
    # Testing purpose
    #
    #
    
    @route('/v1/RemoteJob/checkuserwstoken')     
    def checkuserwstoken(self,checktoken='' ):
        query_parameters = request.args
        args = extract_parameters(request.args)
        checktoken = args.get('checktoken')
        _valid=False
        _res = 0
        _resFriendly = '0 Mb'
        if checktoken != None:
            _res = self.__GetUserTokenQueryCount__(checktoken)
            _resFriendly = self.daemon.convert_size(_res)
            if _res>0:
                _valid = True
        
            
            
        return self.returnJSON({'valid':_valid, 'size':_res , 'size_friendly':_resFriendly})
        
    
    
    