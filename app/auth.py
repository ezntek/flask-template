from flask import *

auth = Blueprint('auth', __name__)
@auth.route("/")
def authindex():
    return "<h1>auth</h1>"