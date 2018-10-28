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

print(Solution().minimumTotal([
[0]
]))

