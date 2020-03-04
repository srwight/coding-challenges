# from main import app
from flask import request, render_template

def bad_request_400(e):
    if request.is_json:
        return {'error':'Your JSON string does not match the required format.',
                'format':'One array containing nine arrays, each of which contains nine elements that are either numerals or single spaces'},400
    else:
        return render_template("error_400.html", error=e),400

def unknown_404(e):
    if request.is_json:
        return {'error':str(e)},404
    else:
        return render_template('error_404.html'), 404

def wrong_method_405(e):
    if request.is_json:
        return {'error':str(e)},405
    else:
        return render_template('error_405.html'),405

def teapot_418(e):
    if request.is_json:
        return{'error':str(e)}
    else:
        return render_template('error_418.html'),418
