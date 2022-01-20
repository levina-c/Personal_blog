from blog import db
from blog.models import User, Post, Rating, Comment

#clear out existing database (not deleting existing database)
db.drop_all()

#create the database schema (making empty tables)
db.create_all()

#create users
user1 = User(username="User1", first_name = "One", email="user1@test.ac.uk", password="passuser1")
user2 = User(username="User2", first_name = "Two", email="user2@test.ac.uk", password="passuser2")
#create post
#use backref for the author_id
post1 = Post(title="When", 
            content="When every dream\n\thas turned to dust,\n\tand your highest hopes\n\tno longer soar.\n\nWhen places you\n\tonce yearned to see,\n\tgrow further away\n\ton distant shores.\n\nWhen every night\n\tyou close your eyes,\n\tand long inside\n\tfor something more.\n\nRemember this\n\tand only this,\n\tif nothing else\n\tyou can recall--\n\nThere was a life\n\ta girl once led,\n\twhere you were loved\n\tthe most of all.", 
            user=user1, 
            image_file="blog1.jpg")
post2 = Post(title="Second Post", content="2abcd", user=user1, image_file="blog2.jpg")
post3 = Post(title="Third Post", content="3abcd", user=user1, image_file="blog3.jpg")
post4 = Post(title="Fourth Post", content="4abcd", user=user1, image_file="blog4.jpg")

rating1 = Rating(star=5, user_id=1, post_id=2)
rating2 = Rating(star=1, user_id=1, post_id=1)

comment1 = Comment(user_id=1, post_id=1, content='Good!')
#add object to database session
db.session.add(user1)
db.session.add(user2)
db.session.add(post1)
db.session.add(post2)
db.session.add(post3)
db.session.add(post4)
db.session.add(rating1)
db.session.add(rating2)
db.session.add(comment1)
#save database session
db.session.commit()