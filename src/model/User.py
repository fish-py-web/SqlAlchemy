from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# ORM类的基类
Base = declarative_base()


"""
用户表
"""
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    password = Column(String(30))
    fullname = Column(String(20))
    nickname = Column(String(20))

    def __repr__(self):
        return "<User(id='%s', password='%s', fullname='%s', nickname='%s')>" % (
                         self.id, self.password, self.fullname, self.nickname)
