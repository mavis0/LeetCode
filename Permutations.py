class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = list()
        if len(nums) == 1 or len(nums) == 0:
            return [nums]
        else:
            for i in self.permute(nums[:-1]):
                for j in range(len(i)+1):
                    i.insert(j, nums[-1])
                    ans.append(i.copy())
                    i.pop(j)
        return ans
s = Solution()
print(s.permute([]))
