mport unittest

def remove_space(str_):
    if isinstance(str_, str):
        return str_.replace(' ', '')
    raise TypeError("Invalid string argument str_: " + str(str_))


class Test_remove_space(unittest.TestCase):
    def test_remove_space_given_str_with_spaces_expect_spaces_removed(self):
        self.assertEqual('ab', remove_space(' ab'))
        self.assertEqual('XDQ', remove_space('X D Q'))
        self.assertEqual('#@2313W@#!#!@#SADsa', remove_space('# @ 23 13 W @#!#!@# SAD sa'))

    def test_remove_space_given_str_with_no_spaces_expect_no_effect(self):
        self.assertEqual('ab', remove_space('ab'))
        self.assertEqual('HELLOworld!', remove_space('HELLOworld!'))

    def test_remove_space_given_non_str_expect_TypeError_exception_throw(self):
        self.assertRaises(TypeError, remove_space, 999)
        self.assertRaises(TypeError, remove_space, [1, 2])
        self.assertRaises(TypeError, remove_space, {'key': 123})
        self.assertRaises(TypeError, remove_space, ('Hi', 'There'))


if __name__ == '__main__':
    unittest.main()