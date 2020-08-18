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
        for i in range(start, n + 1):
            c.append(i)
            self.generate_combination(n, k, i + 1, c, res)
            c.pop()