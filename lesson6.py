# # # class User:
# # #
# # #     users = []
# # #
# # #     # Создает экземпляр класса
# # #     def __new__(cls, *args, **kwargs):
# # #         instance = super().__new__(cls)
# # #         cls.users.append(instance)
# # #         return instance
# # #
# # #     # Инициализатор (конструктор)
# # #     def __init__(self, name: str, age: int, length: int, email: str, city: str):
# # #         if not isinstance(name, str):
# # #             raise TypeError('argument `name` must be string')
# # #
# # #         if not isinstance(age, int):
# # #             raise TypeError('argument `age` must be integer')
# # #
# # #         if age < 18:
# # #             raise ValueError('argument `age` must be great then 18')
# # #
# # #         self.name: str = name.title()
# # #         self.age: int = age
# # #         self.length: int = length
# # #         self.email: str = email.lower()
# # #         self.city: str = city.title()
# # #
# # #     def birthday(self):
# # #         self.age += 1
# # #
# # #     def dict(self):
# # #         return {'name': self.name, 'age': self.age, 'length': self.length, 'email': self.email, 'city': self.city}
# # #
# # #     @classmethod
# # #     def change_gender(cls, value):
# # #         cls.gender = value
# # #
# # #     def __len__(self):
# # #         return self.length ** 2
# # #
# # #     def __getitem__(self, item):
# # #         return getattr(self, item)
# # #
# # #     def __str__(self):
# # #         return self.name
# # #
# # #
# # # vasya = User('vasya', 35, 182, 'vasya@info.com', 'Minsk')
# # # petya = User('petya', 25, 174, 'petya@info.com', 'Gomel')
# # # # data = vasya.dict()
# # # print(vasya)
# # # # print(vasya['name'])
# # # # print(len(vasya))
# # # # print(data)
# # # # print(petya.users[0].name)
# # # # print(vasya.users)
# # #
# #
# #
# # # TODO Написать класс Numbers, конструктор класса принимает список чисел
# # #  и определяет атрибут объекта, написать метод объекта average
# # #  возвращающий среднее арифмитрическое между всеми числами
# # #  написать метод объекта max_count возвращающий число, которое встречается чаще всего
# # #  если таких чисел несколько, вернуть среднее арифимитическое среди таких чисел
# #
# #
# # class Numbers:
# #
# #     def __init__(self, numbers: list[int]):
# #         self.numbers = numbers
# #
# #     def average(self):
# #         result = sum(self.numbers) / len(self.numbers)
# #         # return sum(self.numbers) / len(self.numbers)
# #         return result
# #
# #     def max_count(self):
# #         counter = {}
# #         for number in self.numbers:
# #             counter[number] = self.numbers.count(number)
# #         max_count = max(counter.values())
# #         result = []
# #         for number in self.numbers:
# #             if counter[number] == max_count:
# #                 result.append(number)
# #         return sum(result) / len(result)
# #
# #
# # # TODO посчитать среднее арифмитическое чисел списка numbers
# # # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # print(sum(numbers) / len(numbers))
# #
# # n = Numbers([4, 2, 6, 3, 54, 2, 4, 2, 4, 2, 4, 34, 5, 6, 7, 78, 45, ])
# # print(n.average())
# # print(n.max_count())
#
# # TODO написать класс Student
# #  конструктор принимает аргументы first_name: str, group: int, marks: list[int]
# #  написать магический метод __str__ возвращающий форматированную строку с данными об студенте
# #  написать функцию sort_student(не метод), принимающий список студентов и сортирующий их по имени
#
# class Student:
#     """
#     Класс представления объекта студента
#     """
#
#     def __init__(self, first_name, group, marks):
#         self.first_name = first_name.title()
#         self.group = group
#         self.marks = marks
#         self.i = -1
#
#     def __str__(self):
#         return f'Student {self.first_name} {self.group} {self.marks}'
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i < len(self.marks):
#             return self.marks[self.i]
#         else:
#             self.i = -1
#             raise StopIteration
#
#
# vasya = Student('vasya', 2, [4, 5, 4, 5, 4, 5, 4, 5, 4, 5])
# petya = Student('petya', 3, [5, 8, 6, 4, 5, 6, 4, 6, 1, 5, 3, 5])
# masha = Student('masha', 1, [7, 8, 5, 6, 9, 6, 4, 7, 5])
# # print(Student.__doc__)
# # for mark in vasya:
# #     print(mark)
# # students = [vasya, petya, masha]
#
#
# def sort_student(students):
#     """Соритровка списка студентов по именам
#
#     :param students: список экземпляров класса Student
#     :return: отсортированный список экземпляров класса Student по атрибуту first_name
#     """
#     students.sort(key=lambda student: student.first_name)
#     return students
# #
# #
# # for student in sort_student(students):
# #     print(student)
#
# # TODO Написать класс Rectangle
# #  1. конструктор класса принимает координаты точек по диагонали (правая нижняя и левая верхняя
# #  точки или левая нижняя и правая верхняя точки)
# #  2. написать метод объекта perimeter высчитывающий и возвращающий периметр получившегося
# #  прямоугольника
# #  3. написать метод объекта square высчитывающий и возвращающий площадь получившегося
# #  прямоугольника
#
#
# class Point:
#
#     def __init__(self, x, y):
#         if not isinstance(x, int):
#             raise TypeError
#
#         if not isinstance(y, int):
#             raise TypeError
#
#         self.x = x
#         self.y = y
#
#
# class Rectangle:
#
#     def __init__(self, point1: Point, point2: Point):
#         self.width = abs(point2.x - point1.x)
#         self.height = abs(point2.y - point1.y)
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def square(self):
#         return self.width * self.height
#
#
# point1 = Point(-3, -5)
# point2 = Point(2, 4)
# r = Rectangle(point1, point2)
# print(r.perimeter())
# print(r.square())


