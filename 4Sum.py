class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #4sum 退化成 3sum，再退化成2sum，整体的复杂度是O(n^3)，在leetcode上的成绩是979 ms，36%
        # nums.sort()
        # l, i, rm = [], 0, []
        # while i < len(nums) - 3:
        #     n = i + 1
        #     while n < len(nums) - 2:
                
        #         ln = nums[n]
        #         start, end = n+1, len(nums)-1
        #         t = nums[i] + nums[n] + nums[start] + nums[end]
        #         while start < end:
        #             if t < target:
        #                 start += 1
        #             elif t > target:
        #                 end -= 1
        #             else:
        #                 tmp = [nums[i], nums[n], nums[start], nums[end]]
        #                 if rm != tmp:
        #                     l.append(tmp)
        #                 rm = tmp
        #                 start += 1
        #                 end -= 1
        #             t = nums[i] + nums[n] + nums[start] + nums[end]
        #         while nums[n] == nums[n+1] and n < len(nums) - 2:
        #             n += 1
        #         n += 1
            
        #     while nums[i] == nums[i+1] and i < len(nums) - 3:
        #         i += 1
        #     i += 1
        # return l
        #尝试一下用hashtable的办法，应该可以将算法复杂度降到O(n^2)，分成两个2sum，然后再进行相加
        #但是去重好像都是用的set， 没有什么更好的办法，可能效果还不如退化成3sum，所以，就没有再往下写
        nums.sort()
        a, d, n = set(), {}, len(nums)
        for i in range(n - 1):
            j = i + 1
            while j < n:
                s = nums[i] + nums[j]
                if s not in d.keys():
                    d[s] = [[i, j]]
                else:
                    d[s].append([i, j])
                j += 1

        for i in range(n-3):
            for j in range(i+1, n-2):
                r = target - nums[i] - nums[j]
                if r in d.keys():
                    for k in d[r]:
                        if k[0] > j:
                            a.add((nums[i],nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in a]

        # for i in d.keys():
        #     if target - i in d.keys():
        #         for m in d[i]:
        #             for n in d[target-i]:
        #                 if m[1] < n[0]:
        #                     tmp = m.copy()
        #                     tmp.extend(n)
        #                     a.append(tmp)
        


s = Solution()
print(s.fourSum([-1,2,2,-5,0,-1,4], 3))