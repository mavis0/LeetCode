class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if not haystack and not needle: return 0
        # if not haystack and needle: return -1
        # i = 0
        # while i < len(haystack):
        #     p = 0
        #     while p < len(needle) and i+p < len(haystack) and haystack[i+p] == needle[p] :
        #          p += 1

        #     if p == len(needle):
        #         return i 
        #     elif i+p == len(haystack):
        #         return -1
        #     else:
        #         i += 1
        
        # return i if i != len(haystack) else -1
        #用KMP试一试，第一版，但是也只是9.22%，也不应该啊，再试试吧
        j, k = 0, -1
        h, n = len(haystack), len(needle)
        nx = [-1] * n
        while j < n - 1:
            if k == -1 or needle[j] == needle[k]:
                k += 1
                j += 1
                nx[j] = k
            else:
                k = nx[k]

        i, j = 0, 0
        while i < h:
            while i < h and j < n and haystack[i] == needle[j]:
                i, j = i+1, j+1

            if j == n:
                return i - j
            elif j == 0:
                i += 1
            else:
                j = nx[j]

        return -1


s = Solution()
print(s.strStr("mississippi", "a"))