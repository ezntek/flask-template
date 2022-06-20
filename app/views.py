from flask import *

views = Blueprint('views', __name__)
@views.route("/") 
def index():
    return render_template("index.html")