class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        dp = [1] * (len(s) + 1)
        dp[1] = 1 if s[0] != '0' else 0
        #dp[1] = 1 if int(s[:2]) == 10 or int(s[:2]) == 20 else 2 if 10 < int(s[:2]) < 27 else 0
        for i in range(2, len(s)+1):
            if s[i-1] == '0':
                dp[i] = dp[i - 2] if s[i-2] == '1' or s[i-2] == '2' else 0
            else:
                dp[i] = dp[i - 1] + dp[i - 2] if 10 < int(s[i - 2: i]) < 27 else dp[i - 1]
        return dp
print(Solution().numDecodings(
    '110'
))
