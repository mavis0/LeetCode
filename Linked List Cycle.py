from ListLink import ListLink

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #有关链表的题，多考虑双指针！！
        if (not head) or (not head.next):return False
        slow, fast = head, head.next
        while fast:
            if slow == fast:return True
            slow = slow.next
            fast = fast.next.next
        return False
s = Solution()
print(s.hasCycle(ListLink([1, 2, 3, 4]).head))