class MinStack:

    def __init__(self):
        self.st = []

    def push(self, value: int) -> None:
        if len(self.st) == 0:
            self.st.append([value, value])
        else:
            mini = min(value, self.st[-1][-1])
            self.st.append([value, mini])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        if self.st is not None:
            return self.st[-1][0]
        else:
            None        

    def getMin(self) -> int:
        if self.st is not None:
            return self.st[-1][1]
        else:
            None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()