from flask import Flask, render_template

app = Flask(__name__)

# Dummy data (Suppose this is the data we received from some database)
# Data is in the form of list of dictionaries
posts = [
    {
        'author':'Aditya Pradhan',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'April 20 2018'
    },
    {
        'author':'Ashutosh Pradhan',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'April 21 2018'
    }
]

# We can pass this data into our template
# And for that we can use jinja2 which is a powerful templating engine that flask uses
# Syntax for jinja template - https://www.tutorialspoint.com/flask/flask_templates.htm
# With jinja2 we can manipulate html, using variables, for loop, and if elif else blocks.

# Making some more data
user_data = [
    {'type':'Admin', 'age':56, 'gender':'male'},
    {'type':'Client', 'age':78, 'gender':'female'}
]

title = "About-me"

# Routes and rendered templates.
@app.route("/")
@app.route("/home")
def home():
    # Sending the posts data to the home.html template.
    home_html = render_template("home.html", posts=posts, user_data=user_data) 
    # Parameter posts is the one that will be sent, the argument passed is actual value.
    # Same with user_data.
    return home_html

@app.route("/about")
def about():
    return render_template("about.html", title=title) # Sending the title

if __name__ == "__main__":
    app.run(debug=True)