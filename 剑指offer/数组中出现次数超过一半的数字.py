def more_than_half(num_lst):
    if not num_lst:
        return -1  # 数组为空
    count = 1
    now_num = num_lst[0]
    for num in num_lst[1: ]:
        if num == now_num:
            count += 1
        else:
            if count > 0:
                count -= 1
            else:
                count = 1
                now_num = num
    return now_num


if __name__ == '__main__':
    print(more_than_half([4, 7, 5, 6, 7, 7, 7, 4, 7]))