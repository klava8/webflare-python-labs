"""Проверки модуля приветствия."""
import unittest
from message import greeting


class GreetingTests(unittest.TestCase):
    """Обычный ввод, пробелы и отсутствие имени."""

    def test_name(self):
        self.assertEqual(greeting("Anna"), "Hello, Anna!")

    def test_spaces(self):
        self.assertEqual(greeting(" Bob "), "Hello, Bob!")

    def test_empty(self):
        with self.assertRaises(ValueError):
            greeting("   ")


if __name__ == "__main__":
    unittest.main()
