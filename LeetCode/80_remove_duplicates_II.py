class Solution:
    def remove_duplicates(self, nums):
        k = 0  # nums 中,[0...k]的元素均为满足要求的元素
        for item in nums:
            # 一直维护 k 的值,使[0...k]的元素均为满足要求的元素
            if k < 2 or item != nums[k - 2]:
                nums[k] = item
                k += 1
        return k
