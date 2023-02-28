# class Car:
#
#     def __init__(self, count_passenger_seat: int, is_baby_seat: bool):
#         self.count_passenger_seat = count_passenger_seat
#         self.is_baby_seat = is_baby_seat
#         self.is_busy = False
#
#     def __str__(self):
#         return f'Car (count_passenger_seat={self.count_passenger_seat}, is_baby_seat={self.is_baby_seat}, is_busy={self.is_busy})'
#
#
# class Taxi:
#
#     def __init__(self, cars: list[Car]):
#         self.cars = cars
#
#     def find_car(self, count_passenger, is_baby):
#         cars = filter(lambda x: not x.is_busy, self.cars)
#         for car in cars:
#             if car.count_passenger_seat >= count_passenger:
#                 if not is_baby:
#                     car.is_busy = True
#                     return car
#                 elif car.is_baby_seat:
#                     car.is_busy = True
#                     return car
#
#
# class Category:
#     categories: list[str] = []
#
#     @classmethod
#     def add(cls, new_category: str) -> int:
#         if new_category.title() not in cls.categories:
#             cls.categories.append(new_category.title())
#             return cls.categories.index(new_category.title())
#         raise ValueError('category is not unique')
#
#     @classmethod
#     def get(cls, i: int) -> str:
#         return cls.categories[i]
#
#     @classmethod
#     def delete(cls, i: int) -> None:
#         try:
#             del cls.categories[i]
#         except IndexError:
#             pass
#
#     @classmethod
#     def update(cls, i: int, new_category_name: str) -> int:
#         if new_category_name.title() in cls.categories:
#             raise ValueError('category is no unique')
#         if i not in range(len(cls.categories)):
#             return cls.add(new_category_name)
#         cls.categories[i] = new_category_name.title()
#

class Category:
    categories: list[dict[str, ...]] = []

    @classmethod
    def add(cls, new_category: dict[str, ...]) -> int:
        for category in cls.categories:
            if category.get('name') == new_category.get('name'):
                raise ValueError('category is no unique')
        cls.categories.append(new_category)
        return cls.categories.index(new_category)

    @classmethod
    def delete(cls, i: int) -> None:
        try:
            del cls.categories[i]
        except IndexError:
            pass

    @classmethod
    def get(cls, i: int) -> dict[str, ...]:
        return cls.categories[i]

    @classmethod
    def update(cls, i: int, new_category_name: str) -> int:
        for category in cls.categories:
            if category.get('name') == new_category_name:
                raise ValueError('category is not unique')
        if i in range(len(cls.categories)):
            cls.categories[i]['name'] = new_category_name
        else:
            return cls.add({'name': new_category_name, 'is_published': False})

    @classmethod
    def make_published(cls, i: int) -> None:
        cls.categories[i]['is_published'] = True

    @classmethod
    def make_unpublished(cls, i: int) -> None:
        cls.categories[i]['is_published'] = False


# file = open('input.txt', 'r', encoding='utf-8')
# lines = [line.strip() for line in file if line.strip()]
# file.seek(0)
# print(file.read())
# print(lines)
# print(file.readlines())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# text = file.read()
# print(text)
# file.close()

# file = open('output.txt', 'w', encoding='utf-8')
# file.write('hello\n')
# file.writelines(['world\n', 'python'])
# file.close()

# with open('input.txt', 'r', encoding='utf-8') as file:
#     print(file.readlines())


# TODO Дан файл с текстом
#  Необходимо прочитать файл и подсчитать количество слов в каждой строке отдельно
#  результат записать в новый файл
# with open('input.txt', 'r', encoding='utf-8') as file:
#     lines = [line.strip() for line in file]
# words_count = [f'{line.count(" ") + 1}\n' if line else '0\n' for line in lines]
# with open('output.txt', 'w', encoding='utf-8') as file:
#     file.writelines(words_count)
# from json import load, loads, dump, dumps

# text = '''
# {
#   "name": "Alex",
#   "age": 34,
#   "is_human": true,
#   "language": null
# }
# '''
# print(loads(text))
# a = open('input.json', 'r', encoding='utf-8')
# data = load(a)
# a.close()
# print(data)

# data = {
#     'title': 'Coffee',
#     'descr': 'ГОРЯЧИЙ!',
#     'price': 5.5,
#     'doping': ['milk', 'sugar']
# }
# with open('output.json', 'w', encoding='utf-8') as file:
#     dump(data, file, indent=2, ensure_ascii=False)
from csv import reader, DictReader, writer, DictWriter

# with open('users.csv', 'r', encoding='utf-8') as file:
#     for user in DictReader(file):
#         print(user)

# users = [
#     {'name': 'name1', 'age': 1, 'city': 'city1'},
#     {'name': 'name2', 'age': 2, 'city': 'city2'},
#     {'name': 'name3', 'age': 3, 'city': 'city3'},
#     {'name': 'name4', 'age': 4, 'city': 'city4'},
#     {'name': 'name5', 'age': 5, 'city': 'city5'},
#     {'name': 'name6', 'age': 6, 'city': 'city6'},
# ]
# with open('output.csv', 'w', encoding='utf-8') as file:
#     w = DictWriter(file, fieldnames=('name', 'age', 'city'), delimiter=';')
#     w.writeheader()
#     w.writerows(users)

from yaml import safe_load, safe_dump


# with open('input.yaml', 'r', encoding='utf-8') as file:
#     data = safe_load(file)
# print(data)

# data = {
#     'name': 'name',
#     'age': 35,
#     'lang': ['ru', 'en'],
#     'city': None,
#     'is_human': True
# }
# with open('output.yaml', 'w', encoding='utf-8') as file:
#     safe_dump(data, file, sort_keys=False, indent=2)

from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')
print(parser.sections())
print(parser.options('FIRST'))
parser.set('FIRST', 'option1', 'new_value')
print(parser.get('FIRST', 'option1'))
with open('config.ini', 'w', encoding='utf-8') as file:
    parser.write(file, space_around_delimiters=False)
