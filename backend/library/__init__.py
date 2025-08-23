from flask import Flask,request,Blueprint
from extension import db, ma
from library import config
from model import tasks
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from model import users as User


BASE_DIR = os.path.abspath(os.path.dirname(__file__))




def create_db(app):
    db_path = 'to-do-list.db' 
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
            print("Database created successfully.")

def create_app():
    app = Flask(
        __name__,
        template_folder="/Users/thinhmountain/Desktop/to-do-list-api/frontend/templates",
        static_folder=os.path.join(BASE_DIR, "/Users/thinhmountain/Desktop/to-do-list-api/frontend"))
   
    # add
    bcrypt = Bcrypt(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login_task.login_page"
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    app.config.from_object(config)
    db.init_app(app)
    ma.init_app(app)
    create_db(app)
    return app


