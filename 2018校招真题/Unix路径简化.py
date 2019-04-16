import re
path_input = input().strip()
dir_stack = []
name_lst = re.split('/+', path_input)
name_lst = [i for i in name_lst if i != '.'and i != '']
for i in name_lst:
    if i != '..':
        dir_stack.append(i)
    else:
        if len(dir_stack) != 0:
            dir_stack.pop()
print('/' + '/'.join(dir_stack))