# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p0, p1 = head, head.next
        
        while p1:
            p2 = p1.next

            p1.next = head
            p0.next = p2
            head = p1

            p1 = p2
        return head
    #群里看到的一个其他的小题目，和leetcode无关
    def circle(self, n):
        l, m = [[0] * n for _ in range(n)], 1
        i = j = c = 0
        cur_row = cur_col = n
        while 1:
            while c < cur_col:
                l[i][j] = m
                i, m, c = i+1, m+1, c+1
            i, j, c = i-1, j+1, 0
            while c < cur_row-1:
                l[i][j] = m
                j, m, c = j+1, m+1, c+1
            i, j, c = i-1, j-1, 0
            while c < cur_col-1:
                l[i][j] = m
                i, m, c = i-1, m+1, c+1
            i, j, c = i+1, j-1, 0
            while c < cur_row-2:
                l[i][j] = m
                j, m, c = j-1, m+1, c+1
            i, j, c = i+1, j+1, 0

            if m > n ** 2:break
            cur_col -= 2
            cur_row -= 2
        
        return l

l = Solution().circle(7)
for i in l:
    for j in i:
        print("%3d" % j, end = ' ')
    print()






