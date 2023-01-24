from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mahesh123@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    contact = db.Column(db.String(12), nullable=False)

    def __init__(self, id, name, email, contact=None):
        self.customer_id = id,
        self.name = name,
        self.email = email,
        self.contact = contact
        db.create_all()

# class Order(db.Model):
#     order_id = db.Column(db.Integer, primary_key=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
#     order_date = db.Column(db.Date)

@app.route('/')
def index():
    return 'Hello, are you ready to create schemas in MySQL?'

@app.route('/create-customer', methods=['POST', 'GET'])
def create_customer():
    if request.method == 'POST':
        data = request.get_json()
        fixed_digits = 4
        id = random.randrange(1000, 99999, fixed_digits)

        doc = db.session.query(Customer).filter_by(email=data['email'])
        if doc:
            return 'Email is already in use'

        new_customer = Customer(id=id, name=data['name'], email=data['email'], contact=data['contact'])
        db.session.add(new_customer)
        db.session.commit()
        return 'Success', 201

if __name__ == '__main__':
    app.run(debug=True)