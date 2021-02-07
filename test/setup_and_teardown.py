import unittest

def add(x, y):
    return x+y


class TestCaseAdd(unittest.TestCase):
    def setUp(self):
        self.val1 = 1
        self.val2 = 2

    def test_add1(self):
        self.assertEqual(3, add(self.val1, self.val2))

    def test_add2(self):
        self.val2 = 3
        self.assertEqual(4, add(self.val1, self.val2))

    def test_add3(self):
        self.val2 = 3
        self.assertEqual(4, add(self.val1, self.val2))

    #def tearDown(self):


if __name__ == '__main__':
    unittest.main()   