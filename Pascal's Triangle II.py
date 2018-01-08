class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def factorial(x):
            s = 1
            for i in range(1, x+1):
                s *= i
            return s
        a = []
        for i in range(rowIndex+1):
            a.append(int(factorial(rowIndex)/(factorial(i)*factorial(rowIndex - i))))
        return a

s = Solution()
print(s.getRow(1))