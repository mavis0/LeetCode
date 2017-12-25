class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = list()
        maxlen = tmplen = 0
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if stack[-1] == '(':
                    tmplen += 2
                    maxlen = max(tmplen, maxlen)
                    stack.pop()
                else:
                    tmplen = 0
        return maxlen

    # def isPar(self, s):
    #     stack = list()
    #     for i in s:
    #         if i == '(':
    #             stcak.append('(')
    #         else:
    #             if stack:
    #                 stack.pop()
    #             else:
    #                 return 1
    #     if stack:
    #         return -1 
    #     else:
    #         return 0


        
s = Solution()
print(s.longestValidParentheses("()(()"))