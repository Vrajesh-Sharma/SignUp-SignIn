from flask import Flask, render_template, request, redirect, url_for, session
import csv

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# File to store user credentials
USER_FILE = 'users.csv'


# Helper function to check if the user exists
def user_exists(username):
    with open(USER_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return True
    return False


# Helper function to validate user login
def validate_user(username, password):
    with open(USER_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
    return False


# Default route
@app.route('/')
def home():
    return redirect(url_for('signup'))  # Redirect to signup page


# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if user_exists(username):
            return render_template('signup.html', error="Username already exists.")
        with open(USER_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        return redirect(url_for('signin'))
    return render_template('signup.html')


# Signin route
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if validate_user(username, password):
            session['username'] = username
            return redirect(url_for('profile'))
        return render_template('signin.html', error="Invalid credentials. Please try again.")
    return render_template('signin.html')


# Profile route
@app.route('/profile')
def profile():
    if 'username' in session:
        return render_template('profile.html', username=session['username'])
    return redirect(url_for('signin'))


# Signout route
@app.route('/signout', methods=['POST'])
def signout():
    session.pop('username', None)
    return redirect(url_for('signin'))


if __name__ == '__main__':
    # Create the CSV file if it doesn't exist
    try:
        open(USER_FILE, 'r').close()
    except FileNotFoundError:
        open(USER_FILE, 'w').close()
    app.run(debug=True)
