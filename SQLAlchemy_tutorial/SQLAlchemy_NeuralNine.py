"""SQLAlchemy Tutorial by NeuralNine [https://www.youtube.com/watch?v=AKQ3XEDI9Mw]"""

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base() #returns a class that will be the base

class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender}, {self.age})"

class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column('description', String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid}) {self.description} owned by {self.owner}"


#create an engine
engine = create_engine("sqlite:///mydb.db", echo=True)

#connect to the database and creat all the tables in this case a people table will be created using the Person class
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine) #convention 
session = Session()

#create a new person object
person_one = Person(12346, "Kingsley", "Budu", "m", 22) 
person_two = Person(13468, "John", "Doe", "m", 35) 
person_three = Person(12846, "Angela", "Mcclaren", "f", 30) 
session.add(person_one)
session.add(person_two)
session.add(person_three)
session.commit()

#create new thing
t1 = Thing(12, "Car", person_one.ssn)
t2 = Thing(12, "Laptop", person_one.ssn)
t3 = Thing(12, "Truck", person_two.ssn)
session.add(t1)
session.add(t2)
session.add(t3)
session.commit()

#query
results = session.query(Person).all() #similar to select * from people
# results = session.query(Person).filter(Person.lastname == "Doe")
# results = session.query(Person).filter(Person.age > 25)
# results = session.query(Person).filter(Person.firstname.like("%ng%"))
for r in results:
    print(r)

new_results = session.query(Thing, Person).filter(Thing.owner == Person.ssn).filter(Person.firstname == "Kingsley")
for r in new_results:
    print(r)