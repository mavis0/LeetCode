class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        margin = 10000000
        ans = 'a'
        for i in range(len(nums)-2):
            s, e = i+1, len(nums)-1
            while s < e:
                t = nums[s] + nums[e] + nums[i]
                tmp = t-target
                if abs(tmp) < margin:
                    margin = abs(tmp)
                    ans = t 
                if tmp < 0:
                    s += 1
                elif tmp > 0:
                    e -= 1
                else:
                    return t

        return ans


s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4,-1, 2, 1, -4,-1, 2, 1, -4], 1))