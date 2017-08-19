class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: return len([])
        nums.sort()
        k = 0

        for j in nums:
            if j != val:
                nums[k] = j
                k += 1

        return nums[:k]


s = Solution()
print(s.removeElement([1,2,3,3,3,3,3,4,5,6], 3))