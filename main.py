from Model.LongitudinalCalc.LongitudinalCalc import LongitudinalCalc
from flask import Flask, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "aas1ert55t523fwqed123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///c:/Users/Пользователь/PycharmProjects/ErzyaAerospace/my_db/mysql.db'

db = SQLAlchemy(app)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return "<{}:{}>".format(self.id,  self.title[:10])

# Create A Model For Table

@app.route('/')
def index():
    print("ASD")
    return render_template('index.html')

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