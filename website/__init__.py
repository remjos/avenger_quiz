from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from os import path

db = SQLAlchemy
DB_name = "database.db"


#creates app for flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'uoihweiuhb ewfuewhfwefhewfuih'
    app.config['SQLALCHEMY_DATABSE_URI'] = f'sqlite:///{DB_name}'
    db.init_app(app)

    from .views import views 
    from .auth import auth 
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note


    create_database(app)
    
    return app

def create_database(app): 
    if not path.exists('website'/ + DB_name): 
        db.create_all(app=app)
        print('Created the database!')
