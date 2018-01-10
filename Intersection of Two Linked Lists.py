from ListLink import ListLink
class Solution(object):
    # def getIntersectionNode(self, headA, headB):
    #     """
    #     :type head1, head1: ListNode
    #     :rtype: ListNode
    #     """
    #     s, prt = set(), headA
    #     while prt:
    #         s.add(prt)
    #         prt = prt.next
    #     prt = headB
    #     while prt:
    #         if prt in s:return prt
    #         prt = prt.next
    #     return prt\
    # 这样的一个双循环指针我还真是没想到，真是够trick的
    def getIntersectionNode(self, headA, headB):
        if not (headA and headB):return None
        prtA, prtB = headA, headB
        endNodeA = endNodeB = None
        while prtA != prtB:
            
            if not prtA.next:endNodeA = prtA
            if not prtB.next:endNodeB = prtB
            prtA, prtB = prtA.next, prtB.next
            if not prtA:prtA = headB
            if not prtB:prtB = headA
            if endNodeA and endNodeB and endNodeA != endNodeB:return None
            
        return prtA


s = Solution()
print(s.getIntersectionNode(ListLink([1, 3]).head, ListLink([]).head))