'''
Created on 8 févr. 2022

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

class P2PMarketView(wxCustomFlaskView):
    route_base = '/api/'

    decorators = [auth_required]
    
   

    @route('/v1/p2pmarket/settings/')
    def settings( self):
        self.logger.info("Settings")
        query_parameters = request.args
                
        _c = self.__checkMarketEnable__()
        if _c != None:
            return _c
        else:
            #p2pMarketPlugins = self.wxRavenInstance.GetPlugin('P2PMarket')
            #allMarkets =  p2pMarketPlugins.PLUGIN_SETTINGS['p2p_markets']
            return jsonify(self.returnJSON("Administration Area Reserved"))
        
        
        
        
        
        
    @route('/v1/p2pmarket/markets/all')    
    def market_list(self ):
        self.logger.info("market_list")
        query_parameters = request.args
            
        _c = self.__checkMarketEnable__()
        if _c != None:
            return _c
        else:
            p2pMarketPlugins = self.wxRavenInstance.GetPlugin('P2PMarket')
            allMarkets =  p2pMarketPlugins.PLUGIN_SETTINGS['p2p_markets']
        return jsonify(self.returnJSON(allMarkets))
        
            #id = query_parameters.get('method')
            #published = query_parameters.get('published')
            #author = query_parameters.get('author')
            #return jsonify(self.returnJSON_ServiceNotAvailableOnNetwork())
        
    
    @route('/v1/p2pmarket/markets/<id>') 
    def get(self, id):
        p2pMarketPlugins = self.wxRavenInstance.GetPlugin('P2PMarket')
        _c = self.__checkMarketEnable__()
        if _c != None:
            return _c
        else:
            allMarkets =  p2pMarketPlugins.getData('P2P_Market_Listing')
            if allMarkets.__contains__(id):
                    
                _market = allMarkets[id]
                    
                _listJson = {}
                    
                for key in _market:
                    _listJson[key] = _market[key].JSON()
                    
                    
                    
                return jsonify(self.returnJSON(_listJson))
                
                
            else:
                return jsonify(self.returnJSONError("Unknown or unlisted market, please contact the administrator"))

    
    
    @route('/v1/p2pmarket/markets/', methods=['GET']) 
    def market_data(self):
        query_parameters = request.args
            
        name = query_parameters.get('name')
        self.logger.info(f"market_data {name}")
            
        return self.get(name)
    
    
    



    
    
    
    def __checkMarketEnable__(self):
        p2pMarketPlugins = self.wxRavenInstance.GetPlugin('P2PMarket')
        _enable =  p2pMarketPlugins.PLUGIN_SETTINGS['p2p_markets_enable']
        if not _enable:
            return jsonify(self.returnJSONError("Market is disabled"))
        else:
            return None
