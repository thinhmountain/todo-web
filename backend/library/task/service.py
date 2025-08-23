from flask import request, jsonify, render_template, redirect, url_for,session
from extension import db
from library.task_schema import Task_Schema
from model import tasks, users
from sqlalchemy import func
import json
from datetime import datetime
from flask_login import login_user, logout_user

task_schema = Task_Schema()
task_schemas = Task_Schema(many=True)




# GET METHOD
def get_task_by_id_service(id):
    task = tasks.query.get(id)
    if task:
        return task_schema.jsonify(task)
    else:
        return jsonify({"message": f"Not found this task!"}), 404

def get_all_task_service():
    all_tasks = tasks.query.all()
    if all_tasks:
        print(all_tasks)
        return task_schemas.jsonify(all_tasks)
    else:
        return jsonify({"message": f"Not found any task!"}), 404
    

# POST METHOD, ADD TASK
def create_task_service():
    title = request.form.get("title")
    deadline = request.form.get('deadline')
    completed = False
    
    if title and deadline:
        new_task = tasks(title=title,
                        deadline=datetime.strptime(deadline, "%Y-%m-%d").date(),
                        completed=completed)
        db.session.add(new_task)
        db.session.commit()
    

    return redirect(url_for('todo_task.todo_page'))


# UPDATE METHOD, UPDATE CHECKBOX
def update_task_by_id_service(id):
    task = tasks.query.get(id)
    if not task:
        return jsonify({"message": "Task not found!"}), 404

    # lấy dữ liệu từ form (checkbox)
    completed = request.form.get("completed")

    # checkbox chỉ gửi khi nó được tick
    task.completed = True if completed == "on" else False

    db.session.commit()
    return redirect(url_for("todo_task.todo_page"))



# DELETE METHOD, DELETE TASK
def delete_task_by_id_service(id):
    task = tasks.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for("todo_task.todo_page"))
    else:
        return redirect(url_for("todo_task.todo_page"))




# LOGIN
def login_service():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        password = request.form.get("password")

        user = users.query.filter_by(fullname=fullname).first()

        if user and user.check_password(password):
            login_user(user)  
            return redirect(url_for('todo_task.todo_page'))
        else:
            return render_template('login.html', error = 'Invalid user')
    return render_template('login.html')


# LOGOUT
def logout_service():
    logout_user()
    return redirect(url_for('login_task.login_page'))


# REGISTER
def register_service():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        password = request.form.get("password")
        email = request.form.get("email")
        password_confirmation = request.form.get("password_confirmation")


        new_user = users(fullname=fullname, password=password,email=email,password_confirmation=password_confirmation)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login_task.login_page"))

    return render_template("register.html")



