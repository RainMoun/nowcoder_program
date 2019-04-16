def quick_sort(num_lst, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = num_lst[low]
    while left < right:
        while left < right and num_lst[right] >= key:
            right -= 1
        num_lst[left] = num_lst[right]
        while left < right and num_lst[left] <= key:
            left += 1
        num_lst[right] = num_lst[left]
    num_lst[right] = key
    quick_sort(num_lst, low, left - 1)
    quick_sort(num_lst, left + 1, high)


lst = [7, 5, 3, 9, 10, 1, 4, 15]
quick_sort(lst, 0, len(lst) - 1)
print(lst)