class Solution:
    def rob(self, nums):
        # memo = [-1] * len(nums)
        #
        # # 考虑抢劫 nums[index...len(nums))这个范围内的所有房子
        # def try_rob(nums, index):
        #     res = 0
        #     if index >= len(nums):
        #         return 0
        #     if memo[index] != -1:
        #         return memo[index]
        #     for i in range(index, len(nums)):
        #         res = max(res, nums[i] + try_rob(nums, i + 2))
        #     memo[index] = res
        #     return res
        #
        # return try_rob(nums, 0)
        n = len(nums)
        if n == 0:
            return 0
        # memo[i] 表示考虑抢劫 nums[i...n-1]这个范围内的所有房子所能获得的最大收益
        memo = [-1] * n
        # memo[n-1] = nums[n-1]
        # for i in range(n-2, -1, -1):
        #     for j in range(i, len(nums)):
        #         memo[i] = max(memo[i], nums[j] + (memo[j + 2] if j + 2 < n else 0))
        # return memo[0]
        # memo[i] 表示考虑抢劫 nums[0...i]这个范围内的所有房子所能获得的最大收益
        # memo[0] = nums[0]
        # for i in range(1, n):
        #     for j in range(i, -1, -1):
        #         memo[i] = max(memo[i], nums[j] + (memo[j - 2] if j - 2 >= 0 else 0))
        # return memo[n - 1]
        # 状态转移方程  dp[i]=max(dp[i−2]+nums[i],dp[i−1])
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        for i in range(2, n):
            memo[i] = max(memo[i-2] + nums[i], memo[i-1])
        return memo[n-1]

