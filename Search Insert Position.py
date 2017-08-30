class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]: return 0
        if target > nums[-1]: return len(nums)
        # if target == nums[-1]: return len(nums) - 1
        s, e = 0, len(nums)
        while s < e - 1:
            m = (s + e) // 2
            if nums[m] < target:
                s = m
            elif nums[m] > target:
                e = m
            else:
                return m
        return s + 1

s = Solution()
print(s.searchInsert([1,2,3], 3))