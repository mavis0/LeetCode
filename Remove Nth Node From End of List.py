# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #----------------竟然用list保存了所有的node指针，真是蠢啊蠢
        # l, p = [head], head

        # while p.next:
        #     l.append(p.next)
        #     p = p.next

        # if len(l) == 1:
        #     return []

        # if n == 1:
        #     l[-2].next = None
        # elif n == len(l):
        #     head = l[1]
        # else:
        #     l[-n-1].next = l[-n+1]

        # return head
        #双指针思想，两个指针相隔n-1，每次两个指针向后一步，
        #当后面一个指针没有后继了，前面一个指针就是要删除的节点。
        #Cool！

        d = ListNode(0)
        d.next = head
        first = second = d
        for _ in range(n):
            second = second.next

        while second.next:
            first = first.next
            second = second.next

        first.next = first.next.next

        return d.next






s = Solution()
print(s.removeNthFromEnd())