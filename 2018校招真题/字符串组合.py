input_str = list(input().strip())
len_str = len(input_str)
result = []
len_now = 1
while len_now <= len_str:
    result_now = set()
    for i in range(len_str - len_now + 1):
        result_now.add(''.join(input_str[i: i + len_now]))
    print(result_now)
    result_now = list(sorted(list(result_now)))
    result.extend(result_now)
    len_now += 1
print(' '.join(list(sorted(result))))