def find_tel_num(s):
    result = [0 for _ in range(10)]
    result[0] = s.count('Z')
    result[2] = s.count('W')
    result[4] = s.count('U')
    result[5] = s.count('F') - result[4]
    result[6] = s.count('X')
    result[7] = s.count('S') - result[6]
    result[8] = s.count('G')
    result[1] = s.count('O') - result[0] - result[2] - result[4]
    result[3] = s.count('T') - result[8] - result[2]
    result[9] = s.count('I') - result[5] - result[6] - result[8]
    result = result[8:] + result[0: 8]
    tel_num = ''
    for i in range(len(result)):
        if result[i] != 0:
            for j in range(result[i]):
                tel_num += str(i)
    return tel_num


n = int(input().strip())
for i in range(n):
    input_str = input().strip()
    print(find_tel_num(input_str))