
class Stack:
    def __init__(self):
        self.stack = []
        
    def __len__(self):
        return len(self.stack)
    
    def push(self,val):
        self.stack.append(val)
        
    def pop(self):
        return self.stack.pop()
        
    def top(self):
        return self.stack[-1]
    
    def __iter__(self):
        return iter(self.stack[::-1])
    