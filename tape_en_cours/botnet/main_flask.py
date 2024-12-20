from flask import Flask

app = Flask(__name__)


@app.route("/<name:str>")
def hello_world(name):
    return f"<p>Hello {name}!</p>"
