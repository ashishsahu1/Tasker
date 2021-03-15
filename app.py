from flask import Flask, render_template, request, redirect
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
    p = db.Column(db.Integer,nullable = False)

    #explain what to print hen todo object is printed
    def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        p = request.form.getlist('pr')[0]
        todo = Todo(title = title, desc = desc, p=p)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html',allTodo = allTodo)

@app.route('/delete/<int:sno>')
def delete(sno):
    deletTodo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(deletTodo)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:sno>', methods = ['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        updateTodo = Todo.query.filter_by(sno=sno).first()
        updateTodo.title = title
        updateTodo.desc = desc
        db.session.add(updateTodo)
        db.session.commit()
        return redirect('/')

    updateTodo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html',updateTodo = updateTodo)

if __name__ == "__main__":
    app.run(debug=True)