'''
imports the app constructor and creates the app
'''
from server import create_app

app = create_app("main_config.cfg")

# from server import routes
# from server import errors
