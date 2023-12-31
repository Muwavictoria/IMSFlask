from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager




app = Flask(__name__)



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ims.db"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///inventory_system_db.db"
app.config['SECRET_KEY']='secretkey'

db = SQLAlchemy(app)

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view= "login"





from app import routes
