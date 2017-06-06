class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
         end =  prt = length = 0
         val = []

         d = {}

         for i in range(len(s)):
             if s[i] in d:
                 start = d[s[i]]
                 if start < prt:
                     continue
                 end = i
                 if end - start > length:
                     length = end - start
                     val = [start, end]
                 prt = end
             d[s[i]] = i
        
         return s[val[0]: val[1] + 1]
         pass

         start = 0
         val = [0, 0]
         for i in range(len(s)):
             for j in range(i+1, len(s)):
                 if self.jud(s[i: j+1]):
                     if (j - i) > val[1] - val[0]:
                         val[1] = j
                         val[0] = i

         return s[val[0]: val[1] + 1]

    

         if len(s) == 0:
             return ''
         if len(s) == 1:
             return s
         if len(s) == 2:
             return s if s[1] == s[0]
         l = s[0:2]
         i = maxlen = 0
         while i < len(s):
             if s[i] == l[len(l)-2]:
                 tmp = 1
                 for j in s[i:]:
                     if j == l[len(l)-2-tmp] and len(l)-2-tmp >= 0:
                         tmp += 1
                     else:
                         break
         if len(s) == 1 or len(num) == 1:
             return s

         d = {}
         maxlen = 0
         mas = ''
         for i in range(len(s)):
             if s[i] in d:                
                 for j in range(len(d[s[i]])).__reversed__():
                     if self.jud(s[d[s[i]][j]: i+1]):
                         if i - d[s[i]][j] + 1 >= maxlen:
                             mas = s[d[s[i]][j]: i+1]
                             maxlen = i - d[s[i]][j] + 1
                 d[s[i]].append(i)
             else:
                 d[s[i]] = [i]
            
         if mas == '':
             return s[0]

         return mas

     def jud(self, s):
         for i in range(len(s) // 2):
             if s[i] != s[-i-1]:
                 return 0
         return 1
    都是没用的！~
        if s == '':
            return ''
        if len(s) == 1 or len(set(s)) == 1:
            return s[0]

        d = dict()
        longeststr = ''
        i = 0
        while i < len(s):
            if s[i] not in d:
                d[s[i]] = [i]
                i += 1
            else:
                d[s[i]].append(i)
                if i - d[s[i]][-2] > 2:
                    continue
                elif i - d[s[i]][-2] == 2:
                    j = 0
                    while i - 1 + j < len(s) and i - 1 - j >= 0:
                        if s[i - 1 + j] != s[i - 1 - j]:
                            longeststr = s[i-j: i+j+1] if 2*j-1 > len(longeststr) else longeststr
                            break
                        j += 1
                    i += 1
                else:
                    j = 1
                    while s[i+j] == s[i] and i+j < len(s)-1:
                        j += 1
                    longeststr = s[i-1: i+j] if j+1 > len(longeststr) else longeststr
                    k = 1
                    while i-1-k >=0 and i+j-1+k < len(s):
                        if s[i-1-k] != s[i+j-1+k]:
                            longeststr = s[i-k: i+j-1+k] if 2*k+j-1 > len(longeststr) else longeststr
                            break
                        k += 1
                    i += j
        '''
        #---------------------------Manachar算法---------------------------------
        #预处理
        if len(s) < 2:
            return s
        
        new_s = '&' + '#'.join(s) + '&'
        middle = 0
        right_max = 0
        rd = [0] * len(new_s)

        for i in range(len(new_s)):
            if i < right_max:
                j = 2 * middle - i
                if j - rd[j] > 2 * middle - right_max:
                    rd[i] = rd[j]
                    continue
                else:
                    r = right_max - i
            else:
                r = 0
                
            while new_s[i] != '&' and new_s[i+r+1] == new_s[i-r-1] and new_s[i-r-1] != '&' and new_s[i+r+1] != '&':
                r += 1
            rd[i] = r
            middle = i
            right_max = i + r

        print(rd)
        
        max_r= 0
        max_m = 0
        
        for k in range(len(rd)):
            if rd[k] > max_r:
                max_m = k
                max_r = rd[k]
            elif rd[k] == max_r:
                 if len(new_s[k-rd[k]: k-rd[k]+1].replace('#','')) > len(new_s[max_m-max_r: max_m+max_r+1].replace('#','')):
                     max_m = k
                     max_r = rd[k]
        return new_s[max_m-max_r: max_m+max_r+1].replace('#','')





s = Solution()
print(len((s.longestPalindrome('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg'))))
# print(s.jud('abcgba'))

#ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg