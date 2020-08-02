class Solution:
    def remove_element(self, nums, val):
        # 由于遇到目标元素会直接删除改元素,因此采用倒序遍历
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)

