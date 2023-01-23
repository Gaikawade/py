# importing Flask library
from flask import Flask
# importing Connect and Error class from mysql-connector-python library 
from mysql.connector import connect, Error

# Creating and instance for Flask
app = Flask(__name__)

# function to connect MySQL database
def connect_to_database():
    print('before connection to database')
    try:
        # Stroing the connection into a separate variable
        # connect() function is used to establish a connection to a MySQL server using the following parameters:
        connection = connect(
            host='localhost',
            port='3306',
            user='root',
            password='mahesh123',
            database='flask'
        )
        print('connection established')
        return connection
    except Error as e:
        print(e)
        return e

# Route Decorator
@app.route('/')
# Main API function
def index():
    cnx = connect_to_database()
    # a cursor object is used to execute SQL commands on a MySQL database
    cursor = cnx.cursor()
    # cursor.execute() method is used to execute a SQL SELECT statement on the table 'employee'
    cursor.execute('select * from employee')
    # fetchall() is a method of a cursor object in python that is used to retrieve all the rows from the result set of a SQL query. It returns a list of tuples, where each tuple represents a row 
    result = cursor.fetchall()
    # retult = [ (row-1), (row-2), (row-3) ]
    # returning the result in a string format
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)