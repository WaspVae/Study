class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0  # nums 中,[0...k)的元素均为非 0 元素
        # 遍历到第 i 个元素后,保证[0...i]中所有非 0 元素都按序排列在[0...k)中
        for i in range(len(nums)):
            if nums[i]:
                if i != k:
                    nums[k], nums[i] = nums[i], nums[k]
                    k += 1
                else:
                    k += 1
