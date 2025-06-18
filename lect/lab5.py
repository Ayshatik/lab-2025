class MinValueDescriptor:
    def __init__(self, min_value):
        self.min_value = min_value
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, self.min_value)

    def __set__(self, instance, value):
        if value < self.min_value:
            raise ValueError(f"Значение должно быть не меньше {self.min_value}")
        instance.__dict__[self.name] = value

class Product:
    price = MinValueDescriptor(0)
    quantity = MinValueDescriptor(1)

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
