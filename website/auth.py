from flask import Blueprint, render_template, request, flash 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>this is the logout page</p"


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error') 
        elif len(firstname) < 2:
            flash('First name must be greater than 2 characters', category='error') 
        elif len(password1) != password2:
            flash('Error, password mismatch', category='error')
        elif len(password2) < 7: 
            flash('Password must be more than 7 characters', category='error') 
        else: 
            flash('Account created!', category='success') 
        
    return render_template("signup.html")
