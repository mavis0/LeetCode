class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return len(pattern) == len(str.split()) and len(set(zip(list(pattern), str.split()))) == len(set(pattern)) == len(set(str.split()))
