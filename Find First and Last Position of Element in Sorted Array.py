class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binSearch(nums, target):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid
                else:
                    return mid
            return -1

        m = binSearch(nums, target)
        if m == -1: return [-1, -1]
        ml = mr = m
        while ml != -1:
            l = ml
            ml = binSearch(nums[: ml], target)
        while mr != -1:
            r = mr
            if r != len(nums) - 1:
                mr = binSearch(nums[r+1:], target)
                if mr != -1:
                    mr = mr + r + 1
            else:
                break
        return [l, r]

s = Solution()
print(s.searchRange([1, 2, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8], 8))
