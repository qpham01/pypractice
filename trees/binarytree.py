class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = BinaryNode(data)

    def preOrder(self):
        results = []
        self.traverse(self.root, results)
        return results
        
    def traverse(self, node, results):
        if node is None:
            return
        results.append(node.data)
        self.traverse(node.left, results)
        self.traverse(node.right, results)

    def traverseFind(self, node, target):
        if node is None:
            return None

        if node.data == target:
            return node

        result = self.traverseFind(node.left, target)
        if result is not None:
            return result
        result = self.traverseFind(node.right, target)
        return result
        
    def find(self, node, value):
        return None if node is None else self.traverseFind(node, value)

    def leftInsert(self, node, parentData, data):
        parent = self.find(node, parentData)
        if parent is None:
            return None
        parent.left = BinaryNode(data)
        return parent.left

    def rightInsert(self, node, parentData, data):
        parent = self.find(node, parentData)
        if parent is None:
            return None
        parent.right = BinaryNode(data)
        return parent.right