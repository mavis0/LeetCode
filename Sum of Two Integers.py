# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 12:18:07 2018

@author: liaojing
"""

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            a, carry =  a ^ b, a & b
            b = carry << 1
        return a
print(Solution().getSum(-1, 1))