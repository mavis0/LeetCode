class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 2: return 1
        left, right = 0, x-1
        while right > left + 1:
            center = int((left + right)/2)
            if center ** 2 < x:
                left = center
            elif center ** 2 > x:
                right = center
            else:
                return center
        return left

s = Solution()
print(s.mySqrt())