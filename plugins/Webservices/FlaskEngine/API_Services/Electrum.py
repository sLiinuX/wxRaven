'''
Created on 22 févr. 2022

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
class ElectrumView(object):
    '''
    classdocs
    '''


    route_base = '/api/'
    default_methods = ['GET', 'POST']
    
    @route('/v1/electrum/test')     
    def test(self, command=''):
        query_parameters = request.args
        
        #self.logger.info(f"request.args {request.args}")
        #self.logger.info(f"request.params {request.params}")
        
        args = extract_parameters(request.args)
        
        
        #self.logger.info(f"args {args}")
        #
        # CALL HERE THE RPC CLIENT EQUIVALENT METHOD
        # 
        '''
        command = args.get('command')
        network = self.daemon.getNetwork()
        if command == None:
            command = ''
            
        '''
        return jsonify({'result':None})  