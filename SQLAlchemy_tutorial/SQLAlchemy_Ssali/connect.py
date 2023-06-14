"""SQLAlchemy Tutorial by Ssali Jonathan [https://www.youtube.com/watch?v=XWtj4zLl_tg]"""

from sqlalchemy import create_engine, text


engine = create_engine("sqlite:///sample.db", echo=True)

with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))

    print(result.all())