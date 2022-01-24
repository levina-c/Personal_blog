from blog import db
from blog.models import User, Post, Rating, Comment

#clear out existing database (not deleting existing database)
db.drop_all()

#create the database schema (making empty tables)
db.create_all()

#create users
user1 = User(username="User1", first_name = "One", email="user1@test.ac.uk", password="passuser1")
user2 = User(username="marygoo", first_name = "Mary", email="mary@test.ac.uk", password="mary")
user3 = User(username="henrywater", first_name = "Henry", email="henry@test.ac.uk", password="henry")
user4 = User(username="carolinelore", first_name = "Caroline", email="caroline@test.ac.uk", password="caroline")
user5 = User(username="kateyyy", first_name = "Katie", email="katie@test.ac.uk", password="katie")
#create post
#use backref for the author_id

rating1 = Rating(star=5, user_id=1, post_id=1)
rating2 = Rating(star=4, user_id=2, post_id=2)
rating3 = Rating(star=4, user_id=3, post_id=3)
rating4 = Rating(star=3, user_id=4, post_id=4)

comment1 = Comment(user_id=1, post_id=1, content='Good!')
comment2 = Comment(user_id=2, post_id=1, content='Nice!')
comment3 = Comment(user_id=3, post_id=2, content='Thanks for sharing!')
comment4 = Comment(user_id=4, post_id=3, content='I like it!!')
comment5 = Comment(user_id=5, post_id=4, content='Great Project!')
#add object to database session
db.session.add(user1)
db.session.add(user2)
db.session.add(user4)
db.session.add(user5)
db.session.add(user3)
db.session.add(post1)
db.session.add(rating1)
db.session.add(rating2)
db.session.add(rating3)
db.session.add(rating4)
db.session.add(comment1)
db.session.add(comment2)
db.session.add(comment3)
db.session.add(comment4)
db.session.add(comment5)
#save database session
db.session.commit()