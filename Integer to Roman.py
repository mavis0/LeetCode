class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # roman = ''
        # d = {0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX',\
        #  10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L',60:'LX', 70:'LXX',80:'LXXX', 90:'XC',\
        #   100:'C',200:'CC', 300:'CCC', 400:'CD', 500:'D',600:'DC', 700:'DCC', 800:'DCCC', 900:'CM',\
        #    1000:'M', 2000:'MM', 3000:'MMM'}
        #
        # for i in range(3, -1, -1):
        # 	tmp = num // 10 ** i * 10 ** i
        # 	roman += d[tmp]
        # 	num %= 10 ** i
        #
        # return roman
        def bitToRoman(n, I, V, X):
            if not n:return ''
            d  = {4: I + V, 5: V, 9: I + X}
            if n < 4:
                return n * I
            elif n in d:
                return d[n]
            return V + (n-5) * I
        num = str(num)
        roman, l = list(), len(num)
        d = {4: ('M', '', ''), 3: ('C', 'D', 'M'), 2: ('X', 'L', 'C'), 1: ('I', 'V', 'X')}
        for i in range(l, 0, -1):
            roman.append(bitToRoman(int(num[l-i]), d[i][0], d[i][1], d[i][2]))
        return ''.join(roman)

s = Solution()
print(s.intToRoman(10))