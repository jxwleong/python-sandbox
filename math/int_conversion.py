import unittest

def hex2decimal(hex_: int):
    return int(str(hex_), base=10)



class Test_hex2decimal(unittest.TestCase):
    def test_hex2decimal_expect_correct_value(self):
        self.assertEqual(10, hex2decimal(0xa))
        self.assertEqual(255, hex2decimal(0xff))



if __name__ == '__main__':
    unittest.main()

