x_init = int(input().strip())


def find_min(x_init):
    if x_init % 1000000007 == 0:
        return 0
    else:
        x_0 = x_init
        x_1 = x_0 * 4 + 3
        x_2 = x_1 * 4 + 3
        if x_1 % 1000000007 == 0:
            return 1
        if x_2 % 1000000007 == 0:
            return 2
        lst = [x_0, x_1, x_2]
        for i in range(len(lst)):
            original_num = lst[i]
            for j in range(100000 - i):
                original_num = original_num * 8 + 7
                if original_num % 1000000007 == 0:
                    return j + i + 1
        return -1


print(find_min(x_init))