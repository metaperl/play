from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import pandas as pd

engine = create_engine("sqlite:///:memory:", echo=True)

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


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

_ = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session.add(_)

_ = User(name='ted', fullname='TEd Jones', nickname='tedsnickname')
session.add(_)

_ = User(name='red', fullname='rEd Jones', nickname='redsnickname')
session.add(_)

session.commit()


users = session.query(User.name, User.fullname)

df = pd.DataFrame(users)

print(df)
