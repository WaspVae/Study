class Solution:
    def restoreIpAddresses(self, s: str):
        n = len(s)
        res = []
        if n < 4 or n > 12:
            return res

        # 回溯从Start开始的子串
        def dfs(s, index, sub):
            # Condition1:满四段，且用光所有字符
            if len(sub) == 4 and index == n:
                res.append('.'.join(sub))
                return
            # Condition2：满四段，但没用光所有字符
            if len(sub) == 4 and index < n:
                return
            # 三种长度的选择
            for i in range(3):
                # 字符不存在，超出边界了
                if index >= n:
                    return
                # 长度超过1的子串不能是“0”开头
                if len(s[index: index + i + 1]) > 1 and s[index] == '0':
                    return
                # 不能超过255
                if i == 2 and int(s[index: index + 3]) > 255:
                    return
                sub.append(s[index: index + i + 1])
                dfs(s, index + i + 1, sub)
                sub.pop()

        dfs(s, 0, [])
        return res
