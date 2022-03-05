import unittest

from binarytree import BinaryNode, BinaryTree

class BinaryTreeTests(unittest.TestCase):

    def test_case01(self):
        """ Test Constructor """
        tree = BinaryTree(5)
        self.assertEqual(5, tree.root.data)
        self.assertEqual(None, tree.root.left)
        self.assertEqual(None, tree.root.right)

    def test_case02(self):
        """ Test left insert """
        tree = BinaryTree(1)
        tree.leftInsert(tree.root, 1, 2)
        tree.leftInsert(tree.root, 2, 3)
        self.assertEqual(2, tree.root.left.data)
        self.assertEqual(None, tree.root.right)
        self.assertEqual(3, tree.root.left.left.data)
        self.assertEqual(None, tree.root.left.right)

    def test_case03(self):
        """ Test right insert """
        tree = BinaryTree(1)
        tree.rightInsert(tree.root, 1, 2)
        tree.rightInsert(tree.root, 2, 3)
        self.assertEqual(2, tree.root.right.data)
        self.assertEqual(None, tree.root.left)
        self.assertEqual(3, tree.root.right.right.data)
        self.assertEqual(None, tree.root.right.left)

    def test_case04(self):
        """ Test preorder """
        tree = BinaryTree(1)
        tree.rightInsert(tree.root, 1, 2)
        tree.rightInsert(tree.root, 2, 5)
        tree.leftInsert(tree.root, 5, 3)
        tree.rightInsert(tree.root, 5, 6)
        tree.rightInsert(tree.root, 3, 4)
        results = tree.preOrder()
        self.assertEqual(6, len(results))
        self.assertListEqual([1, 2, 5, 3, 4, 6], results)

if __name__ == '__main__':
    unittest.main(verbosity=2)