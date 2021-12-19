'''
Created on 11 déc. 2021

@author: slinux
'''


import requests 
from requests.auth import HTTPBasicAuth
import base64
import json
from libs import RVNpyRPC

class Ravencoin:
    def __init__(self, username, password, host='localhost', port=8766):
        self.username = username
        self.password = password 
        self.host = host
        self.port = port
        self.id = 0 
    
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







from ._wallet import *
from ._squawker import *




class RavenpyRPC(object):
    '''
    classdocs
    '''
    
    
    RPCconnexion = None
    
    wallet = None

    def __init__(self, connexion):
        '''
        Constructor
        '''
        self.RPCconnexion = connexion
        self.wallet = RVNpyRPC_Wallet(connexion) 
        self.squawker = RVNpyRPC_Squawker(connexion)
        
        