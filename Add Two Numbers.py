class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class LinkList(object):
#     def __init__(self, ln):
#         self.header = ln
#         self.pointer = self.header
#         self.num = 1

#     def add(self, ln):
#         self.pointer.next = ln
#         self.pointer = ln
#         self.num += 1

#     def f(self):
#         l = []
#         tmp = self.header
#         while tmp.next != None:
#             l.append(tmp.val)
#             tmp = tmp.next
#         l.append(tmp.val)
#         return l

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # ll1 = LinkList(ListNode(l1[0]))
        # ll2 = LinkList(ListNode(l2[0]))
        # for i in l1[1:]:
        #     ll1.add(ListNode(i))
        # for j in l2[1:]:
        #     ll2.add(ListNode(j))
        
        # lh1 = l1
        # lh2 = l2

        flag = 0

        while l1.next != None or l2.next != None:
            l1.val = l1.val + l2.val + flag
            flag = l1.val // 10
            l1.val = l1.val % 10
            l1 = l1.next
            l2 = l2.next
        l1.val = l1.val + l2.val + flag
        flag = l1.val // 10
        l1.val %= 10
        if flag:
            l1.next = ListNode(flag)
        return l1

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        l = []
        while l1 != None and l2 != None:
            tmp = l1.val + l2.val + flag
            flag = tmp // 10
            l.append(tmp % 10)
            l1 = l1.next
            l2 = l2.next

        while(l1):
            tmp = l1.val + flag
            flag = tmp // 10
            l.append(tmp % 10)
            l1 = l1.next

        while(l2):
            tmp = l2.val + flag
            flag = tmp // 10
            l.append(tmp % 10)
            l2 = l2.next

        if flag:
            l.append(flag)
        return l




s = Solution()

print(s.addTwoNumbers([2,4,3], [5,6,8]))