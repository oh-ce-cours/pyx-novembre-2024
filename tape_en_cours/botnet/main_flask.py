from flask import Flask, request

app = Flask(__name__)


@app.route("/action", methods=["POST"])
def action():
    data = request.get_json()
    return {"salut": "les gars", {"pong": data}}


@app.route("/")
def hello_world():
    return {"salut": "les gars"}
