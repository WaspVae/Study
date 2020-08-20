# 01背包问题
# F(n, C) 考虑将 n 个物品放入容量为 C 的背包,使其价值最大
# F(i, c) = max(F(i-1, c), v(i) + F(i-1, c-w(i))

class Solution:
    def knapsack01(self, w, v, C):
        # assert len(w) == len(v)
        # n = len(w)
        # if n == 0:
        #     return 0
        # memo = [[-1] * (C + 1)] * n
        #
        # # 用[0...index]的物品填充容积为 c 的背包的最大价值
        # def best_value(w, v, index, c):
        #     if index < 0 or c <= 0:
        #         return 0
        #     if memo[index][c] != -1:
        #         return memo[index][c]
        #     res = best_value(w, v, index - 1, c)
        #     if c >= w[index]:
        #         res = max(res, v[index] + best_value(w, v, index - 1, c - w[index]))
        #     memo[index][c] = res
        #     return res
        #
        # return best_value(w, v, n - 1, C)
        assert len(w) == len(v)
        n = len(w)
        if n == 0:
            return 0
        memo = [[-1] * (C + 1) for i in range(n)]
        for j in range(C + 1):
            memo[0][j] = v[0] if w[0] <= j else 0
        for i in range(1, n):
            for j in range(C + 1):
                memo[i][j] = memo[i - 1][j]
                if w[i] <= j:
                    memo[i][j] = max(memo[i][j], v[i] + memo[i-1][j - w[i]])
        return memo[-1][-1]


