# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p3 = dummy

        while p3.next and p3.next.next:
            p2 = p3.next
            p1 = p2.next

            p3.next = p1
            p2.next = p1.next
            p1.next = p2

            p3 = p2

        return dummy.next



s = Solution()
print(s.swapPairs())