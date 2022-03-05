class BinaryNode:
    def __init__(self, data):
        self.data=data
        self.left = None
        self.right = None

def preOrder(root):
    results = []
    traverse(root, results)
    return results
    
def traverse(node, results):
    if node is None:
        return
    results.append(node.data)
    traverse(node.left, results)
    traverse(node.right, results)

def traverseFind(node, target):
    if node is None:
        return None

    if node.data == target:
        return node

    result = traverseFind(node.left, target)
    if result is not None:
        return result
    result = traverseFind(node.right, target)
    return result
    
def find(node, value):
    return None if node is None else traverseFind(node, value)

def leftInsert(node, parentData, data):
    parent = find(node, parentData)
    if parent is None:
        return None
    parent.left = BinaryNode(data)
    return parent.left

def rightInsert(node, parentData, data):
    parent = find(node, parentData)
    if parent is None:
        return None
    parent.right = BinaryNode(data)
    return parent.right