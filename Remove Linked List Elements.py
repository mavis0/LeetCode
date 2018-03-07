# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        fake = ListNode(-1)
        fake.next = head
        first, second = fake, head
        while second.next:
            if second.val == val:
                first.next = second.next
            first, second = second, second.next
        if second.val == val:first.next = None
        return fake.next

