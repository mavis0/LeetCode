class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 时间复杂度太高了。。。
        # if len(nums) == 0 or len(nums) == 1:return True
        # if len(nums) == 2: return True if nums[0] != 0 else False
        # for i in range(2, len(nums)):
        #     if nums[0] >= len(nums)-1 or (self.canJump(nums[: i]) and self.canJump(nums[i-1:])):
        #         return True
        # return False
        n, m, s = len(nums), 0, 0
        for i, j in enumerate(nums[:-1]):
            s = max(j, s)
            m = max(m, i + s)
            if s == 0 :break
            s -= 1
        return m >= (n-1)

s = Solution()
print(s.canJump([3, 2, 1, 0, 4]))