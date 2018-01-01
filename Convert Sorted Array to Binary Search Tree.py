from binary_tree import Tree, TreeNode

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums);mid = int(l/2)
        if l == 0:return None
        if l == 1:return TreeNode(nums[0])
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

s = Solution()
t = Tree([])
t.root = s.sortedArrayToBST([-10,-3,0,5,9])
print(t.BFS())
