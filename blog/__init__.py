from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_url
from flaskext.markdown import Markdown
import os

app = Flask(__name__)
Markdown(app)

# define database
dbName = "blog.db"
basedir = os.path.abspath(os.path.dirname(__file__))
# print(f"{basedir=}")
finalpath = os.path.join(basedir, dbName)
# print(f"{finalpath=}")
destination = f"sqlite:///{finalpath}"
# print(f"{destination=}")

app.config['SECRET_KEY'] = 'd0f4bcd97c8e139b9a0d31264cdd4c2d2d45109b6d8ff5fa'

# suppress SQLAlchemy warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB Connection changed to mysql
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://USERNAME:PASSWORD@csmysql.cs.cf.ac.uk:3306/USERNAME_DATABASE_NAME'
app.config['SQLALCHEMY_DATABASE_URI'] = destination

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from blog import routes
