from flask import Flask

app = Flask(__name__)


@app.route("/action", methods=["GET", "POST"])
def action():
    1 / 0
    return {"salut": "les gars"}


@app.route("/")
def hello_world():
    return {"salut": "les gars"}
