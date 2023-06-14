from models import User, Comment
from sqlalchemy.orm import Session
from connect import engine

session = Session(bind=engine)

user1 = User(
    username = 'Kingsley',
    email_address = 'kay@sql.org',
    comments = [
        Comment(text="Hello World"),
        Comment(text="Learn more")
    ]
)

paul = User(
    username = 'Paul',
    email_address = 'paul@sql.org',
    comments = [
        Comment(text="Hello Fam"),
        Comment(text="Excited")
    ]
)

cathy = User(
    username = 'Cathy',
    email_address = 'cathy@sql.org'
)

session.add_all([user1, paul, cathy])
session.commit()