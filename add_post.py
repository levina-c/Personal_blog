from blog import db
from blog.models import User, Post, Rating, Comment

rating3 = Rating(star=1, user_id=2, post_id=5)

# comment1 = Comment(user_id=1, post_id=1, content='Good!')
#add object to database session
db.session.add(rating3)

#save database session
db.session.commit()