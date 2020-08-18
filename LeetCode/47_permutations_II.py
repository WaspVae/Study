class Solution:

    def permute(self, nums):
        nums.sort()
        res = []
        used = [False] * len(nums)
        if not len(nums):
            return res
        self.generate_permutation(res, used, nums, 0, [])
        return res

    def generate_permutation(self, res, used, nums, index, p):
        # p中保存了一个有 index 个元素的排列
        # 向这个排列的末尾添加第 index+1 元素,获得一个 index+1 个元素的排列
        if index == len(nums):
            res.append(p[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                # 对重复元素进行处理
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                p.append(nums[i])
                used[i] = True
                self.generate_permutation(res, used, nums, index + 1, p)
                # 在回溯的过程中,定义的变量的状态也要回溯,即保持定义时的状态
                p.pop()
                used[i] = False
