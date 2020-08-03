class Solution:
    def remove_element(self, nums, val):
        # 由于遇到目标元素会直接删除改元素,因此采用倒序遍历
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)
        # 方法二:将目标元素直接移到末尾
        # k = 0  # [0...k)表示非 0 元素
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[i], nums[k] = nums[k], nums[i]
        #         k += 1
        # return k

