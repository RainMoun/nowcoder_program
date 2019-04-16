n = int(input().strip())
n_lst = []
all_node = set()
sub_node = set()
for i in range(n - 1):
    temp_lst = list(map(int, input().strip().split()))
    sub_node.add(temp_lst[1])
    all_node.add(temp_lst[0])
    all_node.add(temp_lst[1])
    n_lst.append(temp_lst)
now_node = list(all_node - sub_node)
depth = 0
while now_node:
    temp_lst = []
    while now_node:
        node = now_node.pop()
        for i in n_lst:
            if i[0] == node:
                temp_lst.append(i[1])
    depth += 1
    now_node = temp_lst[:]
print(depth)
