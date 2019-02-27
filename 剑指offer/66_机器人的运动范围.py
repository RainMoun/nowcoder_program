# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        flag_matrix = [0 for _ in range(rows * cols)]

        def find_total(threshold, i, j, rows, cols):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return 0
            sum_value = sum(list(map(int, list(str(i))))) + sum(list(map(int, list(str(j)))))
            if sum_value > threshold or flag_matrix[i * rows + j] == 1:
                return 0
            flag_matrix[i * rows + j] = 1
            result = find_total(threshold, i + 1, j, rows, cols) + find_total(threshold, i - 1, j, rows, cols) + \
                find_total(threshold, i, j + 1, rows, cols) + find_total(threshold, i, j - 1, rows, cols) + 1
            return result
        return find_total(threshold, 0, 0, rows, cols)


if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(15, 100, 10))