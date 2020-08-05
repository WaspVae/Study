class Solution:
    # 使用二分查找
    # def two_sum(self, nums, target):
    #     for i in range(len(nums)):
    #         other_num = target - nums[i]
    #         other_num_index = self.binary_search(nums, other_num, i + 1, len(nums) - 1)
    #         if other_num_index != -1:
    #             return i + 1, other_num_index + 1
    #
    # def binary_search(self, arr, target, l_index, r_index):
    #     l = l_index
    #     r = r_index
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if arr[mid] == target:
    #             return mid
    #         elif arr[mid] > target:
    #             r = mid - 1
    #         else:
    #             l = mid + 1
    #     return -1
    # 对撞指针
    def two_sum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return i + 1, j + 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1


test = Solution()
nums = [2, 7, 11, 15]
print(test.two_sum(nums, 26))
