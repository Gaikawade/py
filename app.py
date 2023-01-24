from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'xyzsdfg'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mahesh123'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/register', methods =['GET', 'POST'])
def register():
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'password' in request.form :
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        account = cursor.fetchone()
        if account:
            return 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return 'Invalid email address !'
        elif not name or not password or not email:
            return 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user VALUES ( %s, %s, %s)', (name, email, password,))
            mysql.connection.commit()
            return 'You have successfully registered!'
    elif request.method == 'POST':
        return 'Please fill out the form !'

@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['name'] = user['name']
            session['email'] = user['email']
            print(session)
            
            return 'Logged in successfully !'
        else:
            return 'Please enter correct email / password!'
    else:
        return 'Please enter your credentials!'
  
@app.route('/logout')
def logout():
    if session.get('loggedin') == 'true':
        session.pop('loggedin', None)
        session.pop('name', None)
        session.pop('email', None)
        print(session)
        return 'logged out'
    else:
        return 'You are not logged in'


if __name__ == '__main__':
    app.run(debug=True)