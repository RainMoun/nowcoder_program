n = int(input())
n_lst = list(map(int, input().strip().split()))
if len(n_lst) == 0 or len(n_lst) == 1:
    print(0)
else:
    count = 0
    while True:
        if n_lst[0] == n_lst[-1]:
            n_lst = n_lst[1: -1]
        else:
            if n_lst[0] > n_lst[-1]:
                item_1 = n_lst.pop(-1)
                item_2 = n_lst.pop(-1)
                n_lst.append(item_1 + item_2)
                count += 1
            else:
                item_1 = n_lst.pop(0)
                item_2 = n_lst.pop(0)
                n_lst.insert(0, item_1 + item_2)
                count += 1
        if len(n_lst) == 0 or len(n_lst) == 1:
            break
    print(count)
