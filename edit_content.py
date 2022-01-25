from blog import db
from blog.models import Post 

post = Post.query.filter_by(id=1).first()
post.title = "Instant 20 Game App"
db.session.commit()