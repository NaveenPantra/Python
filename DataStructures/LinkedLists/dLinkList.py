class Head(object):
    def __init__(self):
        self.node = None


class Node(object):
    def __init__(self, value):
        self.prevNode = None
        self.value = value
        self.nextNode = None


class DLinkList(object):
    head = Head()

    def __init__(self):
        print(f"Double Linked List implementation...")

    def getCount(self):
        temp = self.head.node
        if temp:
            return 0
        else:
            count = 0
            while temp.nextNode:
                temp = temp.nextNode
                count += 1
            return count

    def insert(self, node, pos):
        temp = self.head.node
        if pos == 1:
            node.nextNode = self.head.node
            self.head = node
        elif 1 < pos <= self.getCount():
            count = 0
            while count < pos:
                temp = temp.nextNode
                count += 1
            node.nextNode = temp.nextNode
            temp.nextNode = node
        else:
            print(f"Cannot Insert")

    def delete(self, pos):
        temp = self.head.node
        if pos == 1:
            head = temp.nextNode
            del temp
        elif 1 < pos <= self.getCount():
            count = 0
            while count < pos:
                temp = temp.nextNode
                count += 1
            temp.nextNode = temp.nextNode.nextNode
        else:
            print(f"Cannot delete")
