class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """ 
        #-------------------------------------------naive------------------------------------
        #不能解决"aaaabbb", ".*a.*"之类的问题，对于匹配到哪一个字符为止还需改进
        # i = j = 0
        # flag = False
        # while i < len(s) and j < len(p):
        #     if j != len(p)-1:
        #         if p[j+1] != '*':
        #             if s[i] == p[j] or p[j] == '.':
        #                 i += 1
        #                 j += 1
        #                 continue
        #             else:
        #                 break
        #         else:
        #             while (s[i] == p[j] or p[j] == '.') and i < len(s):
        #                 i += 1
        #                 if i == len(s):
        #                     break
        #             j += 2
        #     else:
        #         if p[j] == '*':
        #             continue
        #         else:
        #             if s[i] == p[j] or p[j] == '.':
        #                 i += 1
        #                 j += 1
        #                 continue
        #             else:
        #                 break
        # if i == len(s) and j == len(p):
        #     flag = True
        # return flag
        #-------------------------------动态规划----------------------------------------------
        #重要的是划分子问题已经找好递推式，动态规划有一种传递性

        m = len(s)
        n = len(p)
        d = [[] for i in range(m+1)]
        for i in range(m+1):
            d[i].extend([False] * (n+1))
            
        d[0][0] = True
        #初始化状态数组
        for i in range(1, n, 2):
            if p[i] == '*':
                d[0][i+1] = True
            else:
                break
        for i in range(m):
            for j in range(n):
                if p[j] != '.' and p[j] != '*':
                    d[i+1][j+1] = d[i][j] if s[i] == p[j] else False

                elif p[j] == '.':
                    d[i+1][j+1] = d[i][j]

                else:
                    if d[i+1][j-1]:
                        d[i+1][j+1] = True
                    elif s[i] == p[j-1] or p[j-1] == '.':
                        d[i+1][j+1] = d[i][j+1]

                # elif p[j] == '*' and p[j-1] != '.':
                #     d[i+1][j+1] = d[i+1][j-1] or d[i][j-1] if s[i] == p[j-1] else d[i+1][j-1]

                # else:
                #     if j == 1:
                #         d[i+1][j+1] = True
                #         continue
                #     d[i+1][j+1] = d[i+1][j-1] or d[i][j-1] if (s[i] == p[j-2] or p[j-2] == '.') else d[i][j+1]

        return d


        





        

s = Solution()
print(s.isMatch("aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*"))
#print(s.isMatch("abcb", "a*a.*"))
