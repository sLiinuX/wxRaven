'''
Created on 8 févr. 2022

@author: slinux
'''
from flask_classful import *
from flask_classful import route
import functools
from flask import Flask, redirect, url_for
from flask import request, jsonify

import logging

import json




#logger = logging.getLogger('wxRaven-Webservices')

admin_tokens = []
user_tokens = ['wxravenuser']

import secrets
_newToken = secrets.token_urlsafe(16)
admin_tokens.append(str(_newToken))
#logger.info(f"AUTO-GENERATED security token in {__name__} : {_newToken}")

#
# user must be ADMIN
#
def login_required(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        query_parameters = request.args
        
        argsDtas = extract_parameters(request.args)

        token = argsDtas.get('token', '')
        #token = query_parameters.get('token')
        
        
        logging.info(f"Token : {token}")
        _noAuthRequired = False
        _validToken = False
                
        if len(admin_tokens) == 0:
            _noAuthRequired = True
        else:    
            if token in admin_tokens :
                _validToken = True
                           
                    
                
                
        if _noAuthRequired or _validToken:
            return f(*args, **kwargs)
        else:
                    #print("You need to login first")
            return jsonify( {'result':None, 'error': { 'code' : 99 , 'message': 'Not Allowed or invalid token.'}})
        

    return wrap





def extract_parameters(parms):
    
    #logging.error(f'extract_parameters : {parms}') 
    newDict={}
    for key in parms.copy():
        #print(f"{key} = {type(key)}")
        
        try: 
            convertedData = json.loads(key.replace('\'','"'))
            #print(f"converted = {type(convertedData)}")
            if type(convertedData) is dict:
                for _key in convertedData:
                    newDict[_key] = convertedData[_key]
            
        except Exception as e:
            newDict[key] = parms[key]
            #logging.error(f'extract_parameters ERROR : {e}') 
    
    
    logging.info(f'extract_parameters : {newDict}') 
    return newDict






#
# user must be known
#
def auth_required(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        query_parameters = request.args
        token = query_parameters.get('token')
        
        logging.getLogger('wxRaven-Webservices').info(f"auth_required with the token : {token}")
        
        
        
        _noAuthRequired = False
        _validToken = False
                
        if len(admin_tokens) == 0:
            _noAuthRequired = True
        else:    
            if token in user_tokens :
                _validToken = True
                           
                    
                
                
        if _noAuthRequired or _validToken:
            return f(*args, **kwargs)
        else:
            #logger = logging.getLogger('wxRaven-Webservices')
            logging.getLogger('wxRaven-Webservices').warning(f"Invalid authentification : {token}")
            return jsonify( {'result':None, 'error': { 'code' : 99 , 'message': 'Not Allowed or invalid token.'}})
        

    return wrap







class wxCustomFlaskView(FlaskView):
    '''
    classdocs
    '''
    excluded_methods = ['returnNoneJSON', 'returnJSON','returnJSONError','returnJSON_ServiceNotAvailableOnNetwork','returnJSON_NotImplemented']

    def __init__(self, daemon):
        '''
        Constructor
        '''
        self.logger = logging.getLogger('wxRaven-Webservices')
        self.daemon = daemon
        self.wxRavenInstance = daemon.wxRavenInstance
        self.app = daemon.app
        
        if self.daemon.admintoken != '':
            self.logger.info(f'Admin Token Detected {self.daemon.admintoken} !')
            admin_tokens.append(self.daemon.admintoken)
    
    
    
    
        
    def returnNoneJSON(self):
        _JSON_RPC_Result = {'result': None}
        return _JSON_RPC_Result
    
    def returnJSON(self, result, error=None):
        _JSON_RPC_Result = {'result': result, 'error':error}
        return _JSON_RPC_Result
     
    def returnJSONError(self, errormsg): 
        return self.returnJSON(None, {'code':-1, 'message':errormsg})
     
    def returnJSON_ServiceNotAvailableOnNetwork(self):
        return self.returnJSONError('Feature Not available on this network')
    
    def returnJSON_NotImplemented(self, fct):
        return self.returnJSONError(f'The {fct} method is not implemented')
    
    
    
    
    
    @classmethod
    def register(cls, app, route_base=None, subdomain=None, route_prefix=None,
                 trailing_slash=None, method_dashified=None, base_class=None, daemon=None, **rule_options):
        """Registers a FlaskView class for use with a specific instance of a
        Flask app. Any methods not prefixes with an underscore are candidates
        to be routed and will have routes registered when this method is
        called.

        :param app: an instance of a Flask application

        :param route_base: The base path to use for all routes registered for
                           this class. Overrides the route_base attribute if
                           it has been set.

        :param subdomain:  A subdomain that this registration should use when
                           configuring routes.

        :param route_prefix: A prefix to be applied to all routes registered
                             for this class. Precedes route_base. Overrides
                             the class' route_prefix if it has been set.
        :param trailing_slash: An option to put trailing slashes at the end of
                               routes without parameters.
        :param method_dashified: An option to dashify method name from
                                 some_route to /some-route/ route instead of
                                 default /some_route/
        :param base_class: Allow specifying an alternate base class for customization instead of the default FlaskView
        :param rule_options: The options are passed to 
                                :class:`~werkzeug.routing.Rule` object.
        """

        if cls is FlaskView:
            raise TypeError(
                "cls must be a subclass of FlaskView, not FlaskView itself")

        if not base_class:
            base_class = FlaskView

        if route_base:
            cls.orig_route_base = cls.route_base
            cls.route_base = route_base

        if route_prefix:
            cls.orig_route_prefix = cls.route_prefix
            cls.route_prefix = route_prefix

        if not subdomain:
            if hasattr(app, "subdomain") and app.subdomain is not None:
                subdomain = app.subdomain
            elif hasattr(cls, "subdomain"):
                subdomain = cls.subdomain

        if trailing_slash is not None:
            cls.orig_trailing_slash = cls.trailing_slash
            cls.trailing_slash = trailing_slash

        if method_dashified is not None:
            cls.orig_method_dashified = cls.method_dashified
            cls.method_dashified = method_dashified

        members = get_interesting_members(base_class, cls)

        for name, value in members:
            proxy = cls.make_proxy_method(name, daemon)
            route_name = cls.build_route_name(name)
            try:
                if hasattr(value, "_rule_cache") and name in value._rule_cache:
                    for idx, cached_rule in enumerate(value._rule_cache[name]):
                        rule, options = cached_rule
                        rule = cls.build_rule(rule)
                        sub, ep, options = cls.parse_options(options)

                        if not subdomain and sub:
                            subdomain = sub

                        if ep:
                            endpoint = ep
                        elif len(value._rule_cache[name]) == 1:
                            endpoint = route_name
                        else:
                            endpoint = "{0!s}_{1:d}".format(route_name, idx)
                        # print '1 - {0!s}'.format(rule)
                        app.add_url_rule(
                            rule, endpoint, proxy,
                            subdomain=subdomain, **options)

                elif name in cls.special_methods:
                    methods = cls.special_methods[name]

                    rule = cls.build_rule("/", value)
                    if not cls.trailing_slash and rule != '/':
                        rule = rule.rstrip("/")
                    elif cls.trailing_slash is True and rule.endswith('/') is False:
                        rule = '{0!s}/'.format(rule)
                    # print '2 - {0!s}'.format(rule)
                    app.add_url_rule(
                        rule, route_name, proxy,
                        methods=methods, subdomain=subdomain, **rule_options)

                else:
                    methods = getattr(cls, 'default_methods', ["GET"])

                    if cls.method_dashified is True:
                        name = _dashify_underscore(name)

                    route_str = '/{0!s}/'.format(name)
                    if not cls.trailing_slash:
                        route_str = route_str.rstrip('/')
                    rule = cls.build_rule(route_str, value)
                    if cls.trailing_slash is True and rule.endswith('/') is False:
                        rule = '{0!s}/'.format(rule)
                    # print '3 - {0!s}'.format(rule)
                    app.add_url_rule(
                        rule, route_name, proxy, subdomain=subdomain,
                        methods=methods, **rule_options)
            except DecoratorCompatibilityError:
                raise DecoratorCompatibilityError(
                    "Incompatible decorator detected on {0!s} in class {1!s}"
                    .format(name, cls.__name__))

        if hasattr(cls, "orig_route_base"):
            cls.route_base = cls.orig_route_base
            del cls.orig_route_base

        if hasattr(cls, "orig_route_prefix"):
            cls.route_prefix = cls.orig_route_prefix
            del cls.orig_route_prefix

        if hasattr(cls, "orig_trailing_slash"):
            cls.trailing_slash = cls.orig_trailing_slash
            del cls.orig_trailing_slash

        if hasattr(cls, "orig_method_dashified"):
            cls.method_dashified = cls.orig_method_dashified
            del cls.orig_method_dashified
            
                
        
    @classmethod
    def make_proxy_method(cls, name, daemon ):
        """Creates a proxy function that can be used by Flasks routing. The
        proxy instantiates the FlaskView subclass and calls the appropriate
        method.

        :param name: the name of the method to create a proxy for
        """

        i = cls(daemon)
        view = getattr(i, name)

        # Since the view is a bound instance method,
        # first make it an actual function
        # So function attributes work correctly
        def make_func(fn):
            @functools.wraps(fn)
            def inner(*args, **kwargs):
                return fn(*args, **kwargs)
            return inner
        view = make_func(view)

        # Now apply the class decorator list in reverse order
        # to match member decorator order
        if cls.decorators:
            for decorator in reversed(cls.decorators):
                view = decorator(view)

        @functools.wraps(view)
        def proxy(**forgettable_view_args):
            # Always use the global request object's view_args, because they
            # can be modified by intervening function before an endpoint or
            # wrapper gets called. This matches Flask's behavior.
            del forgettable_view_args

            if hasattr(i, "before_request"):
                response = i.before_request(name, **request.view_args)
                if response is not None:
                    return response

            before_view_name = "before_" + name
            if hasattr(i, before_view_name):
                before_view = getattr(i, before_view_name)
                response = before_view(**request.view_args)
                if response is not None:
                    return response

            response = view(**request.view_args)
            code, headers = None, None

            if isinstance(response, tuple):
                response, code, headers = unpack(response)

            if not isinstance(response, ResponseBase):

                if not bool(cls.representations):
                    # representations is empty, then the default is to just
                    # output what the view function returned as a response
                    response = make_response(response, code, headers)
                else:
                    # Return the representation that best matches the
                    # representations in the Accept header
                    resp_representation = request.accept_mimetypes.best_match(
                        cls.representations.keys())

                    if resp_representation:
                        response = cls.representations[
                            resp_representation
                        ](response, code, headers)
                    elif 'flask-classful/default' in cls.representations:
                        response = cls.representations['flask-classful/default'](
                            response, code, headers
                        )
                    else:
                        # Nothing adequate found, return what the view function
                        # gave us for predictability
                        response = make_response(response, code, headers)

            # If the header or code is set, regenerate the response
            elif any(x is not None for x in (code, headers)):
                # A response can be passed into `make_response` and it will set
                # the key appropriately
                response = make_response(response, code, headers)

            after_view_name = "after_" + name
            if hasattr(i, after_view_name):
                after_view = getattr(i, after_view_name)
                response = after_view(response)

            if hasattr(i, "after_request"):
                response = i.after_request(name, response)

            return response

        return proxy
    
    
def _dashify_underscore(name):
    """convert something_with_underscore into something-with-underscore"""
    return '-'.join(re.split('_', name))