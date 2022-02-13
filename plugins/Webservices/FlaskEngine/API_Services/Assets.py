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

class AssetsView(wxCustomFlaskView):
    route_base = '/api/'
    
    
    
    @route('/v1/assets/listassets/<assetname>') 
    def listassets(self, assetname):
        network = self.wxRavenInstance.getNetwork()
        result = network.listassets(assetname ,True,500, 0)
        return jsonify(result)
    '''
        p2pMarketPlugins = self.wxRavenInstance.GetPlugin('P2PMarket')
        allMarkets =  p2pMarketPlugins.getData('P2P_Market_Listing')
        if allMarkets.__contains__(id):
                    
            _market = allMarkets[id]
                    
            _listJson = {}
                    
            for key in _market:
                _listJson[key] = _market[key].JSON()
                
    '''