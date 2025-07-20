# Here in this app script we will learn HTTPS methods
# There are a lot of HTTPS methods but we will learn about GET and POST
# We will also learn about GETTING DATA FROM FORMS

# Short notes on GET and POST
"""
GET:
1. Used to request data from a server.
2. Data is sent in the url (as query parameters)
3. Commonly used for retrieving information (like viewing a webpage)
4. Does not modify data on the server
5. Example: When you visit a webpage by clicking a link, the browser sends a GET request
6. Not safe for sending data to the server.

POST:
1. Use to send data to the server.
2. Data is included in the body of the request, not in the URL.
3. Commonly used for submitting forms (like login, registration).
4. Usually changes or adds data on the server.
5. Example: When you fill out and submit a form, like a signup or contact form, a POST request is made.
"""

from flask import Flask
from flask import render_template, request
from flask import redirect, url_for

# The request object of the flask helps us to get the data sent by the client.
# Client can referred as a web browser.
# The request object of the flask helps to get the data sent by client and send it to our flask application working in the serverside/backend.

# With the help of this request object, we can access the following:
# 1. Form data (request.form)
# 2. Query parameters (request.args)
# 3. Request methods: HTTPS methods used, like GET or POST (request.method)
# 4. Cookies: Any cookies send by the client (request.cookies)
# 5. Uploaded files: Access to files sent by user (request.files)

app = Flask(__name__)

# Let's make some dummy data to validate user login
# Let's call the dictionary database

database = {
    'adityapradhan202@gmail.com':['mypass1234', 'Aditya Pradhan'],
    'aadi998@gmail.com':['idontlike#ML', "Aadi Bhardwaj"],
    'devansh567@gmail.com':['cppgood!pythontrash', "Devansh Dahiya"],
    'jayesh67@gmail.com':['opiniontrader#45', "Jayesh Patil"]
}

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email-id")
        pswd = request.form.get("password")
        # Check if email is in db
        if email in database:
            if database[email][0] == pswd:
                # return f"Login successful! <br><h2>Welcome {database[email][1]}!<h2>"
                # redirect function redirects to the url given below with a value as query parameter
                return redirect(url_for("user_logged_in", usr=database[email][1]))

            else:
                return "Either entered email or password is wrong! Try again with the right credentials!"
        else:
            return "Email not registered!"
    # If request.method == 'GET' (When we are visiting the /login route)
    else:
        return render_template("login.html")

# Let's create a redirect page
# User will be redirected to this page once logged in

# Query parameter that we send in login route, will be passed here in usr variable
# And variable rule will be followed
@app.route("/<string:usr>") # /login/user_name
def user_logged_in(usr):
    return render_template("logged_in.html", user=usr)


if __name__ == "__main__":
    app.run(debug=True)