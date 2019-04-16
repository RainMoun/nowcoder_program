str_lst = list(input().strip())
print(len(str_lst))
left = 0
right = len(str_lst) - 1
while left < right:
    if str_lst[left] != str_lst[right]:
        str_lst.insert(right + 1, str_lst[left])
        print(str_lst)
        left += 1
    else:
        left += 1
        right -= 1
print(str_lst)
print(len(str_lst))