class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {')' : '(', ']' : '[', '}' : '{'}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0 or d[i] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        if stack == []:
            return True
        else:
            return False

s = Solution()
print(s.isValid(']'))