# def find_longest_str(str_lst):
#     is_same = 0
#     result = 0
#     now_length = 0
#     for i in range(len(str_lst) - 1):
#         if str_lst[i] == str_lst[i + 1] and is_same == 0:
#             now_length = 2
#             is_same = 1
#         elif str_lst[i] == str_lst[i + 1] and is_same == 1:
#             now_length += 1
#         elif str_lst[i] != str_lst[i + 1] and is_same == 1:
#             result = max(result, now_length)
#             is_same = 0
#         if i == len(str_lst) - 2 and is_same == 1:
#             result = max(result, now_length)
#     return result
#
#
# best_length = 0
#
#
# def method(str_lst, swap_time):
#     global best_length
#     if swap_time == 0:
#         best_length = max(best_length, find_longest_str(str_lst))
#         return
#     for i in range(len(str_lst) - 1):
#         method(str_lst[0: i] + [str_lst[i + 1]] + [str_lst[i]] + str_lst[i + 2:], swap_time - 1)
#     return
#
# str_list, n = input().strip().split()
print()