# Definition for singly-linked list.
from ListLink import ListLink, ListNode

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first =  p1 = p2 = ListNode('#')
        p3 = head
        first.next, times = head, 0
        while p3:
            if p3.val != p2.val:
                times += 1
                if times > 1:
                    p1.next = p2
                    p1 = p2
                    times = 1
            else:
                times = 0
            p2 = p3
            p3 = p3.next
        p1.next = p2 if times == 1 else None
        return first.next
s = Solution()
h = ListLink([])
print(s.deleteDuplicates(h.head))



