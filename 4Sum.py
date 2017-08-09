class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        l, i, rm = [], 0, []
        while i < len(nums) - 3:
            n = i + 1
            while n < len(nums) - 2:
                
                ln = nums[n]
                start, end = n+1, len(nums)-1
                t = nums[i] + nums[n] + nums[start] + nums[end]
                while start < end:
                    if t < target:
                        start += 1
                    elif t > target:
                        end -= 1
                    else:
                        tmp = [nums[i], nums[n], nums[start], nums[end]]
                        if rm != tmp:
                            l.append(tmp)
                        rm = tmp
                        start += 1
                        end -= 1
                    t = nums[i] + nums[n] + nums[start] + nums[end]
                while nums[n] == nums[n+1] and n < len(nums) - 2:
                    n += 1
                n += 1
            
            while nums[i] == nums[i+1] and i < len(nums) - 3:
                i += 1
            i += 1
        return l

            


s = Solution()
print(s.fourSum([0, 0, 0, 0], 0))