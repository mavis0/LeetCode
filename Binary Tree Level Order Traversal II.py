from binary_tree import Tree
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        a, offspring = [[root.val]],[]
        if root.left or root.right:offspring = [root.left, root.right]
        while offspring:
            a.append([i.val for i in offspring if i])
            tmp = list()
            # tmp.extend([[i.left, i.right] for i])
            for i in offspring:
                if i:
                    if i.left:tmp.append(i.left)
                    if i.right:tmp.append(i.right)
            offspring = tmp.copy()
        return a[::-1]
s = Solution()
print(s.levelOrderBottom(Tree([3]).root))