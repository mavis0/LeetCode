class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        l, n, m = list(), len(matrix), len(matrix[0])
        for s in range(min((m + 1) // 2, (n + 1) // 2)):
            i = j = s
            l.extend([matrix[i][j] for j in range(j, j + m)])
            l.extend([matrix[i][j+m-1] for i in range(i + 1, i + n)])
            if n != 1: l.extend([matrix[i+n-1][j] for j in range(j + m - 2, j - 1, -1)])
            if m != 1: l.extend([matrix[i][j] for i in range(i + n - 2, i, -1)])
            n, m = n - 2, m - 2
        return l

s = Solution()
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9],[10, 11,12]]))