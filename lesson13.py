# # TODO Написать функцию, имитирующая действия DictReader из модуля CSV
# #  На вход функции так же поступает Pydantic схема, необходимо чтобы
# #  функция возвращала не список словарей, а список схем Pydantic
# from typing import Union
#
# from models import CategorySchema
#
#
# def dict_reader(file, schema, delimiter=',') -> list[dict]:
#     keys = file.readline().strip().split(delimiter)
#     for line in file:
#         if line.strip():
#             values = line.strip().split(delimiter)
#             yield schema(**dict(zip(keys, values)))
#
#
# with open('dump_category.csv', 'r', encoding='utf-8') as file:
#     for line in dict_reader(file, CategorySchema):
#         print(line)
#
from pprint import pprint


# class Mapper(object):
#     __model__ = None
#     __schema__ = None

# def __init__(self, model=None, schema=None, **kwargs):
#
#     if model and not isinstance(model, self.__model__):
#         raise TypeError
#
#     if schema and not isinstance(schema, self.__schema__):
#         raise TypeError
#
#     if model:
#         self._model = model
#         self._schema = self.__schema__(**model.dict())
#     elif schema:
#         self._model = self.__model__(**schema.dict())
#         self._schema = schema
#     elif kwargs:
#         self._model = self.__model__(**kwargs)
#         self._schema = self.__schema__(**kwargs)
#     else:
#         raise ValueError
#
# @property
# def model(self):
#     return self._model
#
# @property
# def schema(self):
#     return self._schema
#
# def dict(self):
#     return self.schema.dict()

#
# text = 'Hello World'
#
#
# def vowels_to_upper(text: str) -> str:
#     return ''.join(i.upper() if i in 'euioa' else i for i in text)
#
#
# print(vowels_to_upper(text))


def chess_board(rows: int, columns: int) -> list[list[str]]:
    board = []
    for row in range(rows):
        line = []
        for column in range(columns):
            if row % 2:
                if column % 2:
                    line.append('O')
                else:
                    line.append('X')
            else:
                if column % 2:
                    line.append('X')
                else:
                    line.append('O')
        board.append(line)
    return board


def sum_unique(numbers: list[int]) -> int:
    res = 0
    for number in numbers:
        if numbers.count(number) == 1:
            res += number
    return res


def create_dict(keys, values):
    data = {}
    for i in range(len(keys)):
        data[keys[i]] = values[i] if i in range(len(values)) else None
    return data


def sort_dict(data: dict) -> list[tuple[int, int]]:
    return [*sorted(data.items(), key=lambda x: x[1], reverse=True)]
