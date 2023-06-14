from main import session
from models import User, Comment
from sqlalchemy import select

cathy = session.query(User).filter_by(username = 'cathy')
print(cathy)