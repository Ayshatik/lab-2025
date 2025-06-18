import unittest
from lab3 import LazyProperty, ExampleClass

class TestLazyProperty(unittest.TestCase):
    def test_lazy_evaluation(self):
        obj = ExampleClass()
        self.assertFalse(hasattr(obj, "_lazy_expensive_calculation"))  # Значение ещё не вычислено

        value = obj.expensive_calculation  # Первое обращение
        self.assertTrue(hasattr(obj, "_lazy_expensive_calculation"))  # Значение кешировано
        self.assertEqual(value, 42)

        # Повторное обращение не вызывает пересчёт
        self.assertEqual(obj.expensive_calculation, 42)
