class Solution:
    def find_content_children(self, g, s):
        g.sort()
        s.sort()
        gi = len(g) - 1
        si = len(s) - 1
        res = 0
        while gi >= 0 and si >= 0:
            if s[si] >= g[gi]:
                res += 1
                si -= 1
                gi -= 1
            else:
                gi -= 1

        return res
