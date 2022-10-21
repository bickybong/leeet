class MyQueue(object):

    def __init__(self):
        self.first = []
        self.last = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.last.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.frontToBack()
        return self.first.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.frontToBack()
        return self.first[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.first) + len(self.last) == 0
    
    def frontToBack(self):
        if not self.first:
            while self.last:
#                 add all elements from last to first to form FIFO if first is empty
                self.first.append(self.last.pop())
        

sol = MyQueue()
sol.push("2")
sol.push("3")

print(sol.peek())
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

