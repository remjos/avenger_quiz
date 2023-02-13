from flask import Blueprint, render_template
from flask_login import login_required, current_user
import sqlite3

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home(): 
    return render_template("home.html", user=current_user)

@views.route('/movies')
def movies():
    print("hello world")

