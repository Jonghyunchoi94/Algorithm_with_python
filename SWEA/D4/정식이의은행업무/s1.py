import sys
sys.stdin = open('input.txt')


def change(number, r, data):
    if number == 1:
        confirm.append(int(''.join(data), 2))
        return

    for i in range(len(data)):
        temp = data[i]
        for j in range(r - 1, -1, -1):
            if str(j) != temp:
                data[i] = str(j)
                change(number + 1, r, data)
                data[i] = temp

def change_confirm(number, r, data):
    global res
    if number == 1:
        if int(''.join(data), 3) in confirm:
            res = int(''.join(data), 3)
        return

    for i in range(len(data)):
        temp = data[i]
        for j in range(r - 1, -1, -1):
            if str(j) != temp:
                data[i] = str(j)
                change_confirm(number + 1, r, data)
                data[i] = temp

T = int(input())

for case in range(T):
    two = list(input())
    three = list(input())
    confirm = []
    res = 0

    change(0, 2, two)
    change_confirm(0, 3, three)

    print('#{} {}'.format(case + 1, res))


