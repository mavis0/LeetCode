class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binSerarch(l, t):
            s, e = 0, len(l)
            while s < e:
                mid = (e - s) // 2 + s
                if l[mid] == t:
                    return mid
                elif l[mid] < t:
                    s = mid + 1
                else:
                    e = mid
            return e
        a = binSerarch([i[0] for i in matrix], target)
        if a < len(matrix) and matrix[a][0] == target: return True
        b = binSerarch(matrix[a-1], target)
        return True if b < len(matrix[a-1]) and matrix[a-1][b] == target else False

print(Solution().searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3))