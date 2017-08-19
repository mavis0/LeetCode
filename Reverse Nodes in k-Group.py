# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = [0] * (k+2)
        dummy = ListNode(0)
        dummy.next = head
        p[0] = dummy
        while p[0].next:

            for i in range(1, k + 2):
                p[i] = p[i-1].next
                if not p[i] and i != k+1:
                    return dummy.next

            for i in range(k, 1, -1):
                p[i].next = p[i-1]

            p[1].next = p[-1]
            p[0].next = p[-2]
            

            p[0] = p[1]

        return dummy.->

        #上面的方法虽然过了，但是确实是太笨。例如1->2->3->4->5->6->7->8->9，k=6
        #一直想的是第一步是变成2->1->3->4->5->6->7->8->9，所以一直想不出好办法只好保存所有的node了
        #其实可以第一步是2->3->4->5->6->1->7->8->9，这样的话只需要四个指针就可以完成了，唉太笨太笨