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
        memo[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            for j in range(i, len(nums)):
                memo[i] = max(memo[i], nums[j] + (memo[j + 2] if j + 2 < n else 0))
        return max(memo)