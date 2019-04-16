n = int(input().strip())
x_lst = list(sorted(list(map(int, input().strip().split())), reverse=True))
flag = 0
for i in range(len(x_lst)):
    if x_lst[i] == 0:
        flag = 1
        print(i)
    for j in range(i + 1, len(x_lst)):
        x_lst[j] = min(x_lst[j], x_lst[i] ^ x_lst[j])
    x_lst = x_lst[0: i + 1] + list(sorted(x_lst[i + 1:], reverse=True))
if flag == 0:
    print(len(x_lst))