from flask import Blueprint
from .service import create_task_service
from .service import get_task_by_id_service,get_all_task_service
from .service import update_task_by_id_service
from .service import delete_task_by_id_service

create = Blueprint('create_task', __name__)
read = Blueprint('read_task', __name__)
update = Blueprint('update_task', __name__)
delete = Blueprint('delete_task', __name__)



# add task
@create.route('/task/create-task', methods = ['POST'])
def create_task():
    return create_task_service()


#get task by id, get all task
@read.route('/task/get-task/<int:id>', methods = ['GET'])
def get_task_by_id(id):
    return get_task_by_id_service(id)

@read.route('/task/get-task/all', methods = ['GET'])
def get_all_task():
    return get_all_task_service()


# update task by id
@update.route('/task/update-task/<int:id>', methods = ['PUT'])
def update_task_by_id(id):
    return update_task_by_id_service(id)


# deleted task by id
@delete.route('/task/delete-task/<int:id>', methods  = ['DELETE'])
def delete_task_by_id(id):
    return delete_task_by_id_service(id)


