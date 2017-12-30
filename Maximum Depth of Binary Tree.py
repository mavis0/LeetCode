from binary_tree import Tree
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        l, r = root.left, root.right
        if l and r:return max(self.maxDepth(l), self.maxDepth(r)) + 1
        if (not l) and (not r):return 1
        if l:return self.maxDepth(l) + 1
        if r:return self.maxDepth(r) + 1