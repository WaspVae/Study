class Solution:
    def valid_palindrome(self, s):
        # import re
        # s = ''.join(re.findall('[A-Za-z0-9]', s.lower()))
        s = ''.join(filter(str.isalnum, s)).lower()
        if not len(s):
            return True
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
