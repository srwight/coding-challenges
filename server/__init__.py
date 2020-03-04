from flask import Flask
from server.routes import simple_blueprint
from server.errors import   bad_request_400,\
                            unknown_404,\
                            wrong_method_405,\
                            teapot_418

def register_blueprints(app):
    app.register_blueprint(simple_blueprint)

def register_errorhandlers(app):
    app.register_error_handler(400,bad_request_400)
    app.register_error_handler(404,unknown_404)
    app.register_error_handler(405,wrong_method_405)
    app.register_error_handler(418,teapot_418)

def create_app(config_filename=None):
    flask_app = Flask(__name__, instance_relative_config=False)
    flask_app.config.from_pyfile(config_filename)
    register_blueprints(flask_app)
    register_errorhandlers(flask_app)
    return flask_app

