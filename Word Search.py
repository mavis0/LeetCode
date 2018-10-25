import copy
class Solution:
    # def exist(self, board, word):
    #     """
    #     :type board: List[List[str]]
    #     :type word: str
    #     :rtype: bool
    #     """
    #     # def find_exist(i, j, k, v):
    #     #     if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]): return False
    #     #     if k == len(word) - 1:
    #     #         return True if board[i][j] == word[k] and v[i][j] else False
    #     #     if board[i][j] == word[k] and v[i][j]:
    #     #         v[i][j] = False
    #     #         return find_exist(i-1, j, k+1, copy.deepcopy(v)) or \
    #     #             find_exist(i, j+1, k+1, copy.deepcopy(v)) or \
    #     #             find_exist(i+1, j, k+1, copy.deepcopy(v)) or \
    #     #             find_exist(i, j-1, k+1, copy.deepcopy(v))
    #     #     return False
    #     #
    #     # l1, l2, ans = len(board), len(board[0]), False
    #     # visited = [[True] * l2 for i in range(l1)]
    #     # for i in range(l1):
    #     #     for j in range(l2):
    #     #         if find_exist(i, j, 0, copy.deepcopy(visited)):
    #     #             return True
    #     # return ans
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0:  # all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
                or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
        board[i][j] = tmp
        return res


s = Solution()
print(s.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))
