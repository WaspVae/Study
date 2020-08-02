class Solution:
    def remove_duplicates(self, nums):
        k = 0  # nums 中,[0...k]的元素均为非重复元素
        for i in range(len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        del nums[k + 1:]
        return len(nums)
