class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute(nums):
            ans = list()
            if len(nums) == 0 or len(nums) == 1:
                return [nums]
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i-1]: continue
                    num = nums.pop(i)
                    for p in permute(nums):
                        ans.append([num] + [i for i in p])
                    nums.insert(i, num)
            return ans

        nums.sort()
        return permute(nums)

s = Solution()
d = dict()
print(s.permuteUnique([1, 1, 2]))
print(s.permuteUnique([1, 1, 2, 2]))

