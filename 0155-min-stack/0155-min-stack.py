class MinStack:

    def __init__(self):
        self.data=[]
        

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> None:
        del self.data[-1]
        

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return min(self.data)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()