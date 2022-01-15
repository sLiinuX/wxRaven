'''
Created on 5 janv. 2022

@author: slinux
'''



import sys
# The answer is that the module xmlrpc is part of python3
import xmlrpc.client
import os




class IPFS_RPC_Client(object):
    
    #Put your server IP here
    _ip='0.0.0.0'
    _port=1234
    _url = ""
    
    _client = None
    
    def __init__(self, ip="127.0.0.1", port=9000):
        self._ip = ip
        self._port = port
        self.url = 'http://{}:{}'.format(ip, port)
        self._client = xmlrpc.client.ServerProxy(self.url)



    
    def sendFile(self, filename):
        curDir = os.path.dirname(os.path.realpath(__file__))
        #filename = sys.argv[1]
        #fpn = curDir + '/' + filename
        fpn = filename
        localadd, remotefnae = os.path.split(filename)
        print(' filename -> ({})'.format(filename))
        print(' fpn -> ({})'.format(remotefnae))
        if not os.path.exists(fpn):
            print('Missing file -> ({})'.format(fpn))
            #sys.exit(1)
        _resultUpload = None
        with open(fpn, "rb") as handle:
            binary_data = xmlrpc.client.Binary(handle.read())
            _resultUpload = self._client.server_receive_file(binary_data, remotefnae)
            

        
        
        print(f'_resultUpload = {_resultUpload}')
        return _resultUpload




    def sendJSON(self, JSON):
        print(f'JSON = {JSON}')
        _resultUpload = self._client.server_receive_json(JSON)
        #print(f'_resultUpload = {_resultUpload}')
        return _resultUpload
        #.add_json(self.compile_message(message))


