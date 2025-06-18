"""использование метода __str__"""
class House:
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __str__(self):
        return f'{self.street}, {self.number}'

house1 = House('Вешняковская', 2)
print(house1)

"""использование метода __repr__"""
class House:
    def __init__(self, street, number):
        self.street = street
        self.number = number
    def __repr__(self):
        return f'street={self.street}, number={self.number}'

house2 = House('Рязанский проспект', 7)
print(repr(house2))



