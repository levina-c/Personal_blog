from blog import db
from blog.models import User, Post, Rating, Comment

post1 = Post(title="When", 
            content="When every dream\n\thas turned to dust,\n\tand your highest hopes\n\tno longer soar.\n\nWhen places you\n\tonce yearned to see,\n\tgrow further away\n\ton distant shores.\n\nWhen every night\n\tyou close your eyes,\n\tand long inside\n\tfor something more.\n\nRemember this\n\tand only this,\n\tif nothing else\n\tyou can recall--\n\nThere was a life\n\ta girl once led,\n\twhere you were loved\n\tthe most of all.", 
            user=user1, 
            image_file="blog1.jpg")

# comment1 = Comment(user_id=1, post_id=1, content='Good!')
#add object to database session
db.session.add(post1)

#save database session
db.session.commit()