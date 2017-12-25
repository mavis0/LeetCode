class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag,l  = 0, [1]
        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + 1 + flag if i == len(digits)-1 else digits[i] + flag
            if digits[i] > 9:
                flag = 1
                digits[i] %= 10
            else:
                flag = 0
        l.extend(digits)
        return l if flag == 1 else digits

s = Solution()
print(s.plusOne([9, 9, 9]))