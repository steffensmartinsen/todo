from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# Initialize APP and API
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

class ToDoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))
    summary = db.Column(db.String(200))

# Only need it once to create the db file
#with app.app_context():
#    db.create_all()

# Interim database
todos = {}

resource_fields = {
    'id': fields.Integer,
    'task': fields.String,
    'summary': fields.String,
}

# Request parser to ensure the correct data is sent
task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, required=True, help="Task is required")
task_post_args.add_argument("summary", type=str, required=True, help="Summary is required")

task_put_args = reqparse.RequestParser()
task_put_args.add_argument("task", type=str)
task_put_args.add_argument("summary", type=str)

# Class to return all tasks
class ToDoList(Resource):
    def get(self):
        tasks = ToDoModel.query.all()
        todos = {}
        for task in tasks:
            todos[task.id] = {"task": task.task, "summary": task.summary}
        return todos

# Class to that handles an individual task
class ToDo(Resource):
    
    @marshal_with(resource_fields)
    def get(self, todo_id):
        task = ToDoModel.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message="Could not find task with that ID")
        return task
    
    @marshal_with(resource_fields)
    def post(self, todo_id):
        args = task_post_args.parse_args()
        task = ToDoModel.query.filter_by(id=todo_id).first()
        if task:
            abort(409, message="Task ID already taken")
        
        todo = ToDoModel(id=todo_id, task=args["task"], summary=args["summary"])
        db.session.add(todo)
        db.session.commit()
        return todo, 201
    
    @marshal_with(resource_fields)
    def put(self, todo_id):
        args = task_put_args.parse_args()
        task = ToDoModel.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message="Task doesn't exist, cannot update")
        if args["task"]:
            task.task = args["task"]
        if args["summary"]:
            task.summary = args["summary"]
        db.session.commit()
        return task

    def delete(self, todo_id):
        task = ToDoModel.query.filter_by(id=todo_id).first()
        db.session.delete(task)
        db.session.commit()
        return '', 204

# Add endpoints
api.add_resource(ToDo, '/todo/<int:todo_id>')
api.add_resource(ToDoList, '/todo')

# Run the app on a local server
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
