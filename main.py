from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

# Initialize APP and API
app = Flask(__name__)
api = Api(app)

# Making an interin DB
todos = {
    1: {"task": "Write hello world program.", "summary": "Write the code using pyhon."},
    2: {"task": "Task 2.", "summary": "Write Task 2."},
    3: {"task": "Task 3", "summary": "Write task 3."},
    
}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, required=True, help="Task is required")
task_post_args.add_argument("summary", type=str, required=True, help="Summary is required")

# Class to return all tasks
class ToDoList(Resource):
    def get(self):
        return todos

# Class to that handles an individual task
class ToDo(Resource):
    def get(self, todo_id):
        return todos[todo_id]
    
    def post(self, todo_id):
        args = task_post_args.parse_args()
        if todo_id in todos:
            abort(409, "Task ID already taken")
        todos[todo_id] = {"task": args["task"], "summary": args["summary"]}
        return todos[todo_id], 201

# Add endpoints
api.add_resource(ToDo, '/todo/<int:todo_id>')
api.add_resource(ToDoList, '/todo')

# Run the app on a local server
if __name__ == '__main__':
    app.run(debug=True)
