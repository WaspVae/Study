# 使用三路快排思想解决
class Solution:
    def sort_colors(self, nums):
        zero, two, i = -1, len(nums), 0
        while i < two:
            if nums[i] == 0:
                zero += 1
                nums[i], nums[zero] = nums[zero], nums[i]
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            else:
                i += 1
