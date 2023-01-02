from flask import Flask 
#creates app for flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'uoihweiuhb ewfuewhfwefhewfuih'
    return app
