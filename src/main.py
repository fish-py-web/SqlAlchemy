from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.model.User import User
"""
这里就很困惑，User是通过什么机制被注册发现的呢？
我只是import了一下啊。。。。。后面也没有显式的使用
"""

"""
驱动引擎
"""
engine = create_engine('mysql+pymysql://root:@localhost:3306/sql_alchemy')

Base = declarative_base()

# 创建表
Base.metadata.create_all(engine)

# 建立一个session
Session = sessionmaker(bind=engine)
session = Session()

# 测试下创建一个用户
if __name__ == '__main__':
    user = User()
    user.fullname = "asdfes"
    session.add(user)
    session.commit()
    print(user.id)
