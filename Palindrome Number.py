class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x > 2147483647 or x < -2147483648:
        	return False
        s = str(x)
        rs = s[::-1]
        return True if s == rs else False




s = Solution()
print(s.isPalindrome(-0))