class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l1 = list()
        self.l2 = list()
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if not self.l1:
            self.l1.append(x)
            self.l1.extend(self.l2)
            self.l2 = list()
        else:
            self.l2.append(x)
            self.l2.extend(self.l1)
            self.l1 = list()

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.l1:return self.l1.pop()
        if self.l2:return self.l2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.l1:return self.l1[-1]
        if self.l2:return self.l2[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        print(self.l1, self.l2)
        return not (self.l1 or self.l2)
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
# print(obj.pop())
print(obj.peek())
print(obj.empty())