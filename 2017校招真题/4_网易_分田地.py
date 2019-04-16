n, m = map(int, input().strip().split())  # 行 列
field_matrix = [list(map(int, list(input().strip()))) for _ in range(n)]
value_matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        value_matrix[i][j] = value_matrix[i - 1][j] + value_matrix[i][j - 1] \
                             - value_matrix[i - 1][j - 1] + field_matrix[i - 1][j - 1]


def get_area_value(x1, y1, x2, y2):
    return value_matrix[x1][y1] - value_matrix[x1][y2] - value_matrix[x2][y1] + value_matrix[x2][y2]


def judge(value):
    for first_m in range(1, m - 2):
        for second_m in range(first_m + 1, m - 1):
            for third_m in range(second_m + 1, m):
                pre_m = 0
                count = 0
                for line in range(1, n + 1):
                    area_1 = get_area_value(pre_m, 0, line, first_m)
                    area_2 = get_area_value(pre_m, first_m, line, second_m)
                    area_3 = get_area_value(pre_m, second_m, line, third_m)
                    area_4 = get_area_value(pre_m, third_m, line, m)
                    if area_1 >= value and area_2 >= value and area_3 >= value and area_4 >= value:
                        count += 1
                        pre_m = line
                if count >= 4:
                    return True
    return False


low = 0
high = value_matrix[n][m]
result = 0
while low <= high:
    mid = (low + high) // 2
    if judge(mid):
        low = mid + 1
        result = mid
    else:
        high = mid - 1
print(result)




