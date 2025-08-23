from flask import Blueprint, Flask, render_template, url_for, request,redirect
from .service import create_task_service
from .service import get_task_by_id_service, get_all_task_service
from .service import update_task_by_id_service
from .service import delete_task_by_id_service
from .service import register_service
from .service import login_service
from .service import logout_service
from model import tasks
from extension import db
from flask_login import login_required


create = Blueprint("create_task", __name__)
read = Blueprint("read_task", __name__)
update = Blueprint("update_task", __name__)
delete = Blueprint("delete_task", __name__)
login = Blueprint("login_task", __name__)
logout = Blueprint("logout_task" , __name__)
register = Blueprint("register_task", __name__)
todo = Blueprint('todo_task',__name__)


# add task
@create.route("/add", methods=["POST"])
def add_task():
    return create_task_service()


# get task by id, get all task
@read.route("/task/get-task/<int:id>", methods=["GET"])
def get_task_by_id(id):
    return get_task_by_id_service(id)

@read.route("/task/get-task/all", methods=["GET"])
def get_all_task():
    return get_all_task_service()


# update task by id
@update.route("/task/update-task/<int:id>", methods=["POST"])
def update_task_by_id(id):
    return update_task_by_id_service(id)

# update checkbox
@update.route("/task/toggle-complete/<int:id>", methods=["POST"])
def toggle_complete(id):
    task = tasks.query.get(id)
    if task:
        task.completed = not task.completed
        db.session.commit()
    return redirect(url_for('todo_task.todo_page'))


# deleted task by id
@delete.route("/task/delete-task/<int:id>", methods=["POST"])
def delete_task_by_id(id):
    return delete_task_by_id_service(id)



# login page
@login.route("/login", methods =["GET","POST"])
def login_page():
    return login_service()

#logout page
@logout.route('/logout', methods=["POST"])
def logout_page():
    return logout_service()

# register page
@register.route("/register", methods=["GET", "POST"])
def register_page():
    return register_service()

# todo page
# root redirect -> login
@todo.route('/')
def index():
    return redirect(url_for('login_task.login_page'))

@todo.route('/todo')
@login_required
def todo_page():
    all_tasks = tasks.query.all()
    return render_template('todo.html', tasks=all_tasks)








