import unittest
from unittest.mock import patch

from foo import main


class Test_add(unittest.TestCase):
    @patch('foo.add', return_value='Mocked!')
    def test_foo(self, mock_add):
        self.assertEqual('Mocked!' , main())

if __name__ == '__main__':
    unittest.main()