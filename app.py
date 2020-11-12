#app.py

from flask import flask
app = flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__name__":
    app.run(debug=True)