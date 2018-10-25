class Solution(object):
    def convert(self, s, n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # if len(s) == 0 or numRows == 0 or numRows == 1:
        #     return s
        # new_s = [''] * numRows
        # l = [0]
        # l.extend(range(1, numRows))
        # l.extend(range(1, numRows-1).__reversed__())
        # l *= len(s) // (2 * (numRows-1)) + 1
        # for i in range(len(s)):
        # 	new_s[l[i]] += s[i]
        # ss = ''
        # for i in new_s:
        #     ss += i
        # return ss
        ans = list()
        if len(s) < n:return s
        for i in range(n):
            step, j, k = (2 * n - 2 * i - 2, 2 * i), i, 0
            while j < len(s):
                ans.append(s[j])
                if i == 0:
                    j += step[0]
                elif i == n - 1:
                    j += step[1]
                else:
                    j += step[k]
                    k = 0 if k else 1
        return ''.join(ans)



s = Solution()
print(s.convert('df', 1))