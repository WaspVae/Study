class Solution:
    direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def exist(self, board, word):
        visited = [[False for i in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search_word(board, word, 0, i, j, visited):
                    return True
        return False

    def in_area(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

    # 从 board[start_x][start_y] 开始,寻找 [index...len(word))
    def search_word(self, board, word, index, start_x, start_y, visited):
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]
        if board[start_x][start_y] == word[index]:
            visited[start_x][start_y] = True
            for i in range(4):
                new_x = start_x + self.direct[i][0]
                new_y = start_y + self.direct[i][1]
                if self.in_area(board, new_x, new_y) and not visited[new_x][new_y]:
                    if self.search_word(board, word, index + 1, new_x, new_y, visited):
                        return True
            visited[start_x][start_y] = False
        return False


test = Solution()
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
print(test.exist(board, 'ABCCED'))