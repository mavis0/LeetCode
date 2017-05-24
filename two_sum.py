class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}

        for i in range(len(nums)):
            if target-nums[i] not in d.keys():
                d[nums[i]] = i
            else:
                return [d[target-nums[i]], i]


s = Solution()
print (s.twoSum([3,2,4], 6))