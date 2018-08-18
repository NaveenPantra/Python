class Head(object):
    def __init__(self, node = None, value = 0):
        self.node = node
        self.value = 0

class Node(object):
    def __init__(self, nextNode = None, prevNode = None, value = 0):
        self.nextNode = nextNode
        self.prevNode = prevNode
        self.value = value

class BucketSort(object):
    def __init__(self, arr):
        self.arr = arr
    
    def sort(self):
        # Find the maximum element in the entire array
        # By finding the maximum element in the array the find the next immidiate 100, 1000, 10000, 100000, 1000000...
        maxi = max(self.arr)
        
