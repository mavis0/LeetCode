from ListLink import ListLink, ListNode
class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def rotata(head):
            tmp = ListNode("#")
            tmp.next = head
            p1, p2 = tmp, tmp.next
            while p2.next:
                p1, p2 = p2, p2.next
            tmp.next, p2.next, p1.next = p2, tmp.next, None
            return tmp.next
        p1, l = head, 0
        while p1:
            p1, l = p1.next, l + 1
        for i in range(k % l): head = rotata(head)
        return head

s = Solution()
print(s.rotateRight(ListLink([1, 2, 3]).head, 4))
