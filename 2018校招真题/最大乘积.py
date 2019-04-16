n = int(input().strip())
a_lst = list(map(int, input().strip().split()))
max_lst = []
min_lst = []
for i in a_lst:
    if i > 0:
        if len(max_lst) < 3:
            max_lst.append(i)
        else:
            max_lst = list(sorted(max_lst, reverse=True))
            if i > max_lst[2]:
                max_lst[2] = i
    elif i < 0:
        if len(min_lst) < 2:
            min_lst.append(i)
        else:
            min_lst = list(sorted(min_lst))
            if i < min_lst[1]:
                min_lst[1] = i
if len(max_lst) < 3:
    max_lst.extend([0 for _ in range(3 - len(max_lst))])
if len(min_lst) < 2:
    min_lst.extend([0 for _ in range(2 - len(min_lst))])
max_lst = list(sorted(max_lst, reverse=True))
min_lst = list(sorted(min_lst))
print(max(max_lst[0] * max_lst[1] * max_lst[2], min_lst[0] * min_lst[1] * max_lst[0]))