def partition(num_lst, begin, end):
    if begin < 0 or end >= len(num_lst):
        return
    index = begin
    swap(num_lst, index, end)
    small = begin - 1
    for index in range(begin, end + 1):
        if num_lst[index] < num_lst[end]:
            small += 1
            if small != index:
                swap(num_lst, small, index)
    small += 1
    swap(num_lst, small, end)
    return small


def swap(num_lst, a, b):
    temp = num_lst[a]
    num_lst[a] = num_lst[b]
    num_lst[b] = temp


def quick_sort(num_lst, begin, end):
    if begin >= end:
        return
    index = partition(num_lst, begin, end)
    if index > begin:
        quick_sort(num_lst, begin, index - 1)
    if index < end:
        quick_sort(num_lst, index + 1, end)


if __name__ == '__main__':
    num = [4, 2, 6, 3, 5, 7, 9]
    quick_sort(num, 0, 6)
    print(num)