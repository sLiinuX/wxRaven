'''
Created on 11 déc. 2021

@author: slinux
'''
import logging

import requests 
from requests.auth import HTTPBasicAuth
import base64
import json
from libs import RVNpyRPC
#from jsonrpcclient.requests import Request
from libs.jsonrpcclient.requests import Request
from jsonrpcclient import parse, request

import logging


class Ravencoin:
    def __init__(self, username, password, host='localhost', port=8766):
        self.username = username
        self.password = password 
        self.host = host
        self.port = port
        self.id = 0 
    
    
    def rpc_url(self):
        return "http://{}:{}@{}:{}".format(self.username, self.password, self.host, self.port)
    
    def __getattr__(self, name):
        if name.startswith('__') and name.endswith('__'):
            # Python internal stuff
            raise AttributeError

        def ret(*args):
            self.id += 1
            url = f'http://{self.host}:{self.port}'
            auth = HTTPBasicAuth(self.username, self.password)
            data = {
                'method': name,
                'params': list(args),
                'id': self.id,
                'jsonrpc': '2.0',
            }
            response = requests.post(url, json.dumps(data), headers={'Content-Type': 'application/json'}, auth=auth)
            if 'error' in response and response['error'] != None:
                raise Exception(response['error'])
            return json.loads(response.text)

        return ret


    def do_rpc(self,method, log_error=True, **kwargs):
        req = Request(method, **kwargs)
        #req=request(method, **kwargs)
        try:
            url = self.rpc_url()
            resp = requests.post(url, json=req, timeout=10)
            if resp.status_code != 200 and log_error:
                logging.error("RPC ==> {}".format(req))
                logging.error("RPC <== {}".format(resp.text))
            if resp.status_code != 200:
                try:  # Attempt parse response when failed
                    return json.loads(resp.text)
                except:
                    return None
            return json.loads(resp.text)
        except TimeoutError:
            if log_error:
                # Any RPC timeout errors are totally fatal
                logging.error("RPC Timeout")
                #AppInstance.on_exit()
                #show_error("RPC Timeout", "Timeout contacting RPC")
                #exit(-1)
                return None
            else:
                return None
        except Exception as ex:
            logging.error(ex)
            return None



from ._wallet import *
from ._squawker import *
from ._asset import *
from ._utils import *
from ._P2PmarketPlace import *
from ._atomicSwap import *
from ._network import * 

try: 
    from ._directories import *
except ImportError:
    pass

class RavenpyRPC(object):
    '''
    classdocs
    '''
    
    
    RPCconnexion = None
    
    wallet = None
    squawker = None
    asset = None
    utils = None
    
    p2pmarket = None
    atomicswap = None
    network = None
    directories = None

    def __init__(self, connexion):
        '''
        Constructor
        '''
        self.logger = logging.getLogger('wxRaven')
        
        self.RPCconnexion = connexion
        self.wallet = RVNpyRPC_Wallet(connexion, self) 
        self.squawker = RVNpyRPC_Squawker(connexion)
        self.asset = RVNpyRPC_Asset(connexion, self)
        self.utils = RVNpyRPC_Utils(connexion, self)
        self.p2pmarket = RVNpyRPC_P2P_Marketplace(connexion, self)
        self.atomicswap = RVNpyRPC_AtomicSwap(connexion, self)
        self.network = RVNpyRPC_Network(connexion, self)
        
        try:
            self.directories = RVNpyRPC_Directories(connexion, self)
        except:
            self.directories =  None
    
    
    def test_rpc_status(self):
        _status=True
        #chain_info = self.RPCconnexion.getblockchaininfo()
        # Then do a basic test of RPC, also can check it is synced here
        chain_info = self.do_rpc("getblockchaininfo", log_error=False)
        # If the headers and blocks are not within 5 of each other,
        # then the chain is likely still syncing
        self.logger.info(f"chain_info  = {chain_info}")
        chain_updated = False if not chain_info else\
            (chain_info["headers"] - chain_info["blocks"]) < 5
        
        return chain_updated   
    
    
    
    
    def do_rpc(self,method, log_error=True, **kwargs):
        req = Request(method, **kwargs)
        #req=request(method, **kwargs)
        try:
            url = self.RPCconnexion.rpc_url()
            resp = requests.post(url, json=req, timeout=10)
            if resp.status_code != 200 and log_error:
                self.logger.error("RPC ==> {}".format(req))
                self.logger.error("RPC <== {}".format(resp.text))
            if resp.status_code != 200:
                try:  # Attempt parse response when failed
                    return json.loads(resp.text)
                except:
                    return None
            return json.loads(resp.text)["result"]
        except TimeoutError:
            if log_error:
                # Any RPC timeout errors are totally fatal
                self.logger.error("RPC Timeout")
                #AppInstance.on_exit()
                #show_error("RPC Timeout", "Timeout contacting RPC")
                #exit(-1)
                return None
            else:
                return None
        except Exception as ex:
            self.logger.error(ex)
            return None
    
    
    
    def secure_call(self, method, **kwargs):
        try: 
            self.logger.info(f"RVN RPC Secure call for {method.__name__}") 
            return method(**kwargs)
        except Exception as ex:
            print(ex)
            self.logger.error(f"RVN RPC Method {method.__name__} call error :{ex}")
            return None
        