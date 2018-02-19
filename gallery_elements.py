# NOTE: We need to import some modules for the database elements.
# create_engine (starting point of sqlalchemy application), sessionmaker
# (establishes conversations with the database) and database_setup
# to import all the database classes and tables.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Gallery, Base, Pictures, User

engine = create_engine('sqlite:///imagegallery.db')

# NOTE: Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

# NOTE: A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()

session = DBSession()


# Create dummy user

User1 = User(
    name="Admin",
    email="admin@admin.com",
    picture='https://vignette.wikia.nocookie.net/daria/images/1/15/Admin.png/revision/latest?cb=20140902104042')  # NOQA

session.add(User1)
session.commit()

# NOTE Create galleries and pictures for each gallery

##################
# Gallery  - 1 - #
##################

gallery1 = Gallery(title='Animals', imgfile='animal.jpg', user_id=1)

session.add(gallery1)
session.commit()


picture1 = Pictures(
    title='Bambi', imgfile='animal1.jpg', gallery=gallery1, user_id=1
)

session.add(picture1)
session.commit()

picture2 = Pictures(
    title='Angry Cat', imgfile='animal2.jpg', gallery=gallery1, user_id=1
)

session.add(picture2)
session.commit()

picture3 = Pictures(
    title='Sleppy Tiger', imgfile='animal3.jpg', gallery=gallery1, user_id=1
)

session.add(picture3)
session.commit()

picture4 = Pictures(
    title='Rino', imgfile='animal4.jpg', gallery=gallery1, user_id=1
)

session.add(picture4)
session.commit()

picture5 = Pictures(
    title='Cute Dog', imgfile='animal5.jpg', gallery=gallery1, user_id=1
)

session.add(picture5)
session.commit()


##################
# Gallery  - 2 - #
##################


gallery2 = Gallery(title='Abstract', imgfile='abstract.jpg', user_id=1)

session.add(gallery2)
session.commit()


picture1 = Pictures(
    title='Violet', imgfile='abstract1.jpg', gallery=gallery2, user_id=1
)

session.add(picture1)
session.commit()

picture2 = Pictures(
    title='Rubik', imgfile='abstract2.jpg', gallery=gallery2, user_id=1
)

session.add(picture2)
session.commit()

picture3 = Pictures(
    title='Watercolour', imgfile='abstract3.jpg', gallery=gallery2, user_id=1
)

session.add(picture3)
session.commit()

picture4 = Pictures(
    title='Oil Color', imgfile='abstract4.jpg', gallery=gallery2, user_id=1
)

session.add(picture4)
session.commit()

picture5 = Pictures(
    title='Prisma', imgfile='abstract5.jpg', gallery=gallery2, user_id=1
)

session.add(picture5)
session.commit()


##################
# Gallery  - 3 - #
##################


gallery3 = Gallery(title='Cities', imgfile='city.jpg', user_id=1)

session.add(gallery3)
session.commit()


picture1 = Pictures(
    title='Bridge', imgfile='city1.jpg', gallery=gallery3, user_id=1
)

session.add(picture1)
session.commit()

picture2 = Pictures(
    title='Road', imgfile='city2.jpg', gallery=gallery3, user_id=1
)

session.add(picture2)
session.commit()

picture3 = Pictures(
    title='Arc', imgfile='city3.jpg', gallery=gallery3, user_id=1
)

session.add(picture3)
session.commit()

picture4 = Pictures(
    title='NY', imgfile='city4.jpg', gallery=gallery3, user_id=1
)

session.add(picture4)
session.commit()

picture5 = Pictures(
    title='Night City', imgfile='city5.jpg', gallery=gallery3, user_id=1
)

session.add(picture5)
session.commit()

##################
# Gallery  - 4 - #
##################


gallery4 = Gallery(title='Vehicles', imgfile='vehicle.jpg', user_id=1)

session.add(gallery4)
session.commit()


picture1 = Pictures(
    title='Bike', imgfile='vehicle1.jpg', gallery=gallery4, user_id=1
)

session.add(picture1)
session.commit()

picture2 = Pictures(
    title='Cars', imgfile='vehicle2.jpg', gallery=gallery4, user_id=1
)

session.add(picture2)
session.commit()

picture3 = Pictures(
    title='Train', imgfile='vehicle3.jpg', gallery=gallery4, user_id=1
)

session.add(picture3)
session.commit()

picture4 = Pictures(
    title='Lambo', imgfile='vehicle4.jpg', gallery=gallery4, user_id=1
)

session.add(picture4)
session.commit()

picture5 = Pictures(
    title='Porsche', imgfile='vehicle5.jpg', gallery=gallery4, user_id=1
)

session.add(picture5)
session.commit()

##################
# Gallery  - 4 - #
##################


gallery5 = Gallery(title='Technology', imgfile='tech.jpg', user_id=1)

session.add(gallery5)
session.commit()


picture1 = Pictures(
    title='Capacitors', imgfile='tech1.jpg', gallery=gallery5, user_id=1
)

session.add(picture1)
session.commit()

picture2 = Pictures(
    title='LED Tv', imgfile='tech2.jpg', gallery=gallery5, user_id=1
)

session.add(picture2)
session.commit()

picture3 = Pictures(
    title='Linux Laptop', imgfile='tech3.jpg', gallery=gallery5, user_id=1
)

session.add(picture3)
session.commit()

picture4 = Pictures(
    title='Old Headphones', imgfile='tech4.jpg', gallery=gallery5, user_id=1
)

session.add(picture4)
session.commit()

picture5 = Pictures(
    title='Very Old MP3', imgfile='tech5.jpg', gallery=gallery5, user_id=1
)

session.add(picture5)
session.commit()

print "added menu items!"
