# # from datetime import datetime, date, time, timedelta, timezone
# # from time import *
# #
# # # end_date = datetime.now()
# # # delta = timedelta(weeks=52)
# # # print(end_date + delta)
# # # start_date = datetime(year=1998, month=12, day=11, hour=15)
# # # print(end_date - start_date)
# # # print(date_now.timestamp())
# # # print(date_now.strftime('%a %d %B %Y %H/%M'))
# # # print(datetime.strptime('Thu 02 March 2023 14/49', '%a %d %B %Y %H/%M'))
# # from enum import Enum, IntEnum
# #
# #
# # # class HTTPStatus(int, Enum):
# # #     OK: int = 200
# # #     PAGE_NOT_FOUND: int = 404
# # #
# # #
# # # status_code = 200
# # #
# # # if status_code == HTTPStatus.OK:
# # #     pass
# #
# # # class Role(int, Enum):
# # #     ADMIN: int = 1
# # #     USER: int = 2
# # #     MANAGER: int = 3
# #
# # roles = [('admin', 1), ('user', 2), ('manager', 3)]
# #
# # Role = IntEnum("Role", roles)
# #
# #
# # user = {
# #     'name': 'Alex',
# #     'email': 'alex@gmail.com',
# #     'role_id': 1
# # }
# #
# # if user.get('role_id') == Role.admin:
# #     print('admin')
#
#
# from argparse import ArgumentParser
#
#
# # parser = ArgumentParser()
# # parser.add_argument('-p', '--port', default='8000', help='Порт запуска сервера')
# # parser.add_argument('-d', '--debug', action='store_true', help='Режим отладки')
# # args = parser.parse_args()
# # print(args)
#
# import logging
#
#
# logging.basicConfig(
#     filename='log.log',
#     filemode='a',
#     format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
#     # datefmt='%d/%m/%y/%H/%M',
#     level=logging.INFO
# )
#
#
# def foo():
#     try:
#         a = int(input())
#         b = int(input())
#         c = a / b
#     except ValueError:
#         logging.error('Пользователь ввел не число')
#     except ZeroDivisionError:
#         logging.error('Пользователь делит на 0')
#     else:
#         logging.info('Все ОК')
#
#
# foo()


from sqlite3 import connect, Cursor


conn = connect('db.sqlite3')
cur = conn.cursor()
# from collections import namedtuple


# def namedtuple_factory(cursor, row):
#     fields = [column[0] for column in cursor.description]
#     cls = namedtuple("Row", fields)
#     return cls._make(row)
#
#
# cur.row_factory = namedtuple_factory

# cur.execute('''
#     CREATE TABLE IF NOT EXISTS category(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(64) NOT NULL UNIQUE,
#         is_published BOOLEAN DEFAULT(false)
#     );
# ''')
# conn.commit()

# cur.execute('''
#     CREATE TABLE IF NOT EXISTS product(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(64) NOT NULL,
#         price DECIMAL(8, 2) NOT NULL DEFAULT(0),
#         description VARCHAR(2048),
#         category_id INTEGER NOT NULL,
#         FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE
#     );
# ''')
# conn.commit()

# cur.executemany('''
#     INSERT INTO category(name, is_published)
#     VALUES(?, ?);
# ''', (('Coffee', True), ('Hamburger', False)))
# conn.commit()

# cur.execute('''
#     SELECT * FROM category
#     WHERE id > ?;
# ''', (1, ))
# print(cur.description)
# print(cur.fetchall())

# cur.execute('''
#     SELECT *
#     FROM category
#     JOIN product
#     ON category.id = product.category_id
#     WHERE category.is_published = ?;
# ''', (True, ))
# print(cur.description)
# print(cur.fetchall())


# cur.execute('''
#     UPDATE category SET is_published = ?
#     WHERE id = ?;
# ''', (True, 3))
# conn.commit()

# cur.execute('''
#     DELETE FROM product
#     WHERE id = ?;
# ''', (1, ))
# conn.commit()
