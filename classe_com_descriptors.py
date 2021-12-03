from abc import ABC, abstractmethod

MIN_VALUE = 0
MAX_VALUE = 10


class Validator(ABC):
    """
    Descriptor que controla o acesso a atributos da instancia à qual 
    está atrelado
    """
    
    def __set_name__(self, owner, name):
        self.public_attr = name
        self.private_attr = f'_{name}'

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_attr)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_attr, value)

    @abstractmethod
    def validate(self, value):
        raise NotImplementedError('Método não implementado')


class Quantity(Validator):
    """Classe responsável pela implementação da validação de um valor"""

    def __init__(self, *, min_value=MIN_VALUE, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        """
        Valida se o valor inserido está entre o valor mínimo e máximo
        exigidos.
        """
        if not isinstance(value, (int, float)):
            raise TypeError(
                f'O valor de {self.public_attr!r} deve ser um int ou um float.'
            )
        if self.min_value is not None and value < self.min_value:
            raise ValueError(
                f'O valor de {self.public_attr!r} não deve ser menor que '
                f'{self.min_value}.'
            )
        if self.max_value is not None and value > self.max_value:
            raise ValueError(
                f'O valor de {self.public_attr!r} não deve ser maior que '
                f'{self.max_value}.'
            )


class OrderItem:
    """
    Classe que faz uso de descriptors para validar entradas.
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
    weight = Quantity()
    price = Quantity(max_value=MAX_VALUE)

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    import doctest
    doctest.testmod()
