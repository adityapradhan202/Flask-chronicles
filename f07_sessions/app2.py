from flask import Flask
from flask import render_template, request
from flask import session, redirect, url_for

app = Flask(__name__)
app.secret_key = b'catsanddogs45#33nobs' # secret key for session data encryption

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    # This is actually the home page
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        session['username'] = request.form.get('username')
        session['password'] = request.form.get('password')
        return redirect(url_for('user'))

@app.route("/user")
def user():
    if 'username' in session:
        return render_template('user.html', usr=session['username'])
    else:
        return redirect(url_for('index'))

@app.route("/logout")
def logout():
    session.pop('username', None)
    # removes the key and returns the value, but here the default return value is set as default
    # it is None
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)