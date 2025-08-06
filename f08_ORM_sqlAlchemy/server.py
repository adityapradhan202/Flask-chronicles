from flask import Flask
from flask import render_template, request, redirect,  url_for
from flask_sqlalchemy  import SQLAlchemy

app = Flask(__name__)

# configs
app.secret_key = b'hellodude22'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
# avoids warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# create SQLAlchemy instance
db = SQLAlchemy(app)

# every class is a table here
# object of these classes are rows
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String, unique=False, nullable=False)

    def __init__(self, task):
        # self.id = id (remove id from constructor as well)
        self.task = task

    # __repr__ defines official string representation of an obj
    # it is different from  __str__
    # we can use this returned string to recreate the object
    def __repr__(self):
        return f"{self.id}:{self.task}"

# Routes here
@app.route("/")
@app.route("/home")
def home():
    return "<h2>Home page</h2>"

# route for create operation
@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        task = request.form["task"]
        # now this is how we create in db
        # dont pass the id as id will be added automatically (autoincrement way)
        row = Tasks(task=task)

        # db.session is a link between python code and actual db
        # db.session is a space that temporarily stores added data, until we manually commit the session
        db.session.add(row)
        db.session.commit()

        # Onnce added and committed - redirecting to read.html
        return redirect(url_for("read"))

    elif request.method == "GET":
        return render_template('create.html')
    
# route for read operation
@app.route("/read")
def read():
    # we are here actually reading all the rows
    dbrows = Tasks.query.all()
    return render_template('read.html', dbrows=dbrows)

# Some syntax guide
# For select operation
# In order to delete a row, we need to select it first

# employee = EmployeeModel.query.filter_by(employee_id=id).first() -> Selects the first row of that id
# use .all method it to get a list of all the objects of that particular id
# employee = EmployeeModel.query.get(123) -> 123 is the primary key of table EmployeeModel

@app.route("/delete/<int:id>")
def delete(id):
    row = Tasks.query.filter_by(id=id).first()
    # print(f"Row id: {row.id}") -> Prints the row id in the terminal
    db.session.delete(row)
    db.session.commit()
    
    # after deleting redirect to read
    return redirect(url_for("read"))

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    # First we need to get the row
    row = Tasks.query.filter_by(id=id).first()
    if request.method  == "POST":
        db.session.delete(row)
        db.session.commit()

        updated = request.form.get("updated") # get the updated content
        updated_row = Tasks(task=updated)
        updated_row.id = id

        # add the updated row
        db.session.add(updated_row)
        db.session.commit()

        # once updated - redirect to read
        return redirect(url_for("read"))

    elif  request.method == "GET":
        return render_template('update.html', content=row.task)

if __name__ == "__main__":

    # out of the server
    # within the app context
    # things here will be executed or run as if called in CLI
    with app.app_context():
        db.create_all() # creates all the tables that doesn't exist

        print()
        dbrows = Tasks.query.all()
        # dbrows is a list of all the instances of class Tasks
        # or we can say it is a python listof all the rows of table Tasks
        print(dbrows)
        print(f"Type of dbrows: {type(dbrows)}")
        try:
            print(dbrows[0])
            print(f"Type of dbrows[0] is {type(dbrows[0])}")
            print("ID of the first:", dbrows[0].id)
        except Exception as e:
            print(f"Exeption occured {e}")
        print()

    # run the app in debug mode
    app.run(debug=True)