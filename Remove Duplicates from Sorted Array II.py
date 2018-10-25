class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, f, t = 0, 0, 0
        tmp = '#'
        while f < len(nums):
            if nums[f] == tmp:
                t += 1
            else:
                tmp = nums[f]
                t = 0
            if t < 2:
                nums[s] = nums[f]
                s += 1
            f += 1
        return s


s = Solution()
print(s.removeDuplicates([0,0,0,0,1,1,1,1,2,3,3]))
