class Solution:
    def find_anagrams(self, s: str, p: str):
        # index_list = []  # 记录起始索引
        # l, r = 0, len(p) - 1  # s[l..r]是固定滑动窗口,长度等于 p 字符串的长度
        # freq_p = dict((i, p.count(i)) for i in p)  # 记录目标字符串中每个字母出现的频率
        # while r < len(s):
        #     # 放入循环体内在最差情况下会是算法退化到 O(n^2)
        #     freq_s = dict((i, s[l:r + 1].count(i)) for i in p)
        #     if freq_p == freq_s:
        #         index_list.append(l)
        #     l += 1
        #     r += 1
        # return index_list

        res = []  # 记录起始索引
        l = 0
        freq_s = [0] * 26  # 记录 26 个字母在 [l...r] 出现的频率
        freq_p = [0] * 26  # 记录 26 个字母在目标字符串 p 中出现的频率
        for i in p:
            freq_p[ord(i) - ord('a')] += 1
        for r in range(len(s)):
            freq_s[ord(s[r]) - ord('a')] += 1
            if r < len(p) - 1:
                continue
            if freq_p == freq_s:
                res.append(l)
            freq_s[ord(s[l]) - ord('a')] -= 1
            l += 1

        return res
