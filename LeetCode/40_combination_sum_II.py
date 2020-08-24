class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        n = len(candidates)
        res = []
        if n == 0 or sum(candidates) < target:
            return res

        # def generate_conbination(candidates, target, c):
        #     if sum(c) > target:
        #         return
        #     if sum(c) == target:
        #         res.append(c[:])
        #         return
        #     for i in range(len(candidates)):
        #         if candidates[i] > target:
        #             continue
        #         if i > 0 and candidates[i] == candidates[i - 1]:
        #             continue
        #         c.append(candidates[i])
        #         generate_conbination(candidates[i + 1:], target, c)
        #         c.pop()
        #
        # generate_conbination(candidates, target, [])
        used = [False] * n

        def generate_conbination(candidates, target, start, c):
            if sum(c) > target:
                return
            if sum(c) == target:
                res.append(c[:])
                return
            for i in range(start, n):
                if not used[i]:
                    if candidates[i] > target:
                        continue
                    if i > 0 and candidates[i] == candidates[i - 1] and not used[i - 1]:
                        continue
                    used[i] = True
                    c.append(candidates[i])
                    generate_conbination(candidates, target, i + 1, c)
                    c.pop()
                    used[i] = False

        generate_conbination(candidates, target, 0, [])
        return res
