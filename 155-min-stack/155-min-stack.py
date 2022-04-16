class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
      
    def getMin(self) -> int:
        min = float(inf)
        i = 0
        while i < len(self.stack):
          if min > self.stack[i]:
            min = self.stack[i]
          i += 1
        return min
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()