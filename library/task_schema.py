from  extension import ma
from marshmallow import fields

class Task_Schema(ma.Schema):
    id = fields.Integer()
    title = fields.String()
    completed = fields.Boolean()
    deadline = fields.Date()

# class Deadline_Schema(ma.Schema):
#     id = fields.Integer()
#     task_id = fields.Integer()
#     date = fields.Date()