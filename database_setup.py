from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# NOTE Create tables and the relation for each table.
# also adds JSON features to each table using the serialize
# functions.

# NOTE Users table with information about the users
# registered to the website

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


# NOTE gallery table with information about each gallery
# and path of the image.

class Gallery(Base):
    __tablename__ = 'gallery'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    imgfile = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'title': self.title,
            'imgfile': self.imgfile,
            'id': self.id,
        }


# NOTE pictures table with information about each picture
# and path of the image.

class Pictures(Base):
    __tablename__ = 'picture'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    imgfile = Column(String(250), nullable=False)
    gallery_id = Column(Integer, ForeignKey('gallery.id'))
    gallery = relationship(Gallery)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'title': self.title,
            'imgfile': self.imgfile,
            'id': self.id,
            'gallery_id': self.gallery_id,
        }


# NOTE Creates the table with sqlalchemy

engine = create_engine('sqlite:///imagegallery.db')

Base.metadata.create_all(engine)
