from sys import stdin
lst = []
while True:
    line = stdin.readline().strip()
    if line == '':
        break
    item = list(map(int, line.split()))
    lst.append(item)
lst = list(sorted(lst, key=lambda a: a[0]))
price_lst = [-1 for _ in range(15000)]
for i in lst:
    for j in range(i[0], i[1] + 1):
        price_lst[j] = i[2]
begin_day = lst[0][0]
result = []
for i in range(lst[0][0] + 1, lst[-1][1] + 1):
    if price_lst[i] != price_lst[i - 1]:
        result.append([begin_day, i - 1,  price_lst[i - 1]])
        begin_day = i
result.append([begin_day, i, price_lst[i - 1]])
result = [i for i in result if i[2] != -1]
for i in result[: -1]:
    print(i, end=',')
print(result[-1])