from ListLink import ListLink, ListNode
class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        tmp = ListNode('#')
        tmp.next = head
        p1, p2 = tmp, head
        while p2 and p2.val < x:p1, p2 = p2, p2.next
        p3, p4 = p2, p2.next
        while p4:
            if p4.val < x:
                p1.next, p3.next = p4, p4.next
                p4.next, p1, p4 = p2, p4, p3.next
            else:
                p3, p4 = p4, p4.next
        return tmp.next

print(Solution().partition(ListLink([2, 1]).head, 2))