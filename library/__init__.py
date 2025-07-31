from flask import Flask,request,Blueprint
from extension import db, ma
from library import config
from model import tasks
import os


def create_db(app):
    db_path = 'to-do-list.db'  # hoặc 'instance/to-do-list.db'
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
            print("Database created successfully.")

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    ma.init_app(app)
    create_db(app)
    return app


