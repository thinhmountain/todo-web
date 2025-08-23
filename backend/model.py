from extension import db
from flask_bcrypt import Bcrypt,bcrypt
from flask_login import UserMixin

class tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    deadline = db.Column(db.Date, nullable = False)

    def __init__(self,title,completed,deadline):
        self.title = title
        self.completed = completed
        self.deadline = deadline
        

class users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    password_confirmation = db.Column(db.String(10), nullable=False)

    def __init__(self,fullname,password,email,password_confirmation):
        self.fullname = fullname
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.email = email
        self.password_confirmation = bcrypt.hashpw(password_confirmation.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        

    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))







