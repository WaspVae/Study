class Solution:
    # 两种解法均可适用于通解
    def remove_duplicates(self, nums):
        k = 0  # nums 中,[0...k)的元素均为满足要求的元素
        for item in nums:
            # 一直维护 k 的值,使[0...k)的元素均为满足要求的元素
            if k < 2 or item != nums[k - 2]:
                nums[k] = item
                k += 1
        return k

        # sp是慢指针,fp 是快指针
        # 快指针：遍历整个数组；
        # 慢指针：记录可以覆写数据的位置；
        # 题目中规定每个元素最多出现两次，因此，应检查快指针指向的元素和慢指针指针所指向单元的前一个元素是否相等。
        # 相等则不更新慢指针，只更新快指针；不相等时，先将慢指针后移一位，再将快指针指向的元素覆写入慢指针指向的单元，最后更新快指针
        # sp = 1
        # for fp in range(2, len(nums)):
        #     if nums[sp - 1] != nums[fp]:
        #         sp += 1
        #         nums[sp] = nums[fp]
        # return sp + 1
