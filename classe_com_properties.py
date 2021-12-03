MIN_VALUE = 0
MAX_VALUE = 10


class OrderItem:
    """
    Classe que faz uso de properties para validar entradas
    Exemplos:
    >>> OrderItem('beans', '4', 10.0)
    Traceback (most recent call last):
    ...
    TypeError: O valor de 'weight' deve ser um int ou um float.
    >>> beans = OrderItem('beans', 4, 10)
    >>> beans #doctest: +ELLIPSIS
    <__main__.OrderItem object at ...>
    >>> beans.weight = -1
    Traceback (most recent call last):
    ...
    ValueError: O valor de 'weight' não deve ser menor que 0.
    >>> OrderItem('beans', 6, 10.01)
    Traceback (most recent call last):
    ...
    ValueError: O valor de 'price' não deve ser maior que 10.
    """
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"O valor de 'weight' deve ser um int ou um float."
            )
        if value < MIN_VALUE:
            raise ValueError(
                f"O valor de 'weight' não deve ser menor que {MIN_VALUE}."
            )
        self.__weight = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"O valor de 'price' deve ser um int ou um float."
            )
        if value > MAX_VALUE:
            raise ValueError(
                f"O valor de 'price' não deve ser maior que {MAX_VALUE}."
            )
        self.__price = value

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    import doctest
    doctest.testmod()
