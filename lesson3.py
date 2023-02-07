# # # # # # # # # # # # # # # # text = 'hello|world|python'
# # # # # # # # # # # # # # # # words = text.split('|')
# # # # # # # # # # # # # # # # text2 = '---'.join(words)
# # # # # # # # # # # # # # # # print(words)
# # # # # # # # # # # # # # # # # print(text)
# # # # # # # # # # # # # # # # print(text2)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # text = '.,-,.,.,pycharm hello---python hello world ß,,..--.-'
# # # # # # # # # # # # # # # print(text.lstrip(',.-'))
# # # # # # # # # # # # # # # print(text.rstrip(',.-'))
# # # # # # # # # # # # # # # print(text.strip(',.-'))
# # # # # # # # # # # # # # # # print(text.removeprefix('pych'))
# # # # # # # # # # # # # # # # print(text.removeprefix('Pych'))
# # # # # # # # # # # # # # # # print(text.lower())
# # # # # # # # # # # # # # # # print(text.casefold())
# # # # # # # # # # # # # # # # print(text.replace('hello', '', 1))
# # # # # # # # # # # # # # # # i = text.find('hello', 5, 20)
# # # # # # # # # # # # # # # # j = text.rfind('hello')
# # # # # # # # # # # # # # # # print(i)
# # # # # # # # # # # # # # # # print(j)
# # # # # # # # # # # # # # # # print(text.partition('python'))
# # # # # # # # # # # # # # # # print(text.rpartition('python'))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # text = 'hello\tpython\tworld\t'
# # # # # # # # # # # # # # text2 = 'age\tname\tcity\t'
# # # # # # # # # # # # # # print(text.expandtabs(10))
# # # # # # # # # # # # # # print(text2.expandtabs(10))
# # # # # # # # # # # # #
# # # # # # # # # # # # # text = 'hello'
# # # # # # # # # # # # # print(text.center(11, '-'))
# # # # # # # # # # # # # print(text.ljust(11, '-'))
# # # # # # # # # # # # # print(text.rjust(11, '-'))
# # # # # # # # # # # # # print(text.zfill(11))
# # # # # # # # # # # # print(bin(12)[2:].zfill(8))
# # # # # # # # # # #
# # # # # # # # # # # print(bin(14))
# # # # # # # # # # # print(bin(11))
# # # # # # # # # # # print(bin(5))
# # # # # # # # # # # print(14 ^ 11)
# # # # # # # # # #
# # # # # # # # # # # print(~8)
# # # # # # # # # #
# # # # # # # # # # # text = 'qwertyu'
# # # # # # # # # # # print(text[1], text[~1])
# # # # # # # # # #
# # # # # # # # # # print(bin(13))
# # # # # # # # # # print(13 >> 2)
# # # # # # # # # # print(bin(3))
# # # # # # # # #
# # # # # # # # # # a = 4
# # # # # # # # # # b = 4
# # # # # # # # # # print(id(a))
# # # # # # # # # # print(id(b))
# # # # # # # # # print(list('hello'))
# # # # # # # #
# # # # # # # # zeros = [25 / i for i in range(1, 100)]
# # # # # # # # print(zeros)
# # # # # # #
# # # # # # # # words = ['hello', 'python', 'world', 'pycharm', 'python']
# # # # # # # # result = words + [1, 2, 3, 4]
# # # # # # # # print(result)
# # # # # # # # print(words)
# # # # # # # # words.extend([1, 2, 3, 4])
# # # # # # # # print(words)
# # # # # # # # words.remove('python')
# # # # # # # # print(words)
# # # # # # # # del words[1:3]
# # # # # # # # python = words.pop(1)
# # # # # # # # print(words)
# # # # # # # # print(python)
# # # # # # # numbers = [1, 2, 3, 4, 'hello', 'hello']
# # # # # # # print(numbers.count('hello'))
# # # # # # # print(numbers * 3)
# # # # # #
# # # # # # # numbers = [3, 5, 2, 3, 8, 4, 7, 3]
# # # # # # # # numbers.sort(reverse=True)
# # # # # # # sorted_numbers = sorted(numbers)
# # # # # # # print(numbers)
# # # # # # # print(sorted_numbers)
# # # # # #
# # # # # # words = ['hello', 'Python', 'Age', 'apple']
# # # # # # # words.reverse()
# # # # # # # words2 = words[::-1]
# # # # # # words2 = list(reversed(words))
# # # # # # print(words)
# # # # # # print(words2)
# # # # # # # words.sort(key=len)
# # # # # # # print(words)
# # # # # from copy import copy, deepcopy
# # # # # numbers = [1, 2, 3, 4, [5, 6, 7]]
# # # # # numbers2 = deepcopy(numbers)
# # # # # numbers2[4].append(8)
# # # # # print(numbers)
# # # #
# # # # # numbers = (5, 6, 7, [8, 9, 0], 1, 2, 3)
# # # # # numbers[3].append(10)
# # # # # print(numbers)
# # # #
# # # # numbers = 3, 4, 5
# # # # print(numbers)
# # #
# # # user = {
# # #     'name': 'Alex',
# # #     'age': 34,
# # #     'is_human': True,
# # #     'languages': ['ru', 'en'],
# # # }
# # # # user['age'] = 35
# # # user['city'] = 'Minsk'
# # # print(user)
# #
# # # user = dict([('name', 'alex'), ('age', 34), ('city', 'Minsk')])
# # # print(user)
# #
# # # letters = {i: i*2 for i in 'qwerty'}
# # # print(letters)
# #
# # user = dict.fromkeys(('name', 'age', 'city'))
# # print(user)
# # user = {
# #     'name': 'Alex',
# #     'age': 34,
# #     'is_human': True,
# #     'languages': ['ru', 'en'],
# #     'city': 'SPB'
# # }
# # Python 3.10+
# # new_user = user | {'city': 'Minsk', 'surname': 'Petrov'}
# # print(user)
# # print(new_user)
# # user.update(
# #     {
# #         'city': 'Minsk',
# #         'surname': 'Petrov'
# #     }
# # )
# # print(user)
# # print(user.popitem())
# # print(user)
# # print(user.pop('city', 'Minsk'))
# # print(user)
# # print(user.setdefault('city', 'Minsk'))
# # print(user['city'])
#
# # text = 'hello'
# # letter_count = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
#
# N = 5
# numbers = [2, 4, 8, 16, 32]

N = 3

users = {
    0: {'name': 'Alex', 'email': 'alex@info.com'},
    1: {'name': 'Pavel', 'email': 'pavel@info.com'},
    2: {'name': 'Maria', 'email': 'maria@info.com'},
}
