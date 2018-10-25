from binary_tree import TreeNode, Tree

def Soulution(T, n):
    l = list()
    def in_order(T):
        nonlocal l
        if T == None:return 
        l.append(in_order(T.left))
        l.append(T.val)
        l.append(in_order(T.right))
    in_order(T)
    l = [i for i in l if i is not None]
    for i in range(len(l)):
        if l[i] == n:break
    return [l[i-1], l[i+1]] if 0 < i < len(l)-1 else [0, l[1]] if i == 0 else [l[-2], 0]

if __name__ == '__main__':
    T = Tree([10, 6, 15, 4, 8, 11, 17, 1, 5])
    print(Soulution(T.root, 11))