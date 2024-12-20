from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


@api.route("/action")
class Action(Resource):
    def post(self, todo_id):
        todos[todo_id] = request.form["data"]
        return {todo_id: todos[todo_id]}


if __name__ == "__main__":
    app.run(debug=True)
