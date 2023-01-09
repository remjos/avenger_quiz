from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

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

    
    return app
