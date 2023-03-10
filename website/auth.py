from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from . import db 
from flask_login import login_user, login_required, logout_user, current_user




auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else: 
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist. Please sign up to continue', category='error')


    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 2 character', category='error')
        elif password1 != password2:
            flash('Error, password mismatch', category='error')
        elif len(password2) < 7: 
            flash('Password must be more than 7 characters', category='error') 
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256')) 
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True) 
            flash('Account created!', category='success')
            return redirect(url_for('views.home')) 
        
    return render_template("signup.html", user=current_user)

@auth.route('/movies', methods=['GET', 'POST'])
def movies():
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    return render_template("movies.html", user=current_user)

@auth.route('/take_quiz', methods=['GET', 'POST'])
def take_quiz():
    return render_template("take_quiz.html", user=current_user)

@auth.route('/show_movies', methods=['GET', 'POST'])
def show_movies():
    return render_template("show_movies.html", user=current_user)

@auth.route('/pick_a_flix', methods=['GET', 'POST'])
def pick_flix():
    print('hello world')
    return redirect(url_for(pick_flix))
