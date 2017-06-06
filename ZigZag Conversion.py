class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0 or numRows == 0 or numRows == 1:
            return s
        new_s = [''] * numRows
        l = [0]
        l.extend(range(1, numRows))
        l.extend(range(1, numRows-1).__reversed__())
        l *= len(s) // (2 * (numRows-1)) + 1
        for i in range(len(s)):
        	new_s[l[i]] += s[i]
        ss = ''
        for i in new_s:
            ss += i
        return ss



s = Solution()
print(s.convert('ABC', 2))