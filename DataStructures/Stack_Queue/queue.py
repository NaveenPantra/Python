class Queue(object):
    def __init__(self):
        print(f"Queue is Initialized")
        self.queue = []

    def enqueue(self, ele):
        self.queue.insert(0, ele)

    def dequeue(self):
        try:
            return self.queue.pop()
        except IndexError:
            return f"Queue Empty"

    def isEmpty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

    def __len__(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
print(f"{q.dequeue()}")
print(f"{q.dequeue()}")
print(f"{q.dequeue()}")
print(f"{q.isEmpty()}")
print(f"{q.size()}")

