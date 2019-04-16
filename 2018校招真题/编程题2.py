n, last_num = map(int, input().strip().split())
last_num -= 1
a_lst = list(map(int, input().strip().split()))
min_num = min(a_lst)
room_index = last_num
select_room = -1
while True:
    if a_lst[room_index] == min_num:
        select_room = room_index
        break
    if room_index != 0:
        room_index -= 1
    else:
        room_index = n - 1
is_zero = 1 if min_num == 0 else 0
room_index = last_num
people_num = 0
# while True:
#     if room_index == select_room and is_zero == 1:
#         break
#     a_lst[room_index] -= 1
#     people_num += 1
#     if room_index == select_room and a_lst[room_index] == 0:
#         is_zero = 1
#     room_index = room_index - 1 if room_index != 0 else n - 1
for i in range(len(a_lst)):
    a_lst[i] -= min_num
    people_num += min_num
if select_room != last_num:
    begin_index = select_room + 1 if select_room < n - 1 else 0
    while True:
        a_lst[begin_index] -= 1
        people_num += 1
        if begin_index == last_num:
            break
        begin_index = begin_index + 1 if begin_index < n - 1 else 0
a_lst[select_room] = people_num
print(' '.join(list(map(str, a_lst))))