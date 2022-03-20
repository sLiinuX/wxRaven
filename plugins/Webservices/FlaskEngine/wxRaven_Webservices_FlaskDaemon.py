'''
Created on 8 févr. 2022

@author: slinux
'''
import flask
from flask import request, jsonify
import logging
from logging.handlers import TimedRotatingFileHandler
import os
import importlib
import functools
from flask import redirect, url_for
import math
from .API_Services import P2PMarket
import time
import json, sys
from threading import Thread, Lock
import pickle

from wxRavenGUI.version import __VERSION__


session = []

_CONST_MB_SIZE_BYTE = 1048576


class wxRaven_Webservices_FlaskDaemon(object):
    '''
    classdocs
    '''
    
    ip='127.0.0.1'
    port=5000
    _wsInfos = {'name':'wxRaven_Webservices_Daemon',
                'active_services':[],
                'version': __VERSION__}
    
    activeServices = []
    routes = {}
    
    app = None
    
    usertoken=[]
    admintoken=''
    
    forceNetwork = ''
    
    

    def __init__(self,parentFrame, ip='127.0.0.1', port=5000, LogFile='wxRaven_Webservices.log',  forceNetwork='', adminToken='', _exlcude_service_list=[], _options={}):
        '''
        Constructor
        '''
        
        
        self.wxRavenInstance = parentFrame
        
        self.port = port
        self.ip = ip
        self.app = flask.Flask(__name__)
        self.app.config["DEBUG"] = True
        self.admintoken  = adminToken
        self.forceNetwork =  forceNetwork
        self.excludeServices = _exlcude_service_list
        self.activeServices = []
        
        self._lock = Lock()
        
        self._startedTime = time.time()
        self._lifeTime = 0
        
        self.jobFactory = None
        
        
        
        
        
        
        
        #
        # Default Options (but just as declarator, the settings are in server_config.json
        #
        
        self.max_query_size_mb_anonymous = 512000#_CONST_MB_SIZE_BYTE * 3 #10 Mo
        self.max_query_size_mb_user = _CONST_MB_SIZE_BYTE * 10
        self.max_query_size_mb_admin = _CONST_MB_SIZE_BYTE * 1000
        
        self.limit_all_json_results = False
        self.limit_jobs_results = True
        
        self.rvn_to_mb_credit = 104857600
        
        
        self.service_description = ''
        
        
        
        
        
        #
        # Path
        #
        #
        
        
        
        self.routes = {}
        self.API_Root_Path = parentFrame.GetPath("PLUGIN") + '/Webservices/'
        self.API_Configuration_File = parentFrame.GetPath("PLUGIN") + '/Webservices/server_configuration.json'
        self.API_Tokens_Cache_File = parentFrame.GetPath("PLUGIN") + '/Webservices/server_tokens.tokens'
        
        self.API_Services_Path = parentFrame.GetPath("PLUGIN") + '/Webservices/FlaskEngine/API_Services/'
        self.LogFile = LogFile
        
        self.setup_logging()
        self.logger = logging.getLogger('wxRaven-Webservices')
        #logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
        self.app.logger = self.logger
        
        
        
        #
        # Overwritting the Server settings from the JSON
        #
        #
        self.__ApplyServerConfigurationJSON__()
        self.__LoadCache__()
        
        
        
        
        
        
        
        
        
        @self.app.route('/', methods=['GET'])   
        def ws_home():
            #self.logger.info("ws_home")
            self.__UpdateWsInfos__()
            return jsonify(self.returnJSON(self._wsInfos))
        
        '''
        @self.app.route('/api/v1/', methods=['GET'])   
        def api_v1():
            self.logger.info("api_v1")
            return jsonify(self.returnJSON(self._wsInfos))
        '''
        
        @self.app.errorhandler(404)
        def page_not_found(e):
            self.logger.info(f"page_not_found : {e}")
            #return jsonify(self.returnJSON_NotImplemented(str(e))), 404
            return jsonify(self.returnJSON_ServiceNotAvailableOnNetwork()),404

        '''
        @self.app.route('/api/v1/ravencoin', methods=['GET']) 
        def ravencoin_client( ):
            self.logger.info("ravencoin_client")
            query_parameters = request.args

            #id = query_parameters.get('method')
            #published = query_parameters.get('published')
            #author = query_parameters.get('author')
            return jsonify(self.returnJSON_ServiceNotAvailableOnNetwork())
        
        '''
        
        
        
        
        
        
        
        '''
        
        def login_required(f):
            @functools.wraps(f)
            def wrap(*args, **kwargs):
                
                query_parameters = request.args
                token = query_parameters.get('token')
                self.logger.info(f"Token : {token}")
                _noAuthRequired = False
                _validToken = False
                
                if self.admintoken == '':
                    _noAuthRequired = True
                else:    
                    if token == self.admintoken :
                        _validToken = True
                           
                    
                
                
                if _noAuthRequired or _validToken:
                    return f(*args, **kwargs)
                else:
                    #print("You need to login first")
                    return jsonify(self.returnJSONError('Not Allowed or invalid token.'))
        
            return wrap
            
            
        '''
        
        
        """
        Markets
        """
        self.Load_API_Services()
        self.__UpdateWsInfos__()
        #P2PMarket.P2PMarketView.register(self.app , daemon=self)
        
    
    
    """
    
    netowrk manageent
    
    """
    
    def getNetwork(self):
        return self.wxRavenInstance.getNetwork(self.forceNetwork)
    
    def getAdminToken(self):
        return self.admintoken
    
    
    def getRavencoin(self):  
        return self.wxRavenInstance.getRvnRPC(self.forceNetwork)
    
    
    
    
    '''
    User and token management
    
    '''
    
    def __CreditUserToken__(self, token, rvn_amount, asset_amount=0.0):
        self.logger.info(f'__CreditUserToken {token} with {rvn_amount} RVN and {asset_amount} AIRDROP')
        _curentSize = self.__GetTokenSize__(token)
        
        _newCreditSize = self.rvn_to_mb_credit * rvn_amount
        self.__SaveUserToken__(token, _newCreditSize)
        
        return self.convert_size(_newCreditSize)
        
    
    
    def __GetTokenSize__(self, token):
        
        _allTk  = self.__GetUserTokens__()
        _size = self.max_query_size_mb_anonymous
        for _r in _allTk:
            
            if _r['token'] == token:
                _size = _r['size']
                break
                
        return _size
    
    
    
    def __GetUserTokens__(self):
        self.logger.info(f"__GetUserTokens__ {self.usertoken}")
        return self.usertoken.copy()
    
    
    
    
    def __SaveUserToken__(self, token, size):
        self._lock.acquire()
        self.logger.info(f"__SaveUserToken__ {self.usertoken}")
        
        _toremoveRow= None
        for _row in self.usertoken:
            if _row['token'] == token:
                self.logger.info(f"__SaveUserToken__ TOKEN EXIST {self.usertoken}")
                _toremoveRow = _row
                break
                
        if _toremoveRow != None:
            self.usertoken.remove(_row)
        
        
        self.usertoken.append({'token':token, 'size':size})
        self.__saveCache__()
        self._lock.release()
        
        
    def __saveCache__(self):
        try:
            self.logger.info("Webservice Save Token Cache")
            print(self.usertoken )
            pickle.dump( self.usertoken , open(self.API_Tokens_Cache_File, "wb" ) )
        except Exception as e:
            self.logger.error(e) 
    
    def __LoadCache__(self):
        result = []
        try:
            self.logger.info("Webservice Load Token Cache")
            self.usertoken  = pickle.load( open( self.API_Tokens_Cache_File, "rb" ) )
            
            
            
            
        except Exception as e:
            self.logger.error(e) 
        
        return result    
        
    
            
    '''
        
    API Low Level and Basic STUFF 
       
    '''
    
    def __mb_to_bytes__(self, mb):
        return mb*_CONST_MB_SIZE_BYTE
    
    def convert_size(self,size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])  
    
    
    def StartWebService(self):
        self.logger.info(f"StartWebService JSON on the network '{self.forceNetwork}'")
        self.app.run(host=self.ip, port=self.port, debug=True, use_reloader=False)
        
    
    def __ApplyServerConfigurationJSON__(self):
        with open(self.API_Configuration_File, 'r') as f:
            data = json.load(f)
            
            
            for _key in data:
                _val = data[_key]
                try:
                    setattr(self, _key, _val)
                except Exception as e:
                    self.logger.error(f"Unknown Serverconfiguration Option : {_key}")
    
    
    def StopWebService(self):    
        #self.app.
        pass
        
    
        
    
    def Load_API_Services(self):
        
        self.logger.info("Initialize plugin list from " + self.API_Services_Path )
        
        for filename in os.listdir(self.API_Services_Path):
            f = os.path.join(self.API_Services_Path, filename)
            # checking if it is a file
            
            _nameAndExt = str(filename).split('.')
            
            try:
                if _nameAndExt[1] != 'py':
                    continue
            except Exception as e:
                self.logger.error(f"Unknown type {f}")
            
            
            if str(_nameAndExt[0]) in self.excludeServices:
                self.logger.info(f"Excluding {f}")
                continue
            
            
            if os.path.isfile(f):
                if filename == 'wxFlaskCustomView.py':
                    continue
                
                
                
                
                noext = filename.replace('.py','')
                fname = 'plugins/Webservices/FlaskEngine/API_Services/' +noext+ '/<ALLCLASSES>'
                pname = fname.replace("/",".")
                self.logger.info(f"Trying to load {pname}")
                
                module = self.__LoadPluginModule__(pname)
                
                
                self.logger.info(f"Trying to instanciate {noext}View")
                apiservice_init_classe = getattr(module, f'{noext}View')
                
                apiservice_init_classe.register(self.app , daemon=self)
                
                self.activeServices.append(_nameAndExt[0])
                #apiservice_instance = plugin_init_classe(self.appmainframe)
                
                #print(f)
                #head, tail = os.path.split(f)
    
    
    
    #
    # WSServices Function
    #
    #
    
    
    def __RegisterJobFactory__(self, obj):
        self.jobFactory = obj
    
    def __RemoteJobFactory__(self):
        return self.jobFactory 
    
    
    #
    #
    # Service function
    #
    #
    
    
    def __WsTokenServiceActive__(self):
        return 'WebserviceUserTokenProvider' in self.activeServices
        
    def __WsJobsServiceActive__(self):
        return 'RemoteJobs' in self.activeServices
    
    
    def __UpdateWsInfos__(self):
        self._wsInfos['service_description'] = self.service_description
        self._wsInfos['active_services'] = self.activeServices
        self._wsInfos['WebserviceUserTokenProvider'] = self.__WsTokenServiceActive__()
        self._wsInfos['RemoteJobs'] = self.__WsJobsServiceActive__()
        self._wsInfos['start_time'] = self._startedTime
        ts= time.time()
        self._lifeTime = ts - self._startedTime
        self._wsInfos['live_time'] = self._lifeTime 
        self._wsInfos['timestamp'] = ts
        self._wsInfos['rvn_network_restrictions'] = self.forceNetwork
        
    
    def __LoadPluginModule__(self, full_class_string):
        """
        dynamically load a class from a string
        """
        class_data = full_class_string.split(".")
        module_path = ".".join(class_data[:-1])
        class_str = class_data[-1]
        
        #self.logger.info('loading module in :' + module_path)
        #self.logger.info('loading class :' + class_str)
        module = importlib.import_module(module_path)
        # Finally, we retrieve the Class
        #return getattr(module, class_str)  
        return module
    
    
    '''
    
    def __CheckLogin__(self):
        self.logger.info("__CheckLogin__ " )
        
        query_parameters = request.args
        token = query_parameters.get('token')
        
        self.logger.info(f"Token Received : {token}" )
        
        return self.__CheckAdminToken__(token)
    
    
    
        
    def __CheckAdminToken__(self, tk):
        if tk == self.admintoken or self.admintoken=='':
            return True
        else:
            return False    
    '''    
         
         
    '''     
    def EvaluateReturnDatas(self, returnDatas):
        returnDatasStr_Size =   sys.getsizeof(str(returnDatas))
        csize = self.convert_size(returnDatas)   
    '''     
         
    
    def GetJSONResultSize(self,returnDatas ):
        returnDatasStr_Size =   sys.getsizeof(str(returnDatas))
        return returnDatasStr_Size
    
                
    def returnNoneJSON(self):
        _JSON_RPC_Result = {'result': None}
        return _JSON_RPC_Result
    
    def returnJSON(self, result, error=None):
        _JSON_RPC_Result = {'result': result, 'error':error} 
        #if self.limit_all_json_results:
        return _JSON_RPC_Result
    
    
    def returnJSONError(self, errormsg): 
        return self.returnJSON(None, {'code':-1, 'message':errormsg})
    
    
    def returnJSON_ServiceNotAvailableOnNetwork(self):
        return self.returnJSONError('Feature Not available on this network')
    
    def returnJSON_NotImplemented(self, fct):
        return self.returnJSONError(f'The {fct} method is not implemented')
    
    
    
    
    def setup_logging(self, forcePath='',_timeStampIt=False):
        #self._timestamp = round(time.time() * 1000) 
        

        #self._timestamp = round(time.time() * 1000) 
        print(self.LogFile)
        path = os.path.expanduser(self.LogFile)
        
        
        
        #logging.basicConfig(filename = self.LogFile+'.debug', level=logging.DEBUG, format = f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

        
        
        
        #self.ensure_directory(os.path.dirname(path))
        self.logger = logging.getLogger('wxRaven-Webservices')
        self.handler = TimedRotatingFileHandler(path, when='D', interval=1, backupCount=1)
        fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        formatter = logging.Formatter(fmt=fmt, datefmt='%m/%d/%Y %H:%M:%S')
        self.handler.setFormatter(formatter)
        self.handler.setLevel(logging.DEBUG)
        # tee output to console as well
        self.console = logging.StreamHandler()
        self.console.setFormatter(formatter)
        self.console.setLevel(logging.DEBUG)
        self.logger.addHandler(self.console)
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.DEBUG)
    
    
    def stop_logging(self):
        self.logger.removeHandler(self.console)
        self.logger.removeHandler(self.handler)
        
        
        
        
        
        