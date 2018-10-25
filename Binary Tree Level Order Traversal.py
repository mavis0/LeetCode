# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        last, res = [root], [[root.val]]
        while last:
            tmp = list()
            for node in last:
                if node.left:tmp.append(node.left)
                if node.right:tmp.append(node.right)
            if tmp:res.append([i.val for i in tmp])
            last = tmp
        return res

