class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row, col, box = set(), set(), set()

        for i in board:
            for j in i:
                if j != '.':
                    if j in row:return False
                    row.add(j)
            row = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in col:return False
                    col.add(board[i][j])
                col = set()

        for si in range(0, 9, 3):
            for sj in range(0, 9, 3):
                for i in range(3):
                    for j in range(3):
                        if board

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))