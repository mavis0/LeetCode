class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
        	return 0
        d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,\
        				 '7': 7, '8': 8, '9': 9}
        s = str.strip()[::-1]
        n = 0
        k = 0

        for i in range(len(s)-1):
        	if s[i] in d:
        		n += d[s[i]] * 10 ** i
        	else:
        		n = 0
        		k = i + 1
        		
        
        if s[-1] in d:
        		n += d[s[-1]] * 10 ** (len(s)-1)
        elif s[-1] == '-':
        	n = -n
        elif s[-1] == '+':
        	pass
        else:
        	n = 0

        n = int(n / 10 ** k)

        if -2147483647 <= n <= 2147483647 :
        	return n
        elif n > 2147483647:
        	return 2147483647
        else:
        	return -2147483647



s = Solution()
print(s.myAtoi("8798"))