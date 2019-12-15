from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Century(Base):
    __tablename__ = 'century'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Entrepreneur(Base):
    __tablename__ = 'entrepreneur'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    century_id = Column(Integer, ForeignKey('century.id'))
    information = Column(String)
    century = relationship(Century)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'information': self.information,
            'id': self.id,
        }


engine = create_engine('sqlite:///entrepreneurslistwithusers.db')
Base.metadata.create_all(engine)
