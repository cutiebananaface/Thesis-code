import unittest

class DemoTest(unittest.TestCase):

    D1 = {'a': 1, 'b': 2, 'c': [1, 2], 'd': {'cat':2, 'dog':3}}
    D2 = {'a': 1, 'b': 6, 'c': [1], 'd': {'cat':4, 'dog':7}}

    def test_not_so_useful(self):
        assert self.D1 == self.D2

    def test_useful(self):
        self.assertEqual(self.D1, self.D2)


if __name__ == "__main__":
    unittest.main()