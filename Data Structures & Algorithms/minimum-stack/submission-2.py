class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop(-1)
        if self.minStack:
            self.minStack.pop(-1)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
