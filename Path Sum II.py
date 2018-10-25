from binary_tree import TreeNode, Tree

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def path(root, tmp, res, leftSum):
            if not root:return
            if root.val == leftSum and not (root.right) and not(root.left):
                res.append(tmp + [root.val])
                return
            path(root.left, tmp+[root.val], res, leftSum-root.val)
            path(root.right, tmp+[root.val], res, leftSum-root.val)
            return
        res = []
        path(root, [], res, sum)
        return res
