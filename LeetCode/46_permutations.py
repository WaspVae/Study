class Solution:

    def permute(self, nums):
        res = []
        if not len(nums):
            return res
        self.generate_permutation(res, nums, 0, [])
        return res

    def generate_permutation(self, res, nums, index, p):
        # p中保存了一个有 index 个元素的排列
        # 向这个排列的末尾添加第 index+1 元素,获得一个 index+1 个元素的排列
        if index == len(nums):
            res.append(p[:])
            return
        for item in nums:
            if item not in p:
                p.append(item)
                self.generate_permutation(res, nums, index + 1, p)
                # 在回溯的过程中,定义的变量的状态也要回溯,即保持定义时的状态
                p.pop()

