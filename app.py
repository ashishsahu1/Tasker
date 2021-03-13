from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////db/todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200),nullable = False)
    desc = db.Column(db.Integer(500),nullabe = False)
    date_created = db.Column(db.DateTime,default = datetime.utcnow)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)