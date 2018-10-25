from ListLink import ListLink, ListNode
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p, l = ListNode('#'), list()
        p.next, p1 = head, p
        # while p1:
        while len(l) < (n+1) and p1:
            l.append(p1)
            p1 = p1.next
        if len(l) == (n+1):
            for i, j in enumerate(l):
                if i < m+1:continue
                j.next = l[i-1]
            l[m-1].next, l[m].next, l = l[-1], p1, [l[m]]
        return p.next
print(Solution().reverseBetween(ListLink([1, 2, 3, 4, 5]).head, 1, 2))
