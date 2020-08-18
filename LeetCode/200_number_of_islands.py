class Solution:
    direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def num_islands(self, grid):
        visited = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    res += 1
                    self.dfs(grid, i, j, visited)
        return res

    def in_area(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    # 从 grid[start_x][start_y] 开始,进行 floodfill
    # 保证 (start_x,start_y)合法,且 grid[start_x][start_y]是没有被访问过的陆地
    def dfs(self, grid, start_x, start_y, visited):
        visited[start_x][start_y] = True
        for i in range(4):
            new_x = start_x + self.direct[i][0]
            new_y = start_y + self.direct[i][1]
            if self.in_area(grid, new_x, new_y) and not visited[new_x][new_y] and grid[new_x][new_y] == '1':
                self.dfs(grid, new_x, new_y, visited)
