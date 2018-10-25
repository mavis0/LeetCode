class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        reslut, lasttmp, tmp = [[]], [[]], list()
        for _ in nums:
            for r in lasttmp:
                p = r[-1] if r else -1
                if p == len(nums)-1:continue
                for i in range(p+1, len(nums)):
                    tmp.append(r + [i])
            reslut.extend([[nums[v] for v in j] for j in tmp])
            lasttmp, tmp = tmp, list()
        return reslut

print(Solution().subsets([1,3,4,2]))