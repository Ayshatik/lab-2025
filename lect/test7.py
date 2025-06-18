import unittest
# Импортируем функцию из другого файла
from lab7 import hello
# Объявляем класс с тестом
class HelloTestCase(unittest.TestCase):
    # Функция, которая проверит, как формируется приветствие
    def test_hello(self):
        # Отправляем тестовую строку в функцию
        result = hello("миша")
        # Задаем ожидаемый результат
        self.assertEqual(result, "Привет, Миша.")
# Запускаем тестирование
if __name__ == '__main__':
    unittest.main()
