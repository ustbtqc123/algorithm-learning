class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack[-1]

    def push(self, val):
        self.stack.append(val)
        return True  # 这里返回True表示入栈成功，可根据需求调整

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
