from flask import Flask 
from config import Config
from flask_bootstrap import Bootstrap

def create_app(config_name):
    
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app