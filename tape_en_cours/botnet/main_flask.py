from flask import Flask

app = Flask(__name__)


@app.route("/action", methods=["POST"])
def action():
    return {"salut": "les gars"}


@app.route("/")
def hello_world():
    return {"salut": "les gars"}
