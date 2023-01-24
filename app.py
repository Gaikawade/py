from flask import Flask, flash, render_template, request, redirect, url_for, session
# importing MySQL class from flask_mysqldb library
from flask_mysqldb import MySQL
# importing cursors module from MySQLdb library
import MySQLdb.cursors
# importing regular expressions(re) module
import re

app = Flask(__name__)

'''
When a user's session is created, a secure session cookie is created and sent to the user's browser.
This cookie contains a session ID that is used to identify the user's session on the server.
The app.secret_key is used to encrypt and sign the session cookie
'''
app.secret_key = 'xyzsdfg'
# DB Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mahesh123'
app.config['MYSQL_DB'] = 'flask'

'''
creating an instance of the MySQL class and assigns it to the variable "mysql"
MySQL class is used to establish a connection to a MySQL database
The "app" variable is an instance of a Flask application, allows the application to communicate with the MySQL database and perform various operations
'''
mysql = MySQL(app)

# User registration api
@app.route('/register', methods =['GET', 'POST'])
def register():
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'password' in request.form :
        # destructuring the request object
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # A cursor is used to execute SQL commands and manage the results of the commands and returns the result in tuples
        # The DictCursor allows the results to be accessed as a dictionary, rather than a tuple
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # Check whether user is already registered with the email address
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        account = cursor.fetchone()
        # if the email is already registered "if-block" will execute
        if account:
            flash('Account already exists !')
        # if not it will check the email address is in valid format
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address !')
        # if any input is missing this block will execute and send a message using flash() method
        elif not name or not password or not email:
            flash('Please fill out the form !')
        # after validation we are inserting the data into our database in else block
        else:
            cursor.execute('INSERT INTO user VALUES ( %s, %s, %s)', (name, email, password,))
            # commit() will commiting the current transaction to the MySQL database
            mysql.connection.commit()
            flash('You have successfully registered!')
            flash('Please login to access you account')
            return redirect(url_for('login'))
    # if the method is POST and the request form is empty, this block will execute
    elif request.method == 'POST':
        flash('Please fill out the form !')
    # rendering the register template
    return render_template("register.html")

# Login api
@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        # A cursor is used to execute SQL commands and manage the results of the commands and returns the result in tuples
        # The DictCursor allows the results to be accessed as a dictionary, rather than a tuple
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # executing query 
        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password, ))
        user = cursor.fetchone()
        if user:
            # storing the user details in the session
            session['loggedin'] = True
            session['name'] = user['name']
            session['email'] = user['email']
            # rendering the home template after successful login
            return render_template('home.html')
        else:
            flash('Please enter correct email / password!')
    # if the method is POST and the request form is empty, this block will execute
    elif request.method == 'POST':
        flash('Please fill out the form !')
    return render_template('login.html')

# Logout api
@app.route('/logout')
def logout():
    # popping out all the details of the logged in user and redirecting back to login page
    session.pop('loggedin', None)
    session.pop('name', None)
    session.pop('email', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)