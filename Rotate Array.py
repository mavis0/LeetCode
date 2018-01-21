class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Brute Force
        # def rotate_once(nums):
        #     tmp = nums[0]
        #     for i in range(1, len(nums)):
        #         tmp, nums[i] = nums[i], tmp
        #     nums[0] = tmp
        # for i in range(k % len(nums)):
        #     rotate_once(nums)
        # Using duplication
        # dup = [i for i in nums]
        # k %= len(nums)
        # for i in range(len(nums)):nums[i] = dup[i-k]
        #Using reverse
        k %= len(nums)
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]