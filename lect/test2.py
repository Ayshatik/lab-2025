import unittest

from lab2 import House
import pytest

class House:
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __str__(self):
        return f'{self.street}, {self.number}'

    def __repr__(self):
        return f'street={self.street}, number={self.number}'

def test_house_str():
    house = House('Вешняковская', 2)
    assert str(house) == 'Вешняковская, 2', "The __str__ method is not working as expected for valid input"

def test_house_str_non_ascii():
    house = House('Рязанский проспект', 7)
    assert str(house) == 'Рязанский проспект, 7', "The __str__ method failed for street names with non-ASCII characters"

def test_house_repr():
    house = House('Рязанский проспект', 7)
    assert repr(house) == 'street=Рязанский проспект, number=7', "The __repr__ method is not working as expected for valid input"

def test_house_init_empty_strings():
    house = House('', '')
    assert str(house) == ', ', "The __str__ method failed for empty street and number"
    assert repr(house) == 'street=, number=', "The __repr__ method failed for empty street and number"

def test_house_init_zero_number():
    house = House('Main Street', 0)
    assert str(house) == 'Main Street, 0', "The __str__ method failed for number set to 0"
    assert repr(house) == 'street=Main Street, number=0', "The __repr__ method failed for number set to 0"

def test_house_init_special_characters():
    house = House('Special!@#$', '%^&*')
    assert str(house) == 'Special!@#$, %^&*', "The __str__ method failed for street and number with special characters"
    assert repr(house) == 'street=Special!@#$, number=%^&*', "The __repr__ method failed for street and number with special characters"

if __name__ == "__main__":
    unittest.main()