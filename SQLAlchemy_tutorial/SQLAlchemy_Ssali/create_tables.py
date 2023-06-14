from models import Base, User, Comment
from connect import engine

print("CREATINNG TABLES >>>>")
Base.metadata.create_all(bind=engine)