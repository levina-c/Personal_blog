from blog import db
from blog.models import Post 

post = Post.query.filter_by(id=3).first()
post.content = "\t3 Little Red Riding Hood is group project of an interactive Ebook with audio for children readers. The ebook is automatically played after clicking the start button. When the cursor hovers on the graphics, the graphics will be animated. Readers are allowed to turn to previous page or next page or replay the audio.\n\nSkills: Javascript, HTML, CSS, Graphic Design"
db.session.commit()