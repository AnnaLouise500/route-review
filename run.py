import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/create")
def create():
    return render_template("create.html")


@app.route("/addroute")
def addroute():
    return render_template("addroute.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)