# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        #新建一个dummy真的是太巧妙的方法了。
        t = dummy = TreeLinkNode('#')
        while root:
            if root.left:
                t.next = root.left
                t = t.next
            if root.right:
                t.next = root.right
                t = t.next
            root = root.next
            if not root:
                t, root, dummy.next = dummy, dummy.next, None



