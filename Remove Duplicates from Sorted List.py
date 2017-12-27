from ListLink import ListNode, ListLink

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:return []
        first, second = head, head.next
        while second:
            while second and second.val == first.val:
                second = second.next
            first.next = second
            first = second
            if first:second = first.next
        return head

ll = ListLink([1, 2, 3, 3, 4, 4, 5, 5])
print(ll)
print(Solution().deleteDuplicates(ll.head))
l = ListLink([])
print(l)