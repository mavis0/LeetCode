class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        l, carry = [0] * (len(num1) + len(num2) + 1), 0
        for i, j in enumerate(num1):
            for k, v in enumerate(num2):
                l[i+k] += (ord(j)-48)*(ord(v)-48)

        for i in range(len(l)):
            l[i], carry = (l[i] + carry) % 10, (l[i] + carry) // 10

        ans = ''.join([str(j) for j in l[:i]]).rstrip('0')
        return ans[::-1] if ans else 0

s = Solution()
print(s.multiply('2', '3'))
