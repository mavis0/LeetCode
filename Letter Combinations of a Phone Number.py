class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #最后还是用了递归，刚开始想的时候以为不用递归可以做，后来想了好久以为不行，没办法用了递归，
        #后面看了其他人的解法，发现不用递归是可行的，只要每次看成两个字符list的两两组合，保存每次得到
        #的list就好，还是太笨太笨。
        if '' == digits:
            return []
        ans = []
        d = {'0': ' ', '1': '*', '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f']\
            , '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', '0']\
            , '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if len(digits) == 1:
            return d[digits]

        for i in d[digits[0]]:
            for j in self.letterCombinations(digits[1:]):
                ans.append(i + j)

        return ans
            


s = Solution()
print(s.letterCombinations('234'))