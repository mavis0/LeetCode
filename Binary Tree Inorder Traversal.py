from binary_tree import Tree, TreeNode
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, l, p = [], [], root
        while l or p:
            while p:
                l.append(p)
                p = p.left
            tmp = l.pop()
            res.append(tmp.val)
            p = tmp.right
        return res
print(Solution().inorderTraversal(Tree([1, 'null', 2, 3]).root))


