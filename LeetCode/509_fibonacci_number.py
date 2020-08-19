class Solution:
    def fib(self, N: int) -> int:
        memo = [-1] * (N + 1)

        def generate_num(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            # 减枝,去掉重复计算
            if memo[n] == -1:
                memo[n] = generate_num(n - 1) + generate_num(n - 2)
            return memo[n]

        return generate_num(N)
