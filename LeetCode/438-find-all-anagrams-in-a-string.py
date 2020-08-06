class Solution:
    def find_anagrams(self, s: str, p: str):

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
