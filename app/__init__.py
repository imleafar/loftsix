from flask import Flask
from app import routes


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(routes.bp)
    return app