import unittest
from lesson_19.homework.task1.task1 import make_operation


class Text_make_operation(unittest.TestCase):
    def test_make_operation(self):
        self.assertEqual(make_operation('+', 7, 7, 2), 16)
        self.assertEqual(make_operation('-', 5, 5, -10, -20), 30)
        self.assertEqual(make_operation('*', 7, 6, 1), 42)


if __name__ == '__main__':
    unittest.main()
