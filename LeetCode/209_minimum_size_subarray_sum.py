class Solution:
    def min_sub_array_len(self, s, nums):
        l, r = 0, -1  # nums[l...r]是滑动窗口
        sum = 0
        res = len(nums) + 1
        while l < len(nums):
            if r < len(nums) - 1 and sum < s:
                r += 1
                sum += nums[r]
            else:
                sum -= nums[l]
                l += 1
            if sum >= s:
                res = min(res, r - l + 1)
        if res == len(nums) + 1:
            return 0
        return res
