class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        # 还可以使用 256 个 ascii 值统计每个字符出现的频率来判断是否出现重复字符
        occ = set()
        l, r = 0, -1  # s[l..r]是滑动窗口
        res = 0
        while l < len(s):
            if r < len(s) - 1 and s[r + 1] not in occ:
                r += 1
                occ.add(s[r])
            else:
                occ.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
        return res
