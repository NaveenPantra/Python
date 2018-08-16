class TreeList(object):

    def __init__(self, value):
        self.root = [value, [], []]

    def insertLeft(self, value):
        leftNode = self.root.pop(1)
        if len(leftNode) > 1:
            self.root.insert(1, [value, leftNode, []])
        else:
            self.root.insert(1, [value, [], []])

    def insertRight(self, value):
        rightNode = self.root.pop()
        if len(rightNode) > 1:
            self.root.insert(2, [value, [], rightNode])
        else:
            self.root.insert(2, [value, [], []])

    def setRootValue(self, value):
        self.root[0] = value

    getRootValue = lambda self: self.root[0]

    getLeftChild = lambda self: self.root[1]

    getRightChild = lambda self: self.root[2]

    getTree = lambda  self: self.root


tree = TreeList(5)
print("{}{}".format("This is Root: ", tree.getRootValue()))
tree.insertLeft(2)
tree.insertRight(5)
print("{}".format(tree.getTree()))
print(f"{tree.getLeftChild()}")
tree.setRootValue(10)
print(f"{tree.getTree()}")