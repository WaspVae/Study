class Solution:
    def climbing_stairs(self, N: int) -> int:
        # 记忆化搜索,自上而下解决问题
        memo = [-1] * (N + 1)

        def generate_num(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            # 减枝,去掉重复计算
            if memo[n] == -1:
                memo[n] = generate_num(n - 1) + generate_num(n - 2)
            return memo[n]

        return generate_num(N)
        # 自下而上解决问题(动态规划)
        # memo = [-1] * (N + 1)
        # memo[0] = 1
        # memo[1] = 1
        # for i in range(2, N + 1):
        #     memo[i] = memo[i - 1] + memo[i - 2]
        # return memo[N]
