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

from .API_Services import P2PMarket


session = []





class wxRaven_Webservices_FlaskDaemon(object):
    '''
    classdocs
    '''
    
    ip='127.0.0.1'
    port=5000
    _wsInfos = {'name':'wxRaven_Webservices_Daemon',
                'active_services':[],
                'version': 0.1}
    
    activeServices = []
    routes = {}
    
    app = None
    
    usertoken=[]
    admintoken=''
    
    forceNetwork = ''
    
    

    def __init__(self,parentFrame, ip='127.0.0.1', port=5000, LogFile='wxRaven_Webservices.log',  forceNetwork='', adminToken='', _exlcude_service_list=[]):
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
        
        self.routes = {}
        
        self.API_Services_Path = parentFrame.GetPath("PLUGIN") + '/Webservices/FlaskEngine/API_Services/'
        self.LogFile = LogFile
        
        
        self.setup_logging()
        self.logger = logging.getLogger('wxRaven-Webservices')
        
        #logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

        self.app.logger = self.logger
        
        
        @self.app.route('/', methods=['GET'])   
        def ws_home():
            self.logger.info("ws_home")
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
      
                
    '''
        
    API Low Level and Basic STUFF 
       
    '''
    
    
    
    
    def StartWebService(self):
        self.logger.info(f"StartWebService JSON on the network '{self.forceNetwork}'")
        self.app.run(host=self.ip, port=self.port, debug=True, use_reloader=False)
        
    
    
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
    
    
    def __UpdateWsInfos__(self):
        self._wsInfos['active_services'] = self.activeServices
        
    
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
                
    def returnNoneJSON(self):
        _JSON_RPC_Result = {'result': None}
        return _JSON_RPC_Result
    
    
    
    def returnJSON(self, result, error=None):
        _JSON_RPC_Result = {'result': result, 'error':error}
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
        
        
        
        
        
        