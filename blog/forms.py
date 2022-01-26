from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField, RadioField, SelectField
from wtforms.validators import InputRequired, EqualTo, ValidationError, Regexp, Email
from blog.models import User, Rating

class RegistrationForm(FlaskForm):
  username = StringField('Username',validators=[InputRequired(),Regexp('^[A-Za-z0-9]{5,20}$',message='Your username should be between 5 and 20 characters long and only contain letters and numbers.')])
  first_name = StringField('First name',validators=[InputRequired(),Regexp('^[A-Za-z]{4,20}$',message='Your first name should be between 4 and 20 characters and only contain alphabets.')])
  email = EmailField('Email', validators=[InputRequired(), Email(message="Invalid email. Please check.")] )
  password = PasswordField('Password',validators=[InputRequired(),Regexp('^[A-Za-z0-9]{4,20}$',message='Your password contains invalid characters.')])
  confirm_password =  PasswordField('Repeat Password',validators=[InputRequired(), EqualTo('password', message='Passwords do not match. Please try again.')])
  submit = SubmitField('Register')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError('Username already exists. Please choose a different one.')

  def validate_email(self, email):
    email = User.query.filter_by(email=email.data).first()
    if email is not None:
      raise ValidationError('Email already registered.')


class LoginForm(FlaskForm):
  email = EmailField('Email',validators=[InputRequired()])
  password = PasswordField('Password',validators=[InputRequired()])
  submit = SubmitField('Login')
  
class CommentForm(FlaskForm):
  content = TextAreaField('What\'s your thought?', validators=[InputRequired()])
  submit = SubmitField('Submit')


class RatingForm(FlaskForm):
  star = RadioField('Rate this Post', validators=[InputRequired()], choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
  submit = SubmitField('Rate')

  def validate_user_id(self, user_id, post_id, current_user):
    print(current_user.id())
    get_ratedpost = Rating.query.filter_by(post_id=post.id).all()
    list_of_ratedpost = []
    for user in get_ratedpost:
      list_of_ratedpost.append(rating.user_id)
      print(list_of_ratedpost)
      if current_user.id is not None:
        raise ValidationError('You\'ve already rated this post.')

class PostOrder(FlaskForm):
  order = SelectField('Sort by', validators=[InputRequired()],choices=[('date_desc', 'Most Recent'), ('date_asc', 'Oldest')], default='date_desc')
  submit = SubmitField('Sort')
