class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return 1 if n < 2 else sum([self.numTrees(i)*self.numTrees(n-1-i) for i in range(n)])
        res = [1, 1]
        if n < len(res): return res[n]
        for i in range(2, n+1):
            res.append(sum([res[j] * res[i-1-j] for j in range(i)]))
        return res[-1]
print(Solution().numTrees(3))