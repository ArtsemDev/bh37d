# # # # # set1 = {1, 2, 4}
# # # # # set2 = {1, 2, 3, 4, 5}
# # # # # # print(set1.issubset(set2))
# # # # # # print(set1 <= set2)
# # # # # print(set1.union(set2))
# # # # # print(set2 | set1)
# # # # from collections import *
# # # #
# # # #
# # # # # text = 'hello world'
# # # # # text2 = 'hello python'
# # # # # el_counter = Counter(text)
# # # # # el_counter2 = Counter(text2)
# # # # # # print(el_counter)
# # # # # # el_counter.subtract(el_counter2)
# # # # # # print(el_counter2)
# # # # # # print(el_counter)
# # # # # print(el_counter - el_counter2)
# # # #
# # # # # numbers = [1, 2, 3, 4, 5, 6]
# # # # # q = deque(numbers)
# # # # # q.rotate(-2)
# # # # # print(q)
# # # # data = defaultdict(str)
# # # # data['languages'] += 'ru'
# # # # print(data)
# # # # data = OrderedDict({'name': 'alex', 'city': 'Minsk', 'age': 34})
# # # # data.move_to_end('city', last=True)
# # # # print(data)
# # #
# # # # keys = ('name', 'city', 'age')
# # # # User = namedtuple('User', keys)
# # # # vasya = User(name='vasya', city='Minsk', age=34)
# # # # print(vasya._asdict())
# # #
# # # # a = int(input())
# # # # if a == 0:  # True
# # # #     print('zero')  # Выполняется тело if
# # # # print('main thread')
# # #
# # # # a = int(input())
# # # # if a % 2:
# # # #     print('odd')
# # # # elif a == 0:
# # # #     print('zero')
# # # # else:
# # # #     print('even')
# # #
# # # # users = []
# # # # if users:
# # # #     pass
# # #
# # # # a = int(input())
# # # # if a % 2:
# # # #     is_even = 'No'
# # # # elif a == 0:
# # # #     is_even = 'Zero'
# # # # else:
# # # #     is_even = 'Yes'
# # # #
# # # # is_even = 'No' if a % 2 else 'Yes' if a != 0 else 'Zero'
# # #
# # # x = True
# # # y = False
# # # z = False
# # # if not x or y:  # 0 + 0 = 0
# # #     print(1)
# # # elif not x or not y and z:  # 0 + (1 * 0) = 0 + 0 = 0
# # #     print(2)
# # # elif not x or y or not y and x:  # 0 + 0 + (1 * 1) = 0 + 0 + 1 = 1
# # #     print(3)
# # # else:
# # #     print(4)
# #
# # # for number in range(1, 10, 2):  # 1 3 5 7 9
# # #     number **= 2
# # #     if number == 32:
# # #         break
# # #     print(number, end=' ')
# # # else:
# # #     print('finish')
# #
# # # text = 'hello world'
# # # for i in text:
# # #     print(i)
# #
# # # УПОРЯДОЧЕННЫМИ КОЛЛЕКЦИЯМИ
# # # str, list, tuple
# # # text = 'hello world'
# # # for i, j in enumerate(text, 2):
# # #     print(i, j)
# #
# # # text = 'hello world'
# # # for i in range(len(text)):
# # #     print(text[i])
# #
# # data = {
# #     'key1': 'val1',
# #     'key2': 'val2',
# #     'key3': 'val3',
# #     'key4': 'val4',
# #     'key5': 'val5',
# # }
# #
# # # for key in data.keys():
# # #     print(key)
# #
# # # for val in data.values():
# # #     print(val)
# #
# # for key, val in data.items():
# #     print(key, val)
#
# # numbers = [i for i in range(100) if not i % 2]
# # for i in range(100):
# #     if not i % 2:
# #         numbers.append(i)
#
# # n = 5
# # matrix = [[0 for _ in range(n)] for _ in range(n)]
# # print(matrix)
#
# # a = 5
# # if isinstance(a, (int, float)):
# #     pass
#
# # any()
#
# # objs = [4, 6, 'sdf', None]
# # if any(objs):
# #     print('Один из объектов точно True')
#
# # words = ['hello', 'Python', 'World', 'pycharm', 'Skynet']
# #
# # for word in words.copy():
# #     words.append(word)
# # print(words)
# # for a in aa:
# #     if a.istitle():
# #         aa.remove(a)
# # print(aa)
#
# # try:
# #     a = int(input())
# #     b = int(input())
# #     c = a / b
# # except ValueError:
# #     print('A or B is not digit')
# # except ZeroDivisionError:
# #     print('zero division')
# # # except Exception as e:
# # #     print(e)
# # #     print('other')
# # else:
# #     print('Ошибок не было')
# # finally:
# #     print('Выполняется в любом случае')
#
# age = input()
# try:
#     age = int(age)
# except ValueError:
#     print('Are  you stupid?')
# # if age.isdigit():
# #     age = int(age)
# # else:
# #     print('Are you stupid?')

#  TODO спрашивать у пользователя данные с клавиатуры пока он не введет число
# number = input('enter number: ')
# while not number.isdigit():
#     number = input('try again: ')

# number = input()
# while True:
#     try:
#         number = int(number)
#     except ValueError:
#         number = input()
#     else:
#         break

# while not (number := input()).isdigit(): ...

# N = int(input('N: '))
# M = int(input('M: '))
# K = int(input('K: '))
#
# while N:
#     if K % M == 0:
#         N -= 1
#         print(K, end=' ')
#         K += M
#     else:
#         K += 1

# a = int(input('a: '))
# b = int(input('b: '))
# action = input('operation: ')
# if action == '+':
#     print(a + b)
# elif action == '-':
#     print(a - b)
#

# N = int(input())

# VAR 1
# c = 0
# for i in range(2, N+1, 2):
#     print(i, end=' ')
#     c += 1
#     if c % 5 == 0:
#         print()

# VAR 2
# for i in range(2, N+1, 2):
#     print(i, end=' ')
#     if i % 10 == 0:
#         print()

# for i in range(2, N+1, 10):
#     for j in range(i, i+9, 2):
#         if j <= N:
#             print(j, end=' ')
#         else:
#             break
#     print()
