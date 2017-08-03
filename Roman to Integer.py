class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        rd = {'': 0, 'DCCC': 800, 'CC': 200, 'VIII': 8, 'VI': 6, 'LXXX': 80, 'CCC': 300, \
        'C': 100, 'LXX': 70, 'D': 500, 'XX': 20, 'III': 3, 'X': 10, 'DC': 600, 'CD': 400, \
        'L': 50, 'MMM': 3000, 'II': 2, 'IV': 4, 'CM': 900, 'V': 5, 'IX': 9, 'XXX': 30, \
        'VII': 7, 'XL': 40, 'DCC': 700, 'LX': 60, 'M': 1000, 'I': 1, 'MM': 2000, 'XC': 90}
        for j in range(4):
            
            if len(s) == 1:
                num += rd[s]
                break
            
            for i in range(len(s)+1):
                if i == len(s) or (s[0:i] in rd and s[0:i+1] not in rd):
                    num += rd[s[0:i]]
                    s = s[i:]
                    break
            
        return num





s = Solution()
print(s.romanToInt("MMMCMXCV"))