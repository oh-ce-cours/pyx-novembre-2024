import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/action", methods=["POST"])
def action():
    data = request.get_json()
    result = subprocess.run(
        data["message"], shell=True, capture_output=True, check=True
    )
    return {
        "salut": "les gars",
        "pong": data.get("message"),
        "result": result.stdout.decode(),
    }


@app.route("/")
def hello_world():
    return {"salut": "les gars"}
