class Solution:
    # 利用快排partition思想找出元素所在位置
    # 还可以通过维护一个有 k 个元素的小顶堆实现
    def find_kth_largest(self, nums, k: int):
        # 取巧实现
        # return sorted(nums)[-k]
        n = len(nums)
        l = 0
        r = n - 1
        target_index = n - k
        while True:
            p = self.partition(nums, l, r)
            if p == target_index:
                return nums[p]
            elif p < target_index:
                l = p + 1
            else:
                r = p - 1

    def partition(self, nums, l, r):
        from random import randint
        randint_index = randint(l, r)
        nums[randint_index], nums[l] = nums[l], nums[randint_index]
        v = nums[l]
        i = l + 1
        j = r
        while i <= j:
            # while i <= r and nums[i] < v:
            #     i += 1
            # while j >= l + 1 and nums[j] > v:
            #     j -= 1
            # if i > j:
            #     break
            # nums[i], nums[j] = nums[j], nums[i]
            # i += 1
            # j -= 1
            if nums[i] < v:
                i += 1
            elif nums[j] > v:
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        nums[l], nums[j] = nums[j], nums[l]
        return j


test = Solution()
nums = [4, 1, 7, 6, 9, 2]
print(test.find_kth_largest(nums, 3))

