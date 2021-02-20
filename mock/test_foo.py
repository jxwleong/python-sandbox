import unittest
from unittest.mock import patch

from foo import add


class Test_add(unittest.TestCase):
    @patch('foo.add', return_value='Mocked!')
    def test_foo(self, add):
        self.assertEqual('Mocked!' , add())

if __name__ == '__main__':
    unittest.main()