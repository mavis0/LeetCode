class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def partPartition(res, tmp, rest):
            if not rest:
                res.append(tmp.copy())
            for i in range(1, len(rest)+1):
                if rest[:i] == rest[:i][::-1]:
                    tmp.append(rest[:i])
                    partPartition(res, tmp, rest[i:])
                    tmp.pop()
        res = []
        partPartition(res, [], s)
        return res

print(Solution().partition('aab'))


