from ListLink import ListNode, ListLink
from binary_tree import TreeNode, Tree
class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return
        if not head.next: return TreeNode(head.val)
        fast = slow = preslow = head
        while fast and fast.next:
            fast, slow, preslow = fast.next.next, slow.next, slow
        root = TreeNode(slow.val)
        root.right, preslow.next = self.sortedListToBST(slow.next), None
        root.left = self.sortedListToBST(head)
        return root
print(Solution().sortedListToBST(ListLink([-10,-3,0,5,9]).head))
