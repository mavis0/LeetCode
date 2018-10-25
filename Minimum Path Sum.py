class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0] * (len(grid[0])) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0: dp[i][j] = dp[i][j-1] + grid[i][j]
                if i and j == 0: dp[i][j] = dp[i-1][j] + grid[i][j]
                if i and j: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
s = Solution()
print(s.minPathSum([
  [1],
  [2]
]))