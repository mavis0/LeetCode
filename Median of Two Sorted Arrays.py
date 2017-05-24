class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        
        if (m+n) % 2 == 1:
            return float(self.f(nums1, nums2, (m+n) // 2))
        else:
        	 return (self.f(nums1, nums2, (m+n) // 2) + self.f(nums1, nums2, (m+n)//2-1))/ 2.0
    def f(self, nums1, nums2, index):
        	m = len(nums1)
        	n = len(nums2)
        	flag = i = j = 0
        	while i < m and j < n:
        		if flag != index:
        			if nums1[i] <= nums2[j]:
        				i += 1
        			else:
        				j += 1
        			flag += 1
        		else:
        			break
    
        	if i == m:
        	    return nums2[index-flag+j]
        	if j == n:
        		return nums1[index-flag+i]
        	return min(nums1[i], nums2[j])


s = Solution()

print(s.findMedianSortedArrays([1,2,3, 4, 5,6], [2, 3, 4, 5, 6]))