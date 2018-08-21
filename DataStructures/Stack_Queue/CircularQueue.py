class CircularQueue(object):

    def __init__(self, size):
        self.SIZE = size
        self.arr = []
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue(self, ele):
        if self.count == self.SIZE:
            print(f"Queue overflow")
        else:
            self.count += 1
            if self.tail == self.SIZE:
                self.tail = 0
                self.arr.insert(self.tail, ele)
            else:
                self.tail += 1
                self.arr.insert(self.tail, ele)
            print(f"{self.arr}")
            print(f"Head: {self.head}, Tail: {self.tail}")

    def dequeue(self):
        if self.count == 0 or self.tail == self.head:
            print(f"Queue underflow")
        else:
            self.count -= 1
            self.arr.pop(self.head)
            if self.head == self.SIZE:
                self.head = 0
            else:
                self.head += 1
            print(f"{self.arr}")
            print(f"Head: {self.head}, Tail: {self.tail}")

    def getQueue(self):
        i = 0
        temp = self.head
        while i <= self.count:
            print(f"Element {i}: {self.arr[temp]}")
            if temp == self.SIZE:
                temp = 0
            else:
                temp += 1
            i += 1


c_queue = CircularQueue(5)
c_queue.enqueue(1)
c_queue.enqueue(2)
c_queue.enqueue(3)
c_queue.enqueue(4)
c_queue.enqueue(5)
c_queue.dequeue()
c_queue.enqueue(1)
c_queue.enqueue(2)
c_queue.enqueue(3)
c_queue.enqueue(4)
c_queue.dequeue()
c_queue.dequeue()
c_queue.enqueue(5)
# c_queue.getQueue()
