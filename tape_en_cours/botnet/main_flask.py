from flask import Flask

app = Flask(__name__)


@app.route("/<string:name>")
def hello_world(name):
    return f"<p>Hello {name}!</p>"
