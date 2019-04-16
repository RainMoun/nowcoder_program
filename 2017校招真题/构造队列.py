# T = 100
# for j in range(T):
#     n = j
#     output_lst = list(range(1, n + 1))
#     if n == 0:
#         print(None)
#     elif n == 1:
#         print(1)
#     else:
#         uncertain_lst = list(range(n))
#         result = [0 for _ in range(n)]
#         flag = 0
#         while True:
#             if flag == 0:
#                 begin_index = 1
#             else:
#                 begin_index = 0
#             remove_lst = []
#             for i in range(begin_index, len(uncertain_lst), 2):
#                 result[uncertain_lst[i]] = output_lst[0]
#                 output_lst = output_lst[1:]
#                 remove_lst.append(uncertain_lst[i])
#             if i != len(uncertain_lst) - 1:
#                 flag = 1
#             for i in remove_lst:
#                 uncertain_lst.remove(i)
#             if not output_lst:
#                 break
#         result = list(map(str, result))
#         print(' '.join(result))
#
#
T = int(input())
for _ in range(T):
    n = int(input())
    result = []
    for i in range(n, 0, -1):
        result.append(i)
        t = result[0]
        result.pop(0)
        result.append(t)
    for i in range(n - 1):
        print(result[n - i - 1], end=' ')
    print(result[0])


# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     res = []
#     for i in range(n, 0, -1):
#         res.append(i)
#         tmp = res[0]
#         res.pop(0)
#         res.append(tmp)
#
#     len_r = len(res)
#     for i in range(len_r - 1):
#         print(res[len_r - 1 - i], end=' ')
#
#     print(res[0])
