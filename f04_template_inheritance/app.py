# In this particular project folder, f04_template_inheritance.
# We will create a layout, in layout.html
# Then we can reuse it again and again using tempalte inheritance.

from flask import Flask
from flask import render_template

users = [
    {
        'org':'CBI',
        'type':'authority'
    },
    {
        'org':'no-org',
        'type':'normal-client'
    }
]

app = Flask(__name__)

# Routes
@app.route("/")
@app.route("/movies")
def movies():
    return render_template("movies.html")

@app.route("/creepy")
def creepy():
    return render_template("creepy.html", users=users[0])

# There's one concept called the variable rule
# Variable rule!
# We can add variable section to the url
# And then a variable can be appended to the url section
# This makes this variable accessible inside the function
# To read more about this refer to documentation

@app.route("/user_profile/<string:user_name>") # user_name becomes the function param
def show_user_profile(user_name):
    return render_template("user_profile.html", user_name=user_name)

# In the above function the string is the type of user_name
# There are different types that we can mention, read more in official docs

if __name__ == "__main__":
    app.run(debug=True)


