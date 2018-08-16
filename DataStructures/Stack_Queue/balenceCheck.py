
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
            return float('inf')

    def peek(self):
        try:
            return self.stack[len(self.stack) - 1]
        except IndexError:
            return float('inf')

    def isEmpty(self):
        return bool(len(self.stack))


s = Stack()
eq = input("Enter String: ")
for sym in eq:
    print(f"{sym} , {s.peek()}")
    if sym in '({[':
        s.push(sym)

    if sym in "]})":
        if s.pop() != sym:
            print(f"False")
            exit(0)
    # if sym == ")":
    #     if s.peek() == '(':
    #         s.pop()
    #     else:
    #         print(f"False")
    #         exit(0)
    # if sym == "]":
    #     if s.peek() == "[":
    #         s.pop()
    #     else:
    #         print(f"False")
    #         exit(0)
    # if sym == "}":
    #     if s.peek() == "{":
    #         s.pop()
    #     else:
    #         print(f"False")
    #         exit(0)
#
# if not s.isEmpty():
#     print(f"True")
# else:
#     print(f"..False")
