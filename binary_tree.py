# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        queue, s = deque(), ''
        queue.append(self)
        while queue:
            item = queue.pop()
            s = s + str(item.val) + ', ' if item and item != 'null' else s + 'null'+ ', '
            if item != 'null' and item.left:
                queue.appendleft(item.left)
            if item != 'null' and item.right:
                queue.appendleft(item.right)
        return s

class Tree:
    def __init__(self, l):
        if l == []:
            self.root = []
            return 
        tmp = self.root = TreeNode(l.pop(0))
        floor = [tmp]
        while l:
            while floor:
                if not l: break
                tmp = TreeNode(l.pop(0))
                floor_tmp = floor.pop(0)
                if tmp.val != 'null':
                    floor_tmp.left = tmp
                    floor.append(tmp)
                if not l: break
                tmp = TreeNode(l.pop(0))
                if tmp.val != 'null':
                    floor_tmp.right = tmp
                    floor.append(tmp)

    def BFS(self):
        quene, t = [self.root], []
        while quene and self.root:
            tmp = quene.pop(0)
            t.append(tmp.val)
            if tmp.left:
                quene.append(tmp.left)
            
            if tmp.right:
                quene.append(tmp.right)
        return t

    def DFS(self):
        quene, t = [self.root], []
        while quene:
            tmp = quene.pop()
            t.append(tmp.val)
            if tmp.right:
                quene.append(tmp.right)
            if tmp.left:
                quene.append(tmp.left)
        return t

    def __str__(self):
        queue, s = deque(), ''
        queue.append(self.root)
        while queue:
            item = queue.pop()
            s = s + str(item.val) + ', ' if item and item != 'null' else s + 'null'+ ', '
            if item != 'null' and item.left:
                queue.appendleft(item.left)
            if item != 'null' and item.right:
                queue.appendleft(item.right)
        return s

if __name__ == '__main__':
    t = Tree([1, 'null', 3, 4]).root
    print(t)