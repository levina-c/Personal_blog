from blog import db
from blog.models import User, Post, Rating, Comment

rating4 = Rating(star=4, user_id=2, post_id=2)
rating5 = Rating(star=3, user_id=1, post_id=3)
rating6 = Rating(star=2, user_id=3, post_id=4)

# comment1 = Comment(user_id=1, post_id=1, content='Good!')
#add object to database session
db.session.add(rating4)
db.session.add(rating5)
db.session.add(rating6)

#save database session
db.session.commit()