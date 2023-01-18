# Import Flask library from falsk directly
from flask import Flask
# Creating an instance of Flask with name 'app'
# "__name__" argument passed to the Flask class is used to determine the root path of the application
app = Flask(__name__)

# Decorator / URL Endpoint
# Used to define a URL route for the root of the web application
@app.route('/')
# Function declaration
def index():
    return "Hello, World!"


@app.route('/admin')
def admin():
    return "Hello, Admin!"


@app.route('/admin/<name>')
def admin_name(name):
    return f'Hello, {name}. You are an Admin'

"""
  This statement is used to check if the code is being executed as the main program or being imported as a module into another program. When the Python interpreter runs a script, it assigns the special variable __name__ the value __main__. If the source file is being imported into another script, __name__ will be set to the name of the module, not __main__. So, the if __name__ == '__main__': block is only executed if the script is run as the main program. This is useful for writing reusable code that can also be run as a standalone program.
"""
if __name__ == '__main__':
    app.run(debug=True)
