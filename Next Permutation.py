class Solution(object):
    def nextPermutation(self, nums, up_f = True):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 or (n == 1 and up_f):return
        if n == 1 or n == 2:
        	nums = nums[::-1]
        	if up_f:
        		return
        	else:
        		return nums
        for i in range(n - 1, 0, -1):
        	if nums[i] > nums[i-1]:
        		j = n-1
        		while j > i:
        			if nums[j] > nums[i-1]:
        				nums[j], nums[i-1] = nums[i-1], nums[j]
        				break		
        			else:
        				j -= 1
        		tmp = nums[:i]
        		tmp.append(self.nextPermutation(nums[i:], False))
        		nums = tmp
        		break
        	if i == 1: nums = nums[::-1]
        if up_f:
        		return
        else:
            return nums




s = Solution()
print(s.nextPermutation([3,9,8,7]))