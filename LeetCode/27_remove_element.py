class Solution:
    def remove_element(self, nums, val):
        k = 0  # nums 中,[0...k)的元素中不包含 val 元素
        for i in range(len(nums)):
            if nums[i] != val:
                if i != k:
                    nums[i], nums[k] = nums[k], nums[i]
                    k += 1
                else:
                    k += 1
        del nums[k:]

