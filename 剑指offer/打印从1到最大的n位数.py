def print_1_to_max_of_n_digits(n):
    if n <= 0:
        return
    num = ['0' for _ in range(n)]
    end_flag, num = is_end(num)
    while not end_flag:
        print_num(num)
        end_flag, num = is_end(num)


def is_end(num):
    end_flag = False
    is_carry = 0
    for i in range(len(num) - 1, -1, -1):
        n_sum = int(num[i]) + is_carry
        if i == len(num) - 1:
            n_sum += 1
        if n_sum >= 10:
            if i == 0:
                end_flag = True
            else:
                n_sum -= 10
                is_carry = 1
                num[i] = str(n_sum)
        else:
            num[i] = str(n_sum)
            break
    return end_flag, num


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~全排列解法~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def print_1_to_n_digits(n):
    if n <= 0:
        return
    num = ['0' for _ in range(n)]
    for i in range(0, 10):
        num[0] = str(i)
        print_recu(num, n, 0)


def print_recu(num, n, index):
    if index == n - 1:
        print_num(num)
        return
    for i in range(0, 10):
        num[index + 1] = str(i)
        print_recu(num, n, index + 1)


def print_num(num):
    begin = True
    result = ''
    for i in range(0, len(num)):
        if num[i] == '0' and begin:
            continue
        if num[i] != '0':
            begin = False
        result += num[i]
    print(result)


print_1_to_n_digits(3)
