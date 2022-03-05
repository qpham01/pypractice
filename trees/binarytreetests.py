import unittest
import inspect

from binarytree import BinaryNode, leftInsert, rightInsert, preOrder

class TestClass04(unittest.TestCase):

    def test_case01(self):
        """ Test Constructor """
        node = BinaryNode(5)
        self.assertEqual(5, node.data)
        self.assertEqual(None, node.left)
        self.assertEqual(None, node.right)

    def test_case02(self):
        """ Test left insert """
        node = BinaryNode(1)
        leftInsert(node, 1, 2)
        leftInsert(node, 2, 3)
        self.assertEqual(2, node.left.data)
        self.assertEqual(None, node.right)
        self.assertEqual(3, node.left.left.data)
        self.assertEqual(None, node.left.right)

    def test_case03(self):
        """ Test right insert """
        node = BinaryNode(1)
        rightInsert(node, 1, 2)
        rightInsert(node, 2, 3)
        self.assertEqual(2, node.right.data)
        self.assertEqual(None, node.left)
        self.assertEqual(3, node.right.right.data)
        self.assertEqual(None, node.right.left)

    def test_case04(self):
        """ Test preorder """
        node = BinaryNode(1)
        rightInsert(node, 1, 2)
        rightInsert(node, 2, 5)
        leftInsert(node, 5, 3)
        rightInsert(node, 5, 6)
        rightInsert(node, 3, 4)
        results = preOrder(node)
        self.assertEqual(6, len(results))
        self.assertListEqual([1, 2, 5, 3, 4, 6], results)

if __name__ == '__main__':
    unittest.main(verbosity=2)