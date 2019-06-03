import unittest

from src.model.User import User
from src.main import session


class TestDb(unittest.TestCase):

    # 向数据库中添加一条数据
    def test_add(self):
        user = User()
        user.fullname = 'Jon Snow'

        session.add(user)
        session.commit()

        # 如果成功创建用户，id不应该为None
        self.assertIsNotNone(user.id)
        print(user)

    # 向数据库中批量添加数据
    def test_addAll(self):
        user1 = User()
        user1.fullname = 'Jon1'
        user2 = User()
        user2.fullname = 'Jon2'

        session.add_all([user1, user2])
        session.commit()
        self.assertIsNotNone(user1.id)
        self.assertIsNotNone(user2.id)

        print(user1, user2)

    # 向数据库中查询数据
    def test_selectOne(self):
        # 查询id为1的记录
        user = session.query(User).get(1)

        self.assertIsNotNone(user)
        print(user)
        # < User(id='1', password='None', fullname='Jon Snow', nickname='None') >

    # 条件查询某一类用户
    def test_selectMany(self):
        user_list = session.query(User).filter_by(password=None)

        for user in user_list:
            print(user)

    # 删除一个用户
    def test_delete(self):
        session.delete(1)

    # 修改用户信息
    def test_update(self):
        new_name = 'new Name'

        # 查询 -> 修改 -> 保存
        user = session.query(User).get(1)
        user.fullname = new_name
        session.add(user)
        session.commit()

        # 再次查询确保修改成功
        new_user = session.query(User).get(1)
        self.assertEqual(new_name, new_user.fullname)
        print(new_user)
