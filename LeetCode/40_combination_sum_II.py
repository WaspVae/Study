class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        n = len(candidates)
        res = []
        if n == 0 or sum(candidates) < target:
            return res

        def generate_conbination(candidates, target, c):
            if sum(c) > target:
                return
            if sum(c) == target:
                res.append(c[:])
                return
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                c.append(candidates[i])
                generate_conbination(candidates[i + 1:], target, c)
                c.pop()

        generate_conbination(candidates, target, [])
        return res
