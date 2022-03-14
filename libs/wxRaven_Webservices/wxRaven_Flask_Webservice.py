'''
Created on 10 févr. 2022

@author: slinux
'''
import logging
import requests 
from requests.auth import HTTPBasicAuth
import base64
import json
from libs.jsonrpcclient.requests import Request
from jsonrpcclient import parse, request
import inspect
import time
import urllib.parse

import uuid    


def get_kwargs():
    #start_time = time.time()
    frame = inspect.currentframe().f_back
    keys, _, _, values = inspect.getargvalues(frame)
    kwargs = {}
    for key in keys:
        if key != 'self':
            kwargs[key] =  values[key]
            
            if isinstance(values[key], str):
                logging.debug(f'Encoding str parameter {key}')
                kwargs[key] = urllib.parse.quote(values[key].encode('utf8'))
            
            if key == '_jobparams': 
                logging.debug(f'Encoding str parameter {key}')
                _dict = values[key]
                
                
                for _k in _dict:
                    _v = _dict[_k]
                    if isinstance(_v, str):
                        _dict[_k] = urllib.parse.quote(_v.encode('utf8'))
                    
                    
                kwargs[key]   =  _dict
                
      
                
                
            
    end_time = time.time()
    #time_elapsed = (end_time - start_time)
    #print(time_elapsed)
    return kwargs


