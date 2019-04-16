# N, M = map(int, input().strip().split())
# min_step = float('inf')
#
#
# def find(n, m, step):
#     global min_step
#     if n == m:
#         min_step = min(min_step, step)
#         return
#     if n > m:
#         return
#     for i in range(2, (n // 2) + 1):
#         if n % i == 0:
#             find(n + i, m, step + 1)
#     return
#
#
# find(N, M, 0)
# if min_step == float('inf'):
#     print(-1)
# else:
#     print(min_step)


# N, M = map(int, input().strip().split())
# min_step = [float('inf') for _ in range(M + 1)]
# min_step[N] = 0
#
# for i in range(N, M):
#     if min_step[i] == float('inf'):
#         continue
#     j = 2
#     while j * j <= i:
#         if i % j == 0:
#             if i + j <= M:
#                 min_step[i + j] = min(min_step[i] + 1, min_step[i + j])
#             if i + i // j <= M:
#                 min_step[i + i // j] = min(min_step[i] + 1, min_step[i + i // j])
#         j += 1
# if min_step[M] == float('inf'):
#     print(-1)
# else:
#     print(min_step[M])