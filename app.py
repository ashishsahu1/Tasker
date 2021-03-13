from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    #defining database columns
    sno = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200),nullable = False)
    desc = db.Column(db.String(500),nullable = False)
    date_created = db.Column(db.DateTime,default = datetime.utcnow)

    #explain what to print hen todo object is printed
    def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title = title, desc = desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html',allTodo = allTodo)

@app.route('/show')
def show():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'done'

if __name__ == "__main__":
    app.run(debug=True)