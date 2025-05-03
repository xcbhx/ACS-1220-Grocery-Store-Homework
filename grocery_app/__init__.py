from flask import Flask
from grocery_app.extensions import db
from grocery_app.routes import main

def create_app():
  app = Flask(__name__)

  from .config import Config
  app.config.from_object(Config)

  db.init_app(app)
  app.register_blueprint(main)

  return app