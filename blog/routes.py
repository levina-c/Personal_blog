from flask import render_template, url_for, request, redirect, flash, current_app
from sqlalchemy.sql import func
from blog import app, db
from blog.models import User, Post, Comment, Rating
from blog.forms import RegistrationForm, LoginForm, CommentForm, RatingForm, PostOrder
from flask_login import login_user, logout_user, current_user, login_required, login_manager
from statistics import mean
from sqlalchemy import desc, asc

@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home():
  sortBy = PostOrder(order='date_desc')
  posts=Post.query.order_by(desc(Post.id)).all()
  selected = sortBy.order.data
  if sortBy.validate_on_submit():
    if selected == 'date_desc':
      posts=Post.query.order_by(desc(Post.date)).all()
    else:
      posts=Post.query.order_by(asc(Post.date)).all()
  return render_template('home.html', posts=posts, sortBy=sortBy)

@app.route("/about")
def about():
  return render_template('about.html', title='About')

@app.route("/post/<int:post_id>", methods=['GET','POST'])
@login_required
def post(post_id):
  post=Post.query.get_or_404(post_id)
  commentBox = CommentForm()
  ratingscale = RatingForm()
  #get the whole row by filtering the post id
  get_score = Rating.query.filter_by(post_id=post.id).all()
  #get the data from the star column only
  list_of_ratings = []
  for rating in get_score:
    list_of_ratings.append(rating.star)
  #get the mean of the rating
  avg_score = mean(list_of_ratings)
  if ratingscale.validate_on_submit():
    rating = Rating(star=ratingscale.star.data, user=current_user._get_current_object(), post=post)
    db.session.add(rating)
    db.session.commit()
    flash('You have submitted the rating successfully.')
    return redirect(url_for("post", post_id=post.id))
  if commentBox.validate_on_submit():
    comment = Comment(content=commentBox.content.data, user=current_user._get_current_object(), post=post)
    db.session.add(comment)
    db.session.commit()
    flash('Your comment has been published.')
    return redirect(url_for("post", post_id=post.id))
  return render_template('post.html', title='Post', post=post, ratingscale=ratingscale, avg_score=avg_score, commentBox=commentBox)

@app.route("/register",methods=['GET','POST'])
def register():
  user_reg_form = RegistrationForm()
  if user_reg_form.validate_on_submit():
    user = User(username=user_reg_form.username.data, first_name=user_reg_form.first_name.data, email=user_reg_form.email.data, password=user_reg_form.password.data)
    db.session.add(user)
    db.session.commit()
    login_new_user = User.query.filter_by(email=user_reg_form.email.data).first()
    login_user(login_new_user)
    flash('Registration successful!')
    return redirect(url_for('registered'))
    
  return render_template('register.html',title='Register',user_reg_form=user_reg_form)

@app.route("/registered")
def registered():
  return render_template('registered.html', title='registered')

@app.route("/login",methods=['GET','POST'])
def login():
  user_login_form = LoginForm()
  if user_login_form.validate_on_submit():
    userToLogin = User.query.filter_by(email=user_login_form.email.data).first()
    if userToLogin is not None and userToLogin.verify_password(user_login_form.password.data):
      login_user(userToLogin)
      flash('You\'ve successfully logged in,'+' '+ current_user.username +'!')
      return redirect(url_for('home'))
    else:
      flash('Incorrect email or password supplied.')
      return redirect(url_for('loginerror'))
  return render_template('login.html',title='Login', user_login_form=user_login_form)

@app.route("/logout")
def logout():
  logout_user()
  flash('You have been logged out')
  return redirect(url_for('home'))

@app.route("/privacypolicy")
def privacypolicy():
  return render_template('privacypolicy.html', title="Privacy Policy")

@app.route("/loginerror")
def loginerror():
  return render_template('loginerror.html', title="Log in failed")
