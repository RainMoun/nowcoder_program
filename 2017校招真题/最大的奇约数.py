n = int(input().strip())
lst = list(range(1, n + 1))
result = 0
while lst:
    sum_lst = lst[0::2]
    result += (sum_lst[0] + sum_lst[-1]) * len(sum_lst) // 2
    lst = [i//2 for i in lst[1::2]]
print(result)