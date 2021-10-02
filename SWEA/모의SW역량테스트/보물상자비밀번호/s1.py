import sys
sys.stdin = open('input.txt')


T = int(input())

for case in range(T):
    N, K = map(int, input().split())
    password = list(input())
    rotate = len(password) // 4
    m = rotate
    set_data = set()
    while m > 0:
        for idx in range(0, len(password), rotate):
            set_data.add(''.join(password[idx: idx + rotate]))
        password.append(password.pop(0))
        m -= 1

    sorted_data = sorted(list(set_data), key = lambda x:int(x,16), reverse = True)
    print('#{} {}'.format(case + 1, int(sorted_data[K - 1], 16)))