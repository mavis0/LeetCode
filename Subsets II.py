class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result, last_res, res = [[]], [[]], list()
        for _ in range(len(nums)):
            for l in last_res:
                s = l[-1] if l else -1
                for i in range(s+1, len(nums)):
                    if i == 0 or nums[i] != nums[i-1] or i == s+1:
                        res.append(l + [i])
                    else:
                        continue
            result.extend([[nums[j] for j in i] for i in res])
            last_res, res = res, list()
        return result

print(Solution().subsetsWithDup([1, 2, 2]))