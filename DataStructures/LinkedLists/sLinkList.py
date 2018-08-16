class NodeHead(object):
    def __init__(self, node):
        self.node = None

    def setNode(self, node):
        self.node = node

    def getNode(self):
        return self.node


class Node(object):
    def __init__(self, n):
        self.value = n
        self.nextNode = None


c = Node('c')
d = Node('d')
e = Node('e')
head = NodeHead(c)


def insFirst(node):
    node.nextNode = head.node
    head.node = node


def getCount():
    temp = head.node
    ele_count = 0
    while temp.nextNode:
        ele_count += 1
        temp = temp.nextNode
    return ele_count


def getNode(pos):
    temp = head.node
    eleCount = 1
    while eleCount <= pos:
        temp = temp.nextNode
        eleCount += 1
    return temp


def insert(node, pos):
    count = 0
    temp = head.node
    listLen = getCount()
    if pos == 1:
        node.nextNode = pos
        head.node = node
    else:
        temp = getNode(pos)
        node.nextNode = temp.nextNode
        temp.nextNode = node


def deleteNode(pos):
    temp = head.node
    listLen = getCount()
    temp = head.node
    if pos == 1:
        head.node = temp.nextNode
        del temp
    else:
        count = 0
        while count < pos:
            temp = temp.nextNode
        temp.nextNode = temp.nextNode.nextNode
