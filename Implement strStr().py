class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle: return 0
        if not haystack and needle: return -1
        i = 0
        while i < len(haystack):
            p = 0
            while p < len(needle) and i+p < len(haystack) and haystack[i+p] == needle[p] :
                 p += 1

            if p == len(needle):
                return i 
            elif i+p == len(haystack):
                return -1
            else:
                i += 1
        
        return i if i != len(haystack) else -1

s = Solution()
print(s.strStr("mississippi", "a"))