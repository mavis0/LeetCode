from binary_tree import Tree

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # def isSame(p, q):
        #     if p and q:
        #         return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)
        #     return p == q

        def isSym(p, q):
            if p and q:
                return p.val == q.val and isSym(p.left, q.right) and isSym(p.right, q.left)
            return p == q
        return isSym(root.left, root.right) if root else True



s = Solution()
print(s.isSymmetric(Tree([1,2,2,'null',3,'null',3]).root))