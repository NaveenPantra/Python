class Node(object):
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None


class BTree(object):
    def __init__(self, value):
        self.root = Node(value)

    def insertLeft(self, value):
        node = Node(value)
        if self.root.leftNode is None:
            self.root.leftNode = node
        else:
            node.leftNode = self.root.leftNode
            self.root.leftNode = node

    def insertRight(self, value):
        node = Node(value)
        if self.root.rightNode is None:
            self.root.rightNode = node
        else:
            node.rightNode = self.root.rightNode
            self.root.rightNode = node

    def setRootValue(self, value):
        self.root.value = value

    def treeInorder(self, node):
        if node is not None:
            self.treeInorder(node.leftNode)
            print(node.value)
            self.treeInorder(node.rightNode)

    def treePostOrder(self, node):
        if node is not None:
            self.treePostOrder(node)
            self.treePostOrder(node)
            print(node.value)

    def treePreorder(self, node):
        if node is not None:
            print(node.value)
            self.treePreorder(node)
            self.treePreorder(node)

    getRootValue = lambda self: self.root.value

    getLeftChild = lambda self: self.root.leftNode

    getRightChild = lambda self: self.root.rightNode

    getTree = lambda self: self.root


tree = BTree(60)
tree.insertRight(90)
tree.insertRight(100)
tree.insertLeft(30)
tree.insertLeft(40)
root = tree.getTree()
# print(f"{tree.getRootValue()}")
# print(f"{root.value}, {root.leftNode.value}, {root.rightNode.value}")
# print(f"{root.value}, {root.leftNode.leftNode.value}, {root.rightNode.rightNode.value}")
tree.treeInorder(tree.root)
