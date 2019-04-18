def array(num_lst, index):  # 求全排列
    if index == len(num_lst):
        print(num_lst)
    else:
        for i in range(index, len(num_lst)):
            temp = num_lst[i]
            num_lst[i] = num_lst[index]
            num_lst[index] = temp
            array(num_lst, index + 1)
            temp = num_lst[i]
            num_lst[i] = num_lst[index]
            num_lst[index] = temp


def permutation(num_lst):
    if not num_lst:
        return
    for i in range(1, len(num_lst) + 1):
        permutation_iter(num_lst, i, 0, [])


def permutation_iter(num_lst, i, begin, result):
    if i == len(result):
        print(result)
        return
    if begin >= len(num_lst):
        return
    else:
        permutation_iter(num_lst, i, begin + 1, result + [num_lst[begin]])
        permutation_iter(num_lst, i, begin + 1, result)


if __name__ == '__main__':
    # array([1, 2, 3, 4, 5], 0)
    permutation([1, 2, 3, 4, 5])
