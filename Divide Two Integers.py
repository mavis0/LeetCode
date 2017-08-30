class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #O(n)，对于11111111111和1来说太慢了
        # flag = True if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0) else False
        # dividend, divisor = abs(dividend), abs(divisor)
        # if divisor == 0: return -1
        # i = 0
        # while dividend > divisor:
        #     dividend -= divisor
        #     i += 1
        # return i if flag else -i
        #
        if divisor == 0: return -1
        flag = True if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0) else False
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:
            d = 0
            while divisor << d <= dividend:
                d += 1
            ans += 1 << (d-1)
            dividend -= divisor << (d-1)
    
        if ans >= 2147483647:
            if flag:
                ans = 2147483647
            else:
                ans = 2147483647 if ans == 2147483647 else 2147483648
        return ans if flag else -ans





s = Solution()
print(s.divide(2147483648, 1))