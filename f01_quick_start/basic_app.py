# This is the code of a basic flask application
from flask import Flask

# First create an instance of class Flask
# The constructor of this class, takes in the name of the current script
# app is the intance of this class
app = Flask(__name__) 

# @app.route is a decorator for adding routes
# "/" is the default route
# "/home" is another route for home function
# These functions can return html, when we visit the specific routes
@app.route("/")
@app.route("/home")
def home():
    return "Hello world!" # Returning text here
# After you run the script
# Go this link - http://127.0.0.1:5000 to go to home route

# Note - For specific routes, specific functions are called
@app.route("/about")
def about():
    return "<h2>Hello! My name is Aditya Pradhan</h2>" # Adding html h2 tag
# Link - http://127.0.0.1:5000/about 

@app.route("/ramen")
def show_gif():
    return '<img src="https://i.pinimg.com/originals/48/bc/83/48bc8378916e0fe04a895f0e40ac73fa.gif", width=400> <br> <p>This is how it returns different html on different routes!</p>'
# Link - http://127.0.0.1:5000/ramen 

# Now we can do app.run for running the flask app
if __name__ == "__main__":
    # app.run()
    # But there's a better way
    # We can use app.run(debug=True)
    # When debug=True, the web pages changes automatically when we change something here, and save it
    # No need to refresh the web page

    app.run(debug=True)
    
    # Note - This app will run on the local host, and will be running on a port.
    # In the terminal we will see HTTP-200 sort of thing.
    # The HTTPS status code 200 means, the request was successfully received and processed.