# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        len_str = len(s)
        if len_str == 0:
            return 0
        not_num = 0
        result = 0
        for i in range(len_str):
            if (s[len_str - i - 1] == '+' or s[len_str - i - 1] == '-') and i == len_str - 1:
                if s[len_str - i - 1] == '-':
                    result = 0 - result
            elif '0' <= s[len_str - i - 1] <= '9':
                result += int(s[len_str - i - 1]) * pow(10, i)
            else:
                not_num = 1
                break
        if not_num == 0:
            return result
        else:
            return 0


s = Solution()
print(s.StrToInt('-123'))