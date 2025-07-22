# Just practicing some css
# And redirect method, and variable rule

from flask import Flask
from flask import render_template, url_for
from flask import request, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        return redirect(url_for('user', email=email, password=password))
    else:
        # if the request.method is get(When we are visiting /login)
        return render_template("login.html")
    
# But when the user will be redirected to this route, info will appende to the url
# Which can be considered as unsafe
@app.route("/<string:email>/<string:password>")
def user(email, password):
    # Print in the console
    print("-> Login succesful!")
    return render_template('user.html', id=email, pswd=password)

if __name__ == "__main__":
    app.run(debug=True)