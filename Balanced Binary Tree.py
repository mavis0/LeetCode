from binary_tree import Tree
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(r):
            if not r: return 0
            # if (not r.left) and (not r.right):return 1
            return max(depth(r.left), depth(r.right)) + 1 
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            print(root.val, left, right)
            # if left == -1 or right == -1 or abs(left - right) > 1:
            #     return -1
            # print(1 + max(left, right))
            return 1 + max(left, right)
        if not root:return True
        print(root.val, depth(root.right), depth(root.left))
        return abs(depth(root.right) - depth(root.left)) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left)
    def isBalanced2(self, root):
            
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            print(root.val, left, right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            # print(1 + max(left, right))
            return 1 + max(left, right)
            
        return check(root) != -1
s = Solution()
print(s.isBalanced(Tree([1,'null',3,2]).root))