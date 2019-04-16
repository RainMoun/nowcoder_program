n, m = map(int, input().strip().split())
a_lst = list(map(int, input().strip().split()))
if len(a_lst) == 0:
    print()
else:
    result = []
    a_index = 0
    result_index = 0
    while len(result) < n:
        if len(result) <= result_index:
            temp_lst = [a_lst[a_index] for _ in range(a_lst[result_index])]
        else:
            temp_lst = [a_lst[a_index] for _ in range(result[result_index])]
        result.extend(temp_lst)
        result_index += 1
        a_index = a_index + 1 if a_index < len(a_lst) - 1 else 0
    for i in result[0: n]:
        print(i)