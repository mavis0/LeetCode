class MinStack(object):
    # 备份一个最小栈，用来返回最小的值。
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.minstack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:self.minstack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if x == self.minstack[-1]:self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.getMin())

