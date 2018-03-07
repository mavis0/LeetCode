class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = -1
        while n != 1:
            if len(str(n)) == 1: return False
            tmp, last = 0, n
            for i in str(n):
                tmp += int(i) ** 2
            n = tmp
        return True
        
print(Solution().isHappy(19))