class DeQueue(object):
    def __init__(self):
        self.dQueue = []

    def addFront(self, ele):
        self.dQueue.insert(0, ele)

    def addRear(self, ele):
        self.dQueue.append(ele)

    def removeFront(self):
        try:
            return self.dQueue.pop(0)
        except IndexError:
            return  f"DeQueue Empty..."

    def removeRear(self):
        try:
            return self.dQueue.pop()
        except IndexError:
            return f"Dequeue Empty..."

    def isEmpty(self):
        return self.dQueue == []

    def size(self):
        return len(self.dQueue)


dq = DeQueue()
dq.addFront(1)
dq.addRear(2)
print(f"Size: {dq.size()}")
print(f"removeFront: {dq.removeFront()}")
print(f"removeRear: {dq.removeRear()}")
print(f"Size: {dq.size()}")