def is_num(num):
    if not num:
        return
    index, result = scan_integer(num, 0)
    if index < len(num) and num[index] == '.':
        index += 1
        index, result_b = scan_unsigned_integer(num, index)
        result = result or result_b
    if index < len(num) and (num[index] == 'e' or num[index] == 'E'):
        index += 1
        index, result_c = scan_integer(num, index)
        result = result and result_c
    return result and index == len(num)


def scan_unsigned_integer(num, index):
    original_index = index
    num_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while index < len(num) and (num[index] in num_lst):
        index += 1
    return index, index > original_index


def scan_integer(num, index):
    if index < len(num) and (num[index] == '+' or num[index] == '-'):
        index += 1
    return scan_unsigned_integer(num, index)


test_num = '12e+5.4'
print(is_num(list(test_num)))

