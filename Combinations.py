class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # TLE
        # def inner(l, ans, k, v):
        #     if k == 0:
        #         v.append(ans.copy())
        #         return v
        #     for i in range(len(l)):
        #         ans.append(l[i])
        #         inner(l[i+1:], ans, k-1, v)
        #         ans.pop()
        #     return v
        # return inner([i for i in range(1, n+1)], list(), k, list())
        # TLE
        # ans = [[i] for i in range(1, n-k+2)]
        # for i in range(k-1):
        #     for t in range(len(ans)):
        #         a = ans.pop(0)
        #         for j in range(a[-1]+1, n+1):
        #             a.append(j)
        #             ans.append(a.copy())
        #             a.pop()
        # return ans
        if k == 0:return [[]]
        if k == 1: return [[i] for i in range(1, n+1)]
        result = list()
        for ans in self.combine(n-1, k-1):
            for j in range(ans[-1]+1, n+1):
                result.append((ans + [j]).copy())
        return result


print(Solution().combine(4, 2))