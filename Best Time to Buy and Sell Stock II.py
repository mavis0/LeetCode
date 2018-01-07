class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:return []
        m, last = 0, prices[0]
        for i in prices[1:]:
            if i > last:
                m += i-last
            last = i
        return m


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))