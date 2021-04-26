from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user
from .models import Todo

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return redirect('/todo')


@main.route('/todo')
@login_required
def todo():
    todo_list = Todo.query.filter_by(user_id=current_user.id).all()
    return render_template('todo.html', todo_list=todo_list)
