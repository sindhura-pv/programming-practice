from collections import deque


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lis = deque()

    def push(self, x: int) -> None:
        if not self.lis:
            self.lis.append((x, x))
        else:
            self.lis.append((x, min(x, self.lis[-1][1])))

    def pop(self) -> None:
        self.lis.pop()

    def top(self) -> int:
        return self.lis[-1][0]

    def getMin(self) -> int:
        return self.lis[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()