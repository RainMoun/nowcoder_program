def is_even(n):
    return n % 2 == 0


def adjust_lst(lst):
    l_index = 0
    r_index = len(lst) - 1
    while l_index < r_index:
        while l_index < r_index and not is_even(lst[l_index]):
            l_index += 1
        while l_index < r_index and is_even(lst[r_index]):
            r_index -= 1
        temp = lst[l_index]
        lst[l_index] = lst[r_index]
        lst[r_index] = temp


test_lst = [1, 2, 3, 4, 5]
adjust_lst(test_lst)
print(test_lst)