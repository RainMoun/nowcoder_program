n = int(input())
result_num = 0


def is_sushu(num):
    if num == 1:
        return False
    flag = 0
    for k in range(2, (num + 1) // 2 + 1):
        if num % k == 0 and k != num:
            flag = 1
            break
    return True if flag == 0 else False


for i in range(2, (n + 1) // 2 + 1):
    if is_sushu(i):
        last_num = n - i
        if last_num == i:
            result_num += 1
            break
        if is_sushu(last_num):
            result_num += 1

print(result_num)