import unittest

import ast_test


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0
test_str_1 = "'Hello, World!'"
class AstTest(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(ast_test.is_valid("hello_world.py"), True)
    def test_goodbye_world(self):
        self.assertEqual(ast_test.is_valid("goodbye_world.py"), False)
    def test_thing_here(self):
        self.assertEqual(ast_test.is_valid(test_str_1, file=False), False)
if __name__ == '__main__':
    unittest.main()
