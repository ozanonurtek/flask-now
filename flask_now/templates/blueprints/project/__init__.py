from flask import Flask
from .config import Config
# If you have db:
# from .models import db

# Initialize your extensions here:
# login_manager = LoginManager()


def create_app(config=Config):
    # Init app
    app = Flask(__name__)
    app.config.from_object(config)
    # Init extensions
    # Init app for your extensions. Example:
    # login_manager.init_app(app)
    # Initialize db:
    # db.init_app(app)

    register_blueprints(app)
    return app



def register_blueprints(app):
    from project.blueprints.index.controller import bp_index as index_module

    app.register_blueprint(index_module)
