# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        
        # p1, p2 = l1, l2
        # tmp = p1

        # while p1 and p2:
        #     if p1.val < p2.val:
        #         while p1 != None and p1.val < p2.val:
        #             tmp = p1
        #             p1 = p1.next
        #         tmp.next = p2
        #     else:
        #         while p2 != None and p1.val >= p2.val:
        #             tmp = p2
        #             p2 = p2.next
        #         tmp.next = p1

        # if p1:
        #     tmp.next = p1
        # else:
        #     tmp.next = p2

        # return l1 if l1.val < l2.val else l2

        dummy,cur = ListNode(0)

        while l1 or l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2

        return dummy.next





s = Solution()
print(s.mergeTwoLists([], []))