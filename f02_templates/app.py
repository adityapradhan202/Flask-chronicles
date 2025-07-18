from flask import Flask
from flask import render_template

# We must make a directory inside the root directory or project folder,
# with name 'templates'. This will contain all the html code.
# Different routes will return different html.

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)