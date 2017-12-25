class Solution:
    def maxSubArray_0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 分治的思想 看了答案才想起来 关键在于分了之后怎么治 这个是之前没有想到的关键
        # 时间复杂度是O(nlogn)
        if len(nums) == 1:
        	return nums[0]
        if len(nums) == 2:
        	return max(nums[0], nums[1], nums[0]+nums[1])
        cen = int(len(nums) / 2)

        left_max = self.maxSubArray(nums[0:cen])
        right_max = self.maxSubArray(nums[cen:])

        tmp_max = tmp_sum = nums[cen]
        for i in range(cen-1, -1, -1):
        	tmp_sum += nums[i]
        	tmp_max = tmp_sum if tmp_sum > tmp_max else tmp_max
        left_cen_max = tmp_max

        tmp_max = tmp_sum = nums[cen]
        for i in range(cen+1, len(nums)):
        	tmp_sum += nums[i]
        	tmp_max = tmp_sum if tmp_sum > tmp_max else tmp_max
        right_cen_max = tmp_max

        return max(left_max, right_max, left_cen_max+right_cen_max-nums[cen])

    def maxSubArray(self, nums):
    	#36%,这个题这么简单？？为嘛新浪的人要故意刁难我，当时好像想出来了吧但是没有底气
    	#好像当时问他他说还要用blala的？？？是我记错了么？？
        if len(nums) == 1: return nums[0]
        tmp_sum = tmp_max = 0 if nums[0] < 0 else nums[0]
        for i in nums[1:]:
            tmp_sum += i
            tmp_sum = 0 if tmp_sum < 0 else tmp_sum
            tmp_max = max(tmp_sum, tmp_max)
        if tmp_max == 0: return max(nums)
        return tmp_max

s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(s.maxSubArray([-2, 1, -3]))