import os
from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
DATABASE_URL = "postgresql://my_todo_db_cjd8_user:W5Uc7QjE5ReAY9tV2yDlH3p5i7D9xklq@dpg-d2n195vfte5s738t6q80-a.oregon-postgres.render.com/my_todo_db_cjd8"


DATABASE_URL = os.environ.get("DATABASE_URL", DATABASE_URL)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    SNo = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.title}"

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':

       title = request.form['title']
       desc = request.form['desc']

       todo = Todo(title=title, desc=desc)
       db.session.add(todo)
       db.session.commit()
       return redirect("/")   

    todos = Todo.query.all()
    print(todos)
    return render_template("index.html", Todos=todos)

@app.route("/show")
def show():
    todos = Todo.query.all()
    print(todos)
    return render_template("index.html", Todos=todos)

@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    todo = Todo.query.get(sno)
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(SNo=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    return render_template("update.html", todo=todo)

@app.route("/delete/<int:sno>")
def delete_todo(sno):
    todo = Todo.query.get(sno)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)