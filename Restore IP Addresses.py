class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def restore(s, depth, ip, res):
            if not s: return []
            if depth == 4:
                cor = (10 ** (len(s)-1)-1) if len(s) > 1 else -1
                if cor < int(s) < min(256, 10 ** len(s)):
                    res.append((ip+'.'+s).lstrip('.'))
            else:
                for i in range(1, min(4, len(s)+1)):
                    cor = (10 ** (i-1)-1) if i > 1 else -1
                    if cor < int(s[:i]) < min(256, 10 ** i):
                        restore(s[i:], depth+1, ip+'.'+s[:i], res)
            return res
        return restore(s, 1, '', [])

print(Solution().restoreIpAddresses('0000'))