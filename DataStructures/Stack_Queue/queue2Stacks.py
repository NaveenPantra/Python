class Queue2Stacks(object):
    def __init__(self):
        print(f"Queue using 2 Stacks")
        self.inStack = []
        self.outStack = []

    def enqueue(self, ele):
        self.inStack.append(ele)

    def dequeue(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        try:
            return self.outStack.pop()
        except IndexError:
            return f"Queue Empty"

    def peek(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        try:
            return self.outStack[len(self.outStack) - 1]
        except IndexError:
            return "Queue Empty"

    def isEmpty(self):
        return self.inStack == [] or self.outStack == []

    def size(self):
        return len(self.inStack) + len(self.outStack)


q2s = Queue2Stacks()

q2s.enqueue(1)
print(f"{q2s.peek()}")
q2s.enqueue(2)
print(f"{q2s.dequeue()}")
print(f"{q2s.size()}")
print(f"{q2s.isEmpty()}")
print(f"{q2s.dequeue()}")
print(f"{q2s.dequeue()}")
