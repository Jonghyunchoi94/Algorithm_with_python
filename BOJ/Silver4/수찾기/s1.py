import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()
for i in B:
    s, e = 0, len(A) - 1
    Flag = False
    while s <= e:
        mid = (s + e) // 2
        if A[mid] == i:
            Flag = True
            break
        elif A[mid] > i:
            e = mid - 1
        else:
            s = mid + 1

    if Flag:
        print(1)
    else:
        print(0)

