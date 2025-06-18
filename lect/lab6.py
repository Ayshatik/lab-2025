import unittest
import math

# Функция для вычисления факториала
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Динамическое создание тестов
def create_factorial_test_case(n):
    def test_case(self):
        self.assertEqual(factorial(n), math.factorial(n))
    return test_case

class DynamicTestGeneration(unittest.TestCase):
    pass

# Генерация тестов для чисел от 0 до 9
for n in range(10):
    test_name = f"test_factorial_{n}"
    test_case = create_factorial_test_case(n)
    setattr(DynamicTestGeneration, test_name, test_case)

if __name__ == '__main__':
    unittest.main()

