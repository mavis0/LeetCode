class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans, last = [[0] * n for i in range(n)], 1
        for s in range((n+1)//2):
            j = i = s
            for j in range(j, j+n):
                ans[i][j] = last
                last += 1
            for i in range(i+1, i+n):
                ans[i][j] = last
                last += 1
            for j in range(j-1, j-n, -1):
                ans[i][j] = last
                last += 1
            for i in range(i-1, i-n+1, -1):
                ans[i][j] = last
                last += 1
            n -= 2
        return ans


s = Solution()
print(s.generateMatrix(5))