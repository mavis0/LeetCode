class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        #-------------------------naive-------------------------------------
        #本来以为O(n^2)可以过，没想到还是太慢了，311 / 313 passed，leetcode把最长的
        #测试放在后面啊，这个其实也是网上的思路，其实自己也能想得到，果然O(n^2)过不了
        # ans = []
        # nums.sort()
        # for i in nums:
        #     tmp = nums[0:]
        #     tmp.remove(i)
        #     s, e = 0, len(tmp)-1
        #     while s < e:
        #         if tmp[s] + tmp[e] + i < 0:
        #             s += 1
        #         elif tmp[s] + tmp[e] + i > 0:
        #             e -= 1
        #         else:
        #             if sorted([i, tmp[s], tmp[e]]) not in ans:
        #                 ans.append(sorted([i, tmp[s], tmp[e]]))
        #             s +=1
        #             e -=1
        #-------------------------------------------------------------------------
        #不对，O(n^2)确实是极限了，是后面比较的时候估计算法复杂度太高了吧。
        #是来回倒腾数组的事件复杂度太高，两边寻找的时候应该只找后面的就可以了不需要前面的
        #这只是用“先固定一个，再两头找”的方法，用hash虽然复杂度一样，但应该会更快，等4Sum的时候再细写吧
        # nums.sort()
        # last = 'a'
        # ta = []
        # while len(nums) > 2:
        #     i = nums.pop()
        #     if last == i:
        #         continue
        #     last = i
        #     s, e = 0, len(nums)-1
        #     while s < e:
        #         if nums[s] + nums[e] + i < 0:
        #             s += 1
        #         elif nums[s] + nums[e] + i > 0:
        #             e -= 1
        #         else:
        #             if [i, nums[s], nums[e]] != ta:
        #                 ans.append([i, nums[s], nums[e]])
        #                 ta = [i, nums[s], nums[e]]
        #             s +=1
        #             e -=1
        #
        # print(len(ans))
        # return ans
        if not nums:return []
        ans = list()
        nums.sort()
        for k, v in enumerate(nums[:-2]):
            if v > 0: break
            if k > 0 and nums[k] == nums[k-1]: continue
            l, r = k+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] + v > 0:
                    r -= 1
                elif nums[l] + nums[r] + v < 0:
                    l += 1
                else:
                    ans.append([v, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l , r = l + 1, r - 1
        return ans

s = Solution()
print(s.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
# print(s.threeSum([-1, 0, 1, 2, -1, -4]))