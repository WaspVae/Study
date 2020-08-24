class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return board
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def dfs(board, x, y):
            visited[x][y] = True
            for i in range(4):
                new_x = x + direct[i][0]
                new_y = y + direct[i][1]
                if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] and board[new_x][new_y] == 'O':
                    dfs(board, new_x, new_y)

        for i in range(n):
            if board[0][i] == 'O':
                dfs(board, 0, i)
            if board[m - 1][i] == 'O':
                dfs(board, m - 1, i)
        for i in range(m):
            if board[i][0] == 'O':
                dfs(board, i, 0)
            if board[i][n - 1] == 'O':
                dfs(board, i, n - 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'
