import utils
from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

model = api.model(
    "Action",
    {
        "command": fields.String,
    },
)


@api.route("/action")
class Action(Resource):
    def post(self):
        data = request.get_json()
        command = data["command"]
        args, return_code, result = utils.execute_command(command)
        return {"executed_command": args, "return_code": return_code, "result": result}


if __name__ == "__main__":
    app.run(debug=True)
