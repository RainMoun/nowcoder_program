t = int(input())
for _ in range(t):
    n, k, d1, d2 = map(int, input().strip().split())
    last_game_num = n - k
    if last_game_num == 0 and (d1 != 0 or d2 != 0):
        print('no')
    else:
        # 1 > 2 2 > 3
        if last_game_num - d1 - d2 >= 0 and (last_game_num - d1 - d2) % 3 == 0:
            print('yes')
            continue
        # 1 > 2 2 < 3
        if d1 > d2:
            if last_game_num - (d1 + d1 - d2) >= 0 and (last_game_num - (d1 + d1 - d2) >= 0) % 3 == 0:
                print('yes')
                continue
        else:
            if last_game_num - (d2 + d2 - d1) >= 0 and (last_game_num - (d2 + d2 - d1) >= 0) % 3 == 0:
                print('yes')
                continue
        print('no')