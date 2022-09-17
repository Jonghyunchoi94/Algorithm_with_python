def solution(N):
    # write your code in Python 3.6
    binary_value = ''
    while N > 0:
        binary_value = str(N % 2) + binary_value
        N //= 2
    gap = 0
    s = 0
    e = 0
    for i in range(len(binary_value)):
        if binary_value[i] == '1':
            gap = max(gap, e - s)
            s = 0
            e = 0
        else:
            e += 1


    return gap