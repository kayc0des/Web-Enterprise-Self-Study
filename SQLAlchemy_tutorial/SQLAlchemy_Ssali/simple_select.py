from main import session
from models import User, Comment
from sqlalchemy import select

users = session.query(User).all()
for user in users:
    print(user)

statement = select(User).where(User.username.in_(['paul','cathy']))
result = session.scalars(statement)
for r in result:
    print(r)