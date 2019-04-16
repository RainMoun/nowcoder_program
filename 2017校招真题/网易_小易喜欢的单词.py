lst_digit = list(input().strip())
print(lst_digit)
dislike_flag = 0
for i in range(len(lst_digit)):
    if (lst_digit[i] < 'A' or lst_digit[i] > 'Z') or (i < len(lst_digit) - 1 and lst_digit[i] == lst_digit[i + 1]):
        dislike_flag = 1
        break
for i in range(len(lst_digit) - 3):
    for j in range(i + 1, len(lst_digit) - 2):
        for index, k in enumerate(lst_digit[j + 1: ]):
            if k == lst_digit[i] and (lst_digit[j] in lst_digit[index + 1 + j + 1: ]):
                dislike_flag = 1
                break
if dislike_flag == 0:
    print('Likes')
else:
    print('Dislikes')