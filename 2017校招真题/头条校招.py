n = int(input())
diff_list = list(sorted(list(map(int, input().strip().split()))))
result = 0
num_one_test = 0
i = 0
while i < len(diff_list) - 1:
    if diff_list[i + 1] - diff_list[i] <= 10:
        num_one_test += 1
        i += 1
        if num_one_test == 2:
            num_one_test = 0
            i += 1
    elif 10 < diff_list[i + 1] - diff_list[i] <= 20 and num_one_test == 0:
        result += 1
        i += 2
    elif diff_list[i + 1] - diff_list[i] > 20 and num_one_test == 0:
        result += 2
        i += 1
    elif diff_list[i + 1] - diff_list[i] > 10 and num_one_test == 1:
        result += 1
        i += 1
        num_one_test = 0
if i == len(diff_list) and num_one_test == 0:
    print(result)
elif i < len(diff_list) and num_one_test == 0:
    print(result + 2)
else:
    print(result + 1)