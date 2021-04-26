from flask import Blueprint, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Todo
from . import db

todo = Blueprint('todo', __name__)


@todo.route("/add", methods=["POST"])
@login_required
def add():
    title = request.form.get("title")
    description = request.form.get("description")
    new_todo = Todo(user_id=current_user.id, title=title, description=description)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("main.todo"))


@todo.route("/update/<int:todo_id>")
@login_required
def update(todo_id: int):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.checked = not todo.checked
    db.session.commit()
    return redirect(url_for("main.todo"))


@todo.route("/delete/<int:todo_id>")
@login_required
def delete(todo_id: int):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("main.todo"))
