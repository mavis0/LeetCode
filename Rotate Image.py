class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = k = len(matrix)
        while k > 0:
            i = (n - k + 1) // 2
            for j in range(i, n-i-1):
                tmp, matrix[j][n-i-1] = matrix[j][n-i-1], matrix[i][j]
                tmp, matrix[n-i-1][n-j-1] = matrix[n-i-1][n-j-1], tmp
                tmp, matrix[n-j-1][i] = matrix[n-j-1][i], tmp
                matrix[i][j] = tmp
            k -= 2
        return matrix


s = Solution()
print(s.rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
