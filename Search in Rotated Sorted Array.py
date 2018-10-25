class Solution(object):
    def search(self, nums, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binsearch(nums, t):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > t:
                    r = mid
                elif nums[mid] < t:
                    l = mid + 1
                else:
                    return mid
            return -1
        l, r, ans = 0, len(nums)-1, 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                if nums[l] <= t <= nums[mid]: return binsearch(nums[l: mid + 1], t) + l if binsearch(nums[l: mid + 1], t) != -1 else -1
                l = mid + 1
            else :
                if nums[mid] <= t <= nums[r]: return binsearch(nums[mid: r + 1], t) + mid if binsearch(nums[mid: r + 1], t) != -1 else -1
                r = mid - 1
        return -1


s = Solution()
print(s.search([3, -1], 3))