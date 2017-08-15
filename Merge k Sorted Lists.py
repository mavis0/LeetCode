# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLink(l1, l2):
            dummy = ListNode(0)
            cur = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    cur = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    cur = l2
                    l2 = l2.next

            cur.next = l1 or l2

            return dummy.next
        
        while len(lists) > 1:
            tmp = []
            k = len(lists)
            for i in range(0, k - 1, 2):
                tmp.append(mergeTwoLink(lists[i], lists[i+1]))
            if i+1 != k-1:
                tmp.append(lists[-1])
            lists = tmp

        return lists[0]

s = Solution()
print(s.mergeKLists([]))

