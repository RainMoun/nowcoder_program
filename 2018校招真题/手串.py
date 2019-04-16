n, m, c = map(int, input().strip().split())
n_lst = [[] for _ in range(n)]
for i in range(n):
    n_lst[i] = list(map(int, input().strip().split()))[1:]
n_lst = n_lst + n_lst[0: m - 1]
num_appear = [-1 for _ in range(c + 1)]
color_flag = [0 for _ in range(c + 1)]
for i in range(len(n_lst)):
    for color in n_lst[i]:
        if color_flag[color] == 1:
            continue
        if num_appear[color] == -1:
            num_appear[color] = i
        else:
            if i - num_appear[color] < m:
                color_flag[color] = 1
            else:
                num_appear[color] = i
print(sum(color_flag))
