from binary_tree import TreeNode, Tree
class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if (not inorder) or (not postorder): return None
        root, i = TreeNode(postorder[-1]), inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root
print(Solution().buildTree([9,3,15,20,7], [9,15,7,20,3]))