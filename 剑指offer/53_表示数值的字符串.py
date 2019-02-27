# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        is_num = 1
        after_e = 0
        after_num = 0
        after_symbol = 0
        num_point = 0
        e_exist = 0
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                after_symbol = 0
                after_num = 1
                after_e = 0
            elif (s[i] == '+' or s[i] == '-') and (after_e == 1 or i == 0):
                after_symbol = 1
                after_num = 0
                after_e = 0
            elif (s[i] == 'e' or s[i] == 'E') and after_num == 1:
                e_exist = 1
                after_symbol = 0
                after_e = 1
            elif s[i] == '.' and (after_num == 1 or after_symbol == 1) and num_point == 0 and e_exist == 0:
                num_point += 1
                after_symbol = 0
                after_num = 0
            else:
                is_num = 0
                break
        if is_num == 1 and after_symbol == 0 and after_e == 0:
            return True
        else:
            return False


s = Solution()
print(s.isNumeric('12e+5.4'))