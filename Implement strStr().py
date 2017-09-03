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
        #用KMP试一试，第一版，但是也只是9.22%，也不应该啊，再试试吧，看了别人的submit，都反映kmp
        #比暴力算法要慢，可能测试用例有问题吧
        # if not needle: return 0
        # j, k = 0, -1
        # h, n = len(haystack), len(needle)
        # nx = [-1] * n
        # while j < n - 1:
        #     if k == -1 or needle[j] == needle[k]:
        #         k += 1
        #         j += 1
        #         nx[j] = k
        #     else:
        #         k = nx[k]

        # i, j = 0, 0
        # while i < h - n + 1:
        #     while i < h and j < n and haystack[i] == needle[j]:
        #         i, j = i+1, j+1

        #     if j == n:
        #         return i - j
        #     elif j == 0:
        #         i += 1
        #     else:
        #         j = nx[j]

        # return -1
        #看过别人的代码后，再次尝试用暴力算法，11%的成绩太难看
        if not needle: return 0
        i = 0
        h, n = len(haystack), len(needle)
        while i <= h - n:
            for j in range(n):
                if haystack[i+j] != needle[j]:
                    i += 1
                    break
                if j == n - 1:
                    return i
        return -1
        #24%,55ms还是太慢啊，但是Google了一圈也没有找到更快的python代码，
        #哼，他们肯定都是直接用的find函数！

s = Solution()
print(s.strStr("", "as"))