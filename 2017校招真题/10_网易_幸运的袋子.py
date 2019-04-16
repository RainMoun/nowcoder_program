n = int(input().strip())
x_lst = list(sorted(list(map(int, input().strip().split()))))


def dfs(x_lst, index, sum_value, multi_value):
    count = 0
    i = index
    while i < n:
        sum_value += x_lst[i]
        multi_value *= x_lst[i]
        if sum_value > multi_value:
            count += 1 + dfs(x_lst, i + 1, sum_value, multi_value)
        elif sum_value == multi_value:
            count += dfs(x_lst, i + 1, sum_value, multi_value)
        else:
            break
        sum_value -= x_lst[i]
        multi_value /= x_lst[i]
        while i < n - 1 and x_lst[i] == x_lst[i + 1]:
            i += 1
        i += 1
    return count


print(dfs(x_lst, 0, 0, 1))