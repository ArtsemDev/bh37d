# # class Car:
# #
# #     def __init__(self, count_passenger_seat: int, is_baby_seat: bool):
# #         self.count_passenger_seat = count_passenger_seat
# #         self.is_baby_seat = is_baby_seat
# #         self.is_busy = False
# #
# #     def __str__(self):
# #         return f'Car (count_passenger_seat={self.count_passenger_seat}, is_baby_seat={self.is_baby_seat}, is_busy={self.is_busy})'
# #
# #
# # class Taxi:
# #
# #     def __init__(self, cars: list[Car]):
# #         self.cars = cars
# #
# #     def find_car(self, count_passenger, is_baby):
# #         cars = filter(lambda x: not x.is_busy, self.cars)
# #         for car in cars:
# #             if car.count_passenger_seat >= count_passenger:
# #                 if not is_baby:
# #                     car.is_busy = True
# #                     return car
# #                 elif car.is_baby_seat:
# #                     car.is_busy = True
# #                     return car
# #
# #
# # class Category:
# #     categories: list[str] = []
# #
# #     @classmethod
# #     def add(cls, new_category: str) -> int:
# #         if new_category.title() not in cls.categories:
# #             cls.categories.append(new_category.title())
# #             return cls.categories.index(new_category.title())
# #         raise ValueError('category is not unique')
# #
# #     @classmethod
# #     def get(cls, i: int) -> str:
# #         return cls.categories[i]
# #
# #     @classmethod
# #     def delete(cls, i: int) -> None:
# #         try:
# #             del cls.categories[i]
# #         except IndexError:
# #             pass
# #
# #     @classmethod
# #     def update(cls, i: int, new_category_name: str) -> int:
# #         if new_category_name.title() in cls.categories:
# #             raise ValueError('category is no unique')
# #         if i not in range(len(cls.categories)):
# #             return cls.add(new_category_name)
# #         cls.categories[i] = new_category_name.title()
# #
#
# class Category:
#     categories: list[dict[str, ...]] = []
#
#     @classmethod
#     def add(cls, new_category: dict[str, ...]) -> int:
#         for category in cls.categories:
#             if category.get('name') == new_category.get('name'):
#                 raise ValueError('category is no unique')
#         cls.categories.append(new_category)
#         return cls.categories.index(new_category)
#
#     @classmethod
#     def delete(cls, i: int) -> None:
#         try:
#             del cls.categories[i]
#         except IndexError:
#             pass
#
#     @classmethod
#     def get(cls, i: int) -> dict[str, ...]:
#         return cls.categories[i]
#
#     @classmethod
#     def update(cls, i: int, new_category_name: str) -> int:
#         for category in cls.categories:
#             if category.get('name') == new_category_name:
#                 raise ValueError('category is not unique')
#         if i in range(len(cls.categories)):
#             cls.categories[i]['name'] = new_category_name
#         else:
#             return cls.add({'name': new_category_name, 'is_published': False})
#
#     @classmethod
#     def make_published(cls, i: int) -> None:
#         cls.categories[i]['is_published'] = True
#
#     @classmethod
#     def make_unpublished(cls, i: int) -> None:
#         cls.categories[i]['is_published'] = False
#
#
# # file = open('input.txt', 'r', encoding='utf-8')
# # lines = [line.strip() for line in file if line.strip()]
# # file.seek(0)
# # print(file.read())
# # print(lines)
# # print(file.readlines())
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())
# # text = file.read()
# # print(text)
# # file.close()
#
# # file = open('output.txt', 'w', encoding='utf-8')
# # file.write('hello\n')
# # file.writelines(['world\n', 'python'])
# # file.close()
#
# # with open('input.txt', 'r', encoding='utf-8') as file:
# #     print(file.readlines())
#
#
# # TODO Дан файл с текстом
# #  Необходимо прочитать файл и подсчитать количество слов в каждой строке отдельно
# #  результат записать в новый файл
# # with open('input.txt', 'r', encoding='utf-8') as file:
# #     lines = [line.strip() for line in file]
# # words_count = [f'{line.count(" ") + 1}\n' if line else '0\n' for line in lines]
# # with open('output.txt', 'w', encoding='utf-8') as file:
# #     file.writelines(words_count)
# # from json import load, loads, dump, dumps
#
# # text = '''
# # {
# #   "name": "Alex",
# #   "age": 34,
# #   "is_human": true,
# #   "language": null
# # }
# # '''
# # print(loads(text))
# # a = open('input.json', 'r', encoding='utf-8')
# # data = load(a)
# # a.close()
# # print(data)
#
# # data = {
# #     'title': 'Coffee',
# #     'descr': 'ГОРЯЧИЙ!',
# #     'price': 5.5,
# #     'doping': ['milk', 'sugar']
# # }
# # with open('output.json', 'w', encoding='utf-8') as file:
# #     dump(data, file, indent=2, ensure_ascii=False)
# from csv import reader, DictReader, writer, DictWriter
#
# # with open('users.csv', 'r', encoding='utf-8') as file:
# #     for user in DictReader(file):
# #         print(user)
#
# # users = [
# #     {'name': 'name1', 'age': 1, 'city': 'city1'},
# #     {'name': 'name2', 'age': 2, 'city': 'city2'},
# #     {'name': 'name3', 'age': 3, 'city': 'city3'},
# #     {'name': 'name4', 'age': 4, 'city': 'city4'},
# #     {'name': 'name5', 'age': 5, 'city': 'city5'},
# #     {'name': 'name6', 'age': 6, 'city': 'city6'},
# # ]
# # with open('output.csv', 'w', encoding='utf-8') as file:
# #     w = DictWriter(file, fieldnames=('name', 'age', 'city'), delimiter=';')
# #     w.writeheader()
# #     w.writerows(users)
#
# from yaml import safe_load, safe_dump
#
#
# # with open('input.yaml', 'r', encoding='utf-8') as file:
# #     data = safe_load(file)
# # print(data)
#
# # data = {
# #     'name': 'name',
# #     'age': 35,
# #     'lang': ['ru', 'en'],
# #     'city': None,
# #     'is_human': True
# # }
# # with open('output.yaml', 'w', encoding='utf-8') as file:
# #     safe_dump(data, file, sort_keys=False, indent=2)
#
# # from configparser import ConfigParser
# #
# # parser = ConfigParser()
# # parser.read('config.ini')
# # print(parser.sections())
# # print(parser.options('FIRST'))
# # parser.set('FIRST', 'option1', 'new_value')
# # print(parser.get('FIRST', 'option1'))
# # with open('config.ini', 'w', encoding='utf-8') as file:
# #     parser.write(file, space_around_delimiters=False)
#
# from openpyxl import Workbook
#
# book = Workbook()
# book.create_sheet('USERS')
# sheet = book.active
# sheet.append(['name', 'age', 'city'])
# sheet.append(['vasya', 34, 'minsk'])
# book.save('users.xlsx')

