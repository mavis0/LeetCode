class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse(h):
            first, second = None, h
            while second:
                tmp = second.next
                second.next = first
                first, second = second, tmp
            return first
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tail = reverse(slow.next) if fast else reverse(slow)
        while tail:
            if tail.val != head.val:return False
            tail, head = tail.next, head.next
        return True
        #我以为自己一遍过已经很厉害了，没想到这个才是牛逼！！脑袋开光了！！
        # def isPalindrome(self, head):
        #     rev = None
        #     slow = fast = head
        #     while fast and fast.next:
        #         fast = fast.next.next
        #         rev, rev.next, slow = slow, rev, slow.next
        #     if fast:
        #         slow = slow.next
        #     while rev and rev.val == slow.val:
        #         slow = slow.next
        #         rev = rev.next
        #     return not rev
        
        