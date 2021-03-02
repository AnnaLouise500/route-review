import json
import os
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# index
@app.route("/")
def index():
    return render_template("index.html")


# create
@app.route("/review")
def review():
    return render_template("review.html")


# add route
@app.route("/addroute")
def addroute():
    return render_template("addroute.html")


# login
@app.route("/login")
def login():
    return render_template("login.html")


# createlogin
@app.route("/createlogin")
def createlogin():
    return render_template("createlogin.html")


# search
@app.route("/search")
def search():
    return render_template("search.html")


# route record
@app.route("/routerecord")
def routerecord():
    data = []
    with open("data/routerecords.json") as json_data:
        data = json.load(json_data)
    return render_template("routerecord.html", routerecorddata=data)


# @app.route("/##")
# def about():
#    data = []
#    with open("data/company.json", "r") as json_data:
#        data = json.load(json_data)
#    return render_template("about.html", page_title="About", company=data)


# @app.route("/about/<member_name>")
# def about_member(member_name):
#    member = {}
#    with open("data/company.json", "r") as json_data:
#        data = json.load(json_data)
#        for obj in data:
#            if obj["url"] == member_name:
#                member = obj
#    return render_template("member.html", member=member)


# @app.route("/contact", methods=["GET", "POST"])
# need to add this if want to do any forms within this HTML page
# def contact():
#    if request.method == "POST":
#        flash("Thanks {}, we have received your message".format(
#           request.form.get("name")))
#    return render_template("contact.html", page_title="Contact")


# @app.route("/careers")
# def careers():
#    return render_template("careers.html", page_title="Careers")
# page type is a variable name


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
# never use debug=true in a testing environment not in a submitted project
