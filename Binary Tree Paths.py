# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from binary_tree import Tree
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        l = list()
        if not (root.left or root.right):
            return str(root.val)
        if root.left:
            l.extend([str(root.val) + '->' + i for i in self.binaryTreePaths(root.left)])
        if root.right:
            l.extend([str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)])
        return l

print(Solution().binaryTreePaths(Tree([1,2,3,4,5]).root))
