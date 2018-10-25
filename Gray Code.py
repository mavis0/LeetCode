class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0: return [0]
        tmp1, tmp2 = self.grayCode(n-1), list()
        for i in tmp1[::-1]:
            tmp2.append(i+2**(n-1))
        return tmp1+tmp2

print(Solution().grayCode(1))