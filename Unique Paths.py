from functools import reduce
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # TLE
        # if m == 1 or n == 1: return 1
        # return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n -1)
        return reduce(lambda x, y: x* y, range(m + n - 2, m + n - 1 - min(n, m), -1)) \
               // reduce(lambda x, y: x*y, range(1, min(n, m)))


s = Solution()
print(s.uniquePaths(7, 0))