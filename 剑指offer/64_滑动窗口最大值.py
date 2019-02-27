# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        lst = []
        result = []
        for i in range(len(num)):
            if not lst:
                lst.append(i)
            else:
                print(lst)
                while num[lst[-1]] < num[i]:
                    lst = lst[: -1]
                    if not lst:
                        break
                lst.append(i)
            if i - size + 1 >= 0:
                if lst[0] <= i - size:
                    lst = lst[1:]
                result.append(num[lst[0]])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxInWindows([16, 14, 12, 10, 8, 6, 4], 5))
