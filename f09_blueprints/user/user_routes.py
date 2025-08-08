from flask import Blueprint
from flask import render_template

# we need to make our blue print object
# 'user' here is just a name, used as a label by flask to organize errors
# __name__ represents the name of the file/current file where our code related to this blue print obj is there
userBP = Blueprint('user', __name__)

# a blueprint object helps us to break our whole app into reusable components
# a blueprint holds different routes and methods in it
# these methods are called in main app file
# we create blue print here, then we register it on the main app

@userBP.route("/content")
def content():
    return render_template("content.html")

@userBP.route("/playlists")
def playlists():
    return render_template("playlists.html")