def decimal_to_binary(decimal: int) -> str:
    binary = ''
    while decimal > 1:
        binary = f'{decimal % 2}' + binary
        decimal //= 2
    binary = f'{decimal}' + binary
    return binary


def binary_to_decimal(binary: str) -> int:
    decimal = 0
    for i in binary:
        i = int(i)
        decimal *= 2
        decimal += i
    return decimal


# print(binary_to_decimal(decimal_to_binary(14)))


def encode_morse(text: str) -> str:
    morse_code = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        " ": " ",
    }
    morse = ''
    text = text.upper()
    for el in text:
        if el in morse_code:
            morse += morse_code.get(el) + ' '
    return morse


def decode_morse(morse: str) -> str:
    morse = morse.replace('   ', ' | ').split()
    text = ''
    morse_code = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '-----': '0',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '|': ' '
    }
    for el in morse:
        if el in morse_code:
            text += morse_code.get(el)
    return text


# from collections import deque
#
# n = 2
# numbers = [*range(10)]
# q = deque(numbers)
# q.rotate(n)
# numbers = [*q]
# print(numbers)


# objs = [*filter(lambda x: isinstance(x, str), [1, 2, 3, 'hello', 'world', 3, 4, 5])]
# print(objs)
# for i in range(len(objs) - 1, -1, -1):
#     if not isinstance(objs[i], str):
#         del objs[i]
#
# print(objs)

# numbers = [*range(10)]
# for i in range(len(numbers) // 2):
#     numbers[i], numbers[~i] = numbers[~i], numbers[i]
#
# print(numbers)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(numbers)):
#     if i == len(numbers) - 1:
#         print(numbers[i-1] + numbers[0])
#     else:
#         print(numbers[i-1] + numbers[i+1])

def find_country(city: str) -> str:
    countries = {
        'RB': ['Minsk', 'Gomel', 'Mogilev'],
        'RF': ['SPB', 'Moscow', 'EKB']
    }
    for country, cities in countries.items():
        if city in cities:
            return country


# city = input()
# countries = {
#     'RB': ['Minsk', 'Gomel', 'Mogilev'],
#     'RF': ['SPB', 'Moscow', 'EKB']
# }
# country = [*filter(lambda x: city in x[1], countries.items())][0][0]
# print(country)
# for country, cities in countries.items():
#     if city in cities:
#         print(country)
#         break


# users = {
#     1: {
#         'name': 'name1',
#         'email': 'email@info.com'
#     },
#     2: {
#         'name': 'name2',
#         'email': ''
#     },
#     3: {
#         'name': 'name3',
#         'email': None
#     },
#     4: {
#         'name': 'name4'
#     }
# }
# users = dict(filter(lambda x: not x[1].get('email'), users.items()))
# print(users)
# for user in users.values():
#     # if not user.get('email'):
#     #     print(user.get('name'))
#     if user.get('email') == '' or 'email' not in user or user.get('email') is None:
#         print(user.get('name'))
