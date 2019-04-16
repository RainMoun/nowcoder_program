M, N = map(int, input().strip().split())
matrix = [list(input().strip()) for _ in range(M)]
pos_lst = []
for m in range(M):
    for n in range(N):
        if matrix[m][n] == '2':
            pos_lst.append([m, n, []])
            break
steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]
find_flag = 0
step_num = 0
while pos_lst:
    temp_pos = []
    while pos_lst:
        pos = pos_lst.pop()
        m, n, key = pos[0], pos[1], pos[2]
        for step in steps:
            new_key = key[:]
            new_m, new_n = m + step[0], n + step[1]
            if new_m < 0 or new_m >= M or new_n < 0 or new_n >= N or matrix[new_m][new_n] == '0' \
                    or (matrix[new_m][new_n].isupper() and matrix[new_m][new_n].lower() not in new_key):
                continue
            if matrix[new_m][new_n] == '3':
                find_flag = 1
                break
            if matrix[new_m][new_n].islower() and matrix[new_m][new_n] not in new_key:
                new_key.append(matrix[new_m][new_n])
            temp_pos.append([new_m, new_n, new_key])
        if find_flag == 1:
            break
    step_num += 1
    pos_lst = temp_pos[:]
    if find_flag == 1:
        break
print(step_num)


