class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        head = '1'
        for i in range(n-1):
        	head = self.Say(head)
        return head

    def Say(self, s):
    	s += '#'
    	count, next_s = 1, ''
    	for i in range(len(s)-1):
    		if s[i] == s[i+1]:
    			count += 1
    		else:
    			next_s += str(count) + s[i]
    			count = 1
    	return next_s


s = Solution()
print(s.countAndSay(5))