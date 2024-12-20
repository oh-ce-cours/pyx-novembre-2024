from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/<string:name>")
def hello_world(name="default"):
    return f"<p>Hello {name}!</p>"
