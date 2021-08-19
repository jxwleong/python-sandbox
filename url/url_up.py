import urllib.request
import unittest

# https://stackoverflow.com/a/1949360
def is_url_up(url: str):
    return urllib.request.urlopen(url).getcode()

class Test_is_url_up(unittest.TestCase):
    def test_is_url_up_given_valid_url_expect_return_200(self):
        self.assertEqual(200, is_url_up("https://google.com"))

    def test_is_url_up_given_invalid_url_expect_exception(self):
        self.assertRaises(urllib.error.URLError, is_url_up, "https://jajsdkajskldas.com")

if __name__ == '__main__':
    unittest.main()


