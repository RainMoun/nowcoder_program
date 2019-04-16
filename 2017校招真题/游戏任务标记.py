n_1, n_2 = map(int, input().strip().split())
if n_1 < 1 or n_1 > 1024 or n_2 < 1 or n_2 > 1024:
    print(-1)
else:
    flag_lst = [0 for _ in range(32)]
    flag_index = n_1 // 32
    print(flag_index)
    flag = str(bin(flag_lst[flag_index]))[2:]
    if len(flag) < 8:
        gap = 8 - len(flag)
        for i in range(gap):
            flag += '0'
    n_1 = n_1 % 32
    if flag[n_1] == '0':
        flag[n_1] = '1'
        flag = int(flag[n_1], 2)
        flag_lst[flag_index] = flag
    flag_index = n_2 // 32
    flag = str(bin(flag_lst[flag_index]))[2:]
    n_2 = n_2 % 32
    if len(flag) < n_2 or flag[n_1] == '0':
        print(-1)
    else:
        print(1)