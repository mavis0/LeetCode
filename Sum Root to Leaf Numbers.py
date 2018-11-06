from binary_tree import Tree, TreeNode

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        def sumTree(root, s):
            nonlocal res
            if not root:return
            if (not root.left) and (not root.right):
                res += int(s + str(root.val))
            else:
                if root.left:sumTree(root.left, s + str(root.val))
                if root.right:sumTree(root.right, s + str(root.val))
        sumTree(root, '')
        return res

print(Solution().sumNumbers(Tree([]).root))
