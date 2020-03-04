'''
This module provides error capturing routines for errors raised by this server
'''
from flask import request, render_template

def bad_request_400(err):
    '''
    Receives error message and returns error information
    '''
    return {'error':'Your JSON string does not match the required format.',
            'format':'One array containing nine arrays, each of which contains \
                     nine elements that are either numerals or single spaces',
            'text':str(err)}, 400

def unknown_404(err):
    '''
    Receives error message and returns error information
    '''
    if request.is_json:
        return {'error':str(err)}, 404
    return render_template('error_404.html'), 404

def wrong_method_405(err):
    '''
    Receives error message and returns error information
    '''
    if request.is_json:
        return {'error':str(err)}, 405
    return render_template('error_405.html'), 405

def teapot_418(err):
    '''
    Receives error message and returns error information
    '''
    return render_template('error_418.html', error=str(err)), 418
