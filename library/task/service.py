from flask import request, jsonify
from extension import db
from library.task_schema import Task_Schema
from model import tasks
from sqlalchemy import func
import json
from datetime import datetime

task_schema = Task_Schema()
task_schemas = Task_Schema(many=True)


# POST METHOD
def create_task_service():
    data = request.get_json()
    title = data.get("title")
    completed = data.get("completed")
    deadline_str = data.get("deadline")
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d") 
    try:
        new_task = tasks(title, completed, deadline)
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"message": f"Add successfully!"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    

# GET METHOD
def get_task_by_id_service(id):
    task = tasks.query.get(id)
    if task:
        return task_schema.jsonify(task)
    else:
        return jsonify({ 'message' : f'Not found this task!'}), 404
    
def get_all_task_service():
    all_tasks =tasks.query.all()
    if all_tasks:
        return task_schemas.jsonify(all_tasks)
    else:
        return jsonify({'message' : f'Not found any task!'}), 404
    

# UPDATE METHOD
def update_task_by_id_service(id):
    task = tasks.query.get(id)
    data = request.json
    if task:
        if "completed" in data:
            task.completed = data['completed']
            db.session.commit()
            return jsonify({'message' : f'Updated successfully!'}), 200
    else:
        return jsonify({'message' : f'Can not update!'}) , 404
    

# DELETE TASK
def delete_task_by_id_service(id):
    task = tasks.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message" : f'Deleted task successfully!'}), 200
    else:
        return jsonify({'message' : f'Can not deleted task!'}), 404



        


