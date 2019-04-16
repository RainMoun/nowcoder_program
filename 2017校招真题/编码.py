str_list = list(input().strip())
index = -1
sum_lst = [1, 25 + 1, 25 * 25 + 25 + 1, 25 * 25 * 25 + 25 * 25 + 25 + 1]
count = 4
for i in str_list:
    print(ord(i) - ord('a'))
    index += (ord(i) - ord('a')) * sum(sum_lst[0: count])
    if count == 3 or count == 2:
        index += 1
    count -= 1
print(index)