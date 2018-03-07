class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = [True] * n
        for i in range(2, n):
            j = 2
            if b[i-1]:
                while i * j < n:
                    b[i * j -1] = False
                    j += 1

        for i, j in enumerate(b):
            if j:print(i+1, end = ' ') 
        print()
        return sum(b)-1
print(Solution().countPrimes(10))