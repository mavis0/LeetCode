#include <vector>
using namespace std;
class Solution {
public:
	void solve(vector<vector<char>>& board) {
		if (board.empty()) return;
		for (int i = 0; i < board.size(); i++) if (board[i][0] == 'O') DFS(i, 0, board);
		for (int i = 0; i < board.size(); i++) if (board[i][board[0].size()-1] == 'O') DFS(i, board[0].size()-1, board);
		for (int j = 0; j < board[0].size(); j++) if (board[0][j] == 'O') DFS(0, j, board);
		for (int j = 0; j < board[0].size(); j++) if (board[board.size()-1][j] == 'O') DFS(board.size()-1, j, board);

		for (int i = 0; i < board.size(); i++)
			for (int j = 0; j < board[0].size(); j++) {
				if (board[i][j] == 'O')
					board[i][j] = 'X';
				else if (board[i][j] == '&')
					board[i][j] = 'O';
			}
	}
	void DFS(int i, int j, vector<vector<char>>& board) {
		board[i][j] = '&';
		if (i != 0 && board[i-1][j] == 'O') DFS(i - 1, j, board);
		if (i != board.size()-1 && board[i+1][j] == 'O') DFS(i + 1, j, board);
		if (j != 0 && board[i][j-1] == 'O') DFS(i, j - 1, board);
		if (j != board[0].size()-1 && board[i][j+1] == 'O') DFS(i, j + 1, board);
	}
};

int main() {
	cout << Solution().solve(vector<vector<char>> ) << endl;
	return 0;
}