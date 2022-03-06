import unittest

from fastheap import fastheap

class FastHeapTests(unittest.TestCase):

    def test_case01(self):
        """ Test commands 1 """
        commands = ["1 4","1 9","3","2 4","3"]
        result = fastheap(commands)
        expected = [4, 9]
        self.assertListEqual(expected, result)

    def test_case02(self):
        """ Test commands 2 """
        commands = ["1 3","1 65","2 65","3","2 3","1 7","3","1 -1","3","2 -1","3","2 7"]
        result = fastheap(commands)
        expected = [3,7,-1,7]
        self.assertListEqual(expected, result)


if __name__ == '__main__':
    unittest.main(verbosity=2)