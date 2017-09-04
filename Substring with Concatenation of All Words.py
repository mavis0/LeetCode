class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        #大致思路就是保存words的字典，然后构建一个和总长度相同的滑动窗口，一个字符一个字符向后滑动。
        #然后判断当前窗口的字符是否满足要求。时间复杂度大致是O(n^2)，ac了但是成绩812ms，9.57%，很差啊。。。
        if not words[0]:return [i for i in range(len(s))]
        num, length = len(words), len(words[0])
        totlen = num * length
        d,ans = {}, list()
        for i in words:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        for i in range(len(s) - totlen + 1):
            sub, dup_d, k = s[i: i+totlen], d.copy(), 0
            for j in range(0, totlen, length):
                subsub = sub[j:j+length]
                if subsub not in d.keys():
                    break
                else:
                    dup_d[subsub] -= 1
                    if dup_d[subsub] < 0:
                        break
                k += 1
                if k == num:
                    ans.append(i)
        return ans



s = Solution()
print(s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))
# print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))