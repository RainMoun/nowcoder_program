l, r = map(int, input().strip().split())
result = 0
not_meet = []
for num in range(l, r + 1):
    num_lst = list(sorted(list(map(int, list(str(num)))), reverse=True))
    if num_lst not in not_meet and sum(num_lst) % 2 == 0:
        sum_value = sum(num_lst) // 2
        dp = [0 for _ in range(sum_value + 1)]
        dp[0] = 1
        flag = 0
        for i in range(len(num_lst)):
            if flag == 1:
                break
            for j in range(sum_value, 0, -1):
                if num_lst[i] <= j and j - num_lst[i] >= 0:
                    dp[j] = max(dp[j], dp[j - num_lst[i]])
                if j == sum_value and dp[sum_value] > 0:
                    result += 1
                    flag = 1
                    break
        if flag == 0:
            not_meet.append(num_lst)
print(result)