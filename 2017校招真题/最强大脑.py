import re

if __name__ == '__main__':
    while True:
        try:
            s = input()
            s1 = input()
            s2 = input()
            forward = re.match('.*' + s1 + '.*' + s2 + '.*', s)
            backward = re.match('.*' + s1 + '.*' + s2 + '.*', s[::-1])
            if forward and backward:
                print('both')
            elif forward:
                print('forward')
            elif backward:
                print('backward')
            else:
                print('invalid')
        except:
            break
