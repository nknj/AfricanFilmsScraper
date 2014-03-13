from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import DATABASE_NAME

Model = declarative_base() 

class Movie(Model):
  __tablename__ = 'movies'

  uid = Column(Integer, primary_key=True)
  name = Column(String)
  desc = Column(String)
  director = Column(String)
  genre = Column(String)
  length = Column(String)

  def save(self):
    m = MovieManager(self)
    return m.save()

  def __repr__(self):
    return '''
      ID:{m.uid}
      Name:{m.name}
      Desc:{m.desc}
      Director:{m.director}
      Genre:{m.genre}
      Length:{m.length}'''.format(m=self)

db = create_engine(DATABASE_NAME)
db.raw_connection().connection.text_factory = str
Model.metadata.create_all(db)
Session = sessionmaker(bind=db)

class MovieManager(object):
  def __init__(self, movie=None):
    if movie:
      self.__movie = movie
    self.__session = Session()

  def get(self, uid=None, name=None):
    if uid:
      return self.__session.query(Movie).filter_by(uid=uid).first()
    if name:
      return self.__session.query(Movie).filter_by(name=name).first()

  def get_all(self):
    return self.__session.query(Movie).all()

  def save(self):
    self.__session.add(self.__movie)
    self.__session.commit()
    return self.__movie
