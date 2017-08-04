class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        tmp = []
        n = len(strs)

        while n != 1:
            for i in range(0, n-1, 2):
                tmp.append(self.CommonPre(strs[i], strs[i+1]))
            if n % 2 == 1:
                tmp.append(strs[-1])
            strs = tmp
            n = len(strs)
            tmp = []

        return strs[0]

    def CommonPre(self, s1, s2):
        cp = ''
        for i in range(len(s1)):
            cp += s1[i]
            if cp != s2[0: i+1]:
                cp = cp[0:-1]
                break

        return cp


    


s = Solution()
# print(s.CommonPre('ser', 'se'))
print(s.longestCommonPrefix(['ser', 'set', 'seg', 'ssdfg', 'ssdgv', 'ssefr', 'sefg']))
# print(s.longestCommonPrefix(['']))