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

def get_kwargs():
    #start_time = time.time()
    frame = inspect.currentframe().f_back
    keys, _, _, values = inspect.getargvalues(frame)
    kwargs = {}
    for key in keys:
        if key != 'self':
            kwargs[key] = values[key]
            
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
    
    def __init__(self, ip="ec2-18-221-126-115.us-east-2.compute.amazonaws.com", port=9090):
        self._ip = ip
        self._port = port
        self.logger = logging.getLogger('wxRaven')
        self.url = 'http://{}:{}'.format(ip, port)
        self._client = None
        self.id = 0 
        
    
    
    #def generate_GET_argurments(self):
    def rpc_url(self):
        return "http://{}:{}@{}:{}".format('wx', 'wx', self._ip, self._port)
        
        
    def get_query(self, name, params, auth=False):
        self.id += 1
        url = f'http://{self._ip}:{self._port}/{name}'
        #auth = HTTPBasicAuth(self.username, self.password)
        data = {
                'method': name,
                #'params': params,
                'id': self.id,
                'jsonrpc': '2.0',
                
        }
        
        if auth:
            data['token'] = 'wxravenuser'
        
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
