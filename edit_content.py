from blog import db
from blog.models import Post 

post = Post.query.filter_by(id=3).first()
post.image_file = "blog3b.jpg"
db.session.commit()