n = int(input())
num_list = list(map(int, input().strip().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = num_list[i]
for i in range(n - 2, -1, -1):
    print(i)