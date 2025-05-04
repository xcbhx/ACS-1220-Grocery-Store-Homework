from flask import Flask
from grocery_app.extensions import db, login_manager, bcrypt
from grocery_app.routes import main
from grocery_app.config import Config
from grocery_app.models import User

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  # Initialize extensions
  db.init_app(app)
  login_manager.init_app(app)
  bcrypt.init_app(app)

  # Set login view
  login_manager.login_view = 'auth.login'

  # User loader
  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(int(user_id))

  app.register_blueprint(main)

  return app