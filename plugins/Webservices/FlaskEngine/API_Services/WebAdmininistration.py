'''
Created on 9 févr. 2022

@author: slinux
'''



import flask
from flask import request, jsonify
from .wxFlaskCustomView import * 
from flask_classful import route
import functools
from flask import Flask, redirect, url_for
#
#
# This file must be imported WITHIN a specific context
#
#
'''
session = []


def login_required(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            print("You need to login first")
            return redirect(url_for('login_page'))

    return wrap

'''



class WebAdmininistrationView(wxCustomFlaskView):
    route_base = '/api/'


    decorators = [login_required]
    
    
    @route('/v1/admin/shutdown_server')   
    def shutdown_server(self, **kwargs):
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
   
    def this_is_secret(self):
        #if not self.daemon.__CheckLogin__():
        #    return jsonify(self.returnJSONError("Not Authorized. - this_is_secret"))
            
        return jsonify(self.returnJSON("OK !"))
    
    
    def so_is_this(self):
        return "Looking at me? I guess you're logged in."
    
    
    