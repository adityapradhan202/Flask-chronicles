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

if __name__ == "__main__":
    app.run(debug=True)


