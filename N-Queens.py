class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def place_one_queen(p, ans, i):
            for q in range(n):
                f = True
                for c, j in enumerate(p):
                    if q == j or abs(q-j) == (i - c):
                        f = False
                        break
                if f:
                    p.append(q)
                    if i == n - 1:
                        ans.append(p.copy())
                    else:
                        ans = place_one_queen(p, ans, i+1)
                    p.pop()
            return ans

        ans, s, t = place_one_queen(list(), list(), 0), list(), '.' * n
        for a in ans:
            s.append([t[:j] + 'Q' + t[j+1:] for j in a])
        return s


s = Solution()
print(s.solveNQueens(6))