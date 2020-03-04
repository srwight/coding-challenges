'''
This module builds the Flask app
'''

from flask import Flask
from server.routes import SIMPLE_BLUEPRINT
from server.errors import   bad_request_400,\
                            unknown_404,\
                            wrong_method_405,\
                            teapot_418

def register_blueprints(app):
    '''
    Registeres blueprints
    '''
    app.register_blueprint(SIMPLE_BLUEPRINT)

def register_errorhandlers(app):
    '''
    registers error handlers
    '''
    app.register_error_handler(400, bad_request_400)
    app.register_error_handler(404, unknown_404)
    app.register_error_handler(405, wrong_method_405)
    app.register_error_handler(418, teapot_418)

def create_app(config_filename=None):
    '''
    Creates Flask app using the supplied configuration file
    '''
    flask_app = Flask(__name__, instance_relative_config=False)
    flask_app.config.from_pyfile(config_filename)
    register_blueprints(flask_app)
    register_errorhandlers(flask_app)
    return flask_app
