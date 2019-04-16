# n, m, p = map(int, input().strip().split())
# map_lst = []
# for _ in range(n):
#     map_temp = list(map(int, input().strip().split()))
#     map_lst.append(map_temp)
# step_way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
# cost_p = [0, 3, 1, 1]
# min_step = float('inf')
# result = []
# flag_lst = [[-1 for _ in range(m)] for _ in range(n)]
# now_step = [[0, 0, p, [[0, 0]]]]
# find_flag = 0
# while True:
#     if find_flag == 1:
#         break
#     temp_step = []
#     for i in now_step:
#         if find_flag == 1:
#             break
#         for j in range(len(step_way)):
#             n_now = i[0] + step_way[j][0]
#             m_now = i[1] + step_way[j][1]
#             p_now = i[2] - cost_p[j]
#             if p_now < 0 or n_now < 0 or n_now >= n or m_now < 0 or m_now >= m:
#                 continue
#             if flag_lst[n_now][m_now] == 0 or map_lst[n_now][m_now] == 0:
#                 flag_lst[n_now][m_now] = 0
#                 continue
#             if p_now >= 0 and n_now == 0 and m_now == m - 1:
#                 temp_loc = i[3][:]
#                 temp_loc.append([n_now, m_now])
#                 result = temp_loc[:]
#                 find_flag = 1
#                 break
#             temp_loc = i[3][:]
#             temp_loc.append([n_now, m_now])
#             temp_step.append([n_now, m_now, p_now, temp_loc])
#             flag_lst[n_now][m_now] = 0
#     now_step = temp_step[:]
# if find_flag:
#     result_str = '['
#     for i in result:
#         result_str = result_str + '['
#         result_str += str(i[0])
#         result_str += ','
#         result_str += str(i[1])
#         result_str += ']'
#         result_str += ','
#     result_str = result_str[0: -1]
#     result_str += ']'
#     print(result_str)
# else:
#     print("Can not escape!")


N, M, P = map(int, input().strip().split())
map_lst = []
for _ in range(N):
    map_temp = list(map(int, input().strip().split()))
    map_lst.append(map_temp)


def is_valid(matrix, n, m, p, x, y, visited):
    is_visited = (x * m + y in visited)
    is_v = (0 <= x < n) and (0 <= y < m) and (matrix[x][y] == 1)
    has_p = (p >= 0)
    return not is_visited and is_v and has_p


def get_path(matrix, n, m, p, x, y, visited, path):
    if (x, y) == (0, m - 1):
        return True
    else:
        next_pos = [(x, y + 1, p - 1), (x - 1, y, p - 3), (x, y - 1, p - 1), (x + 1, y, p)]
        for now_x, now_y, now_p in next_pos:
            if is_valid(matrix, n, m, now_p, now_x, now_y, visited):
                path.append([now_x, now_y])
                visited.add(now_x * m + now_y)
                if get_path(matrix, n, m, now_p, now_x, now_y, visited, path):
                    return True
                path.pop(-1)
                visited.remove(now_x * m + now_y)
        return False


visited_set = set()
path_lst = [[0, 0]]
if get_path(map_lst, N, M, P, 0, 0, visited_set, path_lst):
    print(','.join(map(str, path_lst)).replace(' ', ''))
else:
    print("Can not escape!")
