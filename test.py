import pymysql

from models.todo import Todo
from models.user import User
from models.session import Session
from models.comment import Comment
from models.weibo import Weibo
from utils import random_string
from secret import database_password


def test():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=database_password,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    with connection.cursor() as cursor:
        cursor.execute('DROP DATABASE IF EXISTS `test_database`')
        cursor.execute('CREATE DATABASE `test_database` CHARACTER SET utf8mb4')
        cursor.execute('USE `test_database`')

        cursor.execute(User.sql_create)
        cursor.execute(Session.sql_create)
        cursor.execute(Todo.sql_create)
        cursor.execute(Comment.sql_create)
        cursor.execute(Weibo.sql_create)
    connection.commit()
    connection.close()

    form = dict(
        username='test',
        password='123',
    )
    User.register_user(form)
    u, result = User.login_user(form)
    assert u is not None, result
    form = dict(
        username='test1',
        password='123',
    )
    User.register_user(form)

    session_id = random_string()
    form = dict(
        session_id=session_id,
        user_id=u.id,
    )
    Session.new(form)
    s: Session = Session.one(session_id=session_id)
    assert s.session_id == session_id

    form = dict(
        title='test todo',
        user_id=u.id,
    )
    t = Todo.add(form, u.id)
    assert t.title == 'test todo'

    form = dict(
        content='111',
        user_id=u.id,
    )
    w = Weibo.add(form, u.id)
    assert w.content == '111'

    form = dict(
        content='2222',
        user_id=u.id,
    )
    w2 = Weibo.add(form, u.id)
    assert w2.content == '2222'

    form = dict(
        content='123333',
        user_id=u.id,
        weibo_id=w.id,
    )
    c = Comment.new(form)
    assert c.content == '123333'


if __name__ == '__main__':
    test()
