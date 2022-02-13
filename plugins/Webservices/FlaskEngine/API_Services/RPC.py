'''
Created on 9 févr. 2022

@author: slinux
'''
import flask
from flask import request, jsonify
from .wxFlaskCustomView import * 
from flask_classful import route
#
#
# This file must be imported WITHIN a specific context
#
#
class RPCView(wxCustomFlaskView):
    route_base = '/api/'
    default_methods = ['GET', 'POST']
    
    @route('/v1/RPC/help')     
    def help(self, command=''):
        query_parameters = request.args
        
        #self.logger.info(f"request.args {request.args}")
        #self.logger.info(f"request.params {request.params}")
        
        args = extract_parameters(request.args)
        
        
        #self.logger.info(f"args {args}")
        command = args.get('command')
        network = self.daemon.getNetwork()
        if command == None:
            command = ''
        return jsonify(network.help(command))  
        '''
        if request.method == 'POST':
            
            if command =='':
                query_parameters = request.args 
                command = query_parameters.get('command')
                
            print(f"GET name {command}")
        else:
            pass
        network = self.daemon.getNetwork()
        
        if command == None:
            command = ''
        return jsonify(network.help(command))    
        '''
     
     
    '''  
    @route('/v1/RPC/help/<command>')     
    def help_cmd(self, command=''):
        network = self.daemon.getNetwork()
        return jsonify(network.help(command))
    '''
    
    
    #def listassets(self, asset="*", verbose=False, count=999999, start=0 ):
    @route('/v1/RPC/listassets') 
    def listassets(self , asset="*", verbose=False, count=999999, start=0):
        
        query_parameters = request.args
        args = extract_parameters(request.args)
        
        #print(args.get('asset'))
        #print(asset)
        assetname = args.get('asset', asset)
        verbose = args.get('verbose', verbose )
        count = args.get('count', count )
        start = args.get('start', start)
        
        #print(assetname)
        
        network = self.daemon.getNetwork()
        result = network.listassets(assetname ,verbose,count,start)
        return jsonify(result)
    
    
    #
    #
    #
    
    
    #def listassetbalancesbyaddress(self,address, onlytotal=False, count=50000, start=0):
    @route('/v1/RPC/listassetbalancesbyaddress') 
    def listassetbalancesbyaddress(self,address='*', onlytotal=False, count=50000, start=0):
        query_parameters = request.args
        args = extract_parameters(request.args)
        
        address = args.get('address', address)
        onlytotal = args.get('onlytotal', onlytotal )
        count = args.get('count', count )
        start = args.get('start', start)
        
        network = self.daemon.getNetwork()
        result = network.listassetbalancesbyaddress(address ,onlytotal,count,start)
        return jsonify(result)
    
    
    
    
    #def listaddressesbyasset(self, asset_name, onlytotal=False, count=50000, start=0):
    @route('/v1/RPC/listaddressesbyasset') 
    def listaddressesbyasset(self,asset_name='*', onlytotal=False, count=50000, start=0):
        query_parameters = request.args
        args = extract_parameters(request.args)
        
        asset_name = args.get('asset_name', asset_name)
        onlytotal = args.get('onlytotal', onlytotal )
        count = args.get('count', count )
        start = args.get('start', start)
        
        network = self.daemon.getNetwork()
        result = network.listaddressesbyasset(asset_name ,onlytotal,count,start)
        return jsonify(result)
    
    
    
    #def getaddressbalance(self,searchAdressListJSON ,showAsset=True):
    @route('/v1/RPC/getaddressbalance') 
    def getaddressbalance(self,addresses ={'addresses': []},showAsset=True):
        query_parameters = request.args
        args = extract_parameters(request.args)
        
        searchAdressListJSON = args.get('addresses', addresses)
        showAsset = args.get('showAsset', showAsset )
        
        
        network = self.daemon.getNetwork()
        result = network.getaddressbalance(searchAdressListJSON ,showAsset)
        return jsonify(result)
    
    
    
    #def validateaddress(self, address):
    @route('/v1/RPC/validateaddress') 
    def validateaddress(self,address='' ):
        query_parameters = request.args
        args = extract_parameters(request.args)
        
        address = args.get('address', address)
        
        
        
        network = self.daemon.getNetwork()
        result = network.validateaddress(address)
        return jsonify(result)
    
    
    
    #def getaddressdeltas(self, searchAdressListJSON):
    @route('/v1/RPC/getaddressdeltas') 
    def getaddressdeltas(self,addresses={'addresses': []} ):
        query_parameters = request.args
        args = extract_parameters(request.args)
        
        addresses = args.get('addresses', addresses)
        
        
        network = self.daemon.getNetwork()
        result = network.getaddressdeltas(addresses)
        return jsonify(result)
    
    
    #def gettxout(self, txId, out):
    @route('/v1/RPC/gettxout') 
    def gettxout(self, txId='', out=0):
        query_parameters = request.args
        args = extract_parameters(request.args)
        
        txId = args.get('txId', txId)
        out = args.get('out', out)
        
        
        network = self.daemon.getNetwork()
        result = network.gettxout(txId, out)
        return jsonify(result)
    
    
    
    #def decoderawtransaction(self, hexstring):
    @route('/v1/RPC/decoderawtransaction') 
    def decoderawtransaction(self, hexstring=''):
        query_parameters = request.args
        args = extract_parameters(request.args)
        
        hexstring = args.get('hexstring', hexstring)
        
        network = self.daemon.getNetwork()
        result = network.decoderawtransaction(hexstring)
        return jsonify(result)
    
    
    
    #def getrawtransaction(self, txid, verbose=False):
    @route('/v1/RPC/getrawtransaction') 
    def getrawtransaction(self, txid='', verbose=False):
        query_parameters = request.args
        args = extract_parameters(request.args)
        
        txid = args.get('txid', txid)
        verbose = args.get('verbose', verbose)
        
        network = self.daemon.getNetwork()
        result = network.getrawtransaction(txid, verbose)
        return jsonify(result)
    
    
    
    
    #def getblockhash(self, bHeight):
    @route('/v1/RPC/getblockhash') 
    def getblockhash(self, height=0):
        query_parameters = request.args
        args = extract_parameters(request.args)
        
        height = args.get('height', height)
        
        network = self.daemon.getNetwork()
        result = network.getblockhash(height)
        return jsonify(result)
    
    
    
    #def getblockhash(self, bHeight):
    @route('/v1/RPC/getblock') 
    def getblock(self , hash='', verbose=False):
        query_parameters = request.args
        args = extract_parameters(request.args)
        
        hash = args.get('hash', hash)
        verbose = args.get('verbose', hash)
        
        network = self.daemon.getNetwork()
        result = network.getblock(hash, verbose)
        return jsonify(result)
    
    
    #def getassetdata(self, asset):
    @route('/v1/RPC/getassetdata') 
    def getassetdata(self, asset='*'):
        query_parameters = request.args
        args = extract_parameters(request.args)
        
        asset = args.get('asset', asset)
        
        
        network = self.daemon.getNetwork()
        result = network.getassetdata(asset)
        return jsonify(result)
    
    """
    
   
    

    
    
    def decoderawtransaction(self, hexstring):
    def getrawtransaction(self, txid, verbose=False):
    
    
    def getblockhash(self, height):
    def getblock(self, bHash, verbose=False):
    def getassetdata(self):
        
    """
    
    
    
    
    