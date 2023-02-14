# # # # def is_palindrome(text):
# # # #     text = text.lower()
# # # #     return text == text[::-1]
# # # #
# # # #
# # # # def foo(a, b=None):
# # # #     if b is None:
# # # #         b = []
# # # #     b.append(a)
# # # #     return b
# # # #
# # # #
# # # # def multiply(*args):
# # # #     mul = 1
# # # #     for arg in args:
# # # #         mul *= arg
# # # #     return mul
# # # #
# # # #
# # # # def bar(**kwargs):
# # # #     print(kwargs)
# # # #
# # # #
# # # # def baz(a, b, *args, c=4, d=None, **kwargs):
# # # #     print(a)
# # # #     print(b)
# # # #     print(c)
# # # #     print(args)
# # # #     print(d)
# # # #     print(kwargs)
# # # #
# # # #
# # #
# # # # def foo():
# # # #     def bar():
# # # #         print('bar')
# # # #     bar()
# # # #
# # # #
# # #
# # #
# # # def foo():
# # #     print('foo')
# # #
# # #
# # # def bar():
# # #     print('bar')
# # #
# # #
# # # def baz():
# # #     print('baz')
# # #
# # #
# # # def error():
# # #     print('error')
# # #
# # #
# # # # a = input()
# # #
# # # data = {
# # #     '1': foo,
# # #     '2': bar,
# # #     '3': baz
# # # }
# # # # data.get(a, error)()
# # #
# # # # if a == '1':
# # # #     foo()
# # # # elif a == '2':
# # # #     bar()
# # # # elif a == '3':
# # # #     baz()
# # # # else:
# # # #     error()
# #
# # #
# # multiply = lambda x, y: x * y
# # #
# # # print(multiply(4, 5))
# #
# #
# # # objs = ['Hello', 4, 'python', 1, 2, 'age', 'apple', 3, 'Pycharm']
# # # objs.sort(key=lambda x: f'{x}')
# # # # ['Hello', '4', 'python', '1', '2', 'age', 'apple', '3', 'Pycharm']
# # # print(objs)
# #
# #
# # # map
# #
# # # numbers = ['1', '2', '3', '4', '5', '6']
# # # result = []
# # # for number in numbers:
# # #     result.append(int(number) ** 2)
# #
# # # result = [*map(lambda number: int(number) ** 2, numbers)]
# # # print(result)
# #
# # # filter
# #
# # # objs = [1, 2, 'hello', 4, 5, 'world', 'python']
# # # result = []
# # # for obj in objs:
# # #     if isinstance(obj, str):
# # #         result.append(obj)
# #
# # # result = [*filter(lambda obj: isinstance(obj, str), objs)]
# # # print(result)
# #
# # # numbers = [1, 2, 3, 4]
# # # reversed_numbers = reversed(numbers)
# # # print(list(reversed_numbers) == list(reversed_numbers))
# # # print(list(reversed_numbers))
# # # print(list(reversed_numbers))
# #
# # # numbers = [1, 2, 3, 4]
# # # iter_numbers = iter(numbers)
# #
# # # zip
# #
# # # text = 'hello'
# # # numbers = [1, 2, 3, 4]
# # # objs = (True, False)
# # #
# # # # strict начиная с python 3.10
# # # result = [*zip(text, numbers, objs, strict=True)]
# # # print(result)
# #
# # # from itertools import zip_longest
# # #
# # #
# # # numbers = [*range(2, 45, 2)]
# # # iter_numbers = iter(numbers)
# # # result = [[*filter(lambda x: x, line)] for line in zip_longest(*[iter_numbers]*5)]
# #
# # # def bar(a):
# # #     def baz(b):
# # #         return a * b
# # #     return baz
# #
# #
# # # func = bar(5)
# # # print(func(4))
# # # print(func(7))
# # # print(func(3))
# #
# #
# # # db = [f'user{i}' for i in range(100)]
# # #
# # #
# # # def get_user():
# # #     for user in db:
# # #         yield user
# # #
# # #
# # # a = get_user()
# # # for user in a:
# # #     print(user)
# #
# # # print(globals().get('multiply')(4, 4))
# #
# # a = 5
# # b = 4
# #
# #
# # def foo():
# #     b = 3
# #
# #     def bar():
# #         global a
# #         print(a)
# #         print(b)
# #     print(locals())
# #     bar()
# #
# #
# # foo()
#
# numbers = [4, 56, 2, 5, 2, 5, 78, 5, 6, [6, 3, 4, 3, [6, 3, 5, [6, 4, 56, 3], [5, 3, 4], 5, 23, 4, [6, 4, 6, 4, [6, 34, 5,]]]]]
#
#
# def recursive_multiply(numbers):
#     mul = 1
#     for number in numbers:
#         if isinstance(number, int | float):
#             mul *= number
#         elif isinstance(number, list | tuple):
#             mul *= recursive_multiply(number)
#     return mul
#
#
# # print(recursive_multiply(numbers))
#
# def is_arguments_string(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if not isinstance(arg, str):
#                 raise TypeError('не строка')
#         for val in kwargs.values():
#             if not isinstance(val, str):
#                 raise TypeError('не строка')
#
#         result = func(*args, **kwargs)
#         # print('post process')
#         return result
#     return wrapper
#
#
# @is_arguments_string
# def is_palindrome(text):
#     text = text.lower()
#     return text == text[::-1]
#
#
# def decorator(c):
#     def _decorator(func):
#         def wrapper(a, b):
#             a += c
#             b += c
#             return func(a, b)
#         return wrapper
#     return _decorator
#
#
# # @decorator(2)
# def foo(a, b):
#     return a * b
#
#
# wrapped_foo = decorator(foo)
#
# print(foo(4, 6))

from time import sleep
from datetime import datetime
from functools import lru_cache, cache, reduce


@cache
def multiply(a, b):
    sleep(3)
    return a * b


# start_time = datetime.now()
# print(multiply(2, 4))
# print(multiply(2, 4))
# print(multiply(2, 4))
# print(multiply(2, 4))
# print(multiply(2, 4))
# print(multiply(2, 4))
# print(multiply(2, 4))
# print(multiply(2, 4))
# end_time = datetime.now()
# print(end_time - start_time)


# numbers = [4, 6, 2, 4, 3]
# result = reduce(lambda x, y: x * y, numbers)
# print(result)


from random import randint


numbers = [randint(1, 10) for _ in range(10)]
print(numbers)
