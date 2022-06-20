from flask import Flask
from .views import views
from .auth import auth

def create_app() -> Flask:
    app = Flask(__name__) 
        
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")

    return app