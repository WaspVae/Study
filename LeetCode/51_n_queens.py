class Solution:
    def solve_q_queens(self, n):
        # col,dia1,dia2 分别记录列,对角线能否摆放皇后
        col = [False] * n
        # n*n 棋盘有 2*n - 1 条对角线
        # 正对角线上点的和相同,值为[0...2*(n-1)]
        # 反对角线上点的差相同,值为[1-n...n-1]
        dia1 = [False] * (2 * n - 1)
        dia2 = [False] * (2 * n - 1)
        res = []

        # 摆放第 index 行的皇后位置
        def put_queen(n, index, row):
            if index == n:
                res.append(self.generate_board(n, row[:]))
                return
            for i in range(n):
                # 尝试将 index 行的皇后摆放在第 i 列
                if not col[i] and not dia1[index + i] and not dia2[index - i + n - 1]:
                    col[i] = True
                    dia1[index + i] = True
                    dia2[index - i + n - 1] = True
                    row.append(i)
                    put_queen(n, index + 1, row)
                    col[i] = False
                    dia1[index + i] = False
                    dia2[index - i + n - 1] = False
                    row.pop()

        put_queen(n, 0, [])
        return res

    def generate_board(self, n, row):
        return ["." * i + "Q" + "." * (n - i - 1) for i in row]
