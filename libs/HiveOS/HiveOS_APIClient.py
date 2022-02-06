'''
Created on 4 févr. 2022

@author: slinux
'''

import requests
from requests.models import Response
import json
import time
import logging


class HiveOS_Client(object):
    '''
    classdocs
    '''
    
    _api_url = "https://api2.hiveos.farm/api/v2/"
    _token = None
    _farmId = None
    _workers = None
    
    def __init__(self, token, farmId, workerList=[] ):
        '''
        Constructor
        '''
        
        self._token = token
        self._farmId = farmId
        self._workers = workerList
        self.session = requests.Session()
        self.logger = logging.getLogger('wxRaven')
   
   
    def __getHeader__(self):
        return { "Authorization" : "Bearer " + str(self._token),"accept": "application/json" }
        
    
    
    def __query__(self, queryPath, _retryAuto=True, _firstCall=True):
        result = None
        executed=False
        
             
        if not _firstCall:
            self.logger.info(f">RETRY QUERY")  
            self.session = requests.Session()
        
        
        try:
            r = self.session.get(self._api_url + queryPath, headers=self.__getHeader__(), timeout=(10,20))
            self.logger.info(f">QUERY : {r.content}")  
            
            if r.ok:
                self.logger.info(f"> {queryPath}  = OK")    
                
                self.logger.info(f"> PARSE  = {r.text}")   
                result = json.loads(r.text)
                self.logger.info(f"> RESULT = {result}")   
                executed = True
            else:
                self.logger.error("HTTP %i - %s, Message %s" % (r.status_code, r.reason, r.text))
                
                
        except Exception as e:                 
            self.logger.error(f"query error {queryPath} : {e}") 
            executed = False   
        except requests.exceptions.Timeout as e: 
            self.logger.error(f"query timeout {queryPath} : {e}")   
            executed = False  
            
        
        self.logger.info(f"> Executed  = {executed}")       
        if executed==False:
            if _retryAuto:
                result =  self.__query__(queryPath, _retryAuto=False, _firstCall=False)
            
            
        return result 
     
    
    
    def __createRIGlist__(self, datas):
        dataList = datas['data']
        
        rigCount = 0
        
        rigList=[]
        
        
        
        for rig in dataList:
            
            rigName = "N/A"
            rigHiveVersions = "N/A"
            rigMaintenanceMode = 0
            rigonline = False
            
            try:
                rigName = rig["name"]
                rigHiveVersions = rig["versions"]["hive"]
                
                
                
            except Exception as e: 
                self.logger.error("    > __createRIGlist__ Error Reading 1")
            
            
            
            try:
                rigMaintenanceMode = rig["options"]["maintenance_mode"]
            except Exception as e: 
                self.logger.error("    > __createRIGlist__ Error Reading 2")
            
            rigBootTime = -1
            rigminerTime = -1
            
            try:
                rigBootTime = rig["stats"]["boot_time"]
                rigonline = rig["stats"]["online"]
            except Exception as e: 
                self.logger.error("    > __createRIGlist__ Error Reading 3")
                
                
            try:
                rigminerTime = rig["stats"]["miner_start_time"]
            except Exception as e: 
                self.logger.error("    > __createRIGlist__ Error Reading 3")    
                
            
            rigCount= rigCount+1    
            rToAdd = {'name':rigName, 'version':rigHiveVersions , 'maintenance': rigMaintenanceMode , 'boot_time':rigBootTime, 'miner_time': rigminerTime, 'online':rigonline}
            rigList.append(rToAdd)
            
        
        return rigList 
       
    def __createGPUlist__(self, datas):
        dataList = datas['data']
        
        rigCount = 0
        
        gpuList=[]
        
        
        
        for rig in dataList:
            
            gpuCount = 0
            
            rigAllGpus = rig["gpu_info"]
            rigAllGpusStats = rig["gpu_stats"]
            
            
            for gpu in rigAllGpus:
                
                gpusName=""
                gpuName=""
                
                try:
                    gpusName = rigAllGpus[gpuCount]["short_name"]
                    gpuName = rigAllGpus[gpuCount]["model"]
                except Exception as e: 
                    self.logger.error("    > __createGPUlist__ Error Reading 1")
                
                
                gpuTemp = "n/a"
                gpuFan = "n/a"
                
                
                try:
                    
                    gpuTemp = rigAllGpusStats[gpuCount]["temp"]
                    gpuFan = rigAllGpusStats[gpuCount]["fan"]
                    
                except Exception as e: 
                    self.logger.error("    > __createGPUlist__ Error Reading 2")
                    
                gpuCount = gpuCount+1    
                gpuToAdd = {'name':gpusName, 'model':gpuName , 'temp': gpuTemp,'fan': gpuFan }
                gpuList.append(gpuToAdd)

            rigCount = rigCount+1
            
        return gpuList   
       
       
       
       
       
       
       
       
       
       
    def GetConnexionStatus(self):
        pass
    
    

    def GetFarmInfos(self, _farmId=None):
        
        if _farmId ==None: 
            _farmId = self._farmId
        _query = "farms/"+str(_farmId)+""
        
        return self.__query__(_query)
        
        
    def GetWorkersGpuInfos(self, _farmId=None):
        
        if _farmId ==None: 
            _farmId = self._farmId
        _query = "farms/"+str(_farmId)+"/workers/gpus"
        
        return self.__query__(_query)
    
    
    def GetWorkerInfos(self, _workerId, _farmId=None ):
        
        if _farmId ==None: 
            _farmId = self._farmId
        _query = "farms/"+str(_farmId)+f"/workers/{_workerId}"
        
        return self.__query__(_query)
    
    
    def GetFarmStats(self, _farmId=None, _workers=[]):
        if _farmId ==None: 
            _farmId = self._farmId
            
            
        farmData = self.GetFarmInfos(_farmId)
        workerGpusData = self.GetWorkersGpuInfos(_farmId)
        farmData['gpus'] = workerGpusData['data']
        
        workersDatas = []
        if len(_workers) > 0:
            for _worker in _workers:
                _wInfos = self.GetWorkerInfos(_worker, _farmId)
                workersDatas.append(_worker)
                
        farmData['workers'] = workersDatas
        
        
        '''
        self.logger.info(f" WorkerData   >  {workerData}")
        
        
        gpuList = []
        try:
            gpuList = self.__createGPUlist__(workerData)
            farmData["gpus"] = gpuList
        except Exception as e: 
            self.logger.error("    > gpuListRes ERROR")
                            
                            
        rigList = []
        try:
            rigList = self.__createRIGlist__(workerData)
            farmData["rigs"] = rigList
        except Exception as e: 
            self.logger.error("    > rigList ERROR")
        
        
        '''
            
        '''
        
        result["gpus"] = gpuList
        result["rigs"] = rigList
        '''    
        return farmData
        
        