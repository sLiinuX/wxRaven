'''
Created on 6 mars 2022

@author: slinux
'''



import flask
from flask import request, jsonify
from .wxFlaskCustomView import * 
from flask_classful import route
import functools
from flask import Flask, redirect, url_for
import secrets

class WebserviceUserTokenProviderView(wxCustomFlaskView):
    '''
    classdocs
    '''
    route_base = '/api/'
    
    
    '''
    def __GetUserTokenQueryCount__(self, usertoken):
        _res = 0
        
        if user_tokens_query_count.__contains__(usertoken):
            self._lock.acquire()
            _res = user_tokens_query_count[usertoken]
            self._lock.release()
        
        return _res
    
    def __NewUserToken__(self, maxQueries=100):
        self._lock.acquire()
        _newToken = secrets.token_urlsafe(16)
        user_tokens.append(_newToken)
        user_tokens_query_count[_newToken] = maxQueries
        self._lock.release()
        return _newToken
        
    '''
    
    def __newPrivateTokenJob__(self, tokenID):
        factory = self.daemon.__RemoteJobFactory__()
        self.logger.info('__newPrivateTokenJob__')
        self.logger.info(f'Factory = {factory}')
        
        _result = {'token':tokenID,
                   'job':None
            }
        
        if factory !=None:
            _m= 'plugins.Webservices.jobs.RemoteJobs_CreatePrivateToken'
            _c = 'Job_CreatePrivateWsTokenRemoteJob_ServerProcess'
            
            _jobKey = factory.__CreateServerSideJob__(_pluginName="Webservices", _class=_c , _module=_m , _jobparams={'_inputToken':tokenID})
            _result['job'] = _jobKey
        
        
        return _result
    
    
    def __generateNewToken__(self, private=False):
        
        _userTokenSize=self.daemon.max_query_size_mb_user
        _newToken = self.__NewUserToken__(_userTokenSize)
        
        _result = _newToken
        
        if private:
            _jobDatas = self.__newPrivateTokenJob__(_newToken)
            _result  = _jobDatas
            
        
        
        return _result
    
    
    
    @route('/v1/wsusertkprovider/getuserwstoken')     
    def getuserwstoken(self , private=False):
        
        query_parameters = request.args
        args = extract_parameters(request.args)
        uuid = args.get('uuid')
        private = args.get('private')
        
        _sessionType = 'USER'
        if private:
            _sessionType = 'USER PRIVATE'
        self.logger.info(f"New {_sessionType} session token request from {uuid}")
        
        if uuid != None:
            
            
            
            _newToken = self.__generateNewToken__(private)
            #_newToken = self.__NewUserToken__(_userTokenSize)
            
            
            
            
            return jsonify(self.returnJSON(_newToken))
        else:
            return self.returnJSONError('Invalid request or missing GUID', 900)
    
    
    @route('/v1/wsusertkprovider/checkuserwstoken')     
    def checkuserwstoken(self,checktoken='' ):
        query_parameters = request.args
        args = extract_parameters(request.args)
        checktoken = args.get('checktoken')
        _valid=False
        _res = 0
        _resFriendly = '0 Mb'
        if checktoken != None:
            _res = self.__GetUserTokenQueryCount__(checktoken)
            _resFriendly = self.daemon.convert_size(_res)
            if _res>0:
                _valid = True
        
        if not _valid:
                _res = self.daemon.max_query_size_mb_anonymous
                _resFriendly = self.daemon.convert_size(_res)
            
        return self.returnJSON({'valid':_valid, 'size':_res , 'size_friendly':_resFriendly})
    
    
    @auth_required
    @route('/v1/wsusertkprovider/testconsume')     
    def testconsume(self, consumesize=1):
        query_parameters = request.args
        args = extract_parameters(request.args)
        token = args.get('token')
        
        c = self.__GetUserTokenQueryCount__(token)
        c = c - consumesize
        self.__SetUserTokenSize__(token, c)
        
        return self.returnJSON(f"Consumed {c}")
    
    