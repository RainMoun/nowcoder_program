from sys import stdin
str_lst = []
while True:
    line = stdin.readline().strip()
    if line == '':
        break
    str_lst.append(line)
for s in str_lst:
    s = list(s)
    max_num = 0
    for i in range(len(s)):
        queen_like = set(['A', 'B', 'C', 'D', 'E'])
        if s[i] in queen_like:
            queen_like.remove(s[i])
            temp_s = s[i:] + s[0: i]
            for j in range(1, len(temp_s)):
                if temp_s[j] in queen_like:
                    queen_like.remove(temp_s[j])
                    if not queen_like:
                        max_num = max(max_num, len(temp_s) - j - 1)
                        break
    print(max_num)