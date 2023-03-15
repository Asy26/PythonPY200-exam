import hashlib


class IdCounter:
    def __init__(self, value=0):
        """
    :Назначение метода: принимаем value
        """
        self.value = value

    def incr(self):
        """
        :Назначение метода: результат увеличения счетчика id на 1
        :return: текущее значение счетчика
        """
        self.value += 1
        return f"Текущее значение счетчика = {self.value}"  # результат увеличения счетчика id на 1

    def current_id(self):
        """
        :Назначение метода: хранение значения
        :return: текущее значение
        """
        a = self.incr()
        return a


# b = IdCounter()
# print(b.current_id())


class Password:
    def __init__(self, password: str, _name: str):
        """
        :param password: пароль пользователя
        :param _name: имя пользователя
        """
        self.password = password
        self._name = _name

    def get_pass(self):     # получение пароля
        """
        :Назначение метода: получение хэш-значения пароля
        :return: хэш-значение пароля
        """
        return hashlib.sha256(self.password.encode()).hexdigest()

    def is_valid(self):
        """
        :Назначение метода: проверка правильности пароля
        :return: пароль в строковом представлении
        """
        g = self.password
        if len(g) == 8:
            return str(self.password)

    def check(self):
        """
        :Назначение метода: проверка хэш-значения
        :return: пароль
        """
        d = self.get_pass()
        if d == hashlib.sha256(self.is_valid().encode()).hexdigest():
            return self.password


c = Password('vbnmkj65', 'Анна')
print(c.check())


class Product:
    def __init__(self, _name: str, price: float, rating: int, _id=0):
        """
        :param _name: получение name
        :param price: получение price
        :param rating: получение rating
        :param _id: получение id
        """
        self._id = id
        self._name = _name
        self.price = price
        self.rating = rating

    def check_type(self):
        """
        :Назначение метода: проверка валидности
        :return: сообщение об ошибке
        """
        if self.price < 0:
            raise ValueError
        if self.rating < 0:
            raise ValueError
        if isinstance(self._name, str):
            raise TypeError
        if str(self.rating).isdigit():
            raise TypeError
        if isinstance(self.price, float):
            raise TypeError

    def current_id(self):
        """
        :Назначение метода: текущий id
        :return: id + 1
        """
        self._id += 1
        return self._id

    def __repr__(self):
        """
        :Назначение метода: возвращает строки атрибутов
        :return: возвращает id, name, price, rating
        """
        return f"Значение id = {self._id}, name = {self._name}, price = {self.price}, rating = {self.rating}"

    def __str__(self):
        """
        :Назначение метода: возвращает строки атрибутов
        :return: возвращает id, name
        """
        return f"{self._id}:{self._name}"


c = Product('Егор', 123.43, 1452)
print(c)


class Cart:
    def __init__(self, product, cart=[]):
        """
        :param product: товар
        :param cart: пустая корзина
        """
        self.product = product
        self.cart = cart

    def add_product(self):
        """
        :Назначение метода: добавление товара в корзину
        :return: обновленный список
        """
        self.cart.append(self.product)
        return self.cart

    def del_product(self):
        """
        :Назначение метода: удаление товара из корзины
        :return: обновленный список
        """
        self.cart.remove(self.product)
        return self.cart


g = Cart('Кофе')
print(g.add_product())


class User:
    def __init__(self, _username: str, password: str, id=0, __cart=[]):
        """
        :param username: имя пользователя
        :param password: пароль пользователя
        :param id: id пользователя
        :param cart: пустая корзина
        """
        self._username = _username
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.id = id
        self.__cart = __cart

    def __str__(self):
        """
        :Назначение метода: возвращение строкового значения
        :return: строки username, password, cart, id
        """
        return f'{self._username}, password1, {self.id}, {self.__cart}'

    def __repr__(self):
        """
        :Назначение метода: возвращение строкового значения
        :return: строки username, password, cart, id
        """
        return f'{self._username}, password1, {self.id}, {self.__cart}'


person = User('Анастасия', 'As2120496')
print(person.__str__())
# Изменения
