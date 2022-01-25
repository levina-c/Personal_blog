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
user6 = User(username="levina", first_name = "Levina", email="levina@test.ac.uk", password="admin")

#create post
post1 = Post(title="Instant 20", 
            content="\tThis is a UX and UI design project for a mini branching decision-based game about the life of a instant photo photographer.\n\tInspired by the street performers in Hong Kong, this project reveals the other side of a photographer who brought up a new craze for taking black and white instant photo in one of the famous streets, Sai Yeung Choi Street in Hong Kong. The goal of the game is to complete the daily routine of the character. Based on the choices the players made, there will be different endings.\n\n Skills: UX UI Design, Graphic Design", 
            user=user6, 
            image_file="blog1.png",
            alt_tag="Instant 20 game app development"
            )

post2 = Post(title="Dancing Star", 
            content="\tDancing Star is a programmed interactive art installation. It imitates the turning dance moves of a lady, capturing attention with the decoration lights on the train of her dress.\n\tThe installation has two outputs, an audio output and a visual projection. An ultrasonic distance sensor is used with processing programming coding. When the audience comes near the installation, Dancing star will start rotating with music and project music visualisation background. The closer the audience are to the installation, the faster it whirls.\n\nSkills: Arduino, Processing", 
            author_id=6, 
            image_file="blog2.jpg",
            alt_tag="Dancing Star Interactive Installation"
            )

post3 = Post(title="Ebook: 3 Little Red Riding Hood", 
            content="\t3 Little Red Riding Hood is group project of an interactive Ebook with audio for children readers. The ebook is automatically played after clicking the start button. When the cursor hovers on the graphics, the graphics will move. Readers are allow to turn to previous page or next page or replay the audio.\n\nSkills: Javascript, HTML, CSS, Graphic Design", 
            author_id=6, 
            image_file="blog3.JPG",
            alt_tag="Interactive ebook"
            )

post4 = Post(title="Giveaway Campaign Page Design", 
            content="\tThis is a work from my previous position as a digital marketing executive for a eCommerce company. This is a page dedicated for a giveaway campaign.\n\tHTML with image mapping are done in the project. Visitor can click different parts of the image and be redirected to other pages for more information or social media accounts to join the giveaway.\n\nSkills: HTML, Graphic Design", 
            author_id=6, 
            image_file="blog4.jpg",
            alt_tag="Online shop website design"
            )


rating1 = Rating(star=5, user_id=1, post_id=1)
rating2 = Rating(star=4, user_id=2, post_id=2)
rating3 = Rating(star=4, user_id=3, post_id=3)
rating4 = Rating(star=3, user_id=4, post_id=4)

comment1 = Comment(user_id=1, post_id=1, content='Interesting!')
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
db.session.add(user6)
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