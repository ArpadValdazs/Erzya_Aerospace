from Model.LongitudinalCalc.LongitudinalCalc import LongitudinalCalc
from flask import Flask, render_template, make_response, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, Session
#from Model.database.Users import Users
from datetime import datetime

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "aas1ert55t523fwqed123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///c:/Users/Пользователь/PycharmProjects/ErzyaAerospace/my_db/mysql.db'

db = SQLAlchemy(app)
session = sessionmaker(bind='engine')

class Users (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable = False)
    calculations = db.relationship('Calculations', backref='author', lazy=True)

class Calculations (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create A Model For Table

@app.route('/')
def index():
    print("ASD")
    return render_template('index.html')

@app.route('/login', methods=['post', 'get'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

    session = Session()

    c1 = Users(
        username="aaa",
        password="adasdf",
        email="adasd@asdf",
        role="user"
    )

    session.add(c1)
    session.commit()

    user = session.query(Users).filter(Users.username == "aaa")
    print(user)

    return render_template('login.html')


@app.route('/signin', methods=['post', 'get'])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
    return render_template('signin.html')

@app.route('/longitude')
def longitude():
    task_len = [1.0, 4.0, 1.0]
    task_areas = [2.0, 4.0, 5]
    # task_loads = [[-1, [0, 5]], [2, [1, 1]], [-1, [6, 6]]]
    # task_loads = [[2, [1, 1]], [-1, [6, 6]]]
    # task_loads = [[2, [2, 2]], [-1, [0, 3]], [-1, [4, 6]], [2, [5, 5]], [-1, [6, 6]]]
    #task_loads = [[2, [3, 3]], [1, [0, 2]], [-1, [4, 6]], [2, [5, 5]]]
    task_loads = [[-1.0, [0.0, 2.0]], [-1.0, [4.0, 5.0]], [-1.0, [6.0, 6.0]]]
    # task_loads = [[-1, [0, 1]], [2, [2, 2]], [-2, [3, 3]], [-1, [5, 6]]]
    task_seal = 0
    task_temp = 0
    task_jung = 0

    long_calc = LongitudinalCalc(task_len, task_loads, task_areas, task_seal, task_temp, task_jung)
    loads = long_calc.loads_calc()
    print("load,", loads)
    res = make_response("200")
    return res
    #return render_template('index.html')




if __name__ == "__main__":
   app.run(debug=True)