import unittest

from queue2stack import processQueue

class TextEditorTests(unittest.TestCase):

    def test_case01(self):
        """ Test commands 1 """
        string = "abcde"
        commands = ["1 42","2","1 14","3","1 28","3","1 60","1 78","2","2"]
        expected = [14, 14]
        results = processQueue(commands)
        self.assertListEqual(expected, results)

    def test_case02(self):
        """ Test commands 2 """
        string = "abcde"
        commands = ["1 76","1 33","2","1 23","1 97","1 21","3","3","1 74","3"]
        expected = [33, 33, 33]
        results = processQueue(commands)
        self.assertListEqual(expected, results)

if __name__ == '__main__':
    unittest.main(verbosity=2)