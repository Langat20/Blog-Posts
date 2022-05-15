from flask import render_template
from . import main

@main.app_errorhandler(404)
def not_found(error):
    '''It returns a 404 error page if page is not found'''
    return render_template('not_found.html'),404