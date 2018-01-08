# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        cur, s = self, ''
        while cur:
            s += str(cur.val) + '--> '
            cur = cur.next
        s += 'None'
        return s

class ListLink(object):

    def __init__(self, l):
        if l == []:
            self.head = None
            return
        else:
            self.head = ListNode(l[0])
        cur = self.head
        for i in l[1:]:
            tmp = ListNode(i)
            cur.next = tmp
            cur = tmp

    def __str__(self):
        cur, s = self.head, ''
        while cur:
            s += str(cur.val) + '--> '
            cur = cur.next
        s += 'None'
        return s