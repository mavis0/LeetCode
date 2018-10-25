class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return nums
        l, r, mid = 0, len(nums) - 1, 0
        while mid <= r:
            if nums[mid] == 0:
                nums[l], nums[mid] = nums[mid], nums[l]
                l += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[r] = nums[r], nums[mid]
                r -= 1
            else:
                mid += 1
        return nums

s = Solution()
print(s.sortColors([2,0,2,1,1,0]))
