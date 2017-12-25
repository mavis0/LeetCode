class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split(' ')

        if len(l) == len(s) + 1: return 0
        for i in range(len(l)-1, -1, -1):
            if l[i] != '': return len(l[i])
            # print(i)

s = Solution()
print(s.lengthOfLastWord("a   "))