class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:return 0
        i, m = prices[0], 0
        for j in prices:
            if j < i:
                i = j
            else:
                m = j - i if j - i > m else m
        return m

print(Solution().maxProfit([2, 4, 1]))