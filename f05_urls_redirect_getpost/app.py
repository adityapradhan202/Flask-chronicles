# Here in this app script we will learn url_for method
from flask import Flask
from flask import render_template
from flask import url_for

# Note:
# url_for is used to crate urls for specific routes
# It takes the name of the html page as the first argument, 
# and any number of keyword argumetns that we want to inject into html using jinja2
# The question arises that why do we even need it when we can hard code the urls
# We need it because it can easily deal with relative and absolute url path issues
# We just need to change the url at one place, and automatically it will be changed in the other places

app = Flask(__name__)

# Some dummy data
anime_list = ["demon slayer", "jjk", "chainsaw man"]

# Making some routes
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/anime")
def anime():
    return render_template("anime.html", anime_list=anime_list)

print("\n\n--> URLS:")
with app.test_request_context():
    print(url_for("index")) # mention function name in string
    print(url_for("anime"))
    # unknown keyword args are appended as query parameters in the url
    print(url_for("anime", anime_name="demon-slayer"))

# Note:
# app.test_request_context() tells Flask to behave as though it’s handling a request even while we use a Python shell.

if __name__ == "__main__":
    app.run(debug=True)
