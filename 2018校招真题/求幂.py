import math

n = int(input())
result_dict = {}
for i in range(1, n + 1):
    for j in range(1, n + 1):
        value = math.pow(i, j)
        if value not in result_dict.keys():
            result_dict[value] = [[i, j]]
        else:
            result_dict[value].append([i, j])
result = 0
for i in result_dict:
    temp_lst = result_dict[i]
    len_temp = len(temp_lst)
    result += (1 + len(temp_lst) - 1) * (len(temp_lst) - 1) + len(temp_lst)
    result %= 1000000007
print(result)