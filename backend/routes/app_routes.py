from flask import Flask
from config import Config
from .cats_routes import cats_routes
from models import db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, support_credentials=False)

    app.register_blueprint(cats_routes)

    app.config.from_object(Config)
    db.init_app(app)

    return app
