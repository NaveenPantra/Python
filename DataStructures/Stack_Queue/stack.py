class Stack(object):
    def __init__(self):
        print(f"Stack Operation initialized")
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            return f"Stack UnderFlow..."

    def peek(self):
        try:
            return self.stack[len(self.stack) - 1]
        except IndexError:
            return f"Empty Stack..."

    def isEmpty(self):
        return bool(len(self.stack))

    def size(self):
        return len(self.stack)


s = Stack()
s.push(10)
s.push(123)
print(s.pop())
print(s.pop())
print(s.pop())
print(f"{s.size()}")
print(f"{s.peek()}")
print(f"{s.size()}")
