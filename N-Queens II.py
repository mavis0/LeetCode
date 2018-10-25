class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def place_one_queen(p,ans, i):
            for q in range(n):
                f = True
                for c, j in enumerate(p):
                    if q == j or abs(q-j) == (i - c):
                        f = False
                        break
                if f:
                    p.append(q)
                    if i == n - 1:
                        ans += 1
                    else:
                        ans = place_one_queen(p, ans, i+1)
                    p.pop()
            return ans

        ans = place_one_queen(list(), 0, 0)
        return ans


s = Solution()
print(s.solveNQueens(6))
