class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:return 0 if len(nums) == 0 else nums[0]
        dp = [0] * (len(nums)+1)
        dp[1] = nums[0]
        for i in range(2, len(nums)+1):
            dp[i] =  max(dp[i-2]+nums[i-1], dp[i-1])
        return dp[-1]

s = Solution()
print(s.rob([2,1,1,2]))
