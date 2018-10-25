from functools import reduce
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # TLE
        # if len(obstacleGrid) < 1 or len(obstacleGrid[0]) < 1:return 0
        # if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:
        #     return 1 if obstacleGrid[0][0] == 0 else 0
        # if obstacleGrid[0][0]: return 0
        # return self.uniquePathsWithObstacles([i[1:] for i in obstacleGrid]) + \
        #        self.uniquePathsWithObstacles(obstacleGrid[1:])
        dp = [[0] * (len(obstacleGrid[0])+1) for i in range(len(obstacleGrid)+1)]
        dp[1][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, len(obstacleGrid)+1):
            for j in range(1, len(obstacleGrid[0])+1):
                right = dp[i][j-1] if j == 1 or obstacleGrid[i-1][j-2] == 0 else 0
                down = dp[i-1][j] if i == 1 or obstacleGrid[i-2][j-1] == 0 else 0
                dp[i][j] = right + down if obstacleGrid[i-1][j-1] == 0 else 0
        return dp[-1][-1]

s = Solution()
print(s.uniquePathsWithObstacles([
    [0, 1]
]))