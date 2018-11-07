class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def DFS(i, j):
            board[i][j] = '$'
            if i != 0 and board[i-1][j] == 'O':DFS(i-1, j)
            if i != len(board)-1 and board[i+1][j] == 'O':DFS(i+1, j)
            if j != 0 and board[i][j-1] == 'O':DFS(i, j-1)
            if j != len(board[0])-1 and board[i][j+1] == 'O':DFS(i, j+1)
            return
        if not board:return
        for j in range(len(board[0])):
            tmp = [0, len(board)-1]
            for i in tmp:
                if board[i][j] == 'O':DFS(i, j)
        for i in range(len(board)):
            tmp = [0, len(board[0])-1]
            for j in tmp:
                if board[i][j] == 'O':DFS(i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 'X' if board[i][j] == 'O' else 'O' if board[i][j] == '$' else 'X'

board = [
    ["X","X","X","X"],["X","O","O","O"],["X","X","O","X"],["X","O","X","X"]
]
Solution().solve(board)
print(board)
