"""
The SQLAlchemy Object Relational Mapper presents a method of associating user-defined Python classes with database tables, and instances of those classes (objects) with rows in their corresponding tables. 
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

#Using an in-memory sqllite database, to connect we use create_engine()
#the return value of create_engine() is an instance of Engine, and it represents the core interface to the database
engine = create_engine('sqlite:///:memory:', echo=True) #echo flag is a shortcut to setting up SQLAlchemy logging

#declare mapping (database tables define - our classes which will be mapped to the database tables)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                           self.name, self.fullname, self.nickname)