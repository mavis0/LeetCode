from binary_tree import TreeNode
class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs(l):
            if not l: return []
            if len(l) == 1: return [TreeNode(l[0])]
            res = list()
            for i in l:
                left, right = dfs(range(l[0], i)), dfs(range(i+1, l[-1]+1))
                for j in range(max(len(left), 1)):
                    for k in range(max(len(right), 1)):
                        root = TreeNode(i)
                        if j < len(left): root.left = left[j]
                        if k < len(right): root.right = right[k]
                        res.append(root)
            return res
        return dfs(range(1, n+1))

for i in Solution().generateTrees(3):
    print(i)
