# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = [0] * (k+2)
        dummy = ListNode(0)
        dummy.next = head
        p[0] = dummy
        while p[0].next:

            for i in range(1, k + 2):
                p[i] = p[i-1].next
                if not p[i] and i != k+1:
                    return dummy.next

            for i in range(k, 1, -1):
                p[i].next = p[i-1]

            p[1].next = p[-1]
            p[0].next = p[-2]
            

            p[0] = p[1]

        return dummy.next