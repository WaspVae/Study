class Solution:

    def combine(self, n, k):
        res = []
        if n <= 0 or n < k or k <= 0:
            return res
        self.generate_combination(n, k, 1, [], res)
        return res

    def generate_combination(self, n, k, start, c, res):
        # 当前已找到的组合存储在 c 中,需要从 start 开始搜索新的元素
        if len(c) == k:
            res.append(c[:])
            return
        # for i in range(start, n + 1):
        # 进行减枝优化
        # 组合 c 中还有 k-len(c) 个空位,所以 [i...n] 中至少要有 k - len(c) 个元素
        # i 最多为 n - (k - len(c)) + 1
        for i in range(start, n - (k - len(c)) + 2):
            c.append(i)
            self.generate_combination(n, k, i + 1, c, res)
            c.pop()