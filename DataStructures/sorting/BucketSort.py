

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
        maxi = max(self.arr)
            
        
