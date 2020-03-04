'''
This module defines the endpoints available on this server.
'''
from flask import   request,\
                    abort,\
                    render_template,\
                    Blueprint

from server.sudoku_check import sudoku_check

SIMPLE_BLUEPRINT = Blueprint('sb', __name__)

@SIMPLE_BLUEPRINT.route('/')
def home():
    '''
    Main landing page and documentation
    '''
    return render_template("index.html")

@SIMPLE_BLUEPRINT.route('/json', methods=['POST'])
def json_endpoint():
    '''
    Endpoint to receive json input
    '''
    if not request.is_json:
        abort(418)
    data = request.get_json()
    if not isinstance(data, list):
        abort(400)
    if any(not isinstance(row, (list, str)) for row in data):
        abort(400)
    result = str(sudoku_check(data))
    return {"result":result}
