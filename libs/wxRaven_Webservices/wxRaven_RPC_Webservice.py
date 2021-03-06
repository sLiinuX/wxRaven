'''
Created on 27 janv. 2022

@author: slinux
'''


import sys
# The answer is that the module xmlrpc is part of python3
import xmlrpc.client
import os

import logging

'''


NOTE : XML RPC got some limitations.
still looking for the best way to bridge 2 wxRaven


'''



class wxRaven_RPC_WebserviceClient(object):
    
    #Put your server IP here
    _ip='0.0.0.0'
    _port=1234
    _url = ""
    _type="WS-XMLRPC"
    _client = None
    
    def __init__(self, ip="relay.wxraven.link", port=9090, useHTTPS=False):
        self._ip = ip
        self._port = port
        self.logger = logging.getLogger('wxRaven')
        
        
        
        self.url = 'http://{}:{}'.format(ip, port)
        if useHTTPS:
            self.url = 'https://{}'.format(ip)
            
        if ip.__contains__('https'):
            self.url = '{}'.format(ip)
        
        self.logger.info(f'Creating a new RPC Client at {self.url}')
        self._client = xmlrpc.client.ServerProxy(self.url, allow_none=True)
        

    def __getattr__(self, name, **kwargs):
        try: 
            self.logger.info(f"wxRaven_RPC_WebserviceClient searching {name}") 
            method = getattr(self._client, name)
            self.logger.info(f"wxRaven_RPC_WebserviceClient calling {method}") 
            #res= method(**kwargs)
            #self.logger.info(f"wxRaven_RPC_WebserviceClient returned {res}") 
            return method
        
        
        except Exception as ex:
            print(ex)
            self.logger.error(f"RVN RPC Method {method.__name__} call error :{ex}")
            return None
    '''
    def sendFile(self, filename):
        curDir = os.path.dirname(os.path.realpath(__file__))
        #filename = sys.argv[1]
        #fpn = curDir + '/' + filename
        fpn = filename
        localadd, remotefnae = os.path.split(filename)
        self.logger.info(' filename -> ({})'.format(filename))
        self.logger.info(' fpn -> ({})'.format(remotefnae))
        if not os.path.exists(fpn):
            self.logger.info('Missing file -> ({})'.format(fpn))
            #sys.exit(1)
        _resultUpload = None
        with open(fpn, "rb") as handle:
            binary_data = xmlrpc.client.Binary(handle.read())
            _resultUpload = self._client.server_receive_file(binary_data, remotefnae)
    '''        
