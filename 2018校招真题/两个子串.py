char_lst = list(map(str, input().strip()))
result = -1
for index in range(1, len(char_lst)):
    last_lst = char_lst[index:]
    # print(index)
    # print(last_lst)
    # print(char_lst[0: len(last_lst)])
    # print('*' * 10)
    if char_lst[0: len(last_lst)] == last_lst:
        result = index
        break
if result == -1:
    char_lst.extend(char_lst)
else:
    char_lst.extend(char_lst[len(char_lst) - index: ])
print(''.join(char_lst))