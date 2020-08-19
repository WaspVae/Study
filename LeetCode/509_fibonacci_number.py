class Solution:
    def fib(self, N: int) -> int:
        # 记忆化搜索,自上而下解决问题
        # memo = [-1] * (N + 1)
        #
        # def generate_num(n):
        #     if n == 0:
        #         return 0
        #     if n == 1:
        #         return 1
        #     # 减枝,去掉重复计算
        #     if memo[n] == -1:
        #         memo[n] = generate_num(n - 1) + generate_num(n - 2)
        #     return memo[n]
        #
        # return generate_num(N)
        # 自下而上解决问题(动态规划)
        memo = [-1] * (N + 1)
        memo[0] = 0
        if N == 0:
            return 0
        memo[1] = 1
        for i in range(2, N + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[N]
