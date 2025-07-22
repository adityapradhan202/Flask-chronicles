# This script contains the ground basics of how session work in flask applications
# The concept and logic here will be very useful!

from flask import session
from flask import url_for, redirect
from flask import request
from flask import Flask

# In order to use session we must have a session key

app = Flask(__name__)
app.secret_key = b'asdavmjk4%4*@kak' # b in from of a string converts into raw binary data

@app.route("/")
@app.route("/home")
def home():
    if "username" in session:
        return "Successfully logged in!"
    else:
        return "You are not logged in!"
    

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect(url_for('home'))
    else:
        # initially when we visit the /login route
        # visiting a link or clicking on a link means a GET request is sent to the server
        # in that case we will display the form
        return """
            <form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        """

# Route for logout
# This route will remove username from session dict, then it will immediately redirect to home
@app.route("/logout")
def logout():
    # Remove the username from session if it's there
    session.pop("username", None) 
    # pop method is of python dictionary
    # None is the default value that will be returned instead of throwing an error if key is not there in the session dictionary
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)