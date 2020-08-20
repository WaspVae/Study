class Solution:

    def length_of_LIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        # memo[i] 表示以 nums[i] 结尾的最长上升子序列的长度
        memo = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[i], 1 + memo[j])
        return max(memo)

