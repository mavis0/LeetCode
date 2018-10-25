class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums: return False
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return True
            elif nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
               r -= 1
        return False


s = Solution()
print(s.search([1, 1, 1, 3, 1], 3))