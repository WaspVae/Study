class Solution:
    # F(i, C) = F(i-1, C) or F(i-1, C - w[i])
    def can_partition(self, nums) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        n = len(nums)
        C = sum_nums // 2
        # memo[i][c] 表示使用索引为 [0...i] 的这些元素,能否完全填充容量为 c 的背包
        # memo = [[-1] * (sum_nums // 2 + 1) for i in range(len(nums))]

        # 使用 nums[0...index] 是否可以完全填充一个容量为 sum 的背包
        # def partition(nums, index, sums):
        #     if sums == 0:
        #         return True
        #     if index < 0 or sums < 0:
        #         return False
        #     if memo[index][sums] != -1:
        #         return memo[index][sums]
        #     memo[index][sums] = partition(nums, index - 1, sums) or partition(nums, index - 1, sums - nums[index])
        #     return memo[index][sums]
        #
        # return partition(nums, len(nums) - 1, sum_nums // 2)
        memo = [False] * (C + 1)
        for i in range(C + 1):
            memo[i] = (nums[0] == i)
        for i in range(1, n):
            for j in range(C, nums[i] - 1, -1):
                memo[j] = memo[j] or memo[j - nums[i]]
        return memo[C]


test = Solution()
nums = [1, 2, 3, 5]
print(test.can_partition(nums))
