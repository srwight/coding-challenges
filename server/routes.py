from flask import   request,\
                    json,\
                    url_for,\
                    abort,\
                    render_template,\
                    Blueprint
                    
# from main import app
from server.sudoku_check import sudoku_check

simple_blueprint = Blueprint('sb',__name__)

@simple_blueprint.route('/')
def home():
    return render_template("index.html")

@simple_blueprint.route('/json', methods=['POST'])
def json_endpoint():
    if not request.is_json:
        abort(418)
    data = request.get_json()
    if type(data) != list:
        print('Outer List')
        print(type(data))
        abort(400)
    if any(type(row) not in [list, str] for row in data):
        print('Inner type')
        abort(400)
    result = str(sudoku_check(data))
    return {"result":result}
