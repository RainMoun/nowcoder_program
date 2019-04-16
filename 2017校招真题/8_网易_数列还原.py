n, k_num = map(int, input().strip().split())
lst = list(map(int, input().strip().split()))
original_lst = []
zero_position = []  # 存储看不清位置
for i in range(len(lst)):
    if lst[i] != 0:
        original_lst.append(lst[i])
    else:
        zero_position.append(i)
original_k = 0
for i in range(0, len(original_lst) - 1):
    for j in range(i + 1, len(original_lst)):
        if original_lst[i] < original_lst[j]:
            original_k += 1
lost_list = [i for i in range(1, n + 1) if i not in original_lst]


def perm(l):
    if len(l) <= 1:
        return [l]
    r = []
    for i in range(len(l)):
        s = l[:i]+l[i+1:]
        p = perm(s)
        for x in p:
            r.append(l[i:i+1] + x)
    return r


all_lst = perm(lost_list)
result = 0
for i in all_lst:
    original_lst_temp = original_lst[:]
    original_k_temp = original_k
    for j in range(len(i)):
        original_lst_temp.insert(zero_position[j], i[j])
        for k in range(len(original_lst_temp)):
            if k != zero_position[j]:
                if (k < zero_position[j] and original_lst_temp[k] < original_lst_temp[zero_position[j]]) \
                        or (k > zero_position[j] and original_lst_temp[k] > original_lst_temp[zero_position[j]]):
                    original_k_temp += 1
        if original_k_temp > k_num:
            break
    if original_k_temp == k_num:
        result += 1
print(result)