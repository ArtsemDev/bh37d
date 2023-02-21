# class User:
#
#     lang: str = 'ru'
#
#     def __init__(self, name: str) -> None:
#         self.name = name.title()
#
#     def __repr__(self) -> str:
#         return self.name
#
#     def dict(self) -> dict:
#         return {'name': self.name}
#
#     @classmethod
#     def foo(cls):
#         print('foo')
#
#
# vasya = User(name='vasya')
# petya = User(name='petya')


# TODO Написать класс RegisterForm
#  конструктор класса принимает аргументы login и password
#  на основании аргументов определяются атрибуты login и password
#  написать метод объекта is_valid проверяющий атрибуты по критериям:
#  1. Логин состоит только из букв и/или цифр, длина не менее 4 символов
#  2. Длина пароля не менее 8 символов
#  3. Пароль должен содержать минимум 1 большую букву
#  4. Пароль должен содержать минимум 1 цифру
#  Если все критерии соблюдены, метод должен возвращать True,
#  в противном случае False


class RegisterForm:

    def __init__(self, login: str, password: str) -> None:
        self.login = login
        self.password = password

    def is_valid(self) -> bool:
        if len(self.login) < 4 or not self.login.isalnum():
            return False
        if len(self.password) < 8 or not self.password.isalnum():
            return False

        is_upper_letter = False
        is_digit = False
        for el in self.password:
            if el.isupper():
                is_upper_letter = True
            if el.isdigit():
                is_digit = True

        if is_digit and is_upper_letter:
            return True
        else:
            return False


# TODO Написать класс Product
#  констурктор класса принимает атрибуты:
#  1. name: str
#  2. descr: str (не обязательный)
#  3. price: float
#  перед объявление атрибутов класса на основании аргументов констурктора,
#  необходимо проверить аргументы на соответствие типам, а так же
#  1. Название должно быть не короче 4 символов
#  2. Цена строго положительная
#  Написать метод объекта discount, принимающий скидку и возвращающий стоимость товара со скидкой
#  Скидка должна быть int | float и не отрицательная, а так же не более 25 (проверить скидку)
#  Написать метод объекта edit_descr принимающий новое описание товара и
#  заменяющий старое описание на новое
#  Написать магический метод __str__ возвращащий строку в формате
#  <b>НАЗВАНИЕ ТОВАРА</b></br></br><i>ОПИСАНИЕ ТОВАРА></i></br></br><b>ЦЕНА</b>


class Product:

    def __init__(self, name: str, price: float, descr: str = None) -> None:
        if not isinstance(name, str):
            raise TypeError
        elif len(name) < 4:
            raise ValueError

        if not isinstance(price, (int, float)):
            raise TypeError
        elif price <= 0:
            raise ValueError

        if descr is not None and not isinstance(descr, str):
            raise TypeError

        self.name = name
        self.price = price
        self.descr = descr

    def discount(self, percent: int | float) -> float:
        if not isinstance(percent, (int, float)):
            raise TypeError
        elif percent < 0 or percent > 25:
            raise ValueError
        return self.price * ((100 - percent) / 100)

    def edit_descr(self, descr: str) -> None:
        if not isinstance(descr, str):
            raise TypeError
        self.descr = descr

    def __str__(self) -> str:
        return f'<b>{self.name.upper()}</b>' \
               f'</br></br>' \
               f'<i>{self.descr}</i>' \
               f'</br></br>' \
               f'<b>{self.price} BYN</b>'


# TODO Написать класс Paginator
#  1. Объявить атрибут класса objs: list[str] (и сразу заполнить)
#  2. Объявить атрибут класса paginate_by: int (по умолчанию 3)
#  3. Написать метод класса get_page принимающий аргумент page: int и возвращающий список объектов
#  из атрибута класса objs для данной страницы


class Paginator:
    objs: list[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    paginate_by: int = 3

    @classmethod
    def get_page(cls, page: int) -> list[str]:
        return cls.objs[
               (page-1) * cls.paginate_by:(page - 1) * cls.paginate_by + cls.paginate_by
               ]


print(Paginator.get_page(2))
