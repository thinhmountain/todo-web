from extension import db

class tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    deadline = db.Column(db.Date, nullable = False)

    def __init__(self,title,completed,deadline):
        self.title = title
        self.completed = completed
        self.deadline = deadline
        

# class deadlines(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'),nullable=False)
#     date = db.Column(db.Date, nullable=False)

#     def __init__(self, task_id, date):
#         self.task_id = task_id
#         self.date = date
        





# class Task(db.Model):
#     __tablename__ = 'task'
    
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(200), nullable=True)
#     completed = db.Column(db.Boolean, default=False)

#     deadlines = db.relationship('Deadline', back_populates='task', cascade='all, delete-orphan')


# class Deadline(db.Model):
#     __tablename__ = 'deadlines'
    
#     id = db.Column(db.Integer, primary_key=True)
#     task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
#     date = db.Column(db.Date, nullable=False)

#     task = db.relationship('Task', back_populates='deadlines')
