class Solution(object):
    def nextPermutation(self, nums, up_f = True):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # if n == 0 or (n == 1 and up_f):return
        # if n == 1 or n == 2:
        # 	nums = nums[::-1]
        # 	if up_f:
        # 		return nums
        # 	else:
        # 		return nums
        # for i in range(n - 1, 0, -1):
        # 	if nums[i] > nums[i-1]:
        # 		j = n-1
        # 		while j >= i:
        # 			if nums[j] > nums[i-1]:
        # 				nums[j], nums[i-1] = nums[i-1], nums[j]
        # 				break		
        # 			else:
        # 				j -= 1
        # 		nums[:i].extend(self.nextPermutation(nums[i:], False))
        # 		break
        # 	if i == 1: nums = nums[::-1]
        # if up_f:
        # 		return nums
        # else:
        #     return nums
        #这个题目确实比较简单。。是我之前想复杂了，，没有想到交换顺序之后的后一半已经是有序的了。。
        #比如排列是(2,3,6,5,4,1)，求下一个排列的基本步骤是这样：
        # 1) 先从后往前找到第一个不是依次增长的数，记录下位置p。比如例子中的3，对应的位置是1;
        # 2) 接下来分两种情况：
        #     (1) 如果上面的数字都是依次增长的，那么说明这是最后一个排列，下一个就是第一个，其实把所有数字反转过来即可(比如(6,5,4,3,2,1)下一个是(1,2,3,4,5,6));
        #     (2) 否则，如果p存在，从p开始往后找，找到下一个数就比p对应的数小的数字，然后两个调换位置，
        #           比如例子中的4。调换位置后得到(2,4,6,5,3,1)。最后把p之后的所有数字倒序，比如例子中得到(2,4,1,3,5,6), 这个即是要求的下一个排列。
        # 以上方法中，最坏情况需要扫描数组三次，所以时间复杂度是O(3*n)=O(n)，空间复杂度是O(1)。
        n = len(nums)

        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i-1]:
                j = n-1
                while j >= i:
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        self.reverse(nums, i, n-1)
                        return 
                    else:
                        j -= 1
                
            if i == 1: self.reverse(nums, 0, n-1)
        return

    def reverse(self, nums, s, e):
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1





s = Solution()
print(s.nextPermutation([7, 9, 8, 3]))