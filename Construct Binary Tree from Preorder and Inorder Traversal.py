from binary_tree import TreeNode, Tree
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if (not preorder) or (not inorder):return None
        root, i = TreeNode(preorder[0]), inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root

print(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))