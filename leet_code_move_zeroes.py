class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        none_zeroes_list = list(filter(lambda x: x != 0, nums))
        for i in range(len(none_zeroes_list)):
            nums[i] = none_zeroes_list[i]
        for i in range(len(none_zeroes_list), len(nums)):
            nums[i] = 0