# TODO Дан txt файл, на каждой строке что-то записано
#  необходимо найти и проссумировать все числа в файле

# file = open('kakoito.txt', 'r', encoding='utf-8')
# lines = [line.strip() for line in file]
#
# res = 0
# for line in lines:
#     if line.isdigit():
#         res += int(line)
# print(res)

# from pydantic import BaseModel, Field
# from pydantic.types import Decimal
#
#
# class CategoryModel(BaseModel):
#     name: str
#     is_published: bool = Field(default=False)
#     parent: "CategoryModel" = Field(default=None)
#
#
# CategoryModel.update_forward_refs()
#
# data = {
#     'name': 'Cat1',
#     'is_published': True,
#     'parent': {
#         'name': 'Parent1',
#         'is_published': True,
#         'parent': {
#             'name': 'ParentParent1'
#         }
#     }
# }
# data = CategoryModel(**data)
# print(data.dict())
# class ProductModel(BaseModel):
#     name: str
#     descr: str = Field(default=None)
#     price: Decimal = Field(max_digits=8, decimal_places=2)
#     category: CategoryModel


# data = {
#     'name': 'Prod1',
#     'price': 100.00,
#     'category': {
#         'name': 'Cat1',
#         'is_published': 'uygijio'
#     }
# }
# data = ProductModel(**data)

# TODO Дан файл products.csv
#  с ключами title, descr, price
#  title: str - обязательный
#  descr: str - не обязательный
#  price: Decimal - 6, 2 обязательный
#  Необходимо Прописать pydantic модель
#  Прочитать CSV файл, каждую запись которого провалидировать с помощью
#  pydantic модели
#  Записи не прошедшие валидацию, необходимо записать в другой файл
from csv import DictReader, DictWriter

from pydantic import BaseModel, Field
from pydantic.types import Decimal


class ProductModel(BaseModel):
    title: str
    descr: str = Field(default=None)
    price: Decimal = Field(max_digits=6, decimal_places=2)


invalid_products = []
with open('products.csv', 'r', encoding='utf-8') as file:
    reader = DictReader(file)
    for product in reader:
        try:
            ProductModel(**product)
        except Exception:
            invalid_products.append(product)

with open('invalid_products.csv', 'w', encoding='utf-8') as file:
    writer = DictWriter(file, fieldnames=('title', 'descr', 'price'))
    writer.writeheader()
    writer.writerows(invalid_products)
