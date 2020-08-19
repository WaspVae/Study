class Solution:
    def integer_break(self, n: int) -> int:
        # 记忆化搜索
        # memo = [-1] * (n + 1)
        # res = -1
        #
        # def break_interge(n):
        #     nonlocal res
        #     if n == 1:
        #         return 1
        #     if memo[n] != -1:
        #         return memo[n]
        #     for i in range(1, n):
        #         res = max(res, i * (n - i), i * break_interge(n - i))
        #     memo[n] = res
        #     return res
        #
        # return break_integer(n)
        memo = [-1] * (n + 1)
        # memo[i] 表示将数字 i 分割(至少分割成两部分)后的最大乘积
        memo[1] = 1
        for i in range(2, n + 1):
            # 求解 memo[i]
            for j in range(1, i):
                memo[i] = max(memo[i], j * (i - j), j * memo[i - j])
        return memo[n]
