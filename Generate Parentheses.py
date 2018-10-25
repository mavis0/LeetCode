class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #====================递归版本，真的是卡特兰数，有了卡特兰数的思路就很好写============
        #真蠢啊自己。。。。。。。。。。
        # 我所了解的卡特兰数有关的问题，大都满足这样一个描述：有一个大问题A，规模为n，要解决这个问题，
        # 可以用分治的思想，首先固定其中某一个元素，将剩下的n-1个元素拆分成两个小问题，
        # 这两个小问题的规模分别是(0,n-1) (1,n-2) (2,n-3) ... (n-1,0)

        if n == 0:
            return ['']
        if n == 1:
            return ['()']

        l = []

        for i in range(0, n):
            for j in self.generateParenthesis(i):
                for k in self.generateParenthesis(n-1-i):
                    l.append(j + '(' + k + ')')

        return l
        # def DFS(l, r, o, res):
        #     print(l, r)
        #     if l > r: return
        #     if l == 0 and r == 0:
        #         res.append(o)
        #     else:
        #         if l > 0:DFS(l-1, r, o+'(', res)
        #         if r > 0:DFS(l, r-1, o+')', res)
        # res = list()
        # DFS(n, n, '', res)
        # return res

s = Solution()
print(s.generateParenthesis(3))