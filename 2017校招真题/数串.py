from sys import stdin
lst = []
while True:
    line = stdin.readline().strip()
    if line == '':
        break
    item = list(map(int, stdin.readline().strip().split()))
    lst.append(item)
