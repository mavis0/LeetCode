class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l, stack = path.split('/'), list()
        for i in l:
            if not i or i == '.': continue
            if i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)

print(Solution().simplifyPath("/../"))

