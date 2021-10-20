from sqlalchemy import Integer, String, Column, Date, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'
    user_id=Column(Integer, primary_key=True)
    username=Column(String(255))
    firstname=Column(String(255))
    lastname=Column(String(255))
    email = Column(String(255))
    password=Column(String(255))


class Moderator(Base):
    __tablename__ = 'moderator'
    moderator_id = Column(Integer, primary_key=True)
    moderatorname=Column(String(255))
    firstname=Column(String(255))
    lastname = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    moderatorkey = Column(String(255))


class Article(Base):
    __tablename__ = 'article'
    article_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    body = Column(String(8000))
    version = Column(String(255))


class State(Base):
    __tablename__ = 'state'
    state_id = Column(Integer, primary_key=True)
    name = Column(String(45))


class UpdatedArticle(Base):
    __tablename__ = 'updated_article'
    updated_article_id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('article.article_id'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    moderator_id = Column(Integer, ForeignKey('moderator.moderator_id'))
    state_id = Column(Integer, ForeignKey('state.state_id'))
    article_body = Column(String(8000))
    date = Column(Date)
    article = relationship("Article")
    user = relationship("User")
    moderator = relationship("Moderator")
    state = relationship("State")
