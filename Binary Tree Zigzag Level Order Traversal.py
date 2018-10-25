# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        last, res, flag = [root], [[root.val]], True
        while last:
            tmp = list()
            for node in last:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            res.append([i.val for i in tmp] if flag else [i.val for i in tmp[::-1]])
            last, flag = tmp, not flag
        return res


