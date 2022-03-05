import unittest

from gridchallenge import gridChallenge

class GridChallengeTests(unittest.TestCase):

    def test_case01(self):
        """ Test commands 1 """
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        result = gridChallenge(grid)
        self.assertEqual("YES", result)

    def test_case02(self):
        """ Test commands 2 """
        grid = ['kc', 'iu']
        result = gridChallenge(grid)
        self.assertEqual("YES", result)

    def test_case03(self):
        """ Test commands 3 """
        grid = ["uxf","vof","hmp"]
        result = gridChallenge(grid)
        self.assertEqual("NO", result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
