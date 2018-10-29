class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #TLE using DFS
        # def minimumLevel(level, tmpSum, i):
        #     if level == len(triangle) - 1:
        #         return tmpSum+min(triangle[level][i], triangle[level][i+1]) if i < len(triangle[level]) - 1 else tmpSum + triangle[level][i]
        #     else:
        #         if i < len(triangle[level]) - 1:
        #             return min(minimumLevel(level+1, tmpSum+triangle[level][i], i),
        #                        minimumLevel(level+1, tmpSum+triangle[level][i+1], i+1))
        #         else:
        #             return minimumLevel(level+1, tmpSum+triangle[level][i], i)
        # return minimumLevel(0, 0, 0)
        #dp with triangle space
        # res = [triangle[0]]
        # for l in range(1, len(triangle)):
        #     levelRes = list()
        #     for i in range(len(triangle[l])):
        #         if i == 0:levelRes.append(res[l-1][i]+triangle[l][i])
        #         elif i == len(triangle[l])-1:levelRes.append(res[l-1][i-1]+triangle[l][i])
        #         else:levelRes.append(triangle[l][i]+min(res[l-1][i-1], res[l-1][i]))
        #     res.append(levelRes.copy())
        # return min(res[-1])
        #还有一种从下到上的dp，空间复杂度仅仅为triangle[-1]
        if not triangle:return
        dp = [i for i in triangle[-1]]
        for i in range(len(triangle)-1, -1, -1):
            for j in range(i):
                dp[j] = triangle[i-1][j] + min(dp[j], dp[j+1])
        return dp[0]



print(Solution().minimumTotal([
[2],
[3, 4],
[6, 5, 7],
[4, 1, 8, 3]
]))

