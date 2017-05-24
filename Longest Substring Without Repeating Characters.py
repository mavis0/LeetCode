
class Solution(object):
    def lengthOfLongestSubstring(self, a):
        """
        :type s: str
        :rtype: int
        """
        if a == '':
            return 0
        if len(a) == 1:
            return 1
        if len(a) == 2:
            if a[0] == a[1]:
                return 1
            else:
                return 2

        start = 0
        end = 1
        longlen = 1
        ss = a[0]
        while end < len(a):
            while a[end] not in ss:
                if end != len(a)-1:
                    end += 1
                else:
                    break
                ss = a[start: end]
            if end != len(a)-1:
                longlen = max(longlen, end - start)
                start += ss.find(a[end]) + 1
                end += 1
            else:
                if a[end] in ss:
                    longlen = max(longlen, end - start)
                else:
                    longlen = max(longlen, end - start + 1)
                break
            ss = a[start: end]
        return longlen


s = Solution()
print(s.lengthOfLongestSubstring("aab"))



        