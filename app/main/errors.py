from flask import render_template
from . import main

@main.errorhandler(404)
def notFoundError(error):
    
    return render_template('notfound.html'),404


@main.app_errorhandler(404)
def four_Ow_four(error):
    
    return render_template('404.html'),404