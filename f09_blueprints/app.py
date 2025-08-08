from flask import Flask
from user import userBP
from authuser import authBp

app = Flask(__name__)

# Register blue print here
# user_prefix means we will get a prefix in the path like user/content/
# it's not mandatory to set url_prefix
# prefixes string must be mentioned with a slash -> /user
app.register_blueprint(blueprint=userBP, url_prefix='/user')
app.register_blueprint(blueprint=authBp, url_prefix='/auth')

# Architecture followed when ORM is used along with blueprints.
# We create the SQLAlchemy's instance, that is db, here.
# Then we import db in blueprint files to create tables and stuff

if __name__ == "__main__":
    app.run(debug=True)

