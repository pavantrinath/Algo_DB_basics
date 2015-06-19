class Stack:
    def __init__(self):
        self.mystack = []

    def push(self,val):
        self.mystack.append(val)

    def pop(self):
        return self.mystack.pop()

    def top(self):
        return self.mystack[-1]

    def __iter__(self):
        return iter(self.mystack)