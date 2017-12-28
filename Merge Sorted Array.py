class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m != len(nums1):
            nums1.pop()
        while n != len(nums2):
            nums2.pop()
        nums1.extend(nums2)
        nums1.sort()


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

s = Solution()
s.merge(nums1, 3, nums2, len(nums2))
print(nums1)