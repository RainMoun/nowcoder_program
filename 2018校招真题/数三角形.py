import math
n = int(input().strip())
list_node = []
for _ in range(n):
    list_node.append(list(map(int, input().strip().split())))
edge_length = [[0 for _ in range(n)] for _ in range(n)]
for i in range(len(list_node)):
    for j in range(i + 1, len(list_node)):
        edge_length[i][j] = math.sqrt((list_node[i][0] - list_node[j][0]) * (list_node[i][0] - list_node[j][0]) +
                                      (list_node[i][1] - list_node[j][1]) * (list_node[i][1] - list_node[j][1]))
result = 0
for i in range(len(list_node)):
    for j in range(i + 1, len(list_node)):
        for k in range(j + 1, len(list_node)):
            len_lst = list(sorted([edge_length[i][j], edge_length[i][k], edge_length[j][k]]))
            if len_lst[0] + len_lst[1] > len_lst[2]:
                result += 1
print(result)