class wxRaven_Flask_WebserviceClient(object):
    '''
    classdocs
    '''
    _ip='0.0.0.0'
    _port=1234
    _url = ""
    id = 0 
    _client = None
    _type='WS-RPC'
    
    _user_token = None
    
    def __init__(self, ip="relay.wxraven.link", port=9090, useHTTPS=False):
        self._ip = ip
        self._port = port
        self.logger = logging.getLogger('wxRaven')
        self.url = 'http://{}:{}'.format(ip, port)
        
        
        if useHTTPS:
            self.url = 'https://{}'.format(ip)
            
        if ip.__contains__('http'):
            self.url = '{}'.format(ip)
        
        self.logger.info(f'Creating a new Flask WebserviceClient Client at {self.url}')
        
        
        
        self._client = None
        self.id = 0 
        
    
    
    #def generate_GET_argurments(self):
    def rpc_url(self):
        return self.url
        #return "http://{}:{}@{}:{}".format('wx', 'wx', self._ip, self._port)
    
    
    def rpc_status(self):
        _args = get_kwargs()
        return self.get_query('', _args)
    
        
        
    def get_query(self, name, params, auth=False):
        self.id += 1
        url = f'{self.url}/{name}'
        self.logger.info(f"WebserviceClient Query : {url}")
        #auth = HTTPBasicAuth(self.username, self.password)
        data = {
                'method': name,
                #'params': params,
                'id': self.id,
                'jsonrpc': '2.0',
                
        }
        
        if self._user_token != None:
            self.logger.info(f"WebserviceClient UserToken enable : {self._user_token}")
            data['token'] = self._user_token
        
        for key, value in params.items():
            data[key] = value
        
        #response = requests.post(url, json.dumps(data), headers={'Content-Type': 'application/json'}, auth=auth)
        response = requests.get(url, json.dumps(data), headers={'Content-Type': 'application/json'})
        return json.loads(response.text)
    
    '''
    def wrapper_query(self, **kwargs):
        return self.get_query(kwargs['method'], kwargs )
    '''
    
    
    
    #
    # Client Start mapping
    #
    
    '''
    def secret(self, _auth=True):
        _url='api/this_is_secret/'
        _args = get_kwargs()
        return self.get_query(_url, _args, auth=_auth)
    
    '''
    
    '''
    def __getattr__(self, name):
        if name.startswith('__') and name.endswith('__'):
            # Python internal stuff
            raise AttributeError

        _url=f'api/v1/RPC/{name}'
        #_args = get_kwargs()
        
        def wrapper_query(**kwargs):
            #if len(kwargs) >0:
            _args = get_kwargs()
            return self.get_query(_url, _args)
        
        
        return self.wrapper_query
    '''
    
    
    def __getattr__(self, name):
        def wrapper_query(**kwargs):
            #if len(kwargs) >0:
            return self.returnJSONError('Feature Not available on this network')
        
    
    def help(self, command=''):
        _url='api/v1/RPC/help'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    
    def listassets(self, asset="*", verbose=False, count=500, start=0 ):
        _url='api/v1/RPC/listassets'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    
    #def listassetbalancesbyaddress(self,address, onlytotal=False, count=50000, start=0):
    def listassetbalancesbyaddress(self,address, onlytotal=False, count=50000, start=0):
        _url='api/v1/RPC/listassetbalancesbyaddress'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    #def listaddressesbyasset(self, asset_name, onlytotal=False, count=50000, start=0):
    def listaddressesbyasset(self, asset_name, onlytotal=False, count=50000, start=0):
        _url='api/v1/RPC/listaddressesbyasset'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    #def getaddressbalance(self,searchAdressListJSON ,showAsset=True):
    def getaddressbalance(self,addresses ,showAsset=True):
        _url='api/v1/RPC/getaddressbalance'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    
    #def validateaddress(self, address):
    def validateaddress(self, address):
        _url='api/v1/RPC/validateaddress'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    #def getaddressdeltas(self, searchAdressListJSON):
    def getaddressdeltas(self, addresses):
        _url='api/v1/RPC/getaddressdeltas'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    
    #def gettxout(self, txId, out):
    def gettxout(self, txId, out):
        _url='api/v1/RPC/gettxout'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    
    
    def decoderawtransaction(self, hexstring):
        _url='api/v1/RPC/decoderawtransaction'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    
    
    def getrawtransaction(self, txid, verbose=False):
        _url='api/v1/RPC/getrawtransaction'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    
    def getblockhash(self, height):
        _url='api/v1/RPC/getblockhash'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    def getblock(self, hash, verbose=False):
        _url='api/v1/RPC/getblock'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    def getassetdata(self, asset):
        _url='api/v1/RPC/getassetdata'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    
    
    
    
    #
    # Special functions for Jobs
    #
    
    def CreateJob(self,_pluginName, _class , _module , _jobparams={}):
        _url='api/v1/RemoteJob/CreateJob'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    def GetJob(self,uniqueKey):
        _url='api/v1/RemoteJob/GetJob'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    def GetJobResult(self,uniqueKey):
        _url='api/v1/RemoteJob/GetJobResult'
        _args = get_kwargs()
        return self.get_query(_url, _args)
    
    
    
    #
    # Special functions for Session Token
    #
    def __CheckSessionToken__(self):
        _url='api/v1/wsusertkprovider/checkuserwstoken'
        _args = get_kwargs()
        _args['checktoken'] = self._user_token
        
        return self.get_query(_url, _args)
    
    def __SetSessionToken__(self, token):
        self._user_token = token
        self.logger.info(f'Session Token for wxRaven Webservices Changed : {self._user_token}')
    
    def __RequestPrivateSessionToken__(self):
        _url='api/v1/wsusertkprovider/getuserwstoken'
        _args = get_kwargs()
        _args['uuid'] = str(uuid.UUID(int=uuid.getnode()))
        _args['private'] = True
        return self.get_query(_url, _args)
    
    def __RequestSessionToken__(self):
        _url='api/v1/wsusertkprovider/getuserwstoken'
        _args = get_kwargs()
        _args['uuid'] = str(uuid.UUID(int=uuid.getnode()))
        
        try:
        
            _res = self.get_query(_url, _args)
            
            if _res['error'] == None:
                self._user_token = _res['result']
            else:
                _e = _res['error']
                self.logger.error(f'RequestSessionToken Error : {_e}')
                
            self.logger.info(f'New Session Token for wxRaven Webservices Requested : {self._user_token}')
            
        except Exception as e:
            self.logger.error(f'RequestSessionToken Error : {e}')
    
    