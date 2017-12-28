from binary_tree import Tree
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == q
        

t = Tree([1, 2, 3, 'null', 5])
# print(t.root.left.right.val)
print(t.BFS())
print(t.DFS())
