import unittest
from arithmetic_expression import find_maximum_value


class ArithmeticExpression(unittest.TestCase):
    def test(self):
        for s, answer in (
            ("5", 5),
            ("2+3", 5),
            ("2-3", -1),
            ("5-8+7*4-8+9", 200),
            ("8-5*3", 9),
            ("8-5*3-5", 18)
        ):
            self.assertEqual(find_maximum_value(s), answer)


if __name__ == '__main__':
    unittest.main()
