from datetime import datetime
from blog import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func

class Rating(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  star = db.Column(db.Integer())
  user_id = db.Column (db.Integer, db.ForeignKey('user.id'), nullable=False)
  post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

  def __repr__(self):
    return f"Rating('{self.star}', '{self.post_id}', '{self.user_id}')"
  

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  title = db.Column(db.Text, nullable=False)
  content = db.Column(db.Text, nullable=False)
  image_file = db.Column(db.String(40), nullable=False, default='default.jpg')
  alt_tag = db.Column(db.String(40), nullable=False)
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  comment = db.relationship('Comment', backref='post', lazy='dynamic') 
  rating = db.relationship('Rating', backref='post', lazy='dynamic')


  def __repr__(self):
    return f"Post('{self.date}', '{self.title}', '{self.content}')"

class User(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(15), unique=True, nullable=False)
  first_name = db.Column(db.String(15), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  hashed_password=db.Column(db.String(128))
  post = db.relationship('Post', backref='user', lazy=True)
  comment = db.relationship('Comment', backref='user', lazy='dynamic')
  rating = db.relationship('Rating', backref='user', lazy=True)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"

  @property
  def password(self):
    raise AttributeError('Password is not readable.')

  @password.setter
  def password(self,password):
    self.hashed_password=generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.hashed_password,password)

class Comment(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
  content = db.Column(db.Text)

  def __repr__(self):
    return f"Comment('{self.date}', '{self.user_id}, '{self.post_id}', '{self.content}')"

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))
