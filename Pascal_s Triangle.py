class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a = [[1], [1, 1]]
        if numRows == 0:return [[]]
        if numRows == 1:return [[1]]
        if numRows == 2:return [[1], [1, 1]]
        for i in range(2, numRows):
            last, tmp = a[-1], [1]
            for j in range(1, i):
                tmp.append(last[j-1] + last[j])
            tmp.append(1)
            a.append(tmp)

        return a

s = Solution()
print(s.generate(10))
