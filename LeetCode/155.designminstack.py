# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

#     push(x) -- Push element x onto stack.
#     pop() -- Removes the element on top of the stack.
#     top() -- Get the top element.
#     getMin() -- Retrieve the minimum element in the stack.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

 

# Constraints:

#     Methods pop, top and getMin operations will always be called on non-empty stacks.

class MinStack:
    # s = []
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x: int) -> None:
        self.s.append(x)
        return
        
    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[len(self.s) - 1]

    def getMin(self) -> int:
        low = self.s[0]
        for i in range(len(self.s)):
            if low > self.s[i]:
                low = self.s[i]
        return low


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()