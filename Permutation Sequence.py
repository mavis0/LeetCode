from functools import reduce
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def Permutation(v, l):
            nonlocal k
            for i in range(n):
                if v[i]:
                    l.append(i+1)
                    v[i] = False
                    ans = Permutation(v, l)
                    if ans: return ans
                    v[i] = True
                    l.pop()
            if True not in v:
                k -= 1
                if k == 0: return l
            return None
        return ''.join([str(i) for i in Permutation([True] * n, list())])

    def getPermutation2(self, n, k):
        l, ans, k = [str(i+1) for i in range(n)], list(), k-1
        while k:
            tmp = reduce(lambda x, y: x*y, range(1, n))
            ans.append(l.pop(k // tmp))
            k, n = k % tmp, n-1
        ans.extend(l)
        return ''.join(ans)


s = Solution()
print(s.getPermutation(4, 1))
print(s.getPermutation2(4, 1))