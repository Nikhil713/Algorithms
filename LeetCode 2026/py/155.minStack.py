class MinStack:

    def __init__(self):
        self.arr = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.arr.append(value)
        currMin = self.arr[-1]
        if self.minStack:
            currMin = self.minStack[-1]
        self.minStack.append(min(value, currMin))

    def pop(self) -> None:
        self.minStack.pop()
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()