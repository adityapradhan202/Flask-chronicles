# explaination is exactly same user package

from flask import Blueprint
from flask import render_template

authBp = Blueprint('authuser', __name__)

@authBp.route("/login")
def login():
    return render_template("login.html")