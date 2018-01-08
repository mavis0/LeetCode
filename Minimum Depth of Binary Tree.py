class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        l, r = self.minDepth(root.left), self.minDepth(root.right)
        if not l:return r + 1
        return l + 1 if not r else min(l, r) + 1
        