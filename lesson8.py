# # # class Person(object):
# # #
# # #     def __init__(self, name: str, email: str) -> None:
# # #         self.name = name.title()
# # #         self.email = email.lower()
# # #
# # #     def dict(self) -> dict:
# # #         return {
# # #             'name': self.name,
# # #             'email': self.email
# # #         }
# # #
# # #
# # # class Manager(Person):
# # #
# # #     def __init__(self, name: str, email: str, salary: float):
# # #         super().__init__(name, email)
# # #         self.salary = salary
# # #
# # #     def __str__(self) -> str:
# # #         return self.name
# # #
# # #     def dict(self) -> dict:
# # #         data = super(Manager, self).dict()
# # #         data['salary'] = self.salary
# # #         return data
# # #
# # #
# # # # vasya = Manager(name='vasya', email='vasya@info.com', salary=1500)
# # # # print(vasya.dict())
# # #
# # # # class D:
# # # #     pass
# # # #
# # # #
# # # # class A(D):
# # # #
# # # #     name = 'A'
# # # #
# # # #
# # # # class B(D):
# # # #
# # # #     name = 'B'
# # # #
# # # #
# # # # class C(A, B):
# # # #     pass
# # # #
# # # #
# # # # print(C.mro())
# # #
# # #
# # # class Cat:
# # #
# # #     def say(self):
# # #         print('Meow')
# # #
# # #
# # # class Dog:
# # #
# # #     def say(self):
# # #         print('Woof')
# # #
# # #
# # # obj = Cat()
# # # obj.say()
# # # obj = Dog()
# # # obj.say()
# #
# #
# # class Category:
# #
# #     @classmethod
# #     def get(cls):
# #         return ['cat1', 'cat2', 'cat3']
# #
# #
# # class Product:
# #
# #     @classmethod
# #     def get(cls):
# #         return ['prod1', 'prod2', 'prod3']
# #
# #
# # class Paginator:
# #
# #     model = Category()
# #
# #     @classmethod
# #     def get_page(cls):
# #         data = cls.model.get()
# #
# #
# # class Person(object):
# #
# #     def __init__(self, name: str, email: str, card_number: str) -> None:
# #         self.name = name.title()
# #         self.email = email.lower()
# #         self.__card_number = card_number
# #
# #     @property
# #     def card_number(self):
# #         return self.__card_number[-4:]
# #
# #     @card_number.setter
# #     def card_number(self, value):
# #         if not isinstance(value, str):
# #             raise TypeError
# #         if not value.isdigit():
# #             raise ValueError
# #         if len(value) != 16:
# #             raise ValueError
# #         self.__card_number = value
# #
# #     def dict(self) -> dict:
# #         return {
# #             'name': self.name,
# #             'email': self.email
# #         }
# #
# #
# # # vasya = Person('vasya', 'vasya@info.com', '1234567896543215')
# # # print(vasya.card_number)
# # # vasya.card_number = '123456789012345678'
# #
# # #  Ассоциация
# # class Engine:
# #
# #     def __init__(self, volume: float, hp: int):
# #         self.volume = volume
# #         self.hp = hp
# #
# #
# # class Car:
# #
# #     def __init__(self, name: str, color: str, engine: Engine):
# #         self.name = name
# #         self.color = color
# #         self.engine = engine
# #
# #
# # # v6 = Engine(4.0, 550)
# # # bmw = Car('X6', 'black', v6)
# #
# #
# # # Агрегация (композиция)
# #
# #
# # class Beer:
# #
# #     def __init__(self, number):
# #         self.number = number
# #
# #     def open(self):
# #         print(f'Пиво {self.number} открыто')
# #
# #
# # class Manufacture:
# #
# #     beers = []
# #
# #     @classmethod
# #     def create_beers(cls, n: int):
# #         objs = [Beer(_) for _ in range(n)]
# #         cls.beers.extend(objs)
# #
# #     @classmethod
# #     def open(cls, *args):
# #         for number in args:
# #             cls.beers[number].open()
# #
# #
# # # Manufacture.create_beers(100)
# # # Manufacture.open(4, 7, 6, 9, 12)
# # # print(Manufacture.beers)
# #
# #
# #
# #
# from abc import ABC, abstractmethod
#
#
# class Person(ABC):
#
#     @abstractmethod
#     def dict(self) -> dict:
#         pass
#
#     @property
#     @abstractmethod
#     def password(self) -> str:
#         pass
#
#     def __init__(self, name: str, password: str):
#         self.name = name
#         self._password = password
#
#     def __str__(self):
#         return self.name
#
#
# class User(Person):
#
#     def dict(self) -> dict:
#         return {
#             'name': self.name,
#             'password': self._password
#         }
#
#     @property
#     def password(self) -> str:
#         return self._password
#

# from dataclasses import dataclass
#
#
# @dataclass(frozen=True)
# class User:
#     name: str
#     age: int
#     email: str
#
#
# vasya = User('vasya', 34, 'email@info.com')
# print(vasya)
# print(vasya.name)


# class User:
#
#     def __init__(self, name: str, age: int, email: str):
#         self.name = name
#         self.age = age
#         self.email = email
#
#     def __repr__(self):
#         return f'User (name={self.name}, age={self.age}, email={self.email})'
#
#     def __setattr__(self, key, value):
#         raise AttributeError
#
#     def __delattr__(self, item):
#         raise AttributeError


from pydantic import BaseModel, EmailStr, Field, validator, root_validator


class User(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(ge=18, lt=65)
    email: EmailStr = None
    password: str = Field(min_length=8)

    # @validator('password')
    # def validate_password(cls, value):
    #     pass
    @root_validator
    def validate_values(cls, values):
        if values.get('name').lower() in values.get('password').lower():
            raise ValueError('имя не должно содержаться в пароле')
        return values


try:
    vasya = User(name='vasya', age=19, email='vasya@info.com', password='qwerVaSyAtyuiop')
    print(vasya.dict())
except Exception as e:
    print(e)
