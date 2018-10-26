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
        if not root: return
        if root.left and root.right:
            tmp1, tmp2 = root.left, root.right
            while tmp1 and tmp2:
                tmp1.next = tmp2
                tmp1, tmp2 = tmp1.right, tmp2.left
            self.connect(root.left)
            self.connect(root.right)
