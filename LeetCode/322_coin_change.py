class Solution:
    def coinChange(self, coins, amount: int) -> int:
        memo = [float('inf')] * (amount + 1)
        memo[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                memo[i] = min(memo[i], 1 + memo[i - coin])
        return memo[amount] if memo[amount] != float('inf') else -1