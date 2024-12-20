import utils
from flask import Flask, request

app = Flask(__name__)


@app.route("/action", methods=["POST"])
def action():
    data = request.get_json()
    command = data["command"]
    args, return_code, result = utils.execute_command(command)
    return {"executed_command": args, "return_code": return_code, "result": result}


@app.route("/")
def hello_world():
    return {"salut": "les gars"}
