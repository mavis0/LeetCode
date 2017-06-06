class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        l = int(s[::-1]) if s[0] != '-' else 0 - int(s[1:][::-1])
        return l if  -2**31< l < 2**31 else 0
        


s = Solution()
print(s.reverse(-1534236469))
