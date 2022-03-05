from cmath import exp
import unittest

from texteditor import text_editor

class TextEditorTests(unittest.TestCase):

    def test_case01(self):
        """ Test commands 1 """
        string = "abcde"
        commands = ["1 fg","3 6","2 5","4","3 7","4","3 4"]
        expected = ["f", "g", "d"]
        results = text_editor(string, commands)
        self.assertListEqual(expected, results)

    def test_case02(self):
        """ Test commands 2 """
        string = ""
        commands = ["1 abc","3 3","2 3","1 xy","3 2","4","4","3 1"]
        expected = ["c", "y", "a"]
        results = text_editor(string, commands)
        self.assertListEqual(expected, results)

if __name__ == '__main__':
    unittest.main(verbosity=2)