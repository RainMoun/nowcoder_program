n, m = map(int, input().strip().split())
map_matrix = [list(input().strip()) for _ in range(n)]
init_x, init_y = map(int, input().strip().split())
num_step = int(input().strip())
step = []
for i in range(num_step):
    step.append(list(map(int, input().strip().split())))
arrived_matrix = [[0 for _ in range(m)] for _ in range(n)]
step_matrix = [[-1 for _ in range(m)] for _ in range(n)]
if map_matrix[init_x][init_y] == 'X':
    print(-1)
else:
    step_matrix[init_x][init_y] = 0
    arrived_matrix[init_x][init_y] = 1
    current_points = [[init_x, init_y]]
    while current_points:
        next_points = []
        for i in current_points:
            x, y = i[0], i[1]
            for j in step:
                x_ = x + j[0]
                y_ = y + j[1]
                if x_ < 0 or y_ < 0 or x_ >= n or y_ >= m or map_matrix[x_][y_] == 'X' or arrived_matrix[x_][y_] == 1:
                    continue
                else:
                    arrived_matrix[x_][y_] = 1
                    step_matrix[x_][y_] = step_matrix[x][y] + 1
                    next_points.append([x_, y_])
        current_points = next_points[:]
    flag = 0
    for i in range(n):
        for j in range(m):
            if map_matrix[i][j] != 'X' and step_matrix[i][j] == -1:
                flag = 1
                print(-1)
                break
        if flag == 1:
            break
    if flag == 0:
        max_step_value = 0
        for i in step_matrix:
            for j in i:
                if j != m * n:
                    max_step_value = max(max_step_value, j)
        print(max_step_value)
