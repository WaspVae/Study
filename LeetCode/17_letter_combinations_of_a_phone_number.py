class Solution:
    letters_dict = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    res = []

    def letter_combinations(self, digits: str):
        self.res.clear()
        if not len(digits):
            return self.res
        self.find_combination(digits, 0, '')
        return self.res

    def find_combination(self, digits, index, s):
        # s保存了此时从 digits[0...index-1] 翻译得到的一个字母字符串
        # 寻找和 digits[index] 匹配的字母,获得 digits[0...index] 翻译得到的解
        if index == len(digits):
            self.res.append(s)
            return
        letters = self.letters_dict[digits[index]]
        for item in letters:
            self.find_combination(digits, index + 1, s + item)